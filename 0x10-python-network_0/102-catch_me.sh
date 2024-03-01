#!/bin/bash
# getting the request from another location 
curl -s -X PUT -L 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: School"
