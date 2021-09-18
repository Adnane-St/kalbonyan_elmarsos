#this is set structure

primaryColor = set(['red','blue','yellow'])

color = 'green'
if(color.lower() in primaryColor):
    print(color.capitalize()," is a primary color.")
else:
    print(color.capitalize()," in not a primary color.")