
# Python program to explain os.listdir() method  
    
# importing os module  
import os 
  
# Get the list of all files and directories 
# in the root directory 
path = "C:\Users\ADMIN\Desktop\Python_project\GGSpread"
dir_list = os.listdir(path) 
  
print("Files and directories in '", path, "' :")  
  
# print the list 
print(dir_list) 