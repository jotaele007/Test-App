# Test-App

Hi there:
To run the script you will need the following requirements:

Python: version 3.10.11
Frida :  
client: 16.1.8
server: frida-server-16.0.9-android-arm

Device used: Samsung Galaxy S5 mini with Android 7.1.2

Instructions:
First run frida server on the device: 
/data/local/tmp/./frida-server-16.0.9-android-arm
Then run frida client to check for processes and confirm the everything is Ok with frida:

frida-ps -U

Tu build and execute the hook you only need to execute the python script

python f1.py
