from typing import List, Dict, Any

class EventParser:
    
    @staticmethod
    def _repo(event: Dict[str, Any]):
        return event.get("repo", {}).get("name", "<unknown-repo>")
    
    @staticmethod
    def _plural(n: int, singular: str) -> str:
        return f"{n} {singular}" if n == 1 else f"{n} {singular}s"
    
    def parse_one(self, event: Dict[str, Any]):
        etype = event.get('type')
        repo = self._repo(event)
        payload = event.get("payload", {}) or {}
        
        if etype == "PushEvent":
            commits = payload.get("commits", []) or []
            return f"Pushed {self._plural(len(commits), "commit")} to {repo}"
        
        if etype == "IssuesEvent":
            action = payload.get("action", "")
            issue = payload.get("issue", {}) or {}
            num = issue.get("number")
            verb = "Opened" if action == "opened" else "Closed" if action == "closed" else action.capitalize() or "Updated"
            return f"{verb} issue #{num}" + (f" in {repo}" if num is not None else f" in {repo}")
        
        if etype == "IssueCommentEvent":
            issue = payload.get("issue", {}) or {}
            num = issue.get("number")
            if num is not None:
                return f"Commented on issue #{num} in {repo}" 
        
        if etype == "PullRequestEvent":
            action = payload.get("action", "")
            pr = payload.get("pull_request", {}) or {}
            num = pr.get("number")
            merged = pr.get("merged")
            if action == "closed" and merged:
                return f"Merged pull request #{num} in {repo}"
            verb = "Opened" if action == "opened" else "Closed" if action == "closed" else action.capitalize() or "Updated"
            return f"{verb} pull request #{num}" + (f" in {repo}" if num is not None else f" in {repo}")
        
        if etype == "PullRequestReviewEvent":
            pr = payload.get("pull_request", {}) or {}
            num = pr.get("number")
            return f"Reviewed pull request #{num} in {repo}" if num is not None else f"Reviewed a pull request in {repo}"
                    
        if etype == "WatchEvent":
            return f"Starred {repo}"
        
        if etype == "CreateEvent":
            ref_type = payload.get("ref_type", "content")
            ref = payload.get("ref")
            if ref_type == "repository":
                return f"Created repository {repo}"
            if ref:
                return f"Created {ref_type} {ref} in {repo}"
            return f"Created a {ref_type} in {repo}"
        
        if etype == "DeleteEvent":
            ref_type = payload.get("ref_type", "content")
            ref = payload.get("ref")
            if ref:
                return f"Deleted {ref_type} {ref} in {repo}"
            return f"Deleted a {ref_type} in {repo}"
        
        if etype == "ForkEvent":
            forkee = payload.get("forkee", {}) or {}
            to_full = forkee.get("full_name")
            return f"Forked {repo} to {to_full}" if to_full else f"Forked {repo}"
        
        if etype == "ReleaseEvent":
            action = payload.get("action", "published")
            release = payload.get("release", {}) or {}
            tag = release.get("tag_name")
            prefix = "Published" if action == "published" else action.capitalize()
            return f"{prefix} release {tag} in {repo}" if tag else f"{prefix} a release in {repo}"
        
        if etype == "PublicEvent":
            return f"Made {repo} public"
        
        if etype:
            pretty = etype.replace("Event", "")
            return f"{pretty} in {repo}"
        
        return None
    
    def parse_many(self, events: List[Dict[str, Any]]):
        lines: List[str] = []
        for ev in events:
            line = self.parse_one(ev)
            if line:
                lines.append(f"- {line}")
        return lines