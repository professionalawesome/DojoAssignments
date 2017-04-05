list = ['magical unicorns',19,'hello',98.98,'world']

string = " "
num = 0
types = []

#for item in list:

    #if isinstance(item, int) or isinstance(item, float):
        #print "The array is integer type"


    #elif isinstance(item, str):
        #print "The array is string type"



for item in list:
    if isinstance(item, int) or isinstance(item, float):
        num += item
        types.append(type(item))
    elif isinstance(item, str):
        string += item + " "
        types.append(type(item))



print "String:", string
print "Sum:", num
print "The array is a mixed type"
print types
