#!/usr/bin/env python

# Module to provide some IR base commands #

# Call using:
#  import irmodule
#  irmodule.myfunc("input")

import subprocess

# Run command
# Return results as array

def my_func(input):
 print "Input: "+input
 return

commandList=['SEND_ONCE','SEND_START','SEND_STOP','LIST','SET_TRANSMITTERS']

commandList.remove('SET_TRANSMITTERS')
commandList.append('SIMULATE')

def ShowCommands():
  for command in commandList:
    print(command)
  return


def RunIRCommand(command,remote,button):
  cmd=['irsend','LIST',remote,'']
  outputList=[]
  for line in runProcess(cmd):
    line=line[:-1]
    outputList.append(line)
  return outputList


def PrintArray(inputList):
  for x in inputList:
    if x.strip():
      print(x)
  return


def runProcess(exe):
  p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  while(True):
    retcode = p.poll() #returns None while subprocess is running
    line = p.stdout.readline()
    yield line
    if(retcode is not None):
      break


#Test commands
PrintArray(RunIRCommand('LIST',"",""))
PrintArray(RunIRCommand('SEND_ONCE','sky_rev10','info'))


