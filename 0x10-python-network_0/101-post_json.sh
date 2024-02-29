#!/bin/bash
# Sending a post request with a json data file
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
