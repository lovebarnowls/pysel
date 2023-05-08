#!/bin/bash

echo -e 'Checking for Dependencies:'

for package in python3-pip; do
    if dpkg -s $package > /dev/null 2>/dev/null; then
        echo $package is installed
        else
        echo -e "$package is NOT installed!"
        apt install $package
    fi
done

echo -e 'DONE\nInstalling Python modules'
for module in pyarmor; do
    pip3 install $module
done

defaultuser=$(getent passwd 1000 | cut -d: -f 1)
echo -e "The default user is currently set to" $defaultuser

defaultlocation='/home/'$cpuser'/Desktop/score.html'
echo -e "The score report location is currently set to "$defaultlocation
# read scorelocation
echo -e '#!usr/bin/env python3\n\nSCORE_REPORT_LOCATION = '\"$defaultlocation\" > score.py

echo "Building Engine..."
echo -e 's_config = """' > score.py
cat PySEL.conf >> score.py
echo -e '"""' >> score.py
cat pysel.py >> score.py

echo -e "DONE\nObfuscating pysel.py..."
pyarmor obfuscate --recursive --output /usr/local/bin/pysel/ score.py
#sed -i '1 i\from pytransform import pyarmor_runtime\npyarmor_runtime()' /usr/local/bin/pysel/score.py
chown $cpuser:$cpuser /usr/local/bin/pysel

echo -e 'DONE\nCreating /pysel-static directory...'
mkdir -p /pysel-static
cp static/*.png /pysel-static/
cp static/*.wav /pysel-static/
cp static/forensic?.txt /home/ubuntu/Desktop
cp static/Readme.txt /home/ubuntu/Desktop
cp static/space-cadets.txt /home/ubuntu/Documents
chown ubuntu:ubuntu /home/ubuntu/Desktop/*
chmod a+rw /home/ubuntu/Desktop/*

echo -e 'DONE\nCreating Team ID Changer...'
# chown $cpuser:$cpuser static/SetTeam.desktop
# cp static/SetTeam.desktop '/home/'$cpuser'/Desktop/'
# chmod 777 '/home/'$cpuser'/Desktop/SetTeam.desktop'
# cp static/setid.sh /pysel-static/
# chmod +x /pysel-static/setid.sh
chmod 777 /usr/local/bin/
echo 'Mensa Students' > /usr/local/bin/pysel/TEAM

echo -e 'DONE\nRegistering scoring service...'
cp static/pysel_scoring.service /etc/systemd/system/
systemctl enable pysel_scoring.service
systemctl start pysel_scoring.service

sudo rm -rf /home/ubuntu/pysel/inject.sh
sudo rm -rf /home/ubuntu/pysel/local.sh
