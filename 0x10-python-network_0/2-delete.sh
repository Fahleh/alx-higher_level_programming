#!/bin/bash
# Sends a DELETE request passed as the first argument & displays the response body
curl -sX DELETE "$1"
