#!/bin/bash
# takes in a URL,sends request to URL,displays the size of body of the response
curl -s "$1" | wc -c
