#!/bin/bash
# diplays all HTTP methods that the server will accept
curl -sI --request OPTIONS "$1" | awk -F': ' '/^allow:/ {print $2}'
