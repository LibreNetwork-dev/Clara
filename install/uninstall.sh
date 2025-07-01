#!/bin/bash

set -e

SERVICE_NAME=clara-py.service
BIN_DIR=/usr/local/bin/clara

REAL_USER=$(logname)
USER_HOME=$(eval echo "~$REAL_USER")
USER_UNIT_DIR="$USER_HOME/.config/systemd/user"

echo "Uninstalling $SERVICE_NAME for user $REAL_USER..."

echo "[1/4] Stopping user service (if running)..."
sudo runuser -l "$REAL_USER" -c \
  'XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user stop clara-py.service || true'

echo "[2/4] Disabling user service..."
sudo runuser -l "$REAL_USER" -c \
  'XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user disable clara-py.service || true'

if [[ -f "$USER_UNIT_DIR/$SERVICE_NAME" ]]; then
    echo "[3/4] Removing service file..."
    sudo rm -f "$USER_UNIT_DIR/$SERVICE_NAME"
else
    echo "[3/4] Service file already removed."
fi

echo "[4/4] Reloading systemd user units..."
sudo runuser -l "$REAL_USER" -c \
  'XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user daemon-reload'

if [[ -d "$BIN_DIR" ]]; then
    echo "Removing $BIN_DIR..."
    sudo rm -rf "$BIN_DIR"
fi

echo "Uninstalled successfully."
