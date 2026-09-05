set -e
aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all=true --listen-port=6800 --daemon=true
exec python3 -m bot
