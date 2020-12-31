#the commands to demonstrate how to access and perform operations on a main file
#run the MODULE of MAIN FILE and import mainfile as a library 
import code as x 
#importing the main file("code") as a library 
x.create("hii",12)
#create a key with key_name,value and with no time-to-live property

x.create("hello",50,1000) 
#create a key with key_name,value  and with time-to-live property value given(number of seconds)

x.read("hii")
#it returns output in  Jasonobject format 'key_name:value'

x.read("hello")
#it returns output in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

x.create("h",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#use delete operation and recreate it

 x.delete("hii")
#it deletes the respective key and its value from the database

# using multiple threads
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#and so on  tn

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
