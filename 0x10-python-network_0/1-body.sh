#!/bin/bash
#sends a GET request to the URL, and displays the body of the response
if [ -n "$(curl -I -L -s "$1" | grep "HTTP/1.1 200 OK")" ]; then curl -L -s "$1"; fi
