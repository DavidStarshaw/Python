"""This program will play Mad Libs"""

#Welcome message
print "Running Mad Libs..."

#Gets user inputs
name = raw_input("Enter a name: ")
verb = raw_input("Enter a verb: ")
object = raw_input("Enter an object: ")


if object.endswith("s"):
  #Don't put an extra 's' on the end
  pass
else:
  #Do put an extra 's' on the end
  object = object + "s"

#Prints the Mad Lib
print "%s was %s when they were distracted by a large display of %s" % (name, verb, object)