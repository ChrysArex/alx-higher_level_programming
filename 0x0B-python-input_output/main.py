#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_fil1234e.txt", "Trying to fix\n")
print(nb_characters)
