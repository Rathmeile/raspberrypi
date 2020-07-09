#!/bin/bash

sudo /etc/init.d/lirc stop
sudo lircd -d /dev/lirc0
sudo /etc/init.d/lirc start

