from .common import name_inner_event
from .newbusinessmessage import NewBusinessMessage
from ..tl import types


@name_inner_event
class BusinessMessageEdited(NewBusinessMessage):
    """
    Occurs whenever a business message is edited. Just like `NewBusinessMessage
    <telethon.events.newbusinessmessage.NewBusinessMessage>`, you should treat
    this event as a `Message <telethon.tl.custom.message.Message>`.
    """
    @classmethod
    def build(cls, update, others=None, self_id=None):
        if isinstance(update, types.UpdateBotEditBusinessMessage):
            return cls.Event(update.message, update.connection_id)

    class Event(NewBusinessMessage.Event):
        pass  # Required if we want a different name for it
