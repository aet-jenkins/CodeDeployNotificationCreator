#!/usr/bin/python3
#Read files

import os 
import subprocess
import fileinput
import json
import re
import sys


file1 = open("apps.txt", "r")
line = file1.readlines()
count = 0
for lines in line:
    count += 1
    app_name=(lines.strip())
    

    fin = open("template.json", "rt")
    fout = open("dyno.json", "wt")
    for line2 in fin:
        
        fout.write(line2.replace('REPLACECODENAME', app_name))
	        
    fin.close()
    fout.close()
    
    #os.system("aws deploy get-deployment-group --application-name " + app_name + " --deployment-group-name INC-DEV >> temp.json")
    
    os.system("aws codestar-notifications create-notification-rule --cli-input-json  file://dyno.json --profile kavishka")
    
    

