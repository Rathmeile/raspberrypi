#!/bin/bash

# https://www.dummies.com/computers/operating-systems/linux/how-to-share-files-with-nfs-on-linux-systems/
# Meh, didn't work, trying another

# https://pimylifeup.com/raspberry-pi-nfs/

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install nfs-kernel-server -y

echo >>/etc/exports <<EOF
/mnt/exports 192.168.0.0/24(rw,sync,no_subtree_check)
EOF

sudo mkdir -p /mnt/scans

sudo chown -R pi:pi /mnt/nfsshare
sudo find /mnt/nfsshare/ -type d -exec chmod 755 {} \;
sudo find /mnt/nfsshare/ -type f -exec chmod 644 {} \;
