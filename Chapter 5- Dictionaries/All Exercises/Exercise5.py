##exercise 5:
list = []
az = {"animal":"cat",
       "owner":"Ahmed"}
list.append(az)
az = {"animal":"dog",
       "owner":"Abdullah"}
list.append(az)
az = {"animal":"parrot",
       "owner":"Mohammed"}
list.append(az)
az = {"animal":"goldfish",
       "owner":"Omar"}
list.append(az)
az = {"animal":"hamster",
       "owner":"Fazal"}
list.append(az)
print(list)
for az in list:
  print("\nbelow are the animal and their owner:")
  for key, value in az.items():
    print(f"\t{key}: {value}")