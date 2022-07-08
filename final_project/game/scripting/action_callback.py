class ActionCallback:
    """A callback that can be used to trigger scene changes."""

    def on_stop(self):
        """Called when we need to stop the game."""
        raise NotImplementedError("execute not implemented in base class")