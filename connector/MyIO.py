from rasa.core.channels.channel import InputChannel
from typing import Any, Text, Dict, List
from typing import Text
class TestChannel(InputChannel):
    def name() -> Text:
        """Name of your custom channel."""
        return "testchannel"