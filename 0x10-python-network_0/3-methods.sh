#!/bin/bash
# diplays all HTTP methods that the server will accept
curl -s -X OPTIONS $1 | grep 'allow' | awk '{print $2}'
