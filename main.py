# def greet():
#   return 'Hello Collins'
# print(greet())  

#=======Functions with parameters====


# def greet(name):
#     return f'Hello {name}, Good morning'
# print(greet('Collino'))
# print(greet('Kingsley')) 

#=======Arbitrary parameters=========

# def fruits(*names):
#   '''
#   Accepts unkown number of fruits names and peints each of them 
#   *name list of fruits
#   '''
#   #names are tuples  - also remember that this is ummutable
#   # print(type(names))

#   for fruit in names:
#     print(fruit)
# fruits('Oranges', 'Banana', 'Apples', 'Grapes')  

#=======Keyword arguments=============
def greet(name, msg):
  
  # This function greets a person with a giben message
  # name: person to greet
  # msg: message to greet person with
  
  return f'Hello {name}, {msg}'
# # print(greet('Mike', 'Come for breakfast'))

print(greet(msg='Mike', name='Come for breakfast'))

#====Arbitrary Keyword parameters==========================
#use this if you sont know the number of parameters
def person(**student):
    # print(type(student))
    # print(student)
    for key in student:
      print(student[key])
person(fname='Kingsley', lname='Ijomah')    