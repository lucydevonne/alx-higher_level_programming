#!/bin/bash
#takes in url, display http methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
