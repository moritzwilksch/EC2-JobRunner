#!/bin/bash
cd /home/ec2-user/environment/EC2-JobRunner
source env/bin/activate
git pull
python3 writetos3.py
