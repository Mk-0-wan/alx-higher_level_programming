#!/bin/bash
# Sending a post request with a json data file
curl -s -d "@'$2'" "$1"
