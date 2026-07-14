#!/usr/bin/env python3

"""
AstroCell
model.py

Main simulation driver.
"""

import os
import sys
import importlib.util

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ----------------------------------------------------------
# Load MCell
# ----------------------------------------------------------

MCELL_PATH = os.environ.get("MCELL_PATH", "")

if not MCELL_PATH:
    raise RuntimeError("MCELL_PATH environment variable is not set.")

LIB_PATH = os.path.join(MCELL_PATH, "lib")

sys.path.append(LIB_PATH)

import mcell as m


# ----------------------------------------------------------
# Parameters
# ----------------------------------------------------------

import shared

if os.path.exists(os.path.join(MODEL_PATH, "customization.py")):
    import customization
else:
    customization = None


if customization and hasattr(customization, "custom_argparse_and_parameters"):
    customization.custom_argparse_and_parameters()


from parameters import *


# ----------------------------------------------------------
# Resume Checkpoint
# ----------------------------------------------------------

checkpoint_dir = m.run_utils.get_last_checkpoint_dir(SEED)

if checkpoint_dir:

    sys.path = m.run_utils.remove_cwd(sys.path)

    sys.path.append(checkpoint_dir)

    spec = importlib.util.spec_from_file_location(
        "model",
        os.path.join(checkpoint_dir, "model.py")
    )

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    sys.exit(0)


# ----------------------------------------------------------
# Create Model
# ----------------------------------------------------------

model = m.Model()

model.config.time_step = TIME_STEP
model.config.seed = SEED
model.config.total_iterations = ITERATIONS

model.config.partition_dimension = 20
model.config.subpartition_dimension = 0.1


# ----------------------------------------------------------
# Notifications
# ----------------------------------------------------------

model.notifications.rxn_and_species_report = False

model.notifications.rxn_probability_changed = True

model.warnings.high_reaction_probability = m.WarningLevel.IGNORE


# ----------------------------------------------------------
# Import Components
# ----------------------------------------------------------

import geometry

import subsystem

import instantiation

import observables


model.add_subsystem(
    subsystem.subsystem
)

model.add_instantiation(
    instantiation.instantiation
)

model.add_observables(
    observables.observables
)


# ----------------------------------------------------------
# Optional User Configuration
# ----------------------------------------------------------

if customization and hasattr(customization, "custom_config"):

    customization.custom_config(model)


# ----------------------------------------------------------
# Initialize
# ----------------------------------------------------------

model.initialize()


# ----------------------------------------------------------
# Export Data Model
# ----------------------------------------------------------

if EXPORT_DATA_MODEL and model.viz_outputs:

    model.export_data_model()


# ----------------------------------------------------------
# Dump
# ----------------------------------------------------------

if DUMP:

    model.dump_internal_state()


# ----------------------------------------------------------
# Run
# ----------------------------------------------------------

if customization and hasattr(customization, "custom_init_and_run"):

    customization.custom_init_and_run(model)

else:

    model.run_iterations(ITERATIONS)

    model.end_simulation()
