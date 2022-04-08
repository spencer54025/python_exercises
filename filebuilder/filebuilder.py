file_builder = open("logger.txt", "w+")

for i in range(100):
    file_builder.write(f"im online {i + 1}\n")

# file_builder.write("im in a file")

file_builder.close()