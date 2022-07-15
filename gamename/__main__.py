import constants

from game.casting.cast import Cast
from game.scripting.script import Script
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.audio_service import AudioService
from game.shared.color import Color
from game.shared.point import Point
from game.scripting.handle_menu_system import handleMenuSystem


def main():

    # create the cast
    cast = Cast()

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    audio_service = AudioService()

    draw_actors_instance = DrawActorsAction(video_service)

    script = Script()
    script.add_action("update", handleMenuSystem(
        keyboard_service, draw_actors_instance, video_service, audio_service))
    script.add_action("output", draw_actors_instance)

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
