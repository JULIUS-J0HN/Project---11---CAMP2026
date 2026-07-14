# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *

# ---- subsystem ----

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))

ER_surface = m.SurfaceClass(
    name = 'ER_surface',
    type = m.SurfacePropertyType.REACTIVE
)

PM_surface = m.SurfaceClass(
    name = 'PM_surface',
    type = m.SurfacePropertyType.REACTIVE
)

# ---- create subsystem object and add components ----

subsystem = m.Subsystem()
subsystem.add_surface_class(ER_surface)
subsystem.add_surface_class(PM_surface)

# load subsystem information from bngl file
subsystem.load_bngl_molecule_types_and_reaction_rules(os.path.join(MODEL_PATH, 'model.bngl'), shared.parameter_overrides)

# set additional information about species and molecule types that cannot be stored in BNGL,
# elementary molecule types are already in the subsystem after they were loaded from BNGL
def set_bngl_molecule_types_info(subsystem):
    ca = subsystem.find_elementary_molecule_type('ca')
    assert ca, "Elementary molecule type 'ca' was not found"
    ca.diffusion_constant_3d = 1.3e-11

    ip3 = subsystem.find_elementary_molecule_type('ip3')
    assert ip3, "Elementary molecule type 'ip3' was not found"
    ip3.diffusion_constant_3d = 2.8e-10

    GCaMP6s = subsystem.find_elementary_molecule_type('GCaMP6s')
    assert GCaMP6s, "Elementary molecule type 'GCaMP6s' was not found"
    GCaMP6s.diffusion_constant_3d = 5e-11

    ca_GCaMP6s = subsystem.find_elementary_molecule_type('ca_GCaMP6s')
    assert ca_GCaMP6s, "Elementary molecule type 'ca_GCaMP6s' was not found"
    ca_GCaMP6s.diffusion_constant_3d = 5e-11

    unb_IP3R = subsystem.find_elementary_molecule_type('unb_IP3R')
    assert unb_IP3R, "Elementary molecule type 'unb_IP3R' was not found"
    unb_IP3R.diffusion_constant_2d = 0

    ip3_IP3R = subsystem.find_elementary_molecule_type('ip3_IP3R')
    assert ip3_IP3R, "Elementary molecule type 'ip3_IP3R' was not found"
    ip3_IP3R.diffusion_constant_2d = 0

    caa_IP3R = subsystem.find_elementary_molecule_type('caa_IP3R')
    assert caa_IP3R, "Elementary molecule type 'caa_IP3R' was not found"
    caa_IP3R.diffusion_constant_2d = 0

    cai_IP3R = subsystem.find_elementary_molecule_type('cai_IP3R')
    assert cai_IP3R, "Elementary molecule type 'cai_IP3R' was not found"
    cai_IP3R.diffusion_constant_2d = 0

    open_IP3R = subsystem.find_elementary_molecule_type('open_IP3R')
    assert open_IP3R, "Elementary molecule type 'open_IP3R' was not found"
    open_IP3R.diffusion_constant_2d = 0

    ca2_IP3R = subsystem.find_elementary_molecule_type('ca2_IP3R')
    assert ca2_IP3R, "Elementary molecule type 'ca2_IP3R' was not found"
    ca2_IP3R.diffusion_constant_2d = 0

    cai_ip3_IP3R = subsystem.find_elementary_molecule_type('cai_ip3_IP3R')
    assert cai_ip3_IP3R, "Elementary molecule type 'cai_ip3_IP3R' was not found"
    cai_ip3_IP3R.diffusion_constant_2d = 0

    ca2_ip3_IP3R = subsystem.find_elementary_molecule_type('ca2_ip3_IP3R')
    assert ca2_ip3_IP3R, "Elementary molecule type 'ca2_ip3_IP3R' was not found"
    ca2_ip3_IP3R.diffusion_constant_2d = 0

    plc = subsystem.find_elementary_molecule_type('plc')
    assert plc, "Elementary molecule type 'plc' was not found"
    plc.diffusion_constant_2d = 0

set_bngl_molecule_types_info(subsystem)
