"""
AstroCell
geometry.py

Geometry definition for the astrocyte model.
Uses the geometry exported from Blender/CellBlender.
"""

import os
import mcell as m

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------
# Geometry
# ---------------------------------------------------------

geometry = m.Geometry.from_geometry_file(
    os.path.join(MODEL_PATH, "astrocyte.inp")
)


# ---------------------------------------------------------
# Geometry Objects
# ---------------------------------------------------------

cytoplasm = geometry.find_geometry_object("cytoplasm")

assert cytoplasm is not None, \
    "Geometry object 'cytoplasm' not found."


ER = geometry.find_geometry_object("ER")

assert ER is not None, \
    "Geometry object 'ER' not found."


# ---------------------------------------------------------
# Surface Regions
# ---------------------------------------------------------

ER_membrane = ER.find_surface_region_by_name(
    "ER_membrane"
)

assert ER_membrane is not None, \
    "Surface region 'ER_membrane' not found."


plasma_membrane = cytoplasm.find_surface_region_by_name(
    "plasma_membrane"
)

assert plasma_membrane is not None, \
    "Surface region 'plasma_membrane' not found."


# ---------------------------------------------------------
# Surface Classes
# ---------------------------------------------------------

cytoplasm_membrane = m.SurfaceClass(
    name="cytoplasm_membrane"
)

ER_lumen = m.SurfaceClass(
    name="ER_lumen"
)


# ---------------------------------------------------------
# Assign Surface Classes
# ---------------------------------------------------------

cytoplasm.surface_class = cytoplasm_membrane
ER.surface_class = ER_lumen
