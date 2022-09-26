import random

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbol = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_', '=', '[', ']', '{', '}', ';', ',', '.', '/', '<', '>']

lower_count = 0
upper_count = 0
number_count = 0
symbol_count = 0

while (lower_count == 0 or upper_count == 0 or number_count == 0 or symbol_count == 0 ):

  all = lower + upper + number + symbol

  password_array = random.sample(all, 16)

  password = "".join(password_array)
  print(password, end=" ")


  for i in range(1, len(lower)):
    if lower[i] in password:
      lower_count += 1

  print('lower:', lower_count, end=" ")

  for i in range(1, len(upper)):
    if upper[i] in password:
      upper_count += 1

  print('upper:', upper_count, end=" ")

  for i in range(1, len(number)):  
    if number[i] in password:
      number_count += 1

  print('number:', number_count, end=" ")

  for i in range(1, len(symbol)):  
    if symbol[i] in password:
      symbol_count += 1

  print('symbol:', symbol_count)
