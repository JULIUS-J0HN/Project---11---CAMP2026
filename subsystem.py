"""
AstroCell
subsystem.py

Defines all molecules, diffusion constants and reactions
for the astrocyte calcium signalling model.

This file is adapted from the original STEPS implementation.
"""

import mcell as m

from parameters import *

# ==========================================================
# SUBSYSTEM
# ==========================================================

subsystem = m.Subsystem()

# ==========================================================
# MOLECULE TYPES
# ==========================================================

ca = m.ElementaryMoleculeType(
    name='ca',
    diffusion_constant_3d=D_CA
)

ip3 = m.ElementaryMoleculeType(
    name='ip3',
    diffusion_constant_3d=D_IP3
)

plc = m.ElementaryMoleculeType(
    name='plc',
    diffusion_constant_3d=0
)

GCaMP6s = m.ElementaryMoleculeType(
    name='GCaMP6s',
    diffusion_constant_3d=D_GCAMP
)

ca_GCaMP6s = m.ElementaryMoleculeType(
    name='ca_GCaMP6s',
    diffusion_constant_3d=D_CA_GCAMP
)

unb_IP3R = m.ElementaryMoleculeType(
    name='unb_IP3R',
    diffusion_constant_2d=0
)

ip3_IP3R = m.ElementaryMoleculeType(
    name='ip3_IP3R',
    diffusion_constant_2d=0
)

caa_IP3R = m.ElementaryMoleculeType(
    name='caa_IP3R',
    diffusion_constant_2d=0
)

cai_IP3R = m.ElementaryMoleculeType(
    name='cai_IP3R',
    diffusion_constant_2d=0
)

open_IP3R = m.ElementaryMoleculeType(
    name='open_IP3R',
    diffusion_constant_2d=0
)

cai_ip3_IP3R = m.ElementaryMoleculeType(
    name='cai_ip3_IP3R',
    diffusion_constant_2d=0
)

ca2_IP3R = m.ElementaryMoleculeType(
    name='ca2_IP3R',
    diffusion_constant_2d=0
)

ca2_ip3_IP3R = m.ElementaryMoleculeType(
    name='ca2_ip3_IP3R',
    diffusion_constant_2d=0
)

subsystem.add_elementary_molecule_type(ca)
subsystem.add_elementary_molecule_type(ip3)
subsystem.add_elementary_molecule_type(plc)
subsystem.add_elementary_molecule_type(GCaMP6s)
subsystem.add_elementary_molecule_type(ca_GCaMP6s)

subsystem.add_elementary_molecule_type(unb_IP3R)
subsystem.add_elementary_molecule_type(ip3_IP3R)
subsystem.add_elementary_molecule_type(caa_IP3R)
subsystem.add_elementary_molecule_type(cai_IP3R)
subsystem.add_elementary_molecule_type(open_IP3R)
subsystem.add_elementary_molecule_type(cai_ip3_IP3R)
subsystem.add_elementary_molecule_type(ca2_IP3R)
subsystem.add_elementary_molecule_type(ca2_ip3_IP3R)

# ==========================================================
# GCaMP BUFFERING
# ==========================================================

GCaMP_bind = m.ReactionRule(
    reactants=[
        m.Complex('ca'),
        m.Complex('GCaMP6s')
    ],

    products=[
        m.Complex('ca_GCaMP6s')
    ],

    forward_rate=GCAMP_BIND
)

GCaMP_unbind = m.ReactionRule(
    reactants=[
        m.Complex('ca_GCaMP6s')
    ],

    products=[
        m.Complex('ca'),
        m.Complex('GCaMP6s')
    ],

    forward_rate=GCAMP_UNBIND
)

# ==========================================================
# CALCIUM HOMEOSTASIS
# ==========================================================

Ca_decay = m.ReactionRule(
    reactants=[
        m.Complex('ca')
    ],

    products=[],

    forward_rate=CA_DECAY
)

Ca_leak = m.ReactionRule(
    reactants=[],

    products=[
        m.Complex('ca')
    ],

    forward_rate=CA_LEAK
)

# ==========================================================
# IP3
# ==========================================================

IP3_decay = m.ReactionRule(
    reactants=[
        m.Complex('ip3')
    ],

    products=[],

    forward_rate=IP3_DECAY
)

PLC_IP3 = m.ReactionRule(

    reactants=[
        m.Complex('plc'),
        m.Complex('ca')
    ],

    products=[
        m.Complex('plc'),
        m.Complex('ca'),
        m.Complex('ip3')
    ],

    forward_rate=PLC_SYNTHESIS
)

subsystem.add_reaction_rule(GCaMP_bind)
subsystem.add_reaction_rule(GCaMP_unbind)

subsystem.add_reaction_rule(Ca_decay)
subsystem.add_reaction_rule(Ca_leak)

