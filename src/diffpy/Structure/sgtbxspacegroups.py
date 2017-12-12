#!/usr/bin/env python
##############################################################################
#
# diffpy.Structure  by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2009 Trustees of the Columbia University
#                   in the City of New York.  All rights reserved.
#
# File coded by:    Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE_DANSE.txt for license information.
#
##############################################################################

'''Extra space group representations generated using sgtbx module from cctbx.
Import of this module extends the SpaceGroupList in the SpaceGroups module.
Notable variables:

sgtbxSpaceGroupList -- list of space group instances defined in this module
'''


from diffpy.Structure.spacegroupmod import SpaceGroup, SymOp
from diffpy.Structure.spacegroupmod import (
    Rot_X_Y_Z, Rot_mX_mY_mZ, Rot_mX_Y_mZ, Rot_X_mY_Z,
    Rot_mX_mY_Z, Rot_X_mY_mZ, Rot_mX_Y_Z, Rot_X_Y_mZ,
    Tr_0_0_0, Tr_0_12_0, Tr_12_12_0, Tr_0_0_12,
    Tr_12_12_12, Tr_0_12_12, Tr_12_0_12, Tr_12_0_0,
    Tr_14_14_14, Tr_14_34_34, Tr_34_14_34, Tr_34_34_14,
)


##############################################################################
# generated using sgtbx_extra_groups.py
##############################################################################

sg2003 = SpaceGroup(
    number = 2003,
    num_sym_equiv = 2,
    num_primitive_sym_equiv = 2,
    short_name = 'P211',
    point_group_name = 'PG2',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 2 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
    ]
)

sg2004 = SpaceGroup(
    number = 2004,
    num_sym_equiv = 2,
    num_primitive_sym_equiv = 2,
    short_name = 'P2111',
    point_group_name = 'PG2',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 21 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
    ]
)

sg4005 = SpaceGroup(
    number = 4005,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'A121',
    point_group_name = 'PG2',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 2 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
    ]
)

sg5005 = SpaceGroup(
    number = 5005,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'I121',
    point_group_name = 'PG2',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 2 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
    ]
)

sg6005 = SpaceGroup(
    number = 6005,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'A112',
    point_group_name = 'PG2',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 1 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
    ]
)

sg7005 = SpaceGroup(
    number = 7005,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'I112',
    point_group_name = 'PG2',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 1 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
    ]
)

sg8005 = SpaceGroup(
    number = 8005,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'B211',
    point_group_name = 'PG2',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'B 2 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
    ]
)

sg9005 = SpaceGroup(
    number = 9005,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'C211',
    point_group_name = 'PG2',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'C 2 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
    ]
)

sg10005 = SpaceGroup(
    number = 10005,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'I211',
    point_group_name = 'PG2',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 2 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
    ]
)

sg2006 = SpaceGroup(
    number = 2006,
    num_sym_equiv = 2,
    num_primitive_sym_equiv = 2,
    short_name = 'Pm11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P m 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
    ]
)

sg2007 = SpaceGroup(
    number = 2007,
    num_sym_equiv = 2,
    num_primitive_sym_equiv = 2,
    short_name = 'P1n1',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 n 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
    ]
)

sg3007 = SpaceGroup(
    number = 3007,
    num_sym_equiv = 2,
    num_primitive_sym_equiv = 2,
    short_name = 'P1a1',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 a 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
    ]
)

sg4007 = SpaceGroup(
    number = 4007,
    num_sym_equiv = 2,
    num_primitive_sym_equiv = 2,
    short_name = 'P11a',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 1 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg5007 = SpaceGroup(
    number = 5007,
    num_sym_equiv = 2,
    num_primitive_sym_equiv = 2,
    short_name = 'P11n',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 1 n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg6007 = SpaceGroup(
    number = 6007,
    num_sym_equiv = 2,
    num_primitive_sym_equiv = 2,
    short_name = 'Pb11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P b 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
    ]
)

sg7007 = SpaceGroup(
    number = 7007,
    num_sym_equiv = 2,
    num_primitive_sym_equiv = 2,
    short_name = 'Pn11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P n 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
    ]
)

