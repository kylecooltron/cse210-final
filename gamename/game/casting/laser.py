import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Laser(Actor):
    """
    A Laser

    The responsibility of Laser is to delete itself when offscreen.

    Attributes:

    """

    def __init__(self, cast):
        super().__init__()
        self._cast = cast

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x (X ONLY FOR LASER).

        Args:
            max_x (int): The maximum x value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y())

        if y <= 0:
            self._cast.remove_actor("lasers", self)
        else:
            self._position = Point(x, y)