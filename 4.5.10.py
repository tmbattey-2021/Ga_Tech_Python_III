



#Recall in an earlier problem you were given two lists: one
#list was a student's answers to a test, and the other was
#the answer key. Your goal was to return a score
#representing the number of problems the student got correct.
#
#Let's do that again, but with dictionaries instead of lists.
#Write a function called calculate_score. calculate_score
#should take two parameters: a dictionary of student answers
#and a dictionary of correct answers. Both dictionaries should
#have integers as their keys, and one-character strings as
#their values.
#
#calculate_score should count how many questions the student
#got right. Or, in more precise terms, calculate_score should
#count how many keys for which the associated value is the
#same in the student's dictionary and in the answer key
#dictionary.
#
#As before, it is possible that there will be more answers in
#one than the other. This means that these answers don't
#belong to the same test! If that happens, return -1.


#Add your function here!
def calculate_score(student_answers, correct_answers):
    count = 0
    count_ans = 0
    for x, y in student_answers.items():
        count_ans = count_ans + 1
        print(x, y)
        x_ans = x
        y_ans = y
#        for x:y in correct_answers.items()
        y_correct = correct_answers.get(x_ans)  
        print(y_correct)
        if y_correct == y_ans:
            count = count + 1
    count_correct = len(correct_answers.keys())
    print(count_correct)
    print(count_ans)
    if count_correct == count_ans:  
        return(count)
    else:
        return(-1)

#def alphabetical_keys(the_dictionary):
#   a = the_dictionary["Joyner, David"]
#    print(a)
 #   final_str = ""
#    y = the_dictionary.keys()
#    keys_as_list = list(y)
#    keys_as_list.sort()
#    print(keys_as_list)
#    for item in keys_as_list:
#        b = item
#        outstr = (item + ": " + str(the_dictionary[b]) + "\n")
#        final_str = final_str + outstr
 #   return(final_str)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3
student_answers = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
correct_answers = {1: "A", 2: "B", 3: "A", 4: "D", 5: "B"}
print(calculate_score(student_answers, correct_answers))



