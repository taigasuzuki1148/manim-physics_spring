

__all__ = [
    "Spring",
]

from typing import Iterable
import pymunk
from manim import *
from .rigid_mechanics import *

class Spring(VMobject):
    def __init__(
        self,
        length :float=3.5,
        bumps :int=14,
        start=ORIGIN,
        natural_length :float = 14,
        **kwargs
    ) -> None:
        self.length = length
        self.empty = 0.4
        self.step = 0.07
        self.bump = 0.18
        self.start = start
        self.natural_length = natural_length
        super().__init__(
            **kwargs
        )

        vertices = np.array(
            [
                [0, 0, 0],
                [self.empty, 0, 0],
                [self.empty + self.step, self.bump, 0],
                *[
                    [
                        self.empty + self.step + self.step * 2 * i,
                        self.bump * (1 - (i % 2) * 2),
                        0,
                    ]
                    for i in range(1, bumps)
                ],
                [self.empty + self.step * 2 * bumps, 0, 0],
                [self.empty * 2 + self.step * 2 * bumps, 0, 0],
            ]
        )
        vertices = vertices * [self.length /
                               (1 + 0.2 * bumps), 1, 0] + np.array(start)

        self.start_new_path(np.array(start))
        self.add_points_as_corners(
            [*(np.array(vertex) for vertex in vertices)])
        
    def start_movement(self) ->None:
        """Start movement."""
        t = ValueTracker()
        # Define displacement
        displacement = self.length-self.natural_length