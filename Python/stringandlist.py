str = "It's thanksgiving day. It's my birthday,too!"
print str.find("day")
print str.replace("day", "month", 1)

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0::7]

z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
z.insert(0,z[0:4])
del z[1:6]
print z
