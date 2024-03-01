#!/bin/bash
# getting the request from another location 
curl -s -L -X PUT -d "user_id=98" -H "Origin: school" 0.0.0.0:5000/catch_me_2
