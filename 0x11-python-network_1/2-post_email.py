#!/usr/bin/python3
"""
    This script does tthe following:
        - Takes in a URL with an email as a parameter,
        - Sends a POST request to the passed URL, and
        - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    payload = urllib.parse.urlencode(email).encode("ascii")

    req = urllib.request.Request(url, payload)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
