#!/bin/bash

DEVICE=skyq

COMMANDS="
qhome 1
pause 1
qdown 5
qdown 5
qselect 1
qright 3
qselect 1
pause 15
qselect 1
pause 5
qdown 5
qselect 1
pause 1
qselect 1
"

while IFS= read -r line
do
  if [ "$line" == "" ];
  then
    continue
  fi
  match=$( echo "$line" | grep "pause" | wc -l )

    QTY=$(echo "$line" | awk '{print $2'})
    CMD=$( echo "$line" | awk '{print $1}')
# | xargs irsend SEND_ONCE $DEVICE)

  if [ "$CMD" == "pause" ];
  then
    echo Pausing for $QTY seconds
    sleep $QTY
  else
    CMD="irsend SEND_ONCE $DEVICE $CMD"
    for i in $(seq 1 $QTY)
    do
      echo $CMD
      $CMD
    done
  fi

done <<< "$COMMANDS"
