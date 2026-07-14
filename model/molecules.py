"""
=============================================================
AstroCell

model/molecules.py

Defines every molecular species in the astrocyte model.

Nothing in this file contains reactions.

Author:
Ishatpreet Singh
=============================================================
"""

from core.species import VolumeSpecies, SurfaceSpecies

from config.parameters import *
from config.constants import *


# ==========================================================
# Cytoplasmic Molecules
# ==========================================================

CA = VolumeSpecies(

    name=VolumeSpecies.CA.value,

    diffusion=D_CA,

    compartment=Compartment.CYTOPLASM.value,

    initial_concentration=CA_REST,

    description="Free cytosolic calcium"

)


IP3 = VolumeSpecies(

    name=VolumeSpecies.IP3.value,

    diffusion=D_IP3,

    compartment=Compartment.CYTOPLASM.value,

    initial_concentration=IP3_REST,

    description="Inositol trisphosphate"

)


PLC = VolumeSpecies(

    name=VolumeSpecies.PLC.value,

    diffusion=0.0,

    compartment=Compartment.CYTOPLASM.value,

    initial_concentration=0.0,

    description="Phospholipase C"

)


GCAMP = VolumeSpecies(

    name=VolumeSpecies.GCAMP.value,

    diffusion=D_GCAMP,

    compartment=Compartment.CYTOPLASM.value,

    initial_concentration=GCAMP_CONC,

    description="GCaMP6s"

)


CA_GCAMP = VolumeSpecies(

    name=VolumeSpecies.CA_GCAMP.value,

    diffusion=D_CAGCAMP,

    compartment=Compartment.CYTOPLASM.value,

    initial_concentration=0.0,

    description="Calcium-bound GCaMP"

)


# ==========================================================
# ER Lumen
# ==========================================================

CA_ER = VolumeSpecies(

    name=VolumeSpecies.CA_ER.value,

    diffusion=D_CA_ER,

    compartment=Compartment.ER.value,

    initial_concentration=CA_ER_REST,

    description="ER calcium store"

)


# ==========================================================
# Pumps
# ==========================================================

SERCA = SurfaceSpecies(

    name=SurfaceSpecies.SERCA.value,

    diffusion=0.0,

    region=Surface.ER_MEMBRANE.value,

    initial_density=SERCA_DENSITY,

    description="SERCA pump"

)


PMCA = SurfaceSpecies(

    name=SurfaceSpecies.PMCA.value,

    diffusion=0.0,

    region=Surface.PLASMA_MEMBRANE.value,

    initial_density=PMCA_DENSITY,

    description="Plasma membrane Ca ATPase"

)


ER_LEAK = SurfaceSpecies(

    name=SurfaceSpecies.ER_LEAK.value,

    diffusion=0.0,

    region=Surface.ER_MEMBRANE.value,

    initial_density=ER_LEAK_DENSITY,

    description="ER leak channel"

)


# ==========================================================
# IP3 Receptor States
# ==========================================================

UNBOUND_IP3R = SurfaceSpecies(

    name=SurfaceSpecies.UNBOUND_IP3R.value,

    diffusion=0.0,

    region=Surface.ER_MEMBRANE.value,

    initial_density=IP3R_DENSITY,

    description="Unbound receptor"

)


IP3_BOUND = SurfaceSpecies(

    name=SurfaceSpecies.IP3_BOUND.value,

    diffusion=0.0,

    region=Surface.ER_MEMBRANE.value,

    initial_density=0.0

)


CAA = SurfaceSpecies(

    name=SurfaceSpecies.CAA.value,

    diffusion=0.0,

    region=Surface.ER_MEMBRANE.value,

    initial_density=0.0

)


CAI = SurfaceSpecies(

    name=SurfaceSpecies.CAI.value,

    diffusion=0.0,

    region=Surface.ER_MEMBRANE.value,

    initial_density=0.0

)


OPEN = SurfaceSpecies(

    name=SurfaceSpecies.OPEN.value,

    diffusion=0.0,

    region=Surface.ER_MEMBRANE.value,

    initial_density=0.0,

    description="Open IP3 receptor"

)


CAI_IP3 = SurfaceSpecies(

    name=SurfaceSpecies.CAI_IP3.value,

    diffusion=0.0,

    region=Surface.ER_MEMBRANE.value,

    initial_density=0.0

)


CA2 = SurfaceSpecies(

    name=SurfaceSpecies.CA2.value,

    diffusion=0.0,

    region=Surface.ER_MEMBRANE.value,

    initial_density=0.0

)


CA2_IP3 = SurfaceSpecies(

    name=SurfaceSpecies.CA2_IP3.value,

    diffusion=0.0,

    region=Surface.ER_MEMBRANE.value,

    initial_density=0.0

)


# ==========================================================
# Master Species List
# ==========================================================

ALL_SPECIES = [

    CA,

    CA_ER,

    IP3,

    PLC,

    GCAMP,

    CA_GCAMP,

    SERCA,

    PMCA,

    ER_LEAK,

    UNBOUND_IP3R,

    IP3_BOUND,

    CAA,

    CAI,

    OPEN,

    CAI_IP3,

    CA2,

    CA2_IP3

]
