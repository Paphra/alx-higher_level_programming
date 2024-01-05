#!/bin/bash
# A Script that sends a request and displays the size of the response body
curl -sI $1 | grep 'Content-Length' | awk '{print $2}'
