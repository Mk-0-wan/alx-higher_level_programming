#!/bin/bash
# getting the body of request that returned 200 status response 
sh -c "[ $(curl -s -o /dev/null -w '%{http_code}' "$1") -eq '200' ]" && echo -n "$(curl -s --get "$1")"
