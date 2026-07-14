"""
=============================================================
 Astrocyte Calcium Signalling Model (MCell4)
-------------------------------------------------------------
File: parameters.py

Author : Ishatpreet Singh
Project: Astrocyte-IP3R-MCell

This file contains all model parameters.

Units:
Length        : meters
Time          : seconds
Concentration : mol/L
Diffusion     : m²/s
Reaction rates: SI units compatible with MCell
=============================================================
"""

# ============================================================
# Diffusion Constants (m²/s)
# ============================================================

D_CA = 1.30e-11          # Cytosolic calcium
D_IP3 = 2.80e-10         # IP3
D_GCAMP = 5.00e-11       # GCaMP6s
D_CAGCAMP = 5.00e-11     # Ca-bound GCaMP

# ER calcium is considered a stored pool.
# Set to zero initially.
D_CA_ER = 0.0


# ============================================================
# Resting Concentrations
# ============================================================

CA_REST = 100e-9         # 100 nM

CA_ER_REST = 300e-6      # 300 µM

IP3_REST = 0.0

GCAMP_CONC = 10e-6       # 10 µM


# ============================================================
# Receptor Densities
# ============================================================

IP3R_DENSITY = 50        # receptors / µm²

SERCA_DENSITY = 10       # pumps / µm²

PMCA_DENSITY = 10        # pumps / µm²

ER_LEAK_DENSITY = 2      # leak channels / µm²


# ============================================================
# IP3 Receptor Kinetics
# (DeYoung–Keizer Model)
# ============================================================

# ---------- IP3 Binding ----------

K_IP3_BIND = 4.10e7

K_IP3_UNBIND = 400


# ---------- Activating Calcium ----------

K_CA_ACT_BIND = 1.20e6

K_CA_ACT_UNBIND = 50


# ---------- Inhibitory Calcium ----------

K_CA_INHIB_BIND = 1.60e4

K_CA_INHIB_UNBIND = 100


# ---------- Channel Flux ----------

K_IP3R_FLUX = 6000


# ============================================================
# GCaMP Buffering
# ============================================================

K_GCAMP_BIND = 7.78e6

K_GCAMP_UNBIND = 1.12


# ============================================================
# Calcium Pumps
# ============================================================

SERCA_RATE = 100

PMCA_RATE = 10

ER_LEAK_RATE = 0.1


# ============================================================
# IP3 Metabolism
# ============================================================

PLC_RATE = 1.0

IP3_DEGRADATION = 1.2e-4


# ============================================================
# Geometry
# ============================================================

CYTOPLASM_NAME = "cytoplasm"

ER_NAME = "ER"

ER_MEMBRANE_NAME = "ER_membrane"

PLASMA_MEMBRANE_NAME = "Plasma_membrane"


# ============================================================
# Simulation
# ============================================================

TIME_STEP = 1e-6

TOTAL_TIME = 10.0

ITERATIONS = int(TOTAL_TIME / TIME_STEP)

RANDOM_SEED = 1


# ============================================================
# Output
# ============================================================

OUTPUT_DIRECTORY = "output"

SAVE_EVERY = 100


# ============================================================
# Validation Flags
# ============================================================

ENABLE_GCAMP = True

ENABLE_SERCA = True

ENABLE_PMCA = True

ENABLE_ER_LEAK = True

ENABLE_IP3R = True
