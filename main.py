from utils.passwordgen import PasswordGen
print("Welcome To Cracker 601\nDeveloped By Openchains\n")
initials = input("Enter initiatials: ")
postFixs = input("Input PostFixs")
year = input("input year: ")
characters = input("input characters")
fileName = input("Enter File Name: ")
passGen = PasswordGen();
passGen.setCharacterSet(characters);
passGen.setInitials(initials)
passGen.setPostFixs(postFixs)
passGen.setYear(year)
passGen.generateList(fileName.strip())