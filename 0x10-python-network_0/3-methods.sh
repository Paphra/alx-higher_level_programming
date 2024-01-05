#!/bin/bash
# diplays all HTTP methods that the server will accept
curl -sI -X OPTIONS $1 | grep 'allow' | awk '{print $2}'
