#!/bin/bash
# sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -sI 0.0.0.0:5000/route_4 | grep -w "Allow:" | cut -d' ' -f2-
