#!/bin/bash
# getting all allowed methods
curl -s -X OPTIONS "$1" | grep -qoi 'Allow' | awk '{print $2}'
