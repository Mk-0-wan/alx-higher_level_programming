#!/bin/bash
# Sending a post request using curl
curl -d 'email=test%40gmail%2ecom&subject=I%20will%20always%20be%20here%20for%20PLD' -X POST "$1"
