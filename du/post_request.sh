#!/bin/bash

ENDPOINT_URL="http://127.0.0.1:8000/import/"

JSON_DATA=$(cat /mnt/Samsung_4TB/prog/du_whys/du/test_data.json)

curl -X POST -d "$JSON_DATA" -H "Content-Type: application/json" "$ENDPOINT_URL"
