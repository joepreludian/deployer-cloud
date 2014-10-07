#!/bin/sh
sudo yum install python-pip git python-devel -y;
sudo yum groupinstall "Development Tools" -y;
sudo pip install virtualenv;