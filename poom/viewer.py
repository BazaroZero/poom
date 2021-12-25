from math import cos, sin

from pygame.math import Vector2


class Viewer:
    """Camera-like object. Has position and view direction."""

    def __init__(self, position: Vector2, angle: float) -> None:
        """Initialize viewer.

        :param position: vector with coordinates
        :param angle: view angle in radians
        """
        self._position = position
        self._angle = angle

    position = property(lambda self: self._position)
    angle = property(lambda self: self._angle)

    @property
    def view_vector(self) -> Vector2:
        """Get normalized vector of player view direction."""
        return Vector2(cos(self._angle), sin(self._angle))
