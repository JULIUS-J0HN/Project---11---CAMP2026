# ----------------------------------------------------------
# Unbound <-> IP3 Bound
# ----------------------------------------------------------

unb_IP3R_bind_ip3_f = m.ReactionRule(
    reactants=[
        m.Complex('unb_IP3R'),
        m.Complex('ip3')
    ],
    products=[
        m.Complex('ip3_IP3R')
    ],
    forward_rate=IP3_FORWARD
)

unb_IP3R_bind_ip3_b = m.ReactionRule(
    reactants=[
        m.Complex('ip3_IP3R')
    ],
    products=[
        m.Complex('unb_IP3R'),
        m.Complex('ip3')
    ],
    forward_rate=IP3_BACKWARD
)

# ----------------------------------------------------------
# Caa <-> Open
# ----------------------------------------------------------

caa_IP3R_bind_ip3_f = m.ReactionRule(
    reactants=[
        m.Complex('caa_IP3R'),
        m.Complex('ip3')
    ],
    products=[
        m.Complex('open_IP3R')
    ],
    forward_rate=IP3_FORWARD
)

caa_IP3R_bind_ip3_b = m.ReactionRule(
    reactants=[
        m.Complex('open_IP3R')
    ],
    products=[
        m.Complex('caa_IP3R'),
        m.Complex('ip3')
    ],
    forward_rate=IP3_BACKWARD
)

# ----------------------------------------------------------
# Cai <-> Cai_IP3
# ----------------------------------------------------------

cai_IP3R_bind_ip3_f = m.ReactionRule(
    reactants=[
        m.Complex('cai_IP3R'),
        m.Complex('ip3')
    ],
    products=[
        m.Complex('cai_ip3_IP3R')
    ],
    forward_rate=IP3_FORWARD
)

cai_IP3R_bind_ip3_b = m.ReactionRule(
    reactants=[
        m.Complex('cai_ip3_IP3R')
    ],
    products=[
        m.Complex('cai_IP3R'),
        m.Complex('ip3')
    ],
    forward_rate=IP3_BACKWARD
)

# ----------------------------------------------------------
# Ca2 <-> Ca2_IP3
# ----------------------------------------------------------

ca2_IP3R_bind_ip3_f = m.ReactionRule(
    reactants=[
        m.Complex('ca2_IP3R'),
        m.Complex('ip3')
    ],
    products=[
        m.Complex('ca2_ip3_IP3R')
    ],
    forward_rate=IP3_FORWARD
)

ca2_IP3R_bind_ip3_b = m.ReactionRule(
    reactants=[
        m.Complex('ca2_ip3_IP3R')
    ],
    products=[
        m.Complex('ca2_IP3R'),
        m.Complex('ip3')
    ],
    forward_rate=IP3_BACKWARD
)

# ----------------------------------------------------------
# Calcium Flux through Open IP3R
# (Faithful to original STEPS implementation)
# ----------------------------------------------------------

IP3R_flux = m.ReactionRule(
    reactants=[
        m.Complex('open_IP3R'),
        m.Complex('ca')
    ],
    products=[
        m.Complex('open_IP3R'),
        m.Complex('ca')
    ],
    forward_rate=IP3R_FLUX
)

# ==========================================================
# ADD REACTIONS TO SUBSYSTEM
# ==========================================================

subsystem.add_reaction_rule(unb_IP3R_bind_caa_f)
subsystem.add_reaction_rule(unb_IP3R_bind_caa_b)

subsystem.add_reaction_rule(unb_IP3R_bind_cai_f)
subsystem.add_reaction_rule(unb_IP3R_bind_cai_b)

subsystem.add_reaction_rule(caa_IP3R_bind_ca_f)
subsystem.add_reaction_rule(caa_IP3R_bind_ca_b)

subsystem.add_reaction_rule(ip3_IP3R_bind_caa_f)
subsystem.add_reaction_rule(ip3_IP3R_bind_caa_b)

subsystem.add_reaction_rule(ip3_IP3R_bind_cai_f)
subsystem.add_reaction_rule(ip3_IP3R_bind_cai_b)

subsystem.add_reaction_rule(cai_IP3R_bind_ca_f)
subsystem.add_reaction_rule(cai_IP3R_bind_ca_b)

subsystem.add_reaction_rule(open_IP3R_bind_ca_f)
subsystem.add_reaction_rule(open_IP3R_bind_ca_b)

subsystem.add_reaction_rule(cai_ip3_IP3R_bind_ca_f)
subsystem.add_reaction_rule(cai_ip3_IP3R_bind_ca_b)

subsystem.add_reaction_rule(unb_IP3R_bind_ip3_f)
subsystem.add_reaction_rule(unb_IP3R_bind_ip3_b)

subsystem.add_reaction_rule(caa_IP3R_bind_ip3_f)
subsystem.add_reaction_rule(caa_IP3R_bind_ip3_b)

subsystem.add_reaction_rule(cai_IP3R_bind_ip3_f)
subsystem.add_reaction_rule(cai_IP3R_bind_ip3_b)

subsystem.add_reaction_rule(ca2_IP3R_bind_ip3_f)
subsystem.add_reaction_rule(ca2_IP3R_bind_ip3_b)

subsystem.add_reaction_rule(IP3R_flux)
