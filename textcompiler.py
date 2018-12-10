import sys

allFiles = sys.argv
filePosition = 1
fileData = []

while filePosition < len(allFiles):
  with open(allFiles[filePosition], 'r') as Data:
      fileData.append(Data.read());
  
  filePosition += 1


newFileName = input("Enter file name to save: ")



with open(newFileName, 'w') as newFile:
  newFile.write("".join(fileData))

  #just type into command line when in folder...
  ## python3 textcompiler.py sample1.txt sample2.txt sample3.txt