sg8007 = SpaceGroup(
    number = 8007,
    num_sym_equiv = 2,
    num_primitive_sym_equiv = 2,
    short_name = 'Pc11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P c 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
    ]
)

sg2008 = SpaceGroup(
    number = 2008,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'A1m1',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 m 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
    ]
)

sg3008 = SpaceGroup(
    number = 3008,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'I1m1',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 m 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
    ]
)

sg4008 = SpaceGroup(
    number = 4008,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'A11m',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 1 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg5008 = SpaceGroup(
    number = 5008,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'I11m',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 1 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg6008 = SpaceGroup(
    number = 6008,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Bm11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'B m 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
    ]
)

sg7008 = SpaceGroup(
    number = 7008,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Cm11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'C m 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
    ]
)

sg8008 = SpaceGroup(
    number = 8008,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Im11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I m 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
    ]
)

sg2009 = SpaceGroup(
    number = 2009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'A1n1',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 n 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
    ]
)

sg3009 = SpaceGroup(
    number = 3009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'I1a1',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 a 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
    ]
)

sg4009 = SpaceGroup(
    number = 4009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'A1a1',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 a 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
    ]
)

sg5009 = SpaceGroup(
    number = 5009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'C1n1',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'C 1 n 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
    ]
)

sg6009 = SpaceGroup(
    number = 6009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'I1c1',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 c 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
    ]
)

sg7009 = SpaceGroup(
    number = 7009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'A11a',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 1 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg8009 = SpaceGroup(
    number = 8009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'B11n',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'B 1 1 n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg9009 = SpaceGroup(
    number = 9009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'I11b',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 1 b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg10009 = SpaceGroup(
    number = 10009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'A11n',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 1 n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg11009 = SpaceGroup(
    number = 11009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'I11a',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 1 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg12009 = SpaceGroup(
    number = 12009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Bb11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'B b 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
    ]
)

sg13009 = SpaceGroup(
    number = 13009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Cn11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'C n 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
    ]
)

sg14009 = SpaceGroup(
    number = 14009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Ic11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I c 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
    ]
)

sg15009 = SpaceGroup(
    number = 15009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Cc11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'C c 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
    ]
)

sg16009 = SpaceGroup(
    number = 16009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Bn11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'B n 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
    ]
)

sg17009 = SpaceGroup(
    number = 17009,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Ib11',
    point_group_name = 'PGm',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I b 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
    ]
)

sg2010 = SpaceGroup(
    number = 2010,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2/m11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 2/m 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
    ]
)

sg2011 = SpaceGroup(
    number = 2011,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21/m11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 21/m 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
    ]
)

sg2012 = SpaceGroup(
    number = 2012,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A12/m1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 2/m 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
    ]
)

sg3012 = SpaceGroup(
    number = 3012,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I12/m1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 2/m 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
    ]
)

sg4012 = SpaceGroup(
    number = 4012,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A112/m',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 1 2/m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg5012 = SpaceGroup(
    number = 5012,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I112/m',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 1 2/m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg6012 = SpaceGroup(
    number = 6012,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'B2/m11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'B 2/m 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
    ]
)

sg7012 = SpaceGroup(
    number = 7012,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'C2/m11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'C 2/m 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
    ]
)

sg8012 = SpaceGroup(
    number = 8012,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I2/m11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 2/m 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
    ]
)

sg2013 = SpaceGroup(
    number = 2013,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P12/n1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 2/n 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
    ]
)

sg3013 = SpaceGroup(
    number = 3013,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P12/a1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 2/a 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
    ]
)

sg4013 = SpaceGroup(
    number = 4013,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P112/a',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 1 2/a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg5013 = SpaceGroup(
    number = 5013,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P112/n',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 1 2/n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg6013 = SpaceGroup(
    number = 6013,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2/b11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 2/b 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
    ]
)

