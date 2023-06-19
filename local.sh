#!/bin/bash
cd /usr/local/bin
sudo mkdir pysel
cd pysel
sudo mkdir Event_checks 
sudo cp /home/ubuntu/pysel/score.py /usr/local/bin/pysel/ 
sudo cp /home/ubuntu/pysel/pysel.py /usr/local/bin/pysel/ 
sudo mv /home/ubuntu/pysel/Event_checks/* /usr/local/bin/pysel/Event_checks/ 
cd /home/ubuntu/pysel
sudo ./inject.sh -y -qq
sudo ./install.sh -y -qq
