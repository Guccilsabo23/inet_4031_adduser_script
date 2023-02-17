#!/usr/bin/python2.7
import os
import re
import sys

def main():
    for line in sys.stdin:
        match = re.match(r'^\s*#', line)

        fields = line.strip().split(':') #strip any whitespace and split into
                                        #into an array

        if match or len(fields) !=5: #this is checking to see  if # is at the start of the line and  also checks if the line has 5 fields
            continue #the continue here is for the FOR loop. So if the line 
                    #starts with a # or does not have five fields, we skip it

        username = fields[0]
        password = fields[1]

        gecos   = "%s %s,,," % (fields[3],fields[2])

        groups  = fields[4].split(',') # it splits the 5th field in the array of fields and also into seperate groups with a comma that seperates

        print "==> Create account for %s..." % (username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        #print cmd
        os.system(cmd) #executes and returns a shell command
        print "==> Setting the password for %s..." % (username)
        cmd = "/bin/echo -ne '%s\n%s' | /user/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd
        os.system(cmd)
        for group in groups: #iterates over a list of groups that are stored, so that it adds users to the groups
            if group != '-':
                print "==> Assigning %s to the %s group..." % (username,group)
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__== '__main__':
    main()
