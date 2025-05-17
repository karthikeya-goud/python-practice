# Keywords are predefined words used for particular purpose
# in simple keywords are reserved words

import keyword
for i in keyword.kwlist:print(i)

for i in keyword.softkwlist:print(i) #['_', 'case', 'match', 'type']

# We Have about 35 Keyords and 4 soft keywords(no error we use this as variable)

#boolean        : True False None
#Conditions     : if elif else for while case match
#operators      : and or not is in del
#jump statements: continue break return pass
#fuctions       : def global nonlocal lambda
#imports        : import from as
#exceptions     : try except finally raise
#opening resource: with
#generator      :yeild
#assertion      : assert
#classes        : class
#asynchoronus   : async await

