#!/bin/bash

# https://www.tomshardware.com/uk/how-to/raspberry-pi-print-server

# Update repos
sudo apt update

# Install Common Unix Print System software
sudo apt install cups

# Allow pi user to access printer services
sudo usermod -a -G lpadmin pi

# Create a static IP address and details
# ideally add if not present
echo >>"/etc/dhcpcd.conf" <<EOF
interface wlan0
static ip_address=193.168.0.23
static routers=192.168.0.1/24
static domain_name_servers=192.168.0.1
EOF

# Allow use from anywhere
sudo cupsctl --remote-any

 