subsystem.add_reaction_rule(IP3_decay)
subsystem.add_reaction_rule(PLC_IP3)

# ==========================================================
# IP3R reactions continue below
# (next file section)
# ==========================================================
# ==========================================================
# IP3R REACTION NETWORK
# ==========================================================
#
# Translation of the DeYoung–Keizer receptor from the
# original STEPS model.
#

# ----------------------------------------------------------
# Unbound <-> Ca Activated
# ----------------------------------------------------------

unb_IP3R_bind_caa_f = m.ReactionRule(
    reactants=[
        m.Complex('unb_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('caa_IP3R')
    ],
    forward_rate=CAA_FORWARD
)

unb_IP3R_bind_caa_b = m.ReactionRule(
    reactants=[
        m.Complex('caa_IP3R')
    ],
    products=[
        m.Complex('unb_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAA_BACKWARD
)

# ----------------------------------------------------------
# Unbound <-> Ca Inactivated
# ----------------------------------------------------------

unb_IP3R_bind_cai_f = m.ReactionRule(
    reactants=[
        m.Complex('unb_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('cai_IP3R')
    ],
    forward_rate=CAI_FORWARD
)

unb_IP3R_bind_cai_b = m.ReactionRule(
    reactants=[
        m.Complex('cai_IP3R')
    ],
    products=[
        m.Complex('unb_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAI_BACKWARD
)

# ----------------------------------------------------------
# Ca Activated <-> Ca2
# ----------------------------------------------------------

caa_IP3R_bind_ca_f = m.ReactionRule(
    reactants=[
        m.Complex('caa_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('ca2_IP3R')
    ],
    forward_rate=CAI_FORWARD
)

caa_IP3R_bind_ca_b = m.ReactionRule(
    reactants=[
        m.Complex('ca2_IP3R')
    ],
    products=[
        m.Complex('caa_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAI_BACKWARD
)

# ----------------------------------------------------------
# IP3 Bound <-> Open
# ----------------------------------------------------------

ip3_IP3R_bind_caa_f = m.ReactionRule(
    reactants=[
        m.Complex('ip3_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('open_IP3R')
    ],
    forward_rate=CAA_FORWARD
)

ip3_IP3R_bind_caa_b = m.ReactionRule(
    reactants=[
        m.Complex('open_IP3R')
    ],
    products=[
        m.Complex('ip3_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAA_BACKWARD
)

# ----------------------------------------------------------
# IP3 Bound <-> Inactivated
# ----------------------------------------------------------

ip3_IP3R_bind_cai_f = m.ReactionRule(
    reactants=[
        m.Complex('ip3_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('cai_ip3_IP3R')
    ],
    forward_rate=CAI_FORWARD
)

ip3_IP3R_bind_cai_b = m.ReactionRule(
    reactants=[
        m.Complex('cai_ip3_IP3R')
    ],
    products=[
        m.Complex('ip3_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAI_BACKWARD
)

# ----------------------------------------------------------
# Cai <-> Ca2
# ----------------------------------------------------------

cai_IP3R_bind_ca_f = m.ReactionRule(
    reactants=[
        m.Complex('cai_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('ca2_IP3R')
    ],
    forward_rate=CAA_FORWARD
)

cai_IP3R_bind_ca_b = m.ReactionRule(
    reactants=[
        m.Complex('ca2_IP3R')
    ],
    products=[
        m.Complex('cai_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAA_BACKWARD
)

# ----------------------------------------------------------
# Open <-> Ca2_IP3
# ----------------------------------------------------------

open_IP3R_bind_ca_f = m.ReactionRule(
    reactants=[
        m.Complex('open_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('ca2_ip3_IP3R')
    ],
    forward_rate=CAI_FORWARD
)

open_IP3R_bind_ca_b = m.ReactionRule(
    reactants=[
        m.Complex('ca2_ip3_IP3R')
    ],
    products=[
        m.Complex('open_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAI_BACKWARD
)

# ----------------------------------------------------------
# Cai_IP3 <-> Ca2_IP3
# ----------------------------------------------------------

cai_ip3_IP3R_bind_ca_f = m.ReactionRule(
    reactants=[
        m.Complex('cai_ip3_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('ca2_ip3_IP3R')
    ],
    forward_rate=CAA_FORWARD
)

cai_ip3_IP3R_bind_ca_b = m.ReactionRule(
    reactants=[
        m.Complex('ca2_ip3_IP3R')
    ],
    products=[
        m.Complex('cai_ip3_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAA_BACKWARD
)
# ----------------------------------------------------------
# Unbound <-> IP3 Bound
# ----------------------------------------------------------

unb_IP3R_bind_ip3_f = m.ReactionRule(
    reactants=[
        m.Complex('unb_IP3R'),
        m.Complex('ip3')
    ],
    products=[
        m.Complex('ip3_IP3R')
    ],
    forward_rate=IP3_FORWARD
)

unb_IP3R_bind_ip3_b = m.ReactionRule(
    reactants=[
        m.Complex('ip3_IP3R')
    ],
    products=[
        m.Complex('unb_IP3R'),
        m.Complex('ip3')
    ],
    forward_rate=IP3_BACKWARD
)

# ----------------------------------------------------------
# Caa <-> Open
# ----------------------------------------------------------

caa_IP3R_bind_ip3_f = m.ReactionRule(
    reactants=[
        m.Complex('caa_IP3R'),
        m.Complex('ip3')
    ],
    products=[
        m.Complex('open_IP3R')
    ],
    forward_rate=IP3_FORWARD
)

caa_IP3R_bind_ip3_b = m.ReactionRule(
    reactants=[
        m.Complex('open_IP3R')
    ],
    products=[
        m.Complex('caa_IP3R'),
        m.Complex('ip3')
    ],
    forward_rate=IP3_BACKWARD
)

# ----------------------------------------------------------
# Cai <-> Cai_IP3
# ----------------------------------------------------------

cai_IP3R_bind_ip3_f = m.ReactionRule(
    reactants=[
        m.Complex('cai_IP3R'),
        m.Complex('ip3')
    ],
    products=[
        m.Complex('cai_ip3_IP3R')
    ],
    forward_rate=IP3_FORWARD
)

cai_IP3R_bind_ip3_b = m.ReactionRule(
    reactants=[
        m.Complex('cai_ip3_IP3R')
    ],
    products=[
        m.Complex('cai_IP3R'),
        m.Complex('ip3')
    ],
    forward_rate=IP3_BACKWARD
)

# ----------------------------------------------------------
# Ca2 <-> Ca2_IP3
# ----------------------------------------------------------

ca2_IP3R_bind_ip3_f = m.ReactionRule(
    reactants=[
        m.Complex('ca2_IP3R'),
        m.Complex('ip3')
    ],
    products=[
        m.Complex('ca2_ip3_IP3R')
    ],
    forward_rate=IP3_FORWARD
)

ca2_IP3R_bind_ip3_b = m.ReactionRule(
    reactants=[
        m.Complex('ca2_ip3_IP3R')
    ],
    products=[
        m.Complex('ca2_IP3R'),
        m.Complex('ip3')
    ],
    forward_rate=IP3_BACKWARD
)

# ----------------------------------------------------------
# Calcium Flux through Open IP3R
# (Faithful to original STEPS implementation)
# ----------------------------------------------------------

IP3R_flux = m.ReactionRule(
    reactants=[
        m.Complex('open_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('open_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=IP3R_FLUX
)

# ==========================================================
# ADD REACTIONS TO SUBSYSTEM
# ==========================================================

subsystem.add_reaction_rule(unb_IP3R_bind_caa_f)
subsystem.add_reaction_rule(unb_IP3R_bind_caa_b)

subsystem.add_reaction_rule(unb_IP3R_bind_cai_f)
subsystem.add_reaction_rule(unb_IP3R_bind_cai_b)

subsystem.add_reaction_rule(caa_IP3R_bind_ca_f)
subsystem.add_reaction_rule(caa_IP3R_bind_ca_b)

subsystem.add_reaction_rule(ip3_IP3R_bind_caa_f)
subsystem.add_reaction_rule(ip3_IP3R_bind_caa_b)

subsystem.add_reaction_rule(ip3_IP3R_bind_cai_f)
subsystem.add_reaction_rule(ip3_IP3R_bind_cai_b)

subsystem.add_reaction_rule(cai_IP3R_bind_ca_f)
subsystem.add_reaction_rule(cai_IP3R_bind_ca_b)

subsystem.add_reaction_rule(open_IP3R_bind_ca_f)
subsystem.add_reaction_rule(open_IP3R_bind_ca_b)

subsystem.add_reaction_rule(cai_ip3_IP3R_bind_ca_f)
subsystem.add_reaction_rule(cai_ip3_IP3R_bind_ca_b)

subsystem.add_reaction_rule(unb_IP3R_bind_ip3_f)
subsystem.add_reaction_rule(unb_IP3R_bind_ip3_b)

subsystem.add_reaction_rule(caa_IP3R_bind_ip3_f)
subsystem.add_reaction_rule(caa_IP3R_bind_ip3_b)

subsystem.add_reaction_rule(cai_IP3R_bind_ip3_f)
subsystem.add_reaction_rule(cai_IP3R_bind_ip3_b)

subsystem.add_reaction_rule(ca2_IP3R_bind_ip3_f)
subsystem.add_reaction_rule(ca2_IP3R_bind_ip3_b)

subsystem.add_reaction_rule(IP3R_flux)
