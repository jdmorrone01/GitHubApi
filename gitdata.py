import requests
import json


def getGitRep(user):

    url = f"https://api.github.com/users/{user}/repos"
    user_data = requests.get(url).json()

    for repository in user_data:
        rep_name = repository["name"]
        url = f"https://api.github.com/users/{user}/{rep_name}/commits"
        usr_commits = len(requests.get(url).json())
        result = "Repo: "+rep_name+" Number of commits: "+str(usr_commits)
        print(result)

    return True
