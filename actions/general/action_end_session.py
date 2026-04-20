from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType


class ActionEndSession(Action):
    def name(self) -> str:
        return "action_end_session"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict
    ) -> list[EventType]:
        return [{"event": "session_ended"}]
