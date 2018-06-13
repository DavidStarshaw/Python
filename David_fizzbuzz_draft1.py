from time import sleep

for x in range(1, 101):
  message = ""
  if x % 3 == 0:
    message += "Fizz"
  if x % 5 == 0:
    message += "Buzz"
  if message == "":
    message = x
  print message
  #sleep(0.5)