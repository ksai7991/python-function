#!/bin/bash

set -e

virtualenv --without-pip virtualenv

# For Python 3.11 runtime
pip install -r requirements.txt --target virtualenv/lib/python3.11/site-packages
