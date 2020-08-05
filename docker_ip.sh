#!/bin/bash

dock_ip=$(ifconfig docker0 | grep  -m 1 inet | awk '{print $2}')
last=$(echo ${dock_ip} | tr "." " " | awk '{ print $4 }')
sum=`expr $last + 1`
ipoct1=$(echo ${dock_ip} | tr "." " " | awk '{ print $1 }')
ipoct2=$(echo ${dock_ip} | tr "." " " | awk '{ print $2 }')
ipoct3=$(echo ${dock_ip} | tr "." " " | awk '{ print $3 }')
ip=$ipoct1.$ipoct2.$ipoct3.$sum
curl http://$ip/video/2DG3pMcNNlw
