#!/bin/bash
# getting all allowed methods
curl -I -s -w "%{stdout}" "$1" | sed -n '/Allow/p' | cut -d" " -f2-
