# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

values=input("Enter the filename with extension: ")

extension=values.split(".")

print("The extension of the file is:",extension[-1])