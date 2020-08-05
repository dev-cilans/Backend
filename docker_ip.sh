#!/bin/bash
echo $(ifconfig)
dock_ip=$(ifconfig docker0 | grep  -m 1 inet | awk '{print $2}')
last=$(echo ${dock_ip} | tr "." " " | awk '{ print $4 }')
sum=`expr $last + 1`
ipoct1=$(echo ${dock_ip} | tr "." " " | awk '{ print $1 }')
ipoct2=$(echo ${dock_ip} | tr "." " " | awk '{ print $2 }')
ipoct3=$(echo ${dock_ip} | tr "." " " | awk '{ print $3 }')
ip=$ipoct1.$ipoct2.$ipoct3.$sum
echo
con_id=$( docker ps | awk '{print $1}' | sed -n '2 p')
doc=$(docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $con_id)
echo $doc 
echo
new_ip=$(echo $doc | awk '{print $3}')
echo $new_ip
curl http://$new_ip/
