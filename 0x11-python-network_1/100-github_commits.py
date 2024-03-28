#!/usr/bin/python3
"""
    A script that takes 2 arguments:
    - Repsitory name.
    - Owner name.
    and lists the 10 most recent commits to the GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    request = requests.get(url)
    commits = request.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
