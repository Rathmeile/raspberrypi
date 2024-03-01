#!/usr/bin/python3

# https://asimuzzaman.com/posts/send-infrared-ir-remote-signal-with-python
# https://lirc.readthedocs.io/en/latest/api-specification.html?ref=localhost
# pip install lirc

import lirc
from lirc.exceptions import LircdCommandFailure

class RemoteControl
    def __init__(self)
        print("This is the constructor method")
        self.client = lirc.Client()
        print(client.version())
        yeild client
        client.close()

    def set_remote_driver(self, driver_name):
        self.remote_driver = driver_name
    
    def list_installed_remotes(self):
        return client.list_remotes()
    
    def list_remote_keys(self, remote_name):
        if defined(remote_name):
            return self.client.list_remote_keys(remote_name)

    def send_command(self, remote_name, command, repetitions=0):
        return client_send_once(remote_name, command, repetitions)
    
    def set_driver_option(self, key, value):
        self.client.driver_option(key, value)


def main():
    # Run our functions we need here
    my_remote = RemoteControl()

    try:
        print(my_remote.list_remotes())
    except LircdCommandFailure as error:
        print(error)


if __name__ == "__main__":
    main()