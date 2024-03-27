#!/bin/bash
# Display all HTTP methods a given server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
