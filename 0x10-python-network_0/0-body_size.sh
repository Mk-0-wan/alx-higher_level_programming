#!/bin/bash
# Getting the content length of the file requested by the client
curl -I -s "$1" -w "%{stdout}" | sed -n '/Content-Length/p' | cut -d" " -f2
