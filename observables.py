"""
AstroCell
observables.py

Observables and visualization outputs.
"""

import mcell as m


# ==========================================================
# VISUALIZATION
# ==========================================================

viz_output = m.VizOutput(

    mode=m.VizMode.CELLBLENDER,

    output_files_prefix="./viz_data/seed_" + str(SEED).zfill(5) + "/Scene",

    every_n_timesteps=1

)


# ==========================================================
# OBSERVABLES
# ==========================================================

observables = m.Observables()

observables.add_viz_output(viz_output)


# ==========================================================
# CALCIUM
# ==========================================================

observables.add_count(
    m.Count(
        name="Ca",
        expression="COUNT[ca]",
        file_name="react_data/Ca.dat"
    )
)


# ==========================================================
# IP3
# ==========================================================

observables.add_count(
    m.Count(
        name="IP3",
        expression="COUNT[ip3]",
        file_name="react_data/IP3.dat"
    )
)


# ==========================================================
# GCaMP
# ==========================================================

observables.add_count(
    m.Count(
        name="GCaMP",
        expression="COUNT[GCaMP6s]",
        file_name="react_data/GCaMP.dat"
    )
)

observables.add_count(
    m.Count(
        name="Ca_GCaMP",
        expression="COUNT[ca_GCaMP6s]",
        file_name="react_data/Ca_GCaMP.dat"
    )
)


# ==========================================================
# IP3R STATES
# ==========================================================

observables.add_count(
    m.Count(
        name="Open_IP3R",
        expression="COUNT[open_IP3R]",
        file_name="react_data/Open_IP3R.dat"
    )
)

observables.add_count(
    m.Count(
        name="Unbound_IP3R",
        expression="COUNT[unb_IP3R]",
        file_name="react_data/Unbound_IP3R.dat"
    )
)

observables.add_count(
    m.Count(
        name="IP3_Bound",
        expression="COUNT[ip3_IP3R]",
        file_name="react_data/IP3_Bound.dat"
    )
)

observables.add_count(
    m.Count(
        name="CAA_IP3R",
        expression="COUNT[caa_IP3R]",
        file_name="react_data/CAA_IP3R.dat"
    )
)

observables.add_count(
    m.Count(
        name="CAI_IP3R",
        expression="COUNT[cai_IP3R]",
        file_name="react_data/CAI_IP3R.dat"
    )
)

observables.add_count(
    m.Count(
        name="CA2_IP3R",
        expression="COUNT[ca2_IP3R]",
        file_name="react_data/CA2_IP3R.dat"
    )
)

observables.add_count(
    m.Count(
        name="CAI_IP3R_IP3",
        expression="COUNT[cai_ip3_IP3R]",
        file_name="react_data/CAI_IP3R_IP3.dat"
    )
)

observables.add_count(
    m.Count(
        name="CA2_IP3R_IP3",
        expression="COUNT[ca2_ip3_IP3R]",
        file_name="react_data/CA2_IP3R_IP3.dat"
    )
)
