#!/bin/bash
sudo sysemctl start cron
sudo sysemctl status cron
crontab -e
0**** cut -d: -f1,6 etc/passwd