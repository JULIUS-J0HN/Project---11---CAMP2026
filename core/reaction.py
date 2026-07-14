"""
=============================================================
AstroCell

core/reaction.py

Defines biochemical reactions.

A Reaction object stores all information needed to
generate MCell reactions.

Author:
Ishatpreet Singh
=============================================================
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Reaction:
    """
    Generic biochemical reaction.
    """

    name: str

    reactants: List

    products: List

    forward_rate: float

    reverse_rate: Optional[float] = None

    compartment: Optional[str] = None

    region: Optional[str] = None

    description: str = ""

    reversible: bool = False

    def __post_init__(self):

        if self.reverse_rate is not None:
            self.reversible = True

    def reaction_string(self):

        lhs = " + ".join([x.name for x in self.reactants])

        rhs = " + ".join([x.name for x in self.products])

        return f"{lhs} -> {rhs}"

    def print(self):

        print("--------------------------------------")
        print(self.name)
        print("--------------------------------------")

        print(self.reaction_string())

        print(f"kf : {self.forward_rate}")

        if self.reversible:
            print(f"kr : {self.reverse_rate}")

        if self.compartment:
            print(f"Compartment : {self.compartment}")

        if self.region:
            print(f"Surface : {self.region}")

        print("--------------------------------------")
