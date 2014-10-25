# This is a single file python cheat sheet for quick access reference.
#
# I had to strike a balance be completeness vs conciseness, so the scope is
# broadly "how to do x in python, if it's different to most other languages"
# and only covers basic, useful or interesting examples.
#
# I've called each section "chapter", so that a text find on "cha.." will show you
# all the sections.
#
# Andrew Buchan 2014
#
# Feel free to copy, add and redistribute.


#
# chapter SYNTAX BASICS
#

# Python uses indentation, in theory it doesn't matter what, so long as it's
# the same throughout the file. Use 4 spaces, not tabs, because it's convention
# and if we all stick to it, then you can copy other people's code without weird
# indentation errors because one chunk uses tabs and the other spaces!)

if True:
    do_somthing()
else:
    do_something_else()

# To carry over a line, use the back slash and indent it more than normal so you
# can tell it appart from normal indented code:
if some_really_long_conditional_statement and \
        some_really_long_conditional_statement:
    do_something()

# This doesn't apply to brackets (round or square), or items separated by commas:
my_list = [
        item1,
        item2,
        ]

#Add returning tuples

#
# chapter FUNCTIONS AND ARGUMENTS
#

def use_a_long_descriptive_name_so_it_is_clear_what_it_does(a, b):
    """Put a doc string at same indentation as code. Explain
    what the parameters are, and what it should return.
    """
    x = any_substantial_functionality_should_be_outsourced_to_another_function(a)
    y = because_it_keeps_this_function_small_easy_to_understand(b, x)
    # Comments are best placed above the line they refer to
    if True:
        # at same level of indentation
        y = something_different()
    # This specifies the value returned, in this case it will be a tuple (x, y)
    # Which is useful for saying if something workes (True, result) vs (False, err_msg)
    return x, y



#
# chapter RUNNING SCRIPTS and COMMAND ARGS
#

# When you run a python file (by opening it) it will execute  all code at indentation 0.
# This will also happen when your file is imported by another file.
# To avoid this happening, you can test if this file is the main file being called,
# and only run stuff if that f

if __name__ == "__main__":
    call_to_some_function()

# To access the args you pass to a python script from the command line:

sys.argv

# To access the executing python file's directory:
path = os.path.dirname(__file__)

#
# chapter IMPORTING
#

# Modules are files, and these need to be found in one of the locations held in
# sys.path. Standard modules will be in the installation folder

from my_module import *
from my_module import SomeSpecificClassOrDefinition, AndAnother
import my_module as mm

# To reload a module:
reload(my_module)

#
# chapter VARIABLES
#

# Python is dynamically typed, ie a variable can change type, which isn't allowed in
# statically typed languages:

a = 'hello'
a = 1

# Functions can be assigned to variables too:

def my_function(x, y):
    return x + y

a = my_function(3, 4)
b = my_function

# Here a stored the return value 7, but b stored a reference to my_function (without calling it)
# It can be called a later time like so:

c = b(5, 6)

#And c would be 11. This is useful for managing variable behaviour.

#
# chapter STRINGS
#

"str".split() # splits a string into a list, breaking on white space.
"str".strip() # removes whitespace on either end

# interpolation

'say %s' % 'hello'
'say %s and %s' % ('hello', 'goodbye')


# Useful string constants:

string.ascii_lowercase # = 'abcdefghijklmnopqrstuvwxyz'
or string.lowercase # locale dependant
string.ascii_uppercase
string.ascii_letters #combination of above
string.digits #The string '0123456789'

# Useful for checking other strings.

#
# chapter DATE AND TIME
#

import datetime, calendar
def AddWeekTo(day, amount):
    oneweek = datetime.timedelta(days=7)
    return day + (oneweek * amount)

print AddWeekTo(datetime.date.today, 1)

#
# chapter LISTS
#

def uniquify(seq, idfun=None):
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

#
# chapter FILES, DIRECTORIES & PATHS

os.path.isfile()
tempfile.gettempdir()
if not os.path.exists(directory):
    os.makedirs(directory)

#Delete directory:
import shutil
shutil.rmtree('/folder_name')

#
# chapter OOP CLASSES
#

#Inheriting from 'object' is how create a "new style" class, and should generally always do this.
def MyClass(object):

    watch_out_this_is_a_class_variable = 'the same for EVERY instance'

    def __init__(self, age):
        self.age = age #This is how you create an instance variable

     #instance methods need 'self' as the first parameter
    def my_function(self, x, y):
        print 'something'
        # this is how you call an instance method
        self.my_other_function(2, 3)


# Data attributes, or instance members by convention are initialised to a
# reasonable value in __init__()
# Like local variables however, they spring into existence when assigned, so
# using the above class, you can this:

c = MyClass(45)
c.some_new_variable = 66
print c.age
>>> 45
print c.some_new_variable
>>> 66

# Python has no function overloading, so you can only have one function with a name
# in the same class.


#
# chapter OOP INHERITANCE
#

class Parent(object):

    def overriden(self):
        print "PARENT"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    #just define it with same name as parent
    def overriden(self):
        print "CHILD"

    #just call super, but beware of super() being funny.
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()

class ToString():
    def __str__(self):
        return 'me'

# classes must inherit from object to be treated as new style classes
#new style classes allow you to use super() and property()

class C(object):

    def __init__(self):
        self.__x = 0

    def getx(self):
        return self.__x

    def setx(self, x):
        if x < 0: x = 0
        self.__x = x

    x = property(getx, setx)

c = C()
c.x = 10

# https://docs.python.org/2/library/functions.html#property
# You can also shortcut a getter by doing:




