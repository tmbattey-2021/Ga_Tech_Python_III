




#Write a function called "reader" that reads in a ".cs1301" 
#file described in the previous problem. The function should 
#return a list of tuples representing the lines in the file like so:
#
#[(line_1_number, line_1_assignment_name, line_1_grade, line_1_total, line_1_weight), 
#(line_2_number, line_2_assignment_name, line_2_grade, line_2_total, line_2_weight)]
#
#All items should be of type int except for the name (string) 
#and the weight (float). You can assume the file will be in the 
#proper format -- in a real program, you would use your code
#from the previous problem to check for formatting before
#trying to call the function below.
#
#Hint: Although you could use readlines() to read in all
#the lines at once, they would all be strings, not a list.
#You still need to go line-by-line and convert each string
#to a list.


#Write your function here!
def reader(filein):
    f = open(filein, "r")
    total = 0
    listout = open("fileout.txt", "a")
    listcreate = ()
    thislist = []
    for line in f.readlines():  
        line_split = line.split()

        if len((line_split)) == 5:
            try:  
#        if len((line_split)) == 5:
                int0 = int(line_split[0])  
                int2 = int(line_split[2])
                int3 = int(line_split[3])
                float4 = float(line_split[4])
                line_split[0] = int0
                line_split[2] = int2
                line_split[3] = int3
                line_split[4] = float4

                total = total + float4 
                listcreate = (line_split[0], line_split[1], line_split[2], line_split[3], line_split[4])
#                if total == 1:
 #                   return True
 #               listout.write(listcreate) 
#                thislist = list(listcreate)
                thislist.append(listcreate)
            except:
                return False

        else:
            return False
    f.close()
    return thislist

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#[(1, 'assignment_1', 85, 100, 0.25), (2, 'test_1', 90, 100, 0.25), (3, 'exam_1', 95, 100, 0.5)]
print(reader("sample.cs1301"))

