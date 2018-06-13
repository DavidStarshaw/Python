"""This program calculates narcissistic numbers with 5 or less digits."""

print "Running program..."

narcissistic_list = []

for number in range(1, 100000):
  number = str(number) #Number is now a string
  
  #The starting total for the below method
  total = 0 
    
  #Raises each digit to the power of the number of digits
  for digit in number):
    total += int(number[digit]) ** len(number)
  
  #Check if the above result is equal to the number itself
  if total == int(number):
    narcissistic_list.append(int(number))

print narcissistic_list

print "Exiting program..."