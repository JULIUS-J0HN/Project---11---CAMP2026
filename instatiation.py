# ==========================================================
# IP3R REACTION NETWORK
# ==========================================================
#
# Translation of the DeYoung–Keizer receptor from the
# original STEPS model.
#

# ----------------------------------------------------------
# Unbound <-> Ca Activated
# ----------------------------------------------------------

unb_IP3R_bind_caa_f = m.ReactionRule(
    reactants=[
        m.Complex('unb_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('caa_IP3R')
    ],
    forward_rate=CAA_FORWARD
)

unb_IP3R_bind_caa_b = m.ReactionRule(
    reactants=[
        m.Complex('caa_IP3R')
    ],
    products=[
        m.Complex('unb_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAA_BACKWARD
)

# ----------------------------------------------------------
# Unbound <-> Ca Inactivated
# ----------------------------------------------------------

unb_IP3R_bind_cai_f = m.ReactionRule(
    reactants=[
        m.Complex('unb_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('cai_IP3R')
    ],
    forward_rate=CAI_FORWARD
)

unb_IP3R_bind_cai_b = m.ReactionRule(
    reactants=[
        m.Complex('cai_IP3R')
    ],
    products=[
        m.Complex('unb_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAI_BACKWARD
)

# ----------------------------------------------------------
# Ca Activated <-> Ca2
# ----------------------------------------------------------

caa_IP3R_bind_ca_f = m.ReactionRule(
    reactants=[
        m.Complex('caa_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('ca2_IP3R')
    ],
    forward_rate=CAI_FORWARD
)

caa_IP3R_bind_ca_b = m.ReactionRule(
    reactants=[
        m.Complex('ca2_IP3R')
    ],
    products=[
        m.Complex('caa_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAI_BACKWARD
)

# ----------------------------------------------------------
# IP3 Bound <-> Open
# ----------------------------------------------------------

ip3_IP3R_bind_caa_f = m.ReactionRule(
    reactants=[
        m.Complex('ip3_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('open_IP3R')
    ],
    forward_rate=CAA_FORWARD
)

ip3_IP3R_bind_caa_b = m.ReactionRule(
    reactants=[
        m.Complex('open_IP3R')
    ],
    products=[
        m.Complex('ip3_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAA_BACKWARD
)

# ----------------------------------------------------------
# IP3 Bound <-> Inactivated
# ----------------------------------------------------------

ip3_IP3R_bind_cai_f = m.ReactionRule(
    reactants=[
        m.Complex('ip3_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('cai_ip3_IP3R')
    ],
    forward_rate=CAI_FORWARD
)

ip3_IP3R_bind_cai_b = m.ReactionRule(
    reactants=[
        m.Complex('cai_ip3_IP3R')
    ],
    products=[
        m.Complex('ip3_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAI_BACKWARD
)

# ----------------------------------------------------------
# Cai <-> Ca2
# ----------------------------------------------------------

cai_IP3R_bind_ca_f = m.ReactionRule(
    reactants=[
        m.Complex('cai_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('ca2_IP3R')
    ],
    forward_rate=CAA_FORWARD
)

cai_IP3R_bind_ca_b = m.ReactionRule(
    reactants=[
        m.Complex('ca2_IP3R')
    ],
    products=[
        m.Complex('cai_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAA_BACKWARD
)

# ----------------------------------------------------------
# Open <-> Ca2_IP3
# ----------------------------------------------------------

open_IP3R_bind_ca_f = m.ReactionRule(
    reactants=[
        m.Complex('open_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('ca2_ip3_IP3R')
    ],
    forward_rate=CAI_FORWARD
)

open_IP3R_bind_ca_b = m.ReactionRule(
    reactants=[
        m.Complex('ca2_ip3_IP3R')
    ],
    products=[
        m.Complex('open_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAI_BACKWARD
)

# ----------------------------------------------------------
# Cai_IP3 <-> Ca2_IP3
# ----------------------------------------------------------

cai_ip3_IP3R_bind_ca_f = m.ReactionRule(
    reactants=[
        m.Complex('cai_ip3_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('ca2_ip3_IP3R')
    ],
    forward_rate=CAA_FORWARD
)

cai_ip3_IP3R_bind_ca_b = m.ReactionRule(
    reactants=[
        m.Complex('ca2_ip3_IP3R')
    ],
    products=[
        m.Complex('cai_ip3_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=CAA_BACKWARD
)
