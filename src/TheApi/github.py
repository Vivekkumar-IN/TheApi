from ._request import Request

class GitHubClient:
    def __init__(self, token: str, username: str):
        self.token = token
        self.username = username
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.request = Request()
