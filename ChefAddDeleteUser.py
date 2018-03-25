#!/usr/local/bin/python2.7
import os
import crypt
import time
import sys
import subprocess


def addnewuser():

	fname=sys.argv[2]
	lname=sys.argv[3]
	uname=sys.argv[4]
	upass=sys.argv[5]
	users_list = subprocess.check_output('chef-server-ctl user-list', shell=True)
	if uname in users_list:
		print "User already exist in Chef Server"
	else:     
	        os.system("chef-server-ctl user-create --filename /etc/chef-server/"+uname+".pem "+uname+" "+fname+" "+lname+" "+uname+"@example.com "+upass)
	        time.sleep(10)
    	        print "Chef user added"
  	        os.system("chef-server-ctl org-user-add osgraphic "+uname)
                time.sleep(10)
                print "user added in orgnisation"
    
def deleteuser():

        uname=sys.argv[2]
	con=sys.argv[3]
	users_list = subprocess.check_output('chef-server-ctl user-list', shell=True)
	if uname in users_list:
		os.system("chef-server-ctl user-delete "+uname+" --"+con)
		print "User Deleted in Chef Server"
	else:
		print "User not present in Chef Server"


Choice=sys.argv[1]
if Choice == 'Add':
	addnewuser()
elif Choice == 'Delete':
	deleteuser()
else: 
	print "Please select correct input"
