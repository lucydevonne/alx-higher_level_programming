#!/bin/bash
#bash script that takes in url, sends request and display size of body in reponse
curl -s "$1" | wc -c 
