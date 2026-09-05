#!/bin/bash
set -e

# Start Aria2 daemon if not running
if ! pgrep -x "aria2c" > /dev/null; then
    echo "Starting Aria2..."
    aria2c --conf-path=/usr/src/app/aria2c.conf --daemon
fi

exec python3 -m bot
