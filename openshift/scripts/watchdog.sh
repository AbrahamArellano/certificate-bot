#!/bin/bash

python -m pip install openshift
wait
python openshift_client_container/dynamic_openshift_client.py