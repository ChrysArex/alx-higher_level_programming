#!/bin/bash
#Bash script that takes in a URL and displays the size of the respons's body
curl -s -I "$1" | grep "Content-Length" | cut -b 17-
