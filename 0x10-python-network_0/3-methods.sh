#!/bin/bash
# diplays all HTTP methods that the server will accept
curl -sI -X OPTIONS $1 | grep -i '^allow:' | tr -d '\r' | awk '{print $2}'
