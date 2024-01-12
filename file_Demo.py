#directory:   /home/imtiaz/code.py
text_file = open('file.txt','r')


line_list = text_file.readlines();

#for each line from the list, print the line
for line in line_list:
    print(line)

text_file.close()



