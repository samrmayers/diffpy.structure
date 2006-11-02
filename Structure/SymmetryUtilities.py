########################################################################
#
# <PackageName>     by DANSE Diffraction group
#                   Simon J.L. Billinge
#                   Michigan State University
#
# File coded by:    Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See COPYRIGHT.txt for copying and usage conditions.
# See LICENSE.txt for license information.
#
########################################################################

"""Symmetry utility functions such as expansion of asymmetric unit,
and generation of positional constraints.
"""

# version
__id__ = '$Id$'

import sys
import re
import numpy

# Constants:
# Default tolerance for equality of 2 positions, also
# used for identification of special positions.
epsilon = 1.0e-5
stdUsymbols = ['U11', 'U22', 'U33', 'U12', 'U13', 'U23']

def isSpaceGroupLatPar(spacegroup, a, b, c, alpha, beta, gamma):
    """Check if space group allows passed lattice parameters.

    spacegroup -- instance of SpaceGroup
    a, b, c, alpha, beta, gamma -- lattice parameters

    Return bool.
    """
    # ref: Benjamin, W. A., Introduction to crystallography,
    # New York (1969), p.60
    crystal_system_rules = {
      "TRICLINIC"  : 'True',
      "MONOCLINIC" : 'alpha == gamma == 90',
      "ORTHORHOMBIC" : 'alpha == beta == gamma == 90',
      "TETRAGONAL" : 'a == b and alpha == beta == gamma == 90',
      "TRIGONAL"   : 'a == b == c and alpha == beta == gamma or ' +
                     'a == b and alpha == beta == 90 and gamma == 120',
      "HEXAGONAL"  : 'a == b and alpha == beta == 90 and gamma == 120',
      "CUBIC"      : 'a == b == c and alpha == beta == gamma == 90',
    }
    rule = crystal_system_rules[spacegroup.crystal_system]
    return eval(rule, locals())

# End of isSpaceGroupLatPar

def isconstantFormula(s):
    """Check if formula string is constant.
    """
    # check for floats or fractions
    pat = '[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$|[-+]?\d+[.]?\d*/[-+]?\d+$'
    return bool( re.match(pat, s.replace(' ', '')) )

# End of isconstantFormula

# Helper class intended for this module only:
class Position2Tuple:
    """Create callable object that converts fractional coordinates to
    a tuple of integers with given precision.  For presision close to zero
    it will return a tuples of double.

    Note: Helper class intended for local use only.

    Data members:

    eps -- cutoff for equivalent coordinates.  When two coordiantes map to the
           same tuple, they are closer than eps.
    """
    def __init__(self, eps=epsilon):
        """Initialize Position2Tuple

        eps -- cutoff for equivalent coordinates
        """
        # ensure self.eps has exact machine representation
        self.eps = eps + 1.0
        self.eps = self.eps - 1.0
        # no conversions for very small eps
        if self.eps == 0.0 or 1.0/self.eps > sys.maxint:
            self.eps = 0.0
        return

    def __call__(self, xyz):
        """Convert array of fractional coordinates to a tuple.

        xyz -- fractional coordinates

        Return a tuple of 3 numbers.
        """
        # no conversion case
        if self.eps == 0.0:
            tpl = tuple(xyz % 1.0)
            return tpl
        # here we convert to integer
        tpl = tuple( [int((xi - numpy.floor(xi))/self.eps) for xi in xyz] )
        return tpl

# End of class Position2Tuple

def positionDifference(xyz0, xyz1):
    """Smallest difference between two coordinates in periodic lattice.

    xyz0, xyz1  -- fractional coordinates

    Return dxyz, a numpy.array dxyz with 0 <= dxyz <= 0.5.
    """
    dxyz = numpy.array(xyz0) - xyz1
    # map differences to [0,0.5]
    dxyz = dxyz - numpy.floor(dxyz)
    mask = (dxyz > 0.5)
    dxyz[mask] = 1.0 - dxyz[mask]
    return dxyz

# End of positionDifference

def nearestSiteIndex(sites, xyz):
    """Index of the nearest site to a specified position.

    sites -- list of coordinates or a 2-dimensional numpy.array
    xyz   -- single position

    Return integer.
    """
    # we use box distance to be consistent with Position2Tuple conversion
    dbox = positionDifference(sites, xyz).max(axis=1)
    nearindex = numpy.argmin(dbox)
    return nearindex

