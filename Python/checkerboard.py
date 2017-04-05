for i in range(0, 8):
    line = ""
    for j in range(0, 4):
        if i % 2 == 0:
            line += "* "
        elif i % 2 == 1:
            line += " *"

    print line
