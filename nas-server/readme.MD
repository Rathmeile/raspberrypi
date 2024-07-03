# Raspberry Pi Storage Server

## Setup

### Install raspbian

### Update OS

sudo apt update -y
sudo apt upgrade -y

### Install NAS/NFS access

https://www.stuffaboutcode.com/2012/05/raspberry-pi-connect-nas-windows-share.html
https://forums.buffalotech.com/index.php?topic=7242.0

sudo apt install smbfs smb-client cifs-utils -y

#### Create mount

mkdir /home/pi/nas
cd nas
mkdir myShare

#### Edit fstab file

sudo vi /etc/fstab

//myNAS/myShare /home/pi/myNAS/myShare cifs username=your_username,password=your_password,workgroup=your_workgroup,vers=1.0,users,auto,user_xattr 0 0

