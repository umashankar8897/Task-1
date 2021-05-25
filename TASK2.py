filename = input("Enter the file name")
f = filename.split(".")
if f[-1] == "py":
    print("The file extension is python")
elif f[-1] == ".java":
    print("The file extension is java")
else:
    print("The file extension is " + f[-1])
    