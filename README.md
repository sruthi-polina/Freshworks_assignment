# Freshworks_assignment
* New key_name and value pairs can be created.
* Time-to-live property can be given and works even if not present.
* The key is always a string -capped at 32 chars.The value is always a JSON object -capped at 16KB.
* If Create is invoked for an existing key,an appropriate error will be returned.
* A Read operation on a key can be performed by providing  the key,and receiving the value in response,as a JSON object.
* A Delete operation can be performed by providing the key.
* Every key supports setting a Time-To-Live property.If provided,it will be evaluated as an integer defining the number of seconds the key must be retained in the data store.Once   the Time-To-Live expired,the key will no longer be available for Read or Delete operations.
* Client process is allowed to access the data store using multiple threads.
