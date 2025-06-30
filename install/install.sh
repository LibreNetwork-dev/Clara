#!/bin/bash

set -e 

if systemctl is-active --quiet clara-py.service; then
    echo "Stopping clara-py.service..."
    sudo systemctl kill clara-py.service || echo "Failed to kill clara-py.service, but moving on."
fi

sudo mkdir -p /usr/local/bin/clara/
sudo cp -r ../dist/* /usr/local/bin/clara/

REAL_USER=$(logname)
USER_HOME=$(eval echo "~$REAL_USER")
USER_UNIT_DIR="$USER_HOME/.config/systemd/user"

echo "[0/3] installing clara-py.service for user $REAL_USER"
sudo -u "$REAL_USER" mkdir -p "$USER_UNIT_DIR"
sudo cp clara-py.service "$USER_UNIT_DIR/"
sudo chown "$REAL_USER:$REAL_USER" "$USER_UNIT_DIR/clara-py.service"
sudo chmod 644 "$USER_UNIT_DIR/clara-py.service"
echo "[1/3] installed clara-py.service"

echo "[2/3] reloading systemd user units"
sudo loginctl enable-linger "$REAL_USER"
sudo runuser -l "$REAL_USER" -c 'XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user daemon-reload'

echo "[3/3] enabling and starting user service"
sudo runuser -l "$REAL_USER" -c 'XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user enable --now clara-py.service'


echo "Finished installation"