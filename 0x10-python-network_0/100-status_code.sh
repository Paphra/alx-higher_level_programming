#!/bin/bash
# sends a request to URl
curl -s -o /dev/null -w "%{http_code}\n" "$1"
