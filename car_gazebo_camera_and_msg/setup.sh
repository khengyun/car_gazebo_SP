#!/bin/bash


pip3 install -r $PWD/requirements.txt


#install cuda

if $(nvcc --version | awk '/V([0-9]+.){2}.[0-9]+$/ {  sub("V","",$NF);if ($NF>11.3) { exit 0 } else { exit 1 } }')
then 
    nvcc --version
else 
echo "Installing... cuda"

echo "DONE"
fi

