#!/bin/bash

now=$(date +%d)$(date +%m)$(date +%Y)
configFile=/etc/lirc/lircd.conf
remotesDir=/etc/lirc/remotes/

if [ -d $remotesDir ] ; then
 echo "Remotes dir found"
else
 echo "No remotes directory found"
 exit 1
fi

if [ $(ls -b $remotesDir | wc -l) -le 0 ] ; then
 echo "No remotes found, skipping"
 exit 1
fi
 
if [ -e $configFile ]; then
 i=1
 backupFile=$configFile.$now
 while [ -e $backupFile ]; do
  backupFile=$configFile.$now-$i
  i=$i+1
 done

 echo Copying $configFile to $backupFile
 cp $configFile $backupFile
fi

echo Building configFile
echo "" >$configFile

for file in $(ls -b $remotesDir) 
do
 fileType=$(file $remotesDir$file | cut -d\   -f2)
 if [ $fileType = "C" ]; then
  fileType=$(file $remotesDir$file | cut -d\   -f4)
 fi
 if [ $fileType = "ASCII"  ]; then
  cat $remotesDir$file >> $configFile
  echo "" >>$configFile
 fi
done

echo "For config to take effect, restart LIRC"

