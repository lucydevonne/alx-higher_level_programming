#!/bin/bash
#bash script that takes in url, sends request and display size of body in reponse
url=$1 curl -s $url | wc -c
