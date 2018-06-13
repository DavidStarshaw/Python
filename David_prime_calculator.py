"""This program will calculate the prime numbers less than 100."""

print "Running program..."
from time import sleep
#number_list = range(2, 101)

prime_list=[]

for number in range(2, 101):
  #sleep(1)
  #print "Number:", number
  multiple = False
  
  for prime in prime_list:
    #sleep(1)
    #print "Checking for a multiple of:", prime
    if number % prime == 0:
      multiple = True
      #sleep(1)
      #print "%d is a multiple of %d. Removed." % (number, prime)
      break
  if not multiple:
    prime_list.append(number)
    #sleep(1)
    #print "Added %d to list of prime numbers" % (number)

print prime_list