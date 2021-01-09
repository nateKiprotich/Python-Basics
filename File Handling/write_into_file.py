# if the file is not available in the directory, a new file will be created
f = open('new_text.txt', 'w')

f.write('Testing write to file. \n a new line as well')

f.close()

# Opens the files and add new lines into it
# If file doesn't exist new file is created
j = open('new_text.txt', 'a')

j.write('\nAttempt file creation and append into it')

j.close()

