#!/bin/bash
set -e

# Start Aria2 daemon directly with safe inline parameters
if ! pgrep -x "aria2c" > /dev/null; then
    echo "Starting Aria2..."
    aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all=true --listen-port=6800 --daemon=true
fi

exec python3 -m bot
