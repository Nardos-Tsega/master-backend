from clients.github_client import GithubAPIClient
from utils.event_parser import EventParser

class ActivityService:
    def __init__(self, client: GithubAPIClient, parser:EventParser):
        self.client = client
        self.parser = parser
    
    def get_activity(self, username:str, limit:int = 20):
        events = self.client.get(f"/users/{username}/events", params={"per_page": str("limit")})
        if not isinstance(events, list):
            return []
        return self.parser.parse_many(events)