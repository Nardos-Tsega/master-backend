import argparse
from clients.github_client import GithubAPIClient
from services.github_services import ActivityService
from utils.event_parser import EventParser
from clients.github_client import NotFoundError, RateLimitError, GitHubAPIError

def main():
    parser = argparse.ArgumentParser(
            prog="github-activity",
            description="Track recent GitHub activity for a user",
        )
    
    parser.add_argument("username", help="Github username")
    parser.add_argument("--limit", type=int, default=20, help="Max number of events to fetch (default: 20)")
    
    args = parser.parse_args()
    
    client = GithubAPIClient()
    github_service = ActivityService(client, EventParser())
    
    try:
        lines = github_service.get_activity(args.username, limit=args.limit)
    except NotFoundError:
        print(f"User '{args.username}' not found.")
        return 1
    except RateLimitError as e:
        print(f"{e}")
        return 2
    except GitHubAPIError as e:
        print(f"Error: {e}")
        return 3
    
    if not lines:
        print(f"No recent public activity for '{args.username}")
        return 0
    
    print(f"Recent activity for {args.username}")
    for line in lines:
        print(line)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())