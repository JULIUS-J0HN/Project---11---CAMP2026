"""
=============================================================
AstroCell

core/species.py

Defines biological species used throughout the model.

These classes are independent of MCell. They simply store
information about each molecule. The MCell interface will
later convert these objects into MCell molecules.

Author:
Ishatpreet Singh
=============================================================
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Dimension(Enum):
    """Spatial dimension of a molecule."""
    VOLUME = 3
    SURFACE = 2


@dataclass
class Species:
    """
    Base class for all molecular species.
    """

    name: str
    dimension: Dimension
    diffusion: float

    initial_concentration: Optional[float] = None
    initial_density: Optional[float] = None

    compartment: Optional[str] = None
    region: Optional[str] = None

    description: str = ""


@dataclass
class VolumeSpecies(Species):
    """
    Molecules that diffuse in a 3D compartment.
    """

    def __init__(
        self,
        name,
        diffusion,
        compartment,
        initial_concentration=0.0,
        description=""
    ):

        super().__init__(
            name=name,
            dimension=Dimension.VOLUME,
            diffusion=diffusion,
            compartment=compartment,
            initial_concentration=initial_concentration,
            description=description
        )


@dataclass
class SurfaceSpecies(Species):
    """
    Molecules that reside on membranes.
    """

    def __init__(
        self,
        name,
        diffusion,
        region,
        initial_density=0.0,
        description=""
    ):

        super().__init__(
            name=name,
            dimension=Dimension.SURFACE,
            diffusion=diffusion,
            region=region,
            initial_density=initial_density,
            description=description
        )


def print_species(species):
    """
    Utility function for debugging.
    """

    print("----------------------------")
    print(f"Name       : {species.name}")
    print(f"Dimension  : {species.dimension.name}")
    print(f"Diffusion  : {species.diffusion}")

    if species.dimension == Dimension.VOLUME:
        print(f"Compartment: {species.compartment}")
        print(f"Initial    : {species.initial_concentration}")

    else:
        print(f"Region      : {species.region}")
        print(f"Density     : {species.initial_density}")

    print("----------------------------")
