


#Write a function called course_info that takes as input a
#list of tuples. Each tuple contains two items: the first
#item in each tuple is a student's name as a string, and the
#second item in each tuple is that student's age as an
#integer.
#
#The function should return a dictionary with two keys.
#The key "students" should have as its value a list of all
#the students (in other words, a list made from the first
#value of each tuple), in the original order in which they
#appeared in the list. The key "avg_age" should have as its
#value a float representing the average age of all the
#students in the list (in other words, the average of all
#the second items in the tuples).
#
#For example:
#
#  course_info([("Jackie", 20), ("Marguerite", 21)])
#  -> {"students": ['Jackie', 'Marguerite'], "avg_age": 20.5}
#
#Hint: Concentrate first on building the list of students
#and calculating the average age. Save creating the
#dictionary for last.


#Write your function here!

def course_info(mytuple):
 #   for item in mytuple:
    mylist = []    
    mydict = {}
    count = 0
    totage = 0
    for item in mytuple:
        print(mytuple[count])
        print(item[0])
        print(item[1])
  #      for first in item:
 #           print(first[0])
#        x = name_list[count]
 #       y = number_list[count]
        mylist.append(item[0])
        print(mylist)
        count = count +1
        totage = totage + item[1]
        print(totage)
#        mydict[x] = y
        
#        print(x)
#        print(y)
        
#        count = count + 1
    avg_age = totage / count
    print(avg_age)
    mydict["students"] = mylist
    mydict["avg_age"] = avg_age
    
    return mydict


#def alphabetical_keys(the_dictionary):
#   a = the_dictionary["Joyner, David"]
#    print(a)
 #   final_str = ""
#    y = the_dictionary.keys()
 #   keys_as_list = list(y)
 #   keys_as_list.sort()
#    print(keys_as_list)
#    for item in keys_as_list:
 #       b = item
#        outstr = (item + ": " + str(the_dictionary[b]) + "\n")
 #       final_str = final_str + outstr
 #   return(final_str)
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'avg_age': 20.5, 'students': ['Jackie', 'Marguerite']}
print(course_info([("Jackie", 20), ("Marguerite", 21)]))



