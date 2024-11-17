with open("log.txt","r") as file:
    lines=file.readlines()
with open("errorlog.txt","w") as errorfile:
    for line in lines:
        if "WARNING" in line:
            errorfile.write(line)
        elif "ERROR" in line:
            errorfile.write(line)