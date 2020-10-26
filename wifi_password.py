# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:12:21 2020

@author: Ritul Singh
"""
"""
I added to the code to save the output in a text file on 27/10/2020 

@abolfazl_samadi
"""
# import subprocess library as su
import subprocess as su

# Getting all saved Wifi name in our computer
a = su.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# We want to know about all the profiles that are stored on our computer and we are stored in the wifi_name list
wifi_name = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
file_name = "password_router.txt"
file = open(file_name,"w")
# toatl number of wifi network in our computer using len
count = len(wifi_name)
file.write("\n The total number of wifi networks in your computer = ")
file.write(str(count))
file.write("\n================================================================\n")
file.write(" Wifi Name                     |  Password\n")

for i in wifi_name:
    # the following command to see the password of any WiFi network:
    results = su.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')

    # search the word key content in results and split the password and again stored in results
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    try:
        # those contain password than the print
        file.write(" {:<50}|  {:<}\n".format(i, results[0]))

    except IndexError:
        # those not contain password
        file.write(" {:<50}|  This wifi contain no passward  {:<}\n".format(i, ""))
