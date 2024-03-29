




#Write a function called write_weird_file. write_weird_file
#should take two positional parameters. The first should be
#a filename, and the second should be a list. The function
#should also have three keyword parameters: mode, sort_first
#and reverse_first. The default value for mode should be "w",
#and the default values for both sort_first and reverse_first
#should be False.
#
#write_weird_file should write the contents of the list to
#the given filename. Each item from the list should be on a
#separate line. The list items could be strings, floats, 
#characters, or integers. If the mode is "w", it should
#overwrite the current contents; if the mode is "a", it
#should append to the current contents. You may assume there
#will be no other value for mode.
#
#If sort_first is True, it should sort the list before
#writing. If reverse_first is True, then it should reverse
#the list before writing. If both are True, it should sort,
#then reverse.


#Add your function here!

def write_weird_file(output1, list1, mode = "w", sort_first=False, reverse_first=False):
 #   f = open(output1, "w")
    if mode == "w":
        f = open(output1, "w", encoding="utf-8")
        if sort_first == True:
            list1.sort()
        if reverse_first == True:
            list1.reverse()      
        for item in list1:
            f.write(str(item) + "\n")
        f.close()
    if mode == "a":
        f = open(output1, "a", encoding="utf-8")
        if sort_first == True:
            list1.sort()
        if reverse_first == True:
            list1.reverse()   
        for item in list1:
            f.write(str(item) + "\n")
        f.close()         
        

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing. However, if you open the file called
#output.txt in the top left after running it, the contents
#of the file should be:
#Wait, where'd the other text go?
#It's gone!
#3
#2)
#1
write_weird_file("AutomatedTestOutput-zsQDQIax.txt", ["censor", "antiperspirant", "Garrisonian", "typology", "snow"])

write_weird_file("output.txt", ["Hmm, I bet this text will disappear.", "I wonder where it will go?"])
write_weird_file("output.txt", ["Wait, where'd the other text go?", "It's gone!"])
write_weird_file("output.txt", [2, 1, 3], mode="a", sort_first=True, reverse_first=True)





