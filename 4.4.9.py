
#You've been sent a list of names. Unfortunately, the names
#come in two different formats:
#
#First Middle Last
#Last, First Middle
#
#You want the entire list to be the same. For this problem,
#we'll say you want the entire list to be Last, First Middle.
#
#Write a function called name_refixer. name_refixer should have two
#parameters: an output filename (the first parameter) and the
#input filename (the second parameter). You may assume that every
#line will match one of the two formats above: either First Middle
#Last or Last, First Middle. 
#
#name_refixer should write to the output file the names all
#structured as Last, First Middle. If the name was already structured
#as Last, First Middle, it should remain unchanged. If it was
#structured as First Middle Last, then Last should be moved
#to the front and a comma should be added after it.
#
#The names should appear in the same order as the original file.
#
#For example, if the input file contained the following lines:
#David Andrew Joyner
#Hart, Melissa Joan
#Cyrus, Billy Ray
#
#...then the output file should contain these lines:
#Joyner, David Andrew
#Hart, Melissa Joan
#Cyrus, Billy Ray


#Add your code here!

def name_refixer(out1, in1):
    final = []
    b = []
    infile = open(in1, "r")
    outfile = open(out1, "w")
    for name in infile:
        if "," in name:
            final.append(name)
            outfile.write(name)
        else:
            a = name.split()
            print(a)
            print(a[2])
#            print(len(a[2]) - 1)
            y = len(a[2])
            print(y)
            a_new = (a[2][0:y])
            print(a_new)
 #           a_new = (a[0]: y)
            b = (a_new + ", " + a[0]+ " " + a[1])
            print(b)
            final.append(b)
            outfile.write(b + "\n")
#    for i in final:
    new_list = [x.replace("'", '"') for x in final]
    return new_list
#    outfile.write(new_list)
    infile.close()
    outfile.close()


#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, output_file.txt should have the text:
#Joyner, David Andrew
#Hart, Melissa Joan
#Cyrus, Billy Ray
name_refixer("output_file.txt", "input_file.txt")
print("Done running! Check output_file.txt for the result.")

#If you accidentally erase input_file.txt, here's its original
#text to copy back in (remove the pound signs):
#David Andrew Joyner
#Hart, Melissa Joan
#Cyrus, Billy Ray


