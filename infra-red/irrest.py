#!/usr/bin/env python

# Run command and capture output
# https://stackoverflow.com/questions/4760215/running-shell-command-from-python-and-capturing-the-output

import web
import subprocess ## .run better but requires python3.5+ otherwise check_output
import xml.etree.ElementTree as ET
from web import form

commandList=['SEND_ONCE','SEND_START','SEND_STOP','LIST','SET_TRANSMITTERS','SIMULATE']

urls = (
    '/remote/','run_remote',
    '/remote/([A-Z_]+)/([a-zA-Z0-9\-\_]+)/([a-zA-Z0-9\-\_]+)/(\d*)','run_remote_command',
    '/view/remotes/','view_remotes',
    '/ir/reset/','reset_ir',
    '/view/remote/([a-zA-Z0-9\-\_]+)/commands/','view_remote_commands',
    '/view/commands/([a-zA-Z0-9\_\-]+)/','view_remote_commands',
    '/help/','view_help'
)

def runProcess(exe):
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        retcode = p.poll() #returns None while subprocess is running
        line = p.stdout.readline()
        yield line
        if(retcode is not None):
            break

class run_remote:
    def GET(self):
        form=run_remote_form()
        return render.formtest(run_remote_form)

class view_remote_commands:
    def GET(self,remote):
        self.response.headers['Content-type']="text/html"
        self.response.write("Viewing commands")
        cmd=['irsend','LIST',remote,'']
        output="Running:"+str(' '.join(cmd))
        for line in runProcess(cmd):
            output+=str(line)+"\n"
            output.replace("\n","<br/>")
        return """
  <html><head></head><body>
"""+output+"</body></html>"


class reset_ir:
    def GET(self):
        #cmd=['/etc/init.d/lirc','stop']
        #runProcess(cmd)
        ##for line in runProcess(cmd):
        ## output+=str(line)
        #cmd=['lircd','-d','/dev/lirc0']
        #runProcess(cmd)
        ##for line in runProcess(cmd):
        ## output+=str(line)
        #cmd=['/etc/init.d/lirc','start']
        #runProcess(cmd)
        #for line in runProcess(cmd):
        # output+=str(line)
        cmd=['sudo','/home/pyweb/resetIR.sh']
        runProcess(cmd)
        output="<p>Reset run</p>"
        return output


class run_remote_command:
    def GET(self,command,remote,button,repeat):
        repeat=int(repeat)
        if repeat<=0:
            repeat=1
        cmd=['irsend',command,remote,button]
        #result=subprocess.run(cmd,stdout=subprocess.PIPE)
        #result.stdout
        #
        #result=subprocess.check_output(cmd)
        output="Running:"+str(' '.join(cmd))
        for iteration in range(repeat):
            for line in runProcess(cmd):
                output+=str(line)
                output+="Command run<br>"
        return output


class view_remotes:
    def GET(self):
        cmd=['irsend','list','','']
        output=""
        for line in runProcess(cmd):
            #print line,
            output+=line+"<br>"
        return output

class view_remote_commands:
    def GET(self,remote):
        cmd=['irsend','list',remote,'']
        output=""
        commands=[]
        for line in runProcess(cmd):
            #output+=line+"<br>"
            # This doesn't seem to work...
            items=line.split(" ")
            commands.append(str(items[2]))
            # This works fine but shows it all
            #commands.append(line)
        output="<br>".join(commands)
        return output

class view_help:
    def GET(self):
        output="<html><body>"+"""
        URLs:<br>\n
"""+"<br>\n\n".join(urls)+"""<br>\n<br>\nCommands: <br>\n
"""+"<br>\n".join(commandList)+"""
<br>\n
<br>\n
Samples:<br>\n
http://x.x.x.x:8080/view/remotes/<br>\n
http://x.x.x.x:8080/<br>\n
http://192.168.0.23:8080/remote/SEND_ONCE/sky_rev10/power/1<br>\n
\n
<p>Download new remotes from http://lirc.sourceforge.net/remotes/</p>
</body></html>
"""
        return output


remoteList=[]
buttonList=[]

cmd=['irsend','list','','']
for line in runProcess(cmd):
    items=line.split(" ")
    if len(items)==2:
        remoteList.append(items[1])


# if form.getvalue('remote') is None:
#     print "None"
# else:
#     print "Something"
#     if len(form.getvalue('remote'))>0:
#         cmd=['irsend','list',remote,'']
#         for line in runProcess(cmd):
#             items=line.split(" ")
#             buttonList.append(str(items[2]))



## Run the hardware setup
# sudo /etc/init.d/lirc stop
# sudo lircd -d /dev/lirc0





app = web.application(urls, globals())



run_remote_form = form.Form(
  form.Dropdown('command',commandList,value='SEND_ONCE'),
  form.Dropdown('remote',remoteList),
  form.Dropdown('button',buttonList),
  form.Dropdown('repeat',range(10)),
  form.Button('Send')
)



print "Recognised URLs are:\n"
print "\n".join(urls)


form=run_remote_form()



render = web.template.render('templates/')


if __name__ == "__main__":
    app.run()
