def insertInfo(info):
    with open("Users.txt", "a") as wfile:
        data = info.strip("\n")
        data=f"{data}\n"
        wfile.write(data)
        wfile.close()