import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body
    

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    

    def get_all_emojis(self):
        r = requests.get('https://api.github.com/emojis')
        body = r.json()

        return dict(code=r.status_code, body = body)
    

    def get_all_commits(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
        body = r.json()

        return body


    def get_commit(self, owner, repo, sha_commit):
            r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits/{sha_commit}")
            body = r.json()

            return dict(code=r.status_code, body = body)