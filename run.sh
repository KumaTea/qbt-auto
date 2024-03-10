#!/usr/bin/env bash

set -ex

cd /home/kuma/qbt

# conda activate qbt || alias python3='/home/kuma/.conda/envs/qbt/bin/python3'

# python3 main.py > /tmp/qbt.log 2>&1 &
/usr/bin/python3 main.py > /tmp/qbt.log 2>&1 &
