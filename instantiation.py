# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *
from subsystem import *
from geometry import *
MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ---- instantiation ----

# ---- release sites ----

# ---- surface classes assignment ----

ER.surface_class = ER_surface
Cyt.surface_class = PM_surface
# ---- compartments assignment ----

Ca_Initial = m.ReleaseSite(
    name = 'Ca_Initial',
    complex = m.Complex('ca'),
    region = Cyt,
    number_to_release = 1000
)

ip3_Initial = m.ReleaseSite(
    name = 'ip3_Initial',
    complex = m.Complex('ip3'),
    region = Cyt,
    number_to_release = 500
)

IP3R_Initial = m.ReleaseSite(
    name = 'IP3R_Initial',
    complex = m.Complex('unb_IP3R', orientation = m.Orientation.UP),
    region = ER_ER_membrane,
    number_to_release = 100
)

GCaMP6s_Initial = m.ReleaseSite(
    name = 'GCaMP6s_Initial',
    complex = m.Complex('GCaMP6s'),
    region = Cyt,
    number_to_release = 500
)

PLC_Initial = m.ReleaseSite(
    name = 'PLC_Initial',
    complex = m.Complex('plc', orientation = m.Orientation.UP),
    region = Cyt_PM_membrane,
    number_to_release = 100
)

# ---- create instantiation object and add components ----

instantiation = m.Instantiation()
instantiation.add_geometry_object(Cyt)
instantiation.add_geometry_object(ER)
instantiation.add_release_site(Ca_Initial)
instantiation.add_release_site(ip3_Initial)
instantiation.add_release_site(IP3R_Initial)
instantiation.add_release_site(GCaMP6s_Initial)
instantiation.add_release_site(PLC_Initial)

# load seed species information from bngl file
instantiation.load_bngl_compartments_and_seed_species(os.path.join(MODEL_PATH, 'model.bngl'), None, shared.parameter_overrides)

