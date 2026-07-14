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
