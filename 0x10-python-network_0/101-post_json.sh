#!/bin/bash
# sends a JSON POST request
curl -s -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
