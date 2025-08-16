from utils.passwordgen import PasswordGen
print("Welcome To Cracker 601\nDeveloped By Openchains\n")
initials = input("Enter initiatials separatebySpace: ")
year = input("input year: ")
characters = input("input characters: ")
fileName = input("Enter File Name: ")
passGen = PasswordGen();
passGen.setCharacterSet(characters);
passGen.setInitials(initials)
passGen.setYear(year)
passGen.generateList(fileName.strip())
print(f"File {fileName.strip()} successfully saved")