# End of nearestSiteIndex

def equalPositions(xyz0, xyz1, eps=epsilon):
    """Equality of two coordinates with optional tolerance.

    xyz0, xyz1 -- fractional coordinates
    eps        -- tolerance for equality of coordinates

    Return bool.
    """
    # we use box distance to be consistent with Position2Tuple conversion
    dxyz = positionDifference(xyz0, xyz1)
    return numpy.all(dxyz <= eps)

# End of equalPositions

def expandPosition(spacegroup, xyz, sgoffset=[0,0,0], eps=epsilon):
    """Obtain unique equivalent positions and corresponding operations.

    spacegroup -- instance of SpaceGroup
    xyz        -- position to be expanded
    sgoffset   -- offset of space group origin [0, 0, 0]
    eps        -- cutoff for equal positions

    Return a tuple with (list of unique equivalent positions, nested
    list of SpaceGroups.SymOp instances, site multiplicity).
    """
    sgoffset = numpy.array(sgoffset, dtype=float)
    pos2tuple = Position2Tuple(eps)
    positions = []
    site_symops = {}    # position tuples with [related symops]
    for symop in spacegroup.iter_symops():
        # operate on coordinates in non-shifted spacegroup
        pos = symop(xyz + sgoffset) - sgoffset
        mask = numpy.logical_or(pos <= -0.5, pos >= 1.0)
        pos[mask] -= numpy.floor(pos[mask])
        tpl = pos2tuple(pos)
        if not tpl in site_symops:
            pos_is_new = True
            site_symops[tpl] = []
            # double check if there is any position nearby
            if positions:
                nearpos = positions[nearestSiteIndex(positions, pos)]
                # is it an equivalent position?
                if equalPositions(nearpos, pos, eps):
                    # tpl should map to the same list as nearpos
                    site_symops[tpl] = site_symops[ pos2tuple(nearpos) ]
                    pos_is_new = False
            if pos_is_new:  positions.append(pos)
        # here tpl is inside site_symops
        site_symops[tpl].append(symop)
    # pos_symops is nested list of symops associated with each position
    pos_symops = [ site_symops[pos2tuple(pos)] for pos in positions ]
    multiplicity = len(positions)
    return positions, pos_symops, multiplicity

# End of expandPosition

def nullSpace(A):
    """Null space of matrix A.
    """
    from numpy import linalg
    u, s, v = linalg.svd(A)
    # s may have smaller dimension than v
    mask = numpy.array([True]*numpy.shape(v)[0])
    mask[s > epsilon] = False
    null_space = numpy.compress(mask, v, axis=0)
    return null_space

# End of nullSpace

