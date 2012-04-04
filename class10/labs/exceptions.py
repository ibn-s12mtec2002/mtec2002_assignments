"""
exceptions.py
=====
To handle errors, use a try/catch block:

-----
try:
	# do your stuff
except SomeError:
	# deal with some error
-----

optionally... you can continue catching more than one exception:

-----
.
.
except AnotherError:
	# deal with another error
-----

Substitute SomeError with the kind of error you want to handle - for example:

KeyError
ValueError
TypeError
IndexError
ZeroDivisionError
"""
#KeyError
d = {"shape":"circle"}
print d['shape']
try:
	print d['shape']
	print d['color']

#ValueError (conversion errors)
try:
	print int("this is not a number")
except ValueError:
	print "I don't think that's a number"
#TypeError 

#IndexError

#ZeroDivisionError

#catching multiple possible exceptions - try possible KeyError AND TypeError like dictionary value divided by another value
#ex... which player do you want to add a score to, and add that score
