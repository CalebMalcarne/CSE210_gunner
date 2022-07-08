from constants import *
from game.casting.cast import Cast
from game.scripting.action_callback import ActionCallback
from game.scripting.script import Script


class Director(ActionCallback):
    """A person who directs the game."""

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._cast = None
        self._script = None
        
    def on_stop(self):
        """Overriden ActionCallback method stops the game."""
        pass
        # TODO: fix this method so it works
        # self._execute_actions(UNLOAD)
        # self._execute_actions(RELEASE)
        
    def start_game(self, cast, script):
        """Starts the game. Runs the main game loop."""
        # set the cast and script to the given ones
        self._cast = cast
        self._script = script

        # run the main game loop
        self._execute_actions(INITIALIZE)
        self._execute_actions(LOAD)
        while self._video_service.is_window_open():
            self._execute_actions(INPUT)
            self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)

        self._execute_actions(UNLOAD)
        self._execute_actions(RELEASE)
        
    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script, self)          