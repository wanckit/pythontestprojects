user = raw_input("Enter your username")
file_object = open("username.txt", "a")
file_object.write(user+"\n")
file_object.close()

file_object2 = open("username.txt", "r")
username = file_object2.read()
file_object2.close()
print "The previous users of this program were:"
print username
