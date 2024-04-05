from .common import EventBuilder, EventCommon, name_inner_event
from ..tl import types


@name_inner_event
class BusinessMessageDeleted(EventBuilder):
    """
    Occurs whenever a business message is deleted. Note that this event isn't 100%
    reliable, since Telegram doesn't always notify the clients that a message
    was deleted.
    """
    @classmethod
    def build(cls, update, others=None, self_id=None):
        if isinstance(update, types.UpdateBotDeleteBusinessMessage):
            return cls.Event(
                connection_id=update.connection_id,
                deleted_ids=update.messages,
                peer=None
            )

    class Event(EventCommon):
        def __init__(self, connection_id, deleted_ids, peer):
            super().__init__(
                chat_peer=peer, msg_id=(deleted_ids or [0])[0]
            )
            self.connection_id = connection_id
            self.deleted_id = None if not deleted_ids else deleted_ids[0]
            self.deleted_ids = deleted_ids
