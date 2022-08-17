#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response. Pipe and redirect not allowed
curl -s -o /dev/null -I -w "%{http_code}" "$1"
