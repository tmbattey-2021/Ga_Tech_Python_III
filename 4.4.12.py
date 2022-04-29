

#Write a function called write_1301 which will write a file
#in the format described in Coding Problem 4.4.2. The
#sample.cs1301 file has been included to refresh your 
#memory. Your function should accept two arguments:
#A string of a filename to write to, and a list of tuples. 
#You can assume that each tuple will have the following 
#format:
#
#(int, str, int, int, float)
#
#Each tuple will represent a line in the file, and each
#item in the tuple should correspond to the 
#assignment number, the assignment name, the student's 
#grade, the total possible number of points, and the 
#assignment weight respectively. 


#Write your function here!

def write_1301(fileout, tupleList):
    f = open(fileout, "w")
    listcreate = ()
    thislist = []
#    for i in tupleList:
    a = len(tupleList)
    count = 0
    for line in tupleList: 
#        print(line)
        thislist = []
        outstr = ""
        count = 1
        lnlen = len(line)
        for i in line:
 #           count = count + 1
            if count < lnlen:
                outstr = outstr + str(i) + " "
                print(outstr)
                
            else:
                outstr = outstr + str(i) + "\n"
            count = count + 1
#            thislist.append(i)
#        outstr = outstr + "\n"
        print(outstr)
        f.write(outstr) 
#        outstr = ""
#        thislist.append(\n)
#        line_split = line.split()
#        if len((line_split)) == 5:
#            try:  
#        if len((line_split)) == 5:
#                int0 = int(line_split[0])  
 #               int2 = int(line_split[2])
#                int3 = int(line_split[3])
#                float4 = float(line_split[4])
#                line_split[0] = int0
#                line_split[2] = int2
 #               line_split[3] = int3
 #               line_split[4] = float4

#                total = total + float4 
#                listcreate = (line_split[0], line_split[1], line_split[2], line_split[3], line_split[4])
#                if total == 1:
 #                   return True
 #               listout.write(listcreate) 
#                thislist = list(listcreate)
#                thislist.append(listcreate)
#            except:
#                return False

#        else:
 #           return False
    f.close()
#    print(thislist)
#    return thislist    
        
#    while count < a:
 #       for x in tuple:
#            f.write(str(x) + " ") 
#        f.write("\n")
#        count = count + 1
#    for y in tuple2:
#        f.write(str(y) + " ")
 #   f.write("\n")
#    f.close()
    


#The code below will test your function. It's not used
#for grading, so feel free to modify it! You may check
#output.cs1301 to see how it worked.
tuple1 = (1, "exam_1", 90, 100, 0.6)
tuple2 = (2, "exam_2", 95, 100, 0.4)
tupleList = [tuple1, tuple2]
write_1301("output.cs1301", tupleList)