class GeneratorSite:
    """Storage of data related to a generator positions.

    Data members:
        xyz          -- fractional coordinates of generator site
        Uij          -- anisotropic thermal displacement at generator site
        sgoffset     -- offset of space group origin [0, 0, 0]
        eps          -- cutoff for equal positions
        eqxyz        -- list of equivalent positions
        eqUij        -- list of displacement matrices at equivalent positions
        symops       -- nested list of operations per each eqxyz
        multiplicity -- generator site multiplicity
        Uisotropy    -- bool flag for isotropic thermal factors
        invariants   -- list of invariant operations for generator site
        null_space   -- null space of all possible differences of invariant
                        rotational matrices, this is a base of symmetry
                        allowed shifts.
        Uspace       -- 3D array of independent components of U matrices.
        pparameters   -- list of (xyz symbol, value) pairs
        Uparameters   -- list of (U symbol, value) pairs
    """

    Ucomponents = numpy.array([
            [[1,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,1,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,1]],
            [[0,1,0],[1,0,0],[0,0,0]],
            [[0,0,1],[0,0,0],[1,0,0]],
            [[0,0,0],[0,0,1],[0,1,0]] ], dtype=float)
    idx2Usymbol = { 0 : 'U11', 1 : 'U12', 2 : 'U13',
                    3 : 'U12', 4 : 'U22', 5 : 'U23',
                    6 : 'U13', 7 : 'U23', 8 : 'U33' }

    def __init__(self, spacegroup, xyz, Uij=numpy.zeros((3,3)),
            sgoffset=[0,0,0], eps=epsilon):
        """Initialize GeneratorSite.

        spacegroup -- instance of SpaceGroup
        xyz        -- generating site.  When xyz is close to special
                      position self.xyz will be adjusted.
        Uij        -- thermal factors at generator site.  Yields self.Uij
                      after adjusting to spacegroup symmetry.
        sgoffset   -- offset of space group origin [0, 0, 0]
        eps        -- cutoff for equal positions
        """
        # just declare the members
        self.xyz = None
        self.Uij = Uij
        self.sgoffset = numpy.array(sgoffset, dtype=float)
        self.eps = eps
        self.eqxyz = []
        self.eqUij = []
        self.symops = None
        self.multiplicity = None
        self.Uisotropy = False
        self.invariants = []
        self.null_space = None
        self.Uspace = None
        self.pparameters = []
        self.Uparameters = []
        # fill in the values
        self.xyz = xyz
        sites, ops, mult = expandPosition(spacegroup, xyz, sgoffset, eps)
        # shift self.xyz exactly to the special position
        if mult > 1:
            xyzdups = numpy.array([op(xyz + self.sgoffset) - self.sgoffset
                for op in ops[0]])
            dxyz = xyzdups - xyz
            dxyz = numpy.mean(dxyz - dxyz.round(), axis=0)
            # recalculate if needed
            if numpy.any(dxyz != 0.0):
                self.xyz = xyz + dxyz
                sites, ops, mult = expandPosition(spacegroup,
                        self.xyz, self.sgoffset, eps)
        # self.xyz, sites, ops are all adjusted here
        self.eqxyz = sites
        self.symops = ops
        self.multiplicity = mult
        # invariant operations are always first in self.symop
        self.invariants = self.symops[0]
        self._findNullSpace()
        self._findPosParameters()
        self._findUSpace()
        self._findUParameters()
        self._findeqUij()
        return

    def signedRatStr(self, x):
        """Convert floating point number to signed rational representation.
        Possible fractional are multiples of 1/3, 1/6, 1/7, 1/9, if these
        are not close, return "%+g" format.

        Return string.
        """
        s = str(x)
        if len(s) < 6:  return "%+g" % x
        den = numpy.array([3.0, 6.0, 7.0, 9.0])
        nom = x * den
        idx = numpy.where(numpy.fabs(nom - nom.round()) < self.eps)[0]
        if idx.size == 0:   return "%+g" % x
        # here we have fraction
        return "%+.0f/%.0f" % (nom[idx[0]], den[idx[0]])

    def _findNullSpace(self):
        """Calculate self.null_space from self.invariants.
        Try to represent self.null_space using small integers.
        """
        R0 = self.invariants[0].R
        Rdiff = [ (symop.R - R0) for symop in self.invariants ]
        Rdiff = numpy.concatenate(Rdiff, 0)
        self.null_space = nullSpace(Rdiff)
        if self.null_space.size == 0:   return
        # reverse sort rows of null_space rows by absolute value
        key = tuple(numpy.fabs(numpy.transpose(self.null_space))[::-1])
        order = numpy.lexsort(key)
        self.null_space = self.null_space[order[::-1]]
        # rationalize by the smallest element larger than cutoff
        cutoff = 1.0/32
        for i in range(len(self.null_space)):
            row = self.null_space[i]
            small = numpy.fabs(row[numpy.fabs(row) > cutoff]).min()
            signedsmall = row[numpy.fabs(row) == small][0]
            self.null_space[i] = self.null_space[i] / signedsmall
        return

    def _findPosParameters(self):
        """Find pparameters and their values for expressing self.xyz.
        """
        usedsymbol = {}
        # parameter values depend on offset of self.xyz
        txyz = self.xyz
        # define txyz such that most of its elements are zero
        for nvec in self.null_space:
            idx = numpy.where(numpy.fabs(nvec) >= epsilon)[0][0]
            varvalue = txyz[idx]/nvec[idx]
            txyz = txyz - varvalue*nvec
            # determine standard parameter name
            vname = [s for s in "xyz"[idx:] if not s in usedsymbol][0]
            self.pparameters.append( (vname, varvalue) )
            usedsymbol[vname] = True
        return

    def _findUSpace(self):
        """Find independent U components with respect to invariant
        rotations.
        """
        self.Uspace = []
        independent = dict.fromkeys(range(6))
        for idx in range(6):
            if idx not in independent:   continue
            # new U space matrix
            Usp = numpy.zeros((3,3), dtype=float)
            Uc = self.Ucomponents[idx]
            for op in self.invariants:
                R = op.R
                Rt = R.transpose()
                Uceq = numpy.dot(R, numpy.dot(Uc, Rt))
                # does Uceq contain -Uc?
                if numpy.all(Uceq*Uc == -Uc):
                    Usp[:] = 0.0
                    break
                for icomp in range(idx,6):
                    if icomp not in independent:   continue
                    Uceqcomp = Uceq * self.Ucomponents[icomp]
                    if not numpy.any(Uceqcomp): continue
                    # here Uceq contains U component icomp
                    Usp += Uceqcomp
                    del independent[icomp]
            if not numpy.any(Usp):  continue
            # make sure first element is 1.0
            flat = Usp.flatten()
            first = flat[flat != 0.0][0]
            Usp /= first
            self.Uspace.append(Usp)
        # finally convert this to 3D array
        self.Uspace = numpy.array(self.Uspace)
        self.Uisotropy = ( len(self.Uspace) == 1 )
        return

    def _findUParameters(self):
        """Find Uparameters and their values for expressing self.Uij.
        """
        Uij = self.Uij
        for Usp in self.Uspace:
            idx = numpy.where(Usp.flatten())[0][0]
            vname = self.idx2Usymbol[idx]
            varvalue = ((Uij + numpy.transpose(Uij))*Usp).sum()/(2*Usp.sum())
            self.Uparameters.append( (vname, varvalue) )
        return

    def _findeqUij(self):
        """Adjust self.Uij and self.eqUij to be consistent with spacegroup
        """
        self.Uij = numpy.zeros((3,3), dtype=float)
        for i in range(len(self.Uparameters)):
            Usp = self.Uspace[i]
            varvalue = self.Uparameters[i][1]
            self.Uij += varvalue*Usp
        # now determine eqUij
        for ops in self.symops:
            # take first rotation matrix
            R = ops[0].R
            Rt = R.transpose()
            self.eqUij.append( numpy.dot(R, numpy.dot(self.Uij, Rt)) )
        return

    def positionFormula(self, pos, xyzsymbols=("x","y","z")):
        """Formula of equivalent position with respect to generator site

        pos        -- fractional coordinates of possibly equivalent site
        xyzsymbols -- symbols for parametrized coordinates

        Return position formulas in a dictionary with keys equal ("x", "y", "z")
        or an empty dictionary when pos is not equivalent to generator.
        Formulas are formatted as "[[-][%g*]{x|y|z}] [{+|-}%g]", for example
        "-x", "z +0.5", "0.25".
        """
        # find pos in eqxyz
        idx = nearestSiteIndex(self.eqxyz, pos)
        eqpos = self.eqxyz[idx]
        if not equalPositions(eqpos, pos, self.eps):    return {}
        # any rotation matrix should do fine
        R = self.symops[idx][0].R
        nsrotated = numpy.dot(self.null_space, numpy.transpose(R))
        # build formulas using eqpos
        # find offset
        teqpos = numpy.array(eqpos)
        for nvec, (vname, varvalue) in zip(nsrotated, self.pparameters):
            teqpos -= nvec * varvalue
        # map varnames to xyzsymbols
        name2sym = dict( zip(("x", "y", "z"), xyzsymbols) )
        xyzformula = 3*[""]
        for nvec, (vname, ignore) in zip(nsrotated, self.pparameters):
            for i in range(3):
                if abs(nvec[i]) < epsilon:  continue
                xyzformula[i] += "%s*%s " % \
                        (self.signedRatStr(nvec[i]), name2sym[vname])
        # add constant offset teqpos to all formulas
        for i in range(3):
            if xyzformula[i] and abs(teqpos[i]) < epsilon: continue
            xyzformula[i] += self.signedRatStr(teqpos[i])
        # reduce unnecessary +1* and -1*
        xyzformula = [ re.sub('^[+]1[*]|(?<=[+-])1[*]', '', f).strip()
                       for f in xyzformula ]
        return dict( zip(("x","y","z"), xyzformula) )

    def UFormula(self, pos, Usymbols=stdUsymbols):
        """List of atom displacement formulas with custom parameter symbols.

        pos        -- fractional coordinates of possibly equivalent site
        Usymbols   -- 6 symbols for possible U matrix parameters

        Return U element formulas in a dictionary where keys are from
        ('U11','U22','U33','U12','U13','U23') or empty dictionary when
        pos is not equivalent to generator.
        """
        # find pos in eqxyz
        idx = nearestSiteIndex(self.eqxyz, pos)
        eqpos = self.eqxyz[idx]
        if not equalPositions(eqpos, pos, self.eps):    return {}
        # any rotation matrix should do fine
        R = self.symops[idx][0].R
        Rt = R.transpose()
        Usrotated = [numpy.dot(R, numpy.dot(Us, Rt)) for Us in self.Uspace]
        Uformula = dict.fromkeys(stdUsymbols, '0')
        name2sym = dict(zip(stdUsymbols, Usymbols))
        for Usr, (vname, ignore) in zip(Usrotated, self.Uparameters):
            Usrflat = Usr.flatten()
            for i in numpy.where(Usrflat)[0]:
                f = '%+g*%s' % (Usrflat[i], name2sym[vname])
                f = re.sub('^[+]1[*]|(?<=[+-])1[*]', '', f).strip()
                smbl = self.idx2Usymbol[i]
                Uformula[smbl] = f
        return Uformula

    def eqIndex(self, pos):
        """Index of the nearest generator equivalent site

        pos -- fractional coordinates

        Return integer.
        """
        return nearestSiteIndex(self.eqxyz, pos)

