import datetime #Imports date and time from module 

now = datetime.datetime.now() #'now' is the name give to the function 'datetime.datetime.now()' which obtains the current date and time to the fraction of the second

formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S") #'strftime' funtion is used to specify the format we want to show the date and time in 
#here we choosed the foramt ---> YYYY-MM-DD HH:MM:SS 

print("Current Date and Time:" ,formatted_datetime) # We add 'Cuurent Date and Time' in the beginning to show what is being printed then the formatted date and time  