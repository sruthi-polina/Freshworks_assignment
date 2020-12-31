import threading 
#this is for python 3.0 and above. use import thread for python2.0 versions
from threading import*
import time

dictionary={} #dictionary to  store data

#create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional 
def create(key,value,timeout=0):
    if key in dictionary:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(dictionary)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    dictionary[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

#read operation
#use syntax "read(key_name)"      
def read(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=dictionary[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                s=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return s
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            s=str(key)+":"+str(b[0])
            return s

# delete operation
#syntax "delete(key_name)"
def delete(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=dictionary[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del dictionary[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            del dictionary[key]
            print("key is successfully deleted")
