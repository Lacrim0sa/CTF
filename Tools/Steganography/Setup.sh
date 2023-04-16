#!/bin/bash

mkdir -p /home/"$SUDO_USER"/CTF/Stegano
home="/home/$SUDO_USER/CTF/Stegano"
cd "$home"

#MAJ SYS
apt update -y && apt upgrade -y

#Stegsolve
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
chmod +x stegsolve.jar

#WINE
apt install wine64 -y

#Stegcracker
apt install stegcracker -y

#Tinyscript LSB / PIT / PVD
pip install tinyscript
wget https://gist.githubusercontent.com/dhondta/90a07d9d106775b0cd29bb51ffe15954/raw/paddinganograph.py && chmod +x paddinganograph.py && sudo mv paddinganograph.py /usr/bin/paddinganograph
wget https://gist.githubusercontent.com/dhondta/d2151c82dcd9a610a7380df1c6a0272c/raw/stegolsb.py && chmod +x stegolsb.py && sudo mv stegolsb.py /usr/bin/stegolsb
wget https://gist.githubusercontent.com/dhondta/30abb35bb8ee86109d17437b11a1477a/raw/stegopit.py && chmod +x stegopit.py && sudo mv stegopit.py /usr/bin/stegopit
wget https://gist.githubusercontent.com/dhondta/feaf4f5fb3ed8d1eb7515abe8cde4880/raw/stegopvd.py && chmod +x stegopvd.py && sudo mv stegopvd.py /usr/bin/stegopvd

#QPDF
apt install qpdf -y

#GIMP
apt install gimp -y

#Tweekpng
wget https://entropymine.com/jason/tweakpng/tweakpng-1.4.6.zip
unzip ./tweakpng-1.4.6.zip
rm -f ./tweakpng-1.4.6.zip
rm -f ./tweakpng-1.4.6/COPYING.txt && rm ./tweakpng-1.4.6/sample.png && rm ./tweakpng-1.4.6/tweakpng-src-1.4.6.zip && rm ./tweakpng-1.4.6/tweakpng.txt

#PNG Tool (pngchunks...)
apt install libpng-tools -y
apt install pngtools -y

#Cleanup
apt autoclean -y && apt autoremove -y
