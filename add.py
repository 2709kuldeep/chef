import os
import crypt
import time

def addnewuser():

    fname=raw_input("First Name: ")
    lname=raw_input("Last Name: ")
    uname=raw_input("Select Username: ")
    upass=raw_input("Select Password ")

    #The encryption module seems to solve the obvious security leak,
    #but I still don't know whether even the exposed encrypted password is safe or not.
#    ucrypt=crypt.crypt(upass,"123")
#   os.system("useradd -m -p "+upass+" "+uname)
    os.system("chef-server-ctl user-create --filename /etc/chef-server/"+uname+".pem "+uname+" "+fname+" "+lname+" "+uname+"@demo.hcinternal.net "+upass)
    time.sleep(10)
    print "Chef user added"
    os.system("chef-server-ctl org-user-add osgraphic "+uname)
    time.sleep(10)
    print "user added in orgnisation"
#addnewuser()

def deleteuser():
        uname=raw_input("Select Username: ")
	os.system("chef-server-ctl user-delete " +uname)

#deleteuser ()

options = { 1 : addnewuser,
	    2 : deleteuser,
        	}

options[2]()
