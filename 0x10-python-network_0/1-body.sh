#!/bin/bash
# getting the body of request that returned 200 status response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s -w "%{stdout}" "$1" | tr -d "\n"
