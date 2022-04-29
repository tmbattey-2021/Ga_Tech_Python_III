#Write a function called get_grade that will read a
#given .cs1301 file and return the student's grade.
#To do this, we would recommend you first pass the
#filename to your previously-written reader() function,
#then use the list that it returns to do your
#calculations. You may assume the file is well-formed.
#
#A student's grade should be 100 times the sum of each
#individual assignment's grade divided by its total,
#multiplied by its weight. So, if the .cs1301 just had
#these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
#Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


#Write your function here!

def get_grade(filein):
    f = open(filein, "r")
    total = 0
    line_tot = 0
    grade = 0
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
                line_tot = (int2 / int3) * float4
                total = total + line_tot
                grade = total * 100
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
    return grade


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 91.55 
print(get_grade("sample.cs1301"))





