from pathlib import Path
from game.scripting.action import Action


class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        # TODO: change the assets paths to whatever they should be
        self._audio_service.load_sounds("final_project/assets/sounds")
        self._video_service.load_fonts("final_project/assets/fonts")
        self._video_service.load_images("final_project/assets/images")
        