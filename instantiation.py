"""
AstroCell
instantiation.py

Initial molecule placement.
"""

import os
import mcell as m

from parameters import *
from subsystem import *
from geometry import *

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ==========================================================
# RELEASE SITES
# ==========================================================

Ca_Initial = m.ReleaseSite(
    name="Ca_Initial",
    complex=m.Complex("ca"),
    region=cytoplasm,
    concentration=CA_INIT
)

IP3_Initial = m.ReleaseSite(
    name="IP3_Initial",
    complex=m.Complex("ip3"),
    region=cytoplasm,
    concentration=IP3_INIT
)

GCaMP_Initial = m.ReleaseSite(
    name="GCaMP_Initial",
    complex=m.Complex("GCaMP6s"),
    region=cytoplasm,
    concentration=GCAMP_INIT
)

PLC_Initial = m.ReleaseSite(
    name="PLC_Initial",
    complex=m.Complex("plc"),
    region=plasma_membrane,
    number_to_release=PLC_NUMBER
)

IP3R_Initial = m.ReleaseSite(
    name="IP3R_Initial",
    complex=m.Complex(
        "unb_IP3R",
        orientation=m.Orientation.UP
    ),
    region=ER_membrane,
    density=IP3R_DENSITY
)


# ==========================================================
# INSTANTIATION
# ==========================================================

instantiation = m.Instantiation()

instantiation.add_geometry_object(cytoplasm)
instantiation.add_geometry_object(ER)

instantiation.add_release_site(Ca_Initial)
instantiation.add_release_site(IP3_Initial)
instantiation.add_release_site(GCaMP_Initial)
instantiation.add_release_site(PLC_Initial)
instantiation.add_release_site(IP3R_Initial)
```
