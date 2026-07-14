# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import sys
import os
import math
import shared
import mcell as m

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))

# ---- model parameters ----

# declare all items from parameter_overrides as variables
for parameter_name, value in shared.parameter_overrides.items():
    setattr(sys.modules[__name__], parameter_name, value)

# auxiliary function used to determine whether a parameter was defined
def not_defined(parameter_name):
    return parameter_name not in globals()

# load parameters from BNGL
bngl_params = m.bngl_utils.load_bngl_parameters(os.path.join(MODEL_PATH, 'model.bngl'), shared.parameter_overrides)

D_Ca = bngl_params['D_Ca']
D_IP3 = bngl_params['D_IP3']
IP3_KB = bngl_params['IP3_KB']
IP3_KB_2 = bngl_params['IP3_KB_2']
CA_ACT_KF = bngl_params['CA_ACT_KF']
CA_ACT_KB = bngl_params['CA_ACT_KB']
SERCA_RATE = bngl_params['SERCA_RATE']
LEAK_RATE = bngl_params['LEAK_RATE']
PMCA_RATE = bngl_params['PMCA_RATE']
FLUX = bngl_params['FLUX']
CA_INH_KF = bngl_params['CA_INH_KF']
CA_INH_KB = bngl_params['CA_INH_KB']

# ---- simulation setup ----

if not_defined('ITERATIONS'):
    ITERATIONS = 100000

if not_defined('TIME_STEP'):
    TIME_STEP = 1e-5

if not_defined('DUMP'):
    DUMP = False

if not_defined('EXPORT_DATA_MODEL'):
    EXPORT_DATA_MODEL = True

if not_defined('SEED'):
    SEED = 1


