#!/bin/bash
# sending a custom header
curl -s --header "X-School-User-Id: 98" "$1"
