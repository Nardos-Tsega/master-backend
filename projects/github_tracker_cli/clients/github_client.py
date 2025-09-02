import requests # type: ignore
from typing import Optional, Dict

API_ROOT = "https://api.github.com"


class GitHubAPIError(Exception):
    """Base GitHub API error."""


class NotFoundError(GitHubAPIError):
    """Resource not found (404)."""


class RateLimitError(GitHubAPIError):
    """Rate limit exceeded (403/429)."""

class GithubAPIClient:
    def __init__(self, timeout: float = 10.0):
        self.timeout = timeout
        self.headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "GitHubActivityCLI/1.0"
        }
        
    def get(self, path:str, params: Optional[Dict[str, str]] = None):
        url = f"{API_ROOT}{path}"
        try:
            resp = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
        except requests.Timeout as e:
            raise GitHubAPIError("Request timed out.") from e
        except requests.ConnectionError as e:
            raise GitHubAPIError("Network error while connecting to GitHub.") from e
        except requests.RequestException as e:
            raise GitHubAPIError("Unexpected request error.") from e
        
        if resp.status_code == 404:
            raise NotFoundError("User not found.")
        
        if resp.status_code in (403, 429):
            reset = resp.headers.get("X-RateLimit-Reset")
            msg = "Rate limit exceeded."
            if reset:
                msg += " Try again later."
            raise RateLimitError(msg)
        
        if resp.status_code >= 400:
            raise GitHubAPIError(f"Github API error ({resp.status_code})")
        
        try:
            return resp.json()
        except ValueError as e:
            raise GitHubAPIError("Failed to parse JSON from Github") from e
            