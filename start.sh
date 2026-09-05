#!/bin/bash
set -e

# Start Aria2 daemon using precise parameters requested by support
if ! pgrep -x "aria2c" > /dev/null; then
    echo "Starting Aria2..."
    aria2c --enable-rpc=true --rpc-listen-all=true --rpc-allow-origin-all=true --rpc-listen-port=6800 --rpc-max-download-limit=0 --check-certificate=false &
    
    # Give Aria2c 3 seconds to fully open the 6800 port boundary
    sleep 3
fi

exec python3 -m bot
