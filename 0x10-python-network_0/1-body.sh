#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response for only 200 status codes
curl -Ls "$1"
