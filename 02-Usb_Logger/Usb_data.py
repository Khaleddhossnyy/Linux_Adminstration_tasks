import os
#------------------------------------------------------------------------------
os.system("echo ----------------------------------------------")
os.system("echo Hello Terminal, we will get the usb drivers data and stor them in a file ")
#------------------------------------------------------------------------------
command = os.popen("lsusb > USB_Data.txt")
command = command.read()

os.system("echo ----------------------------------------------")
os.system("echo ----- Showing data from the USB file we created -----")
command_2 = os.popen("cat USB_Data.txt")
command_2 = command_2.read()
print(command_2)
