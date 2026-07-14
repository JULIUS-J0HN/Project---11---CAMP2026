"""
AstroCell
parameters.py

Global parameters for the astrocyte calcium model.

Units:
Length              meters
Time                seconds
Diffusion           m^2/s
Concentration       M
"""

# ==========================================================
# Simulation
# ==========================================================

TIME_STEP = 1e-6
ITERATIONS = 500000
SEED = 1

EXPORT_DATA_MODEL = True
DUMP = False


# ==========================================================
# Diffusion Constants (m²/s)
# ==========================================================

D_CA = 0.013e-9
D_IP3 = 0.280e-9
D_GCAMP = 0.050e-9
D_CA_GCAMP = D_GCAMP


# ==========================================================
# Initial Conditions
# ==========================================================

CA_INIT = 100e-9

IP3_INIT = 0.0

GCAMP_INIT = 10e-6

CA_GCAMP_INIT = 0.0

PLC_NUMBER = 1000

IP3R_DENSITY = 50.0


# ==========================================================
# GCaMP6s Buffering
# ==========================================================

GCAMP_BIND = 7.78e6
GCAMP_UNBIND = 1.12


# ==========================================================
# Calcium Homeostasis
# ==========================================================

CA_DECAY = 30.0

CA_LEAK = 15e-8


# ==========================================================
# IP3 Dynamics
# ==========================================================

IP3_DECAY = 1.2e-4

PLC_SYNTHESIS = 1.0


# ==========================================================
# IP3R Kinetics
# ==========================================================

CAA_FORWARD = 1.2e6
CAA_BACKWARD = 5e1

CAI_FORWARD = 1.6e4
CAI_BACKWARD = 1e2

IP3_FORWARD = 4.1e7
IP3_BACKWARD = 4e2


# ==========================================================
# Calcium Flux through Open IP3R
# ==========================================================

IP3R_FLUX = 6e3


# ==========================================================
# Geometry
# ==========================================================

ASTROCYTE_MESH = "astrocyte.inp"

SURFACE_FILE = "cylinder_mesh.txt"


# ==========================================================
# Molecule Names
# ==========================================================

CA = "ca"

IP3 = "ip3"

PLC = "plc"

GCAMP = "GCaMP6s"

CA_GCAMP = "ca_GCaMP6s"

UNBOUND_IP3R = "unb_IP3R"

IP3_BOUND = "ip3_IP3R"

CAA_IP3R = "caa_IP3R"

CAI_IP3R = "cai_IP3R"

OPEN_IP3R = "open_IP3R"

CAI_IP3R_IP3 = "cai_ip3_IP3R"

CA2_IP3R = "ca2_IP3R"

CA2_IP3R_IP3 = "ca2_ip3_IP3R"


# ==========================================================
# Observable Names
# ==========================================================

OBS_CA = "Cytosolic_Ca"

OBS_IP3 = "IP3"

OBS_OPEN = "Open_IP3R"

OBS_GCAMP = "GCaMP"

OBS_CA_GCAMP = "Ca_GCaMP"
