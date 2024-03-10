#!/usr/bin/env bash

set -ex

# if ps | grep python3 > /dev/null; then
if pgrep "python3" > /dev/null; then
  echo "qbt running..."
else
  bash /home/kuma/qbt/run.sh
fi