sg7013 = SpaceGroup(
    number = 7013,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2/n11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 2/n 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
    ]
)

sg8013 = SpaceGroup(
    number = 8013,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2/c11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 2/c 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
    ]
)

sg2014 = SpaceGroup(
    number = 2014,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P121/n1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 21/n 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
    ]
)

sg3014 = SpaceGroup(
    number = 3014,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P121/a1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 21/a 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
    ]
)

sg4014 = SpaceGroup(
    number = 4014,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P1121/a',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 1 21/a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg5014 = SpaceGroup(
    number = 5014,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P1121/n',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 1 1 21/n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg6014 = SpaceGroup(
    number = 6014,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21/b11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 21/b 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
    ]
)

sg7014 = SpaceGroup(
    number = 7014,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21/n11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 21/n 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
    ]
)

sg8014 = SpaceGroup(
    number = 8014,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21/c11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'P 21/c 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
    ]
)

sg2015 = SpaceGroup(
    number = 2015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A12/n1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 2/n 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
    ]
)

sg3015 = SpaceGroup(
    number = 3015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I12/a1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 2/a 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
    ]
)

sg4015 = SpaceGroup(
    number = 4015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A12/a1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 2/a 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
    ]
)

sg5015 = SpaceGroup(
    number = 5015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'C12/n1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'C 1 2/n 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
    ]
)

sg6015 = SpaceGroup(
    number = 6015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I12/c1',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 2/c 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
    ]
)

sg7015 = SpaceGroup(
    number = 7015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A112/a',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 1 2/a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg8015 = SpaceGroup(
    number = 8015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'B112/n',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'B 1 1 2/n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg9015 = SpaceGroup(
    number = 9015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I112/b',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 1 2/b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg10015 = SpaceGroup(
    number = 10015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A112/n',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'A 1 1 2/n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg11015 = SpaceGroup(
    number = 11015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I112/a',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 1 1 2/a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg12015 = SpaceGroup(
    number = 12015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'B2/b11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'B 2/b 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
    ]
)

sg13015 = SpaceGroup(
    number = 13015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'C2/n11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'C 2/n 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
    ]
)

sg14015 = SpaceGroup(
    number = 14015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I2/c11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 2/c 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
    ]
)

sg15015 = SpaceGroup(
    number = 15015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'C2/c11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'C 2/c 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
    ]
)

sg16015 = SpaceGroup(
    number = 16015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'B2/n11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'B 2/n 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
    ]
)

sg17015 = SpaceGroup(
    number = 17015,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I2/b11',
    point_group_name = 'PG2/m',
    crystal_system = 'MONOCLINIC',
    pdb_name = 'I 2/b 1 1',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
    ]
)

sg2020 = SpaceGroup(
    number = 2020,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A2122',
    point_group_name = 'PG222',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A 21 2 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
    ]
)

sg3020 = SpaceGroup(
    number = 3020,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'B2212',
    point_group_name = 'PG222',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B 2 21 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
    ]
)

sg2021 = SpaceGroup(
    number = 2021,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A222',
    point_group_name = 'PG222',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A 2 2 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
    ]
)

sg3021 = SpaceGroup(
    number = 3021,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'B222',
    point_group_name = 'PG222',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B 2 2 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
    ]
)

