from cleo.io.io import IO
from poetry.console.application import Application
from cleo.events.console_events import COMMAND
from poetry.plugins.plugin import Plugin
from poetry.poetry import Poetry


# Pronounced like "mmmmultikill" in Quake.
class PPPPlugin(Plugin):
    def activate(self, application: Application, io: IO):

        # application.poetry.pool.remove_repository()
        application.event_dispatcher.add_listener(
            COMMAND, self.load_dotenv
        )
