import datetime # This line imports the datetime module, which is a built-in module in Python used for working with dates and times.

now = datetime.datetime.now() #In this line, the datetime.datetime.now() function is called to retrieve the current date and time.
print ("Current date and time : ") #This line is a print statement that displays the text "Current date and time : " on the console.
#It's just a label to indicate what will be printed next.
print (now.strftime("%Y-%m-%d %H:%M:%S")) #This line prints the formatted date and time to the console. 
