#!/bin/bash
#takes in url, display http methods
curl -I -sX OPTIONS "$1"
