##exercise 3:
#give glosaary varaible value 
glossary = {"print":"prints string or value",
            "list":"stores multiple values",
            "loop":"repeated execution",
            "input":"takes input",
            "dictionary":"stores both keys and value"}
for x in glossary:
  print(x + ":" + glossary[x])
print("\n\nNew Keys:\n")          
#taking value from variable 
glossary.update({"function": "perfom specific tasks"})
glossary.update({"operator": "a symbol used for operations"})
glossary.update({"operand": "the values in operation"})
glossary.update({"control flow": "decision to change flow of program"})
glossary.update({"boolean": "True/false,1/0,Yes/No"})
for x in glossary:
  print(x + ":" + glossary[x]) 

  