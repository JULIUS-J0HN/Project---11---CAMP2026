"""
=============================================================
AstroCell

constants.py

Contains ONLY names used throughout the project.

Changing a molecule name here updates the
entire project automatically.

Author:
Ishatpreet Singh
=============================================================
"""

from enum import Enum


# ==========================================================
# Compartments
# ==========================================================

class Compartment(Enum):

    CYTOPLASM = "cytoplasm"

    ER = "ER"


# ==========================================================
# Surface Regions
# ==========================================================

class Surface(Enum):

    PLASMA_MEMBRANE = "plasma_membrane"

    ER_MEMBRANE = "ER_membrane"


# ==========================================================
# Volume Molecules
# ==========================================================

class VolumeSpecies(Enum):

    CA = "ca"

    CA_ER = "ca_ER"

    IP3 = "ip3"

    PLC = "plc"

    GCAMP = "GCaMP6s"

    CA_GCAMP = "ca_GCaMP6s"


# ==========================================================
# Surface Molecules
# ==========================================================

class SurfaceSpecies(Enum):

    SERCA = "SERCA"

    PMCA = "PMCA"

    ER_LEAK = "ER_Leak"

    UNBOUND_IP3R = "unb_IP3R"

    IP3_BOUND = "ip3_IP3R"

    CAA = "caa_IP3R"

    CAI = "cai_IP3R"

    OPEN = "open_IP3R"

    CAI_IP3 = "cai_ip3_IP3R"

    CA2 = "ca2_IP3R"

    CA2_IP3 = "ca2_ip3_IP3R"


# ==========================================================
# Reaction Names
# ==========================================================

class Reaction(Enum):

    GCAMP_BIND = "GCaMP Binding"

    GCAMP_UNBIND = "GCaMP Unbinding"

    IP3_BIND = "IP3 Binding"

    IP3_UNBIND = "IP3 Unbinding"

    CA_ACTIVATION = "Calcium Activation"

    CA_DEACTIVATION = "Calcium Deactivation"

    CA_INHIBITION = "Calcium Inhibition"

    CA_RECOVERY = "Calcium Recovery"

    IP3R_FLUX = "IP3R Calcium Flux"

    SERCA = "SERCA Uptake"

    PMCA = "PMCA Extrusion"

    ER_LEAK = "ER Leak"

    PLC = "PLC IP3 Production"

    IP3_DEGRADATION = "IP3 Degradation"


# ==========================================================
# Observable Names
# ==========================================================

class Observable(Enum):

    CYTOSOLIC_CA = "Cytosolic Calcium"

    ER_CA = "ER Calcium"

    IP3 = "IP3"

    OPEN_RECEPTOR = "Open IP3R"

    GCAMP = "GCaMP Fluorescence"
