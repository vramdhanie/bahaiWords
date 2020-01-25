

with open("source.txt") as filehandle:
    lines = filehandle.readlines()

with open("source.txt", 'w') as filehandle:
    lines = filter(lambda x: x.strip(), lines)
    filehandle.writelines(lines)
