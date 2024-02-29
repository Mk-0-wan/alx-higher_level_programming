#!/bin/bash
# getting all allowed methods
curl -s -i -X OPTIONS "$1" | grep -i "Allow" | awk '{print $2}' FS=: | sed 's/ //'
