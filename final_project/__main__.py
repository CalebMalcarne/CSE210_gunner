from constants import *
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.unload_assets_action import UnloadAssetsAction

from game.directing.director import Director
from game.casting.cast import Cast
from game.scripting.script import Script
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_video_service import RaylibVideoService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService


def main():

    # create the services that we need
    audio_service = RaylibAudioService()
    video_service = RaylibVideoService()
    keyboard_service = RaylibKeyboardService()
    # TODO: create any other services we need

    # create the cast and actors we need
    cast = Cast()
    # TODO: create any actors that we need
    # TODO: add the actors to tche cast in the appropriate group

    # create the script and actions we need
    script = Script()
    initialize_devices_action = InitializeDevicesAction(audio_service, video_service)
    load_assets_action = LoadAssetsAction(audio_service, video_service)
    # TODO: create any input phase actions
    # TODO: create any update phase actions
    start_drawing_action = StartDrawingAction(video_service)
    # TODO: create any other output phase actions
    end_drawing_action = EndDrawingAction(video_service)
    unload_assets_action = UnloadAssetsAction(audio_service, video_service)
    release_devices_action = ReleaseDevicesAction(audio_service, video_service)
    
    script.add_action(INITIALIZE, initialize_devices_action)
    script.add_action(LOAD, load_assets_action)
    # TODO: add any input phase actions
    # TODO: add any update phase actions
    script.add_action(OUTPUT, start_drawing_action)
    # TODO: add any other output phase actions
    script.add_action(OUTPUT, end_drawing_action)
    script.add_action(UNLOAD, unload_assets_action)
    script.add_action(RELEASE, release_devices_action)

    # start the game
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()