# End of class GeneratorSite

class ExpandAsymmetricUnit:
    """Expand asymmetric unit and anisotropic thermal displacement

    Data members:
        spacegroup  -- instance of SpaceGroup
        corepos     -- list of positions in asymmetric unit,
                       it may contain duplicates
        coreUijs    -- thermal factors for corepos (defaults to zeros)
        sgoffset    -- optional offset of space group origin [0, 0, 0]
        eps         -- cutoff for equivalent positions
    Calculated data members:
        multiplicities -- multiplicity of sites in corepos
        Uisotropy   -- bool flags for isotropic sites in corepos
        expandedpos -- list of equivalent positions per each site in corepos
        expandedUijs -- list of thermal factors per each site in corepos
    """

    # By design Atom instances are not accepted as arguments to keep
    # number of required imports low.
    def __init__(self, spacegroup, corepos, coreUijs=None,
            sgoffset=[0,0,0], eps=0.0):
        """Initialize and calculate instance of ExpandAsymmetricUnit

        spacegroup   -- instance of SpaceGroup
        corepos      -- list of positions in asymmetric unit,
                        it may contain duplicates
        coreUijs     -- thermal factors for corepos (defaults to zeros)
        sgoffset     -- offset of space group origin [0, 0, 0]
        eps          -- cutoff for duplicate positions
        """
        # declare data members
        self.spacegroup = spacegroup
        self.corepos = corepos
        self.coreUijs = None
        self.sgoffset = numpy.array(sgoffset)
        self.eps = eps
        self.multiplicity = []
        self.Uisotropy = []
        self.expandedpos = []
        self.expandedUijs = []
        # obtain their values
        corelen = len(self.corepos)
        if coreUijs:
            self.coreUijs = coreUijs
        else:
            self.coreUijs = numpy.zeros((corelen,3,3), dtype=float)
        for cpos, cUij in zip(self.corepos, self.coreUijs):
            gen = GeneratorSite(self.spacegroup, cpos, cUij,
                    self.sgoffset, self.eps)
            self.multiplicity.append(gen.multiplicity)
            self.Uisotropy.append(gen.Uisotropy)
            self.expandedpos.append(gen.eqxyz)
            self.expandedUijs.append(gen.eqUij)
        return

# End of ExpandAsymmetricUnit

# Helper function for SymmetryConstraints class
def pruneFormulaDictionary(eqdict):
    """Remove constant items from formula dictionary.

    Return pruned formula dictionary.
    """
    pruned = {}
    for smb, eq in eqdict.iteritems():
        if not isconstantFormula(eq):     pruned[smb] = eq
    return pruned

# End of pruneFormulaDictionary

class SymmetryConstraints:
    """Generate symmetry constraints for specified positions

    Data members:
        spacegroup -- instance of SpaceGroup
        positions  -- all positions to be constrained
        Uijs       -- thermal factors for all positions (defaults to zeros)
        sgoffset   -- optional offset of space group origin [0, 0, 0]
        eps        -- cutoff for equivalent positions
    Calculated data members:
        poseqns    -- list of coordinate formula dictionaries per each site.
                      Formula dictionary keys are from ("x", "y", "z") and
                      the values are formatted as [[-]{x|y|z}%i] [{+|-}%g],
                      for example: "x0", "-x3", "z7 +0.5", "0.25".
        pospars    -- list of (xyz symbol, value) pairs
        Ueqns      -- list of anisotropic atomic displacement formula
                      dictionaries per each position.  Formula dictionary
                      keys are from ('U11','U22','U33','U12','U13','U23')
                      and the values are formatted as {[%g*][Uij%i]|0},
                      for example: "U110", "0.5*U2213", "0"
        Upars      -- list of (U symbol, value) pairs
        Uisotropy  -- list of bool flags for isotropic thermal displacements
    """

    def __init__(self, spacegroup, positions, Uijs=None,
            sgoffset=[0,0,0], eps=epsilon):
        """Initialize and calculate SymmetryConstraints.

        spacegroup -- instance of SpaceGroup
        positions  -- list of all positions to be constrained
        Uijs       -- list of U matrices for all constrained positions
        sgoffset   -- optional offset of space group origin [0, 0, 0]
        eps        -- cutoff for equivalent positions
        """
        # fill in data members
        self.spacegroup = spacegroup
        self.positions = numpy.array(positions)
        self.Uijs = None
        self.sgoffset = numpy.array(sgoffset)
        self.eps = eps
        self.poseqns = None
        self.pospars = []
        self.Ueqns = None
        self.Upars = []
        self.Uisotropy = None
        # positions returned by expandAsymmetricUnit have 3 dimensions
        if self.positions.ndim == 3:
            self.positions = numpy.concatenate(self.positions, 0)
        # and make if work for a single position
        elif self.positions.ndim == 1 and self.positions.size == 3:
            self.positions = self.positions.reshape((1,3))
        numpos = len(self.positions)
        # adjust Uijs if not specified
        if not self.Uijs:
            self.Uijs = numpy.zeros((numpos,3,3), dtype=float)
        else:
            self.Uijs = numpy.array(self.Uijs)
        self.poseqns = numpos*[None]
        self.Ueqns = numpos*[None]
        self.Uisotropy = numpos*[False]
        # all members should be initialized here
        self._findConstraints()
        return

    def _findConstraints(self):
        """Find constraints for positions and anisotropic displacements Uij
        """
        numpos = len(self.positions)
        # canonical xyzsymbols and Usymbols
        xyzsymbols = [ smbl+str(i) for i in range(numpos) for smbl in "xyz" ]
        Usymbols = [smbl+str(i) for i in range(numpos) for smbl in stdUsymbols]
        independent = dict.fromkeys(range(numpos))
        for genidx in range(numpos):
            if not genidx in independent:   continue
            # it is a generator
            genpos = self.positions[genidx]
            genUij = self.Uijs[genidx]
            gen = GeneratorSite(self.spacegroup, genpos, genUij,
                    self.sgoffset, self.eps)
            # append new pparameters if there are any
            gxyzsymbols = xyzsymbols[3*genidx : 3*(genidx+1)]
            for k, v in gen.pparameters:
                smbl = gxyzsymbols["xyz".index(k)]
                self.pospars.append( (smbl, v) )
            gUsymbols = Usymbols[6*genidx : 6*(genidx+1)]
            for k, v in gen.Uparameters:
                smbl = gUsymbols[stdUsymbols.index(k)]
                self.Upars.append( (smbl, v) )
            # search for equivalents inside indies
            indies = independent.keys()
            indies.sort()
            for indidx in indies:
                indpos = self.positions[indidx]
                formula = gen.positionFormula(indpos, gxyzsymbols)
                # formula is empty when indidx is independent
                if not formula:  continue
                # indidx is dependent here
                del independent[indidx]
                self.poseqns[indidx] = formula
                self.Ueqns[indidx] = gen.UFormula(indpos, gUsymbols)
                # make sure positions and Uijs are consistent with spacegroup
                eqidx = gen.eqIndex(indpos)
                dxyz = gen.eqxyz[eqidx] - indpos
                self.positions[indidx] += dxyz - dxyz.round()
                self.Uijs[indidx] = gen.eqUij[eqidx]
        # all done here
        return

    def posparSymbols(self):
        """Return list of standard position parameter symbols.
        """
        return [n for n, v in self.pospars]

    def posparValues(self):
        """Return list of position parameters values.
        """
        return [v for n, v in self.pospars]

    def positionFormulas(self, xyzsymbols=None):
        """List of position formulas with custom parameter symbols.

        xyzsymbols -- list of custom symbols used in formula strings

        Return list of coordinate formulas dictionaries.  Formulas dictionary
        keys are from ("x", "y", "z") and the values are formatted as
        [[-]{symbol}] [{+|-}%g], for example: "x0", "-sym", "@7 +0.5", "0.25".
        """
        if not xyzsymbols:  return list(self.poseqns)
        # check xyzsymbols
        if len(xyzsymbols) < len(self.pospars):
            emsg = "Not enough symbols for %i position parameters" % \
                    len(self.pospars)
            raise SymmetryError, emsg
        # build translation dictionary
        trsmbl = dict(zip(self.posparSymbols(), xyzsymbols))
        def translatesymbol(matchobj):
            return trsmbl[matchobj.group(0)]
        pat = re.compile(r'\b[xyz]\d+')
        rv = []
        for eqns in self.poseqns:
            treqns = {}
            for smbl, eq in eqns.iteritems():
                treqns[smbl] = re.sub(pat, translatesymbol, eq)
            rv.append(treqns)
        return rv

    def positionFormulasPruned(self, xyzsymbols=None):
        """List of position formula dictionaries with constant items removed.
        See also positionFormulas().

        xyzsymbols -- list of custom symbols used in formula strings

        Return list of coordinate formula dictionaries.
        """
        rv = [  pruneFormulaDictionary(eqns)
                for eqns in self.positionFormulas(xyzsymbols) ]
        return rv

    def UparSymbols(self):
        """Return list of standard atom displacement parameter symbols.
        """
        return [n for n, v in self.Upars]

    def UparValues(self):
        """Return list of atom displacement parameters values.
        """
        return [v for n, v in self.Upars]

    def UFormulas(self, Usymbols=None):
        """List of atom displacement formulas with custom parameter symbols.

        Usymbols -- list of custom symbols used in formula strings

        Return list of atom displacement formula dictionaries per each site.
        Formula dictionary keys are from ('U11','U22','U33','U12','U13','U23')
        and the values are formatted as {[%g*][Usymbol]|0}, for example:
        "U11", "0.5*@37", "0".
        """
        if not Usymbols:  return list(self.Ueqns)
        # check Usymbols
        if len(Usymbols) < len(self.Upars):
            emsg = "Not enough symbols for %i U parameters" % len(self.Upars)
            raise SymmetryError, emsg
        # build translation dictionary
        trsmbl = dict(zip(self.UparSymbols(), Usymbols))
        def translatesymbol(matchobj):
            return trsmbl[matchobj.group(0)]
        pat = re.compile(r'\bU\d\d\d+')
        rv = []
        for eqns in self.Ueqns:
            treqns = {}
            for smbl, eq in eqns.iteritems():
                treqns[smbl] = re.sub(pat, translatesymbol, eq)
            rv.append(treqns)
        return rv

    def UFormulasPruned(self, Usymbols=None):
        """List of atom displacement formula dictionaries with constant items
        removed.  See also UFormulas().

        Usymbols -- list of custom symbols used in formula strings

        Return list of atom displacement formulas in tuples of
        (U11, U22, U33, U12, U13, U23).
        """
        rv = [  pruneFormulaDictionary(eqns)
                for eqns in self.UFormulas(Usymbols) ]
        return rv

# End of SymmetryConstraints

# basic demonstration
if __name__ == "__main__":
    from SpaceGroups import sg100
    site = [.125, .625, .13]
    Uij = [[1,2,3],[2,4,5],[3,5,6]]
    g = GeneratorSite(sg100, site, Uij=Uij)
    fm100 = g.positionFormula(site)
    print "g = GeneratorSite(sg100, %r)" % site
    print "g.positionFormula(%r) = %s" % (site, fm100)
    print "g.pparameters =", g.pparameters
    print "g.Uparameters =", g.Uparameters
    print "g.UFormula(%r) =" % site, g.UFormula(site)

# End of file