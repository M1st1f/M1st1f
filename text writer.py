date = input("date: ")
entry = "new diary entry \n"
print("new diary entry \n")
information = input("\n")
f = open("diary.txt", "a")  # a means append, this stops new data overwriting old
f.write(date)
f.write(entry)
f.write(information)
f.close()