sg1025 = SpaceGroup(
    number = 1025,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2mm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 2 m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg2025 = SpaceGroup(
    number = 2025,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pm2m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m 2 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg1026 = SpaceGroup(
    number = 1026,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pcm21',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c m 21',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
    ]
)

sg2026 = SpaceGroup(
    number = 2026,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21ma',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 21 m a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg3026 = SpaceGroup(
    number = 3026,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21am',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 21 a m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg4026 = SpaceGroup(
    number = 4026,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pb21m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b 21 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg5026 = SpaceGroup(
    number = 5026,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pm21b',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m 21 b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg1027 = SpaceGroup(
    number = 1027,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2aa',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 2 a a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg2027 = SpaceGroup(
    number = 2027,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pb2b',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b 2 b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg1028 = SpaceGroup(
    number = 1028,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pbm2',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b m 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
    ]
)

sg2028 = SpaceGroup(
    number = 2028,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2mb',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 2 m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg3028 = SpaceGroup(
    number = 3028,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2cm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 2 c m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg4028 = SpaceGroup(
    number = 4028,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pc2m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c 2 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg5028 = SpaceGroup(
    number = 5028,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pm2a',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m 2 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg1029 = SpaceGroup(
    number = 1029,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pbc21',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b c 21',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
    ]
)

sg2029 = SpaceGroup(
    number = 2029,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21ab',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 21 a b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg3029 = SpaceGroup(
    number = 3029,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21ca',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 21 c a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg4029 = SpaceGroup(
    number = 4029,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pc21b',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c 21 b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg5029 = SpaceGroup(
    number = 5029,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pb21a',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b 21 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg1030 = SpaceGroup(
    number = 1030,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pcn2',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c n 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
    ]
)

sg2030 = SpaceGroup(
    number = 2030,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2na',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 2 n a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg3030 = SpaceGroup(
    number = 3030,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2an',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 2 a n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg4030 = SpaceGroup(
    number = 4030,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pb2n',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b 2 n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg5030 = SpaceGroup(
    number = 5030,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pn2b',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n 2 b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg1031 = SpaceGroup(
    number = 1031,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pnm21',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n m 21',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
    ]
)

