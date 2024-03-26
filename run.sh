#!/usr/bin/env bash

set -ex

WORKDIR=/home/kuma/qbt

cd $WORKDIR

# conda activate qbt || alias python3='/home/kuma/.conda/envs/qbt/bin/python3'

# python3 main.py > /tmp/qbt.log 2>&1 &

export PYTHONPATH=$WORKDIR/libs
/usr/bin/python3 main.py > /tmp/qbt.log 2>&1 &
