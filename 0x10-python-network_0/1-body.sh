#!/bin/bash
# sends a GET request to the URL, and displays its body if code is 200
curl -s -w "%{http_code}" $1 | awk '$1 == "200" {print prev} {prev = $0}'
