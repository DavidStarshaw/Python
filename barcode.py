barcode = raw_input("Type the barcode without the last digit: ")

total = 0

for count, digit in enumerate(barcode):
  digit = int(digit)
  if (count % 2 == 0):
    total += digit
  else:
    total += digit * 3

difference = (-1 * total) % 10

print "The last digit is: ", difference

"""if (remainder == 0):
  difference = 0
else:
  difference = 10 - remainder

print "The last digit is: " + str(difference)
"""