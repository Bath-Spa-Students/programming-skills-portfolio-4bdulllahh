#def function to define function 
def make_shirt(size,message):
  print("Your shirt size is ",size," and it says ",message,)  
#ask user thier shirt size and what they want on thier shirt
shirtsize = str(input("Enter your shirt size (S,M,L,XL,XXL): "))##S,M,L
txt = str(input("Enter the message you want to print on the shirt: "))
make_shirt(shirtsize,txt)