# Introduction to Python Types

##What's in a type?
####Mechanical representation
Types communicate behaviors and constraints to the Python language itself.

####Semantic representation
Types communicate behaviors and constraints to other developers.


##Typing System
Typing sysytem aims to give a user some way to model the behaviour and contraints in the language.

Python --> storng
C --> Weak

##Dynamic Vs Static

###Static
Languages that offer static typing embed their typgin information in variables
during build time.

Variable do not change their type at runtime (hence, "static")

Proponents of static typing tout the ability to write safe code out of the gate
and beenfit from a strong safety net.

###Dynamic
Dynamic typing ont he other hand, embeds type information with the value of the
variable itself.

Variables can change types at at runtime quite eaily, becase there is no type information
tied to that variable.


Python is a dynamicaaly typed language.

Unfortunately, the ability to change types at tuntime is a hindrance to robust code
in many cases. You cannot make strong assumption about a variable throught its lifetime.

##Duck Typing
The ability to use objects and entities in a programming language as long as they
adhere to some infterface.

Duck typing is a double edged sword.

Building up a library of solid abstractions able to handle a multitude of types lessens
the need for complex special cases. However, if duck typing is overused, you start to
break down assumptions that a developer can rely upon.