sg2031 = SpaceGroup(
    number = 2031,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21mn',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 21 m n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg3031 = SpaceGroup(
    number = 3031,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21nm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 21 n m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg4031 = SpaceGroup(
    number = 4031,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pn21m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n 21 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg5031 = SpaceGroup(
    number = 5031,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pm21n',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m 21 n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg1032 = SpaceGroup(
    number = 1032,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2cb',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 2 c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2032 = SpaceGroup(
    number = 2032,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pc2a',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c 2 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg1033 = SpaceGroup(
    number = 1033,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pbn21',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b n 21',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
    ]
)

sg2033 = SpaceGroup(
    number = 2033,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21nb',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 21 n b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg3033 = SpaceGroup(
    number = 3033,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P21cn',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 21 c n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg4033 = SpaceGroup(
    number = 4033,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pc21n',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c 21 n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg5033 = SpaceGroup(
    number = 5033,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pn21a',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n 21 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg1034 = SpaceGroup(
    number = 1034,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'P2nn',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P 2 n n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg2034 = SpaceGroup(
    number = 2034,
    num_sym_equiv = 4,
    num_primitive_sym_equiv = 4,
    short_name = 'Pn2n',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n 2 n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg1035 = SpaceGroup(
    number = 1035,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A2mm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A 2 m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2035 = SpaceGroup(
    number = 2035,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Bm2m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B m 2 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg1036 = SpaceGroup(
    number = 1036,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Ccm21',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C c m 21',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
    ]
)

sg2036 = SpaceGroup(
    number = 2036,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A21ma',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A 21 m a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg3036 = SpaceGroup(
    number = 3036,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A21am',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A 21 a m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg4036 = SpaceGroup(
    number = 4036,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Bb21m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B b 21 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg5036 = SpaceGroup(
    number = 5036,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Bm21b',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B m 21 b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg1037 = SpaceGroup(
    number = 1037,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'A2aa',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A 2 a a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg2037 = SpaceGroup(
    number = 2037,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Bb2b',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B b 2 b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg1038 = SpaceGroup(
    number = 1038,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Bmm2',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B m m 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
    ]
)

sg2038 = SpaceGroup(
    number = 2038,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'B2mm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B 2 m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg3038 = SpaceGroup(
    number = 3038,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'C2mm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C 2 m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg4038 = SpaceGroup(
    number = 4038,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Cm2m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C m 2 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg5038 = SpaceGroup(
    number = 5038,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Am2m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A m 2 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg1039 = SpaceGroup(
    number = 1039,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Bma2',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B m a 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
    ]
)

sg2039 = SpaceGroup(
    number = 2039,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'B2cm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B 2 c m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg3039 = SpaceGroup(
    number = 3039,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'C2mb',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C 2 m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg4039 = SpaceGroup(
    number = 4039,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Cm2a',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C m 2 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg5039 = SpaceGroup(
    number = 5039,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Ac2m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A c 2 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg1040 = SpaceGroup(
    number = 1040,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Bbm2',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B b m 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
    ]
)

sg2040 = SpaceGroup(
    number = 2040,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'B2mb',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B 2 m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg3040 = SpaceGroup(
    number = 3040,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'C2cm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C 2 c m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg4040 = SpaceGroup(
    number = 4040,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Cc2m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C c 2 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg5040 = SpaceGroup(
    number = 5040,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Am2a',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A m 2 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg1041 = SpaceGroup(
    number = 1041,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Bba2',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B b a 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
    ]
)

sg2041 = SpaceGroup(
    number = 2041,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'B2cb',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B 2 c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg3041 = SpaceGroup(
    number = 3041,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'C2cb',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C 2 c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg4041 = SpaceGroup(
    number = 4041,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Cc2a',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C c 2 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg5041 = SpaceGroup(
    number = 5041,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Ac2a',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A c 2 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg1042 = SpaceGroup(
    number = 1042,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'F2mm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'F 2 m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg2042 = SpaceGroup(
    number = 2042,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Fm2m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'F m 2 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg1043 = SpaceGroup(
    number = 1043,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'F2dd',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'F 2 d d',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_14_14_14),
        SymOp(Rot_X_Y_mZ, Tr_14_14_14),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_14_34_34),
        SymOp(Rot_X_Y_mZ, Tr_14_34_34),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_34_14_34),
        SymOp(Rot_X_Y_mZ, Tr_34_14_34),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_34_34_14),
        SymOp(Rot_X_Y_mZ, Tr_34_34_14),
    ]
)

sg2043 = SpaceGroup(
    number = 2043,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Fd2d',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'F d 2 d',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_14_14_14),
        SymOp(Rot_X_Y_mZ, Tr_14_14_14),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_14_34_34),
        SymOp(Rot_X_Y_mZ, Tr_14_34_34),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_34_14_34),
        SymOp(Rot_X_Y_mZ, Tr_34_14_34),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_34_34_14),
        SymOp(Rot_X_Y_mZ, Tr_34_34_14),
    ]
)

sg1044 = SpaceGroup(
    number = 1044,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I2mm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I 2 m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg2044 = SpaceGroup(
    number = 2044,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Im2m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I m 2 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg1045 = SpaceGroup(
    number = 1045,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I2cb',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I 2 c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2045 = SpaceGroup(
    number = 2045,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Ic2a',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I c 2 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg1046 = SpaceGroup(
    number = 1046,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Ibm2',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I b m 2',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
    ]
)

sg2046 = SpaceGroup(
    number = 2046,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I2mb',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I 2 m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg3046 = SpaceGroup(
    number = 3046,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'I2cm',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I 2 c m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg4046 = SpaceGroup(
    number = 4046,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Ic2m',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I c 2 m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg5046 = SpaceGroup(
    number = 5046,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Im2a',
    point_group_name = 'PGmm2',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I m 2 a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg1049 = SpaceGroup(
    number = 1049,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmaa',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m a a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg2049 = SpaceGroup(
    number = 2049,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbmb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg1050 = SpaceGroup(
    number = 1050,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pncb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2050 = SpaceGroup(
    number = 2050,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pncb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg3050 = SpaceGroup(
    number = 3050,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcna',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c n a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg4050 = SpaceGroup(
    number = 4050,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcna',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c n a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg1051 = SpaceGroup(
    number = 1051,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmmb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg2051 = SpaceGroup(
    number = 2051,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg3051 = SpaceGroup(
    number = 3051,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg4051 = SpaceGroup(
    number = 4051,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmcm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m c m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg5051 = SpaceGroup(
    number = 5051,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmam',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m a m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg1052 = SpaceGroup(
    number = 1052,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pnnb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n n b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg2052 = SpaceGroup(
    number = 2052,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbnn',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b n n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg3052 = SpaceGroup(
    number = 3052,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcnn',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c n n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg4052 = SpaceGroup(
    number = 4052,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pncn',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n c n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg5052 = SpaceGroup(
    number = 5052,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pnan',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n a n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg1053 = SpaceGroup(
    number = 1053,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pnmb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2053 = SpaceGroup(
    number = 2053,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbmn',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b m n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg3053 = SpaceGroup(
    number = 3053,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcnm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c n m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg4053 = SpaceGroup(
    number = 4053,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pncm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n c m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg5053 = SpaceGroup(
    number = 5053,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pman',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m a n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg1054 = SpaceGroup(
    number = 1054,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pccb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg2054 = SpaceGroup(
    number = 2054,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbaa',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b a a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg3054 = SpaceGroup(
    number = 3054,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcaa',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c a a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg4054 = SpaceGroup(
    number = 4054,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbcb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg5054 = SpaceGroup(
    number = 5054,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbab',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b a b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg1055 = SpaceGroup(
    number = 1055,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmcb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2055 = SpaceGroup(
    number = 2055,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcma',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c m a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg1056 = SpaceGroup(
    number = 1056,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pnaa',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n a a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg2056 = SpaceGroup(
    number = 2056,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbnb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b n b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg1057 = SpaceGroup(
    number = 1057,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcam',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c a m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg2057 = SpaceGroup(
    number = 2057,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmca',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m c a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg3057 = SpaceGroup(
    number = 3057,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmab',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m a b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg4057 = SpaceGroup(
    number = 4057,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbma',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b m a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg5057 = SpaceGroup(
    number = 5057,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcmb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg1058 = SpaceGroup(
    number = 1058,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmnn',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m n n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg2058 = SpaceGroup(
    number = 2058,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pnmn',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n m n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg2059 = SpaceGroup(
    number = 2059,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pnmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg3059 = SpaceGroup(
    number = 3059,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pnmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg4059 = SpaceGroup(
    number = 4059,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmnm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m n m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
    ]
)

sg5059 = SpaceGroup(
    number = 5059,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmnm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m n m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg1060 = SpaceGroup(
    number = 1060,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcan',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c a n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg2060 = SpaceGroup(
    number = 2060,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pnca',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n c a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
    ]
)

sg3060 = SpaceGroup(
    number = 3060,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pnab',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n a b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg4060 = SpaceGroup(
    number = 4060,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbna',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b n a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg5060 = SpaceGroup(
    number = 5060,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcnb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c n b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg1061 = SpaceGroup(
    number = 1061,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcab',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c a b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg1062 = SpaceGroup(
    number = 1062,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmnb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m n b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2062 = SpaceGroup(
    number = 2062,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pbnm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P b n m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg3062 = SpaceGroup(
    number = 3062,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pcmn',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P c m n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg4062 = SpaceGroup(
    number = 4062,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pmcn',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P m c n',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg5062 = SpaceGroup(
    number = 5062,
    num_sym_equiv = 8,
    num_primitive_sym_equiv = 8,
    short_name = 'Pnam',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'P n a m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg1063 = SpaceGroup(
    number = 1063,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Ccmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C c m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg2063 = SpaceGroup(
    number = 2063,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Amma',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A m m a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg3063 = SpaceGroup(
    number = 3063,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Amam',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A m a m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg4063 = SpaceGroup(
    number = 4063,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bbmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B b m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg5063 = SpaceGroup(
    number = 5063,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bmmb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B m m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg1064 = SpaceGroup(
    number = 1064,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Ccmb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C c m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2064 = SpaceGroup(
    number = 2064,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Abma',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A b m a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg3064 = SpaceGroup(
    number = 3064,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Acam',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A c a m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg4064 = SpaceGroup(
    number = 4064,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bbcm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B b c m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg5064 = SpaceGroup(
    number = 5064,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bmab',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B m a b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg1065 = SpaceGroup(
    number = 1065,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Ammm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A m m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2065 = SpaceGroup(
    number = 2065,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bmmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B m m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg1066 = SpaceGroup(
    number = 1066,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Amaa',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A m a a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg2066 = SpaceGroup(
    number = 2066,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bbmb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B b m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg1067 = SpaceGroup(
    number = 1067,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Cmmb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C m m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg2067 = SpaceGroup(
    number = 2067,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Abmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A b m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg3067 = SpaceGroup(
    number = 3067,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Acmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A c m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg4067 = SpaceGroup(
    number = 4067,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bmcm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B m c m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg5067 = SpaceGroup(
    number = 5067,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bmam',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B m a m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
    ]
)

sg1068 = SpaceGroup(
    number = 1068,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Cccb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'C c c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
    ]
)

sg2068 = SpaceGroup(
    number = 2068,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Abaa',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A b a a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg3068 = SpaceGroup(
    number = 3068,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Abaa',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A b a a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg4068 = SpaceGroup(
    number = 4068,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Acaa',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'A c a a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg5068 = SpaceGroup(
    number = 5068,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bbcb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B b c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg6068 = SpaceGroup(
    number = 6068,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bbcb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B b c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg7068 = SpaceGroup(
    number = 7068,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Bbab',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'B b a b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg1072 = SpaceGroup(
    number = 1072,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Imcb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I m c b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2072 = SpaceGroup(
    number = 2072,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Icma',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I c m a',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_12),
    ]
)

sg1073 = SpaceGroup(
    number = 1073,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Icab',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I c a b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg1074 = SpaceGroup(
    number = 1074,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Immb',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I m m b',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_12_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_12_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_0_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_0_12_12),
    ]
)

sg2074 = SpaceGroup(
    number = 2074,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Ibmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I b m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_12),
        SymOp(Rot_X_mY_Z, Tr_0_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_0),
        SymOp(Rot_X_mY_Z, Tr_12_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

sg3074 = SpaceGroup(
    number = 3074,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Icmm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I c m m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_12_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_12_0),
        SymOp(Rot_X_mY_Z, Tr_0_12_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_0_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_0_12),
        SymOp(Rot_X_mY_Z, Tr_12_0_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg4074 = SpaceGroup(
    number = 4074,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Imcm',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I m c m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_12_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_12_0_0),
        SymOp(Rot_mX_mY_Z, Tr_0_0_0),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_12_0_0),
        SymOp(Rot_X_mY_Z, Tr_12_0_0),
        SymOp(Rot_X_Y_mZ, Tr_0_0_0),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_0_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_0_12_12),
        SymOp(Rot_mX_mY_Z, Tr_12_12_12),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_0_12_12),
        SymOp(Rot_X_mY_Z, Tr_0_12_12),
        SymOp(Rot_X_Y_mZ, Tr_12_12_12),
    ]
)

sg5074 = SpaceGroup(
    number = 5074,
    num_sym_equiv = 16,
    num_primitive_sym_equiv = 16,
    short_name = 'Imam',
    point_group_name = 'PGmmm',
    crystal_system = 'ORTHORHOMBIC',
    pdb_name = 'I m a m',
    symop_list = [
        SymOp(Rot_X_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_mZ, Tr_0_0_12),
        SymOp(Rot_mX_mY_Z, Tr_0_0_12),
        SymOp(Rot_mX_mY_mZ, Tr_0_0_0),
        SymOp(Rot_mX_Y_Z, Tr_0_0_0),
        SymOp(Rot_X_mY_Z, Tr_0_0_12),
        SymOp(Rot_X_Y_mZ, Tr_0_0_12),
        SymOp(Rot_X_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_mZ, Tr_12_12_0),
        SymOp(Rot_mX_mY_Z, Tr_12_12_0),
        SymOp(Rot_mX_mY_mZ, Tr_12_12_12),
        SymOp(Rot_mX_Y_Z, Tr_12_12_12),
        SymOp(Rot_X_mY_Z, Tr_12_12_0),
        SymOp(Rot_X_Y_mZ, Tr_12_12_0),
    ]
)

##############################################################################
# end of generated code
##############################################################################

# list of all groups in this module
sgtbxSpaceGroupList = [
        sg2003, sg2004, sg4005, sg5005, sg6005, sg7005, sg8005, sg9005,
        sg10005, sg2006, sg2007, sg3007, sg4007, sg5007, sg6007, sg7007,
        sg8007, sg2008, sg3008, sg4008, sg5008, sg6008, sg7008, sg8008,
        sg2009, sg3009, sg4009, sg5009, sg6009, sg7009, sg8009, sg9009,
        sg10009, sg11009, sg12009, sg13009, sg14009, sg15009, sg16009,
        sg17009, sg2010, sg2011, sg2012, sg3012, sg4012, sg5012, sg6012,
        sg7012, sg8012, sg2013, sg3013, sg4013, sg5013, sg6013, sg7013,
        sg8013, sg2014, sg3014, sg4014, sg5014, sg6014, sg7014, sg8014,
        sg2015, sg3015, sg4015, sg5015, sg6015, sg7015, sg8015, sg9015,
        sg10015, sg11015, sg12015, sg13015, sg14015, sg15015, sg16015,
        sg17015, sg2020, sg3020, sg2021, sg3021, sg1025, sg2025, sg1026,
        sg2026, sg3026, sg4026, sg5026, sg1027, sg2027, sg1028, sg2028,
        sg3028, sg4028, sg5028, sg1029, sg2029, sg3029, sg4029, sg5029,
        sg1030, sg2030, sg3030, sg4030, sg5030, sg1031, sg2031, sg3031,
        sg4031, sg5031, sg1032, sg2032, sg1033, sg2033, sg3033, sg4033,
        sg5033, sg1034, sg2034, sg1035, sg2035, sg1036, sg2036, sg3036,
        sg4036, sg5036, sg1037, sg2037, sg1038, sg2038, sg3038, sg4038,
        sg5038, sg1039, sg2039, sg3039, sg4039, sg5039, sg1040, sg2040,
        sg3040, sg4040, sg5040, sg1041, sg2041, sg3041, sg4041, sg5041,
        sg1042, sg2042, sg1043, sg2043, sg1044, sg2044, sg1045, sg2045,
        sg1046, sg2046, sg3046, sg4046, sg5046, sg1049, sg2049, sg1050,
        sg2050, sg3050, sg4050, sg1051, sg2051, sg3051, sg4051, sg5051,
        sg1052, sg2052, sg3052, sg4052, sg5052, sg1053, sg2053, sg3053,
        sg4053, sg5053, sg1054, sg2054, sg3054, sg4054, sg5054, sg1055,
        sg2055, sg1056, sg2056, sg1057, sg2057, sg3057, sg4057, sg5057,
        sg1058, sg2058, sg2059, sg3059, sg4059, sg5059, sg1060, sg2060,
        sg3060, sg4060, sg5060, sg1061, sg1062, sg2062, sg3062, sg4062,
        sg5062, sg1063, sg2063, sg3063, sg4063, sg5063, sg1064, sg2064,
        sg3064, sg4064, sg5064, sg1065, sg2065, sg1066, sg2066, sg1067,
        sg2067, sg3067, sg4067, sg5067, sg1068, sg2068, sg3068, sg4068,
        sg5068, sg6068, sg7068, sg1072, sg2072, sg1073, sg1074, sg2074,
        sg3074, sg4074, sg5074,
]

# End of file
