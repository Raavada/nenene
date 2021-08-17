#!/bin/bash

if cmp -s "/var/log/currentuser" "/var/log/user_changes"; then
    printf 'The file \n'
else
   date >>  "/var/log/user_changes"  cat "/var/log/currentuser" >> "/var/log/user_changes" 
fi


#!/bin/bash 

echo "inside"

str=$(cut -d: -f1,6 /etc/passwd | md5sum)

content=$(cat /var/log/currentuser)
if [ "$str" == "$content" ];then
   echo "They match"
else
   echo "No match"
   today=$(date +"%Y-%m-%d")
   cat "/var/log/currentuser" >> "/var/log/user_changes" 
   
fi



#!/bin/bash 

echo "inside"

str=$(cut -d: -f1,6 /etc/passwd | md5sum)

content=$(cat /var/log/currentuser)
if [ "$str" == "$content" ];then
   echo "They match"
else
   echo "No match"
   today=$(date +"%Y-%m-%d")
   cat "/var/log/currentuser" >> "/var/log/user_changes" 
   filetoedit="/var/log/user_changes"
   date >>$filetoedit
fi



