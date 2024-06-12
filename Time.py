import time
print(time.ctime(1000000))
print(time.time())

print(time.ctime(time.time()))

time_object =time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)#time.strf format online web chack
print(local_time)

time_string = "20 April, 2020"
time_objects =time.strptime(time_string,"%d %B, %Y")
print(time_objects)
local_times = time.strftime("%B %d %Y %H:%M:%S",time_objects)
print(local_times)

time_tuple =(2020,4,20,4,20,0,0,0,0)
time_strings = time.asctime(time_tuple)
print(time_strings)

time_tuple =(2020,4,20,4,20,0,0,0,0)
time_strings = time.mktime(time_tuple)
print(time_strings)