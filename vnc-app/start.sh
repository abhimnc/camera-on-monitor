#!/bin/bash

export XDG_RUNTIME_DIR=/tmp/runtime-root
mkdir -p $XDG_RUNTIME_DIR
chmod 700 $XDG_RUNTIME_DIR


export DISPLAY=:1
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

if [ -z ${VNC_PASS} ]; then
  echo "STARTING VNC WITHOUT PASSWORD"
  supervisord -c /etc/supervisor/supervisord_np.conf  
else
  echo "STARTING VNC WITH PASSWORD"
  supervisord -c /etc/supervisor/supervisord.conf
fi