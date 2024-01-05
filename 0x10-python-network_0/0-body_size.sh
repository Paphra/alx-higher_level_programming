#!/usr/bin/env bash
# A Script that sends a request and displays the size of the response body
url="$1"
curl -sI $url | grep 'Content-Length' | awk '{print $2}'
