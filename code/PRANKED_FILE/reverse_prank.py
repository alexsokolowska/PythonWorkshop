
#Open a file for reading -- your_file = open(filename, 'r') .fname = raw_input('Enter file name: ')
fh = open('wikipedia_hydraulic_fracturing_pranked.txt', 'r')
#Prompt a user to write a new name of a file(e.g. correct.txt). Corrected text will be written to it. Use function raw_input('your prompt goes here') .
new_file = raw_input('Corrected file name:')
fnew = open(new_file, 'w')

#Write a loop over the lines of code for line in your_file: that will check in each line if there's an f-word string. How? What about if "your_string" in line: ?

for line in fh:
    if "fuck" in line:
        print "Found it!"
#Replace each of them with "frack". See docs how to use line.replace() .
        
        print "I will convert the line: \n", line
        print "into \n", line.replace("fuck","frack") 
#Write line.replace(necessary arguments) to yout correct.txt file.           
    fnew.write(line.replace("fuck","frack"))
#Don't forget to close the file!

fh.close()
fnew.close()


#Write a test function that will go over the file again and print out a statement "Oh no, you missed an f-word!", if it finds an f-word string in this file. Tip: you can set a counter count=0 before the loop and add 1 to it count=count+1 if "your_string" in line . Then just check the value of count at the very end after the loop to print either "Oh no, you missed an f-word!", or "\n\n Good job!!!"

def test(new_file):
    fh = open(new_file, 'r')
    count = 0
    for line in fh:
        if "fuck" in line:
            print "Oh no, you missed an f-word!"
            count = count + 1
    if count == 0:
        print "\n\n Good job!!!"
    fh.close()

test(new_file)



