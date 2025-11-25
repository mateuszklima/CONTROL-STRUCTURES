###
# Check if a Polish name is female
#

name = input("Enter name: ")

if name[-1].lower() == 'a':
    print(f"{name} -- Polish female name")
else:
    print(f"{name} -- Not recognized as a typical Polish female name")
