#!/bin/bash
#takes in url, display http methods
curl -I -X OPTIONS "$1"
