print("Encouragement bot thingy")
print()
while True:
  description = input("Could you describe how you feel in one word?  ")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("there is a small chance that tomorrow will be a better day")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("hapiness is temporary")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("go and sleep")
      counter += 1
    if each_word == "useless":
      feelings_list.append("useless")
      encouragement_list.append("that's sad")
      counter += 1
    if each_word == "shitty":
      feelings_list.append("shitty")
      encouragement_list.append("we all feel like shit")
      counter += 1
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("if you are stressed, then too bad for you")
      counter += 1
    if each_word == "great":
      feelings_list.append("great")
      encouragement_list.append("you will still die, someday")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
