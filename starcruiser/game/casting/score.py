import constants
from game.casting.actor import Actor
from game.shared.point import Point
import random
from game.casting.upgrade import Upgrade


class Score(Actor):
    """
    A record of points made or lost. 

    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """

    def __init__(self, cast):
        super().__init__()
        self._points = 0
        self.set_position(Point(constants.CELL_SIZE * 2, constants.CELL_SIZE * 2))
        self._cast = cast
        # handle upgrades
        self._upgrade_list = constants.UPGRADE_LIST
        self._upgrade_progress = 0
        self.add_points(0)



    def get_points(self):
        return self._points

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        # add the correct amount of points
        self._points += points
        self.set_text(f"Score: {self._points}")

        # if there are more upgrades left
        if self._upgrade_progress <= len(self._upgrade_list)-1:
            # if we've reached the next upgrade point requirement
            if self._points > self._upgrade_list[self._upgrade_progress][0]:
                # make upgrade
                self.make_upgrade(self._upgrade_list[self._upgrade_progress][1])
                # increment
                self._upgrade_progress += 1



    def make_upgrade(self, upgradetype):
        position = Point(random.randint(0, constants.COLUMNS)
                         * (constants.CELL_SIZE), 0)
        # set a velocity to move upward
        velocity = Point(0, constants.CELL_SIZE * 0.25)
        text = "+"  # cross keyboard symbol (for health)
        color = constants.YELLOW
        # apply attributes to a new instance of laser
        upgrade = Upgrade(self._cast)
        upgrade.set_position(position)
        upgrade.set_velocity(velocity)
        upgrade.set_text(text)
        upgrade.set_font_size(25)
        upgrade.set_color(color)
        upgrade.set_type(upgradetype)

        # add laser to the "upgrades" cast
        self._cast.add_actor("upgrades", upgrade)
