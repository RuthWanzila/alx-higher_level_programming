#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
response=$(curl -s -o /dev/null -w "%{http_code}" -X PUT "http://0.0.0.0:5000/catch_me")

# Check if the response code is 200 (OK)
if [[ $response -eq 200 ]]; then
    # If the response code is 200, the server has been "caught"
    printf "You got me!\n"
fi
