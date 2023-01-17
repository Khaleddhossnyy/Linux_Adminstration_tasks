import os
#------------------------------------------------------------------------------
os.system("echo ----------------------------------------------")
os.system("echo Hello Terminal, this is a small guide to Linux bash commands")
#------------------------------------------------------------------------------

#-----------------------------------SUDO---------------------------------------
os.system("echo ----------------------------------------------")
os.system("echo 1-sudo : stands for super user do , which allows you to do administrative tasks ,for example : sudo apt-get update as:")
command = os.popen("sudo apt-get update")
command = command.read()
print(command)
os.system("echo ----------------------------------------------")

#------------------------------------PWD----------------------------------------
os.system("echo 2-pwd : executing pwd will return the full current path as : ")
command = os.popen("pwd")
command = command.read()
print(command)
os.system("echo ----------------------------------------------")
#--------------------------------------------------------------------------------

#---------------------------------cd---------------------------------------------
os.system("echo 3-cd : executing cd allows you to navigate through the file system on your OS whether by giving the full path or directory name depending on your current directory ,for example we are in /home/Khaled/Python_Tasks after execution of cd /home/khaled/C_Tasks ,the current directory will be : ")
os.chdir("/home/khaled/C_Tasks/")
command = os.popen("pwd")
command = command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------ls---------------------------------------------
os.system("echo 4-ls : executing ls will show/list the full content of the current working directory which we changed in the last step of execution of cd as : ")
command = os.popen("ls -a")
command = command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------cat---------------------------------------------
os.system("echo 5-cat : executing cat will write the content of a file in the terminal, it is one of the most used Linux bash commands, you write cat then the file name with its extension and you will get the content of the file displayed as cat test.c :")
command = os.popen("cat test.c")
command = command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------copy---------------------------------------------
os.system("echo 6-cp : executing cp will copy the content of a file from one directory to another, to use cp , type cp followed by file name followed by destination directory for example copying the file test.c from here to Khaled directory as cp test.c /home/khaled/Khaled : ")
command = os.popen("cp test.c /home/khaled/Khaled")
os.system("echo --Changing the directory to the destination directory")
os.chdir("/home/khaled/Khaled")
command_2 = os.popen("pwd")
command_2 = command_2.read()
print(command_2)
os.system("echo --Listing the files and folders in the destination directory to check for file test.c :")
command_3 = os.popen("ls")
command_3= command_3.read()
print(command_3)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------move---------------------------------------------
os.system("echo 7-mv : executing mv will move a file from one directory to another, to use mv , type mv followed by file name followed by destination directory for example moving the file test.c Khaled directory as mv test.c /home/khaled/C_Tasks : ")
command = os.popen("mv test.c /home/khaled/C_Tasks")
os.system("echo --Printing the current directory")
command_2 = os.popen("pwd")
command_2 = command_2.read()
print(command_2)
os.system("echo --Listing the files and folders in the destination directory to check for moving file test.c from this directory :")
command_3 = os.popen("ls")
command_3= command_3.read()
print(command_3)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------make directory---------------------------------------------
os.system("echo 8-mkdir : executing mkdir will make a directory/folder in the given destination as mkdir Tests: ")
os.chdir("/home/khaled/")
command = os.popen("mkdir Tests")
os.system("echo --Changing the directory to the destination directory")
command_2 = os.popen("pwd")
command_2 = command_2.read()
print(command_2)
os.system("echo --Listing the files and folders in the destination directory to check for the new directory we made which is Tests :")
command_3 = os.popen("ls")
command_3= command_3.read()
print(command_3)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------remove directory---------------------------------------------
os.system("echo 9-rmdir : executing rmdir will permenantly remove a directory/folder in the given destination, you write rmdir followed by -p which indicates that the user have sudo privileges in the parent directory followed by main folder followed by a slash followed by the name of the directory you want to remove as  rmdir -p /home/khaled/Tests : ")
os.system("echo --Changing the directory to the destination directory")
os.chdir("/home/khaled/")
command = os.popen("sudo rmdir -p /home/khaled/Tests/")
command_2 = os.popen("pwd")
command_2 = command_2.read()
print(command_2)
os.system("echo --Listing the files and folders in the destination directory to check for the deletion of the directory we created in the last step which is Tests:")
command_3 = os.popen("ls")
command_3= command_3.read()
print(command_3)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------remove file---------------------------------------------
os.system("echo 10-rm : executing rm will permenantly remove a file in the given destination, you write rm then the file name as rm a.out : ")
os.chdir("/home/khaled/C_Tasks")
os.popen("touch a.out")
os.system("echo --Changing the directory to the destination directory")
command_2 = os.popen("pwd")
command_2 = command_2.read()
print(command_2)
command = os.popen("rm a.out")
os.system("echo --Listing the files and folders in the destination directory to check for the deletion of the file a.out :")
command_3 = os.popen("ls")
command_3= command_3.read()
print(command_3)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------touch file---------------------------------------------
os.system("echo 11-rm : executing touch will create a file in the current destination as touch Test.txt : ")
os.chdir("/home/khaled/Khaled")
os.system("echo --Changing the directory to the destination directory")
command_2 = os.popen("pwd")
command_2 = command_2.read()
print(command_2)
command = os.popen("touch Test.txt")
os.system("echo --Listing the files and folders in the destination directory to check for the new file we created :")
command_3 = os.popen("ls")
command_3= command_3.read()
print(command_3)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------Locate file---------------------------------------------
os.system("echo 12-locate : executing locate will locate a file in the database of your system, -i option will execlude the case sensetivity do if you dot remember the exact name of the file it will not be a problem , also if your file name contain two words or more you will have to use the asterisk symbol between them so we can use it like this locate -i test.c: ")
command= os.popen("locate -i test.c")
command= command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------find file---------------------------------------------
os.system("echo 13-find : executing find will find a file within a specific directory, type find followed by directory followed by the keyword -name followed by the file name to search for as : find /home/khaled/C_Tasks -name test.c")
command= os.popen("find /home/khaled/C_Tasks -name test.c")
command= command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------GREP---------------------------------------------
os.system("echo 14-grep : executing grep lets you find a word by searching through all text in a specific file, so it is mainly a filtering method,once grep finds a match it returns all the lines that matches this pattern,as grep int test.c")
os.chdir("/home/khaled/C_Tasks")
command= os.popen("grep int test.c")
command= command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------df---------------------------------------------
os.system("echo 15-df : executing df reports the disk space usage of the current directory in a human readable form as df /home/khaled/C_Tasks : ")
command= os.popen("df /home/khaled/C_Tasks")
command= command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#--------------------------------du--------------------------------------------
os.system("echo 16-du : executing du tells you how much space a file or a directory takes , you must specify the full path for du to work as  du /home/khaled/Python_Tasks : ")
command= os.popen("du -h /home/khaled/Python_Tasks")
command= command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#-------------------------------head--------------------------------------------
os.system("echo 17-head : executing head will print the first 10 line of a text, you can add the option -n to change the number of lines to be printed as: head -n 5 note.txt")
os.chdir("/home/khaled/Documents")
command= os.popen("head -n 5 note.txt")
command= command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#-------------------------------tail--------------------------------------------
os.system("echo 18-tail : executing tail will print the last 10 line of a text, as: tail note.txt")
os.chdir("/home/khaled/Documents")
command= os.popen("tail note.txt")
command= command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#-------------------------------diff--------------------------------------------
os.system("echo 19-Diff : executing diff will compare the content of two files and after analyzing them it will print the parts wich has differeneces as diff note.txt note_2.txt : ")
os.chdir("/home/khaled/Documents")
command= os.popen("diff note.txt note_2.txt")
command= command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------

#-------------------------------Tar--------------------------------------------
os.system("echo 20-Tar : executing Tar will compress a file or a directory, it works same as ZIP, type Tar followed by archive file followed by path of the file or directory to compress as tar Documents.tar /home/khaled/Documents")
os.popen("tar -zcvf Documents.tar.gz /home/khaled/Documents")
os.chdir("/home/khaled/Documents")
command= os.popen("ls")
command= command.read()
print(command)
os.system("echo ----------------------------------------------")
#-------------------------------------------------------------------------------


























