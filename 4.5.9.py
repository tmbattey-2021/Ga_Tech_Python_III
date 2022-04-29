

#Write a function called clean_data. clean_data takes one
#parameter, a dictionary. The dictionary represents the
#observed rainfall in inches on a particular calendar day
#at a particular location. However, the data has some
#errors.
#
#clean_data should delete any key-value pair where the value
#has any of the following issues:
#
# - the type is not an integer or a float. Even if the value
#   is a string that could be converted to an integer (e.g.
#   "5") it should be deleted.
# - the value is less than 0: it's impossible to have a
#   negative rainfall number, so this must be bad data.
# - the value is greater than 100: the world record for
#   rainfall in a day was 71.8 inches
#
#Return the dictionary when you're done making your changes.
#
#Remember, the keyword del deletes items from lists
#and dictionaries. For example, to remove the key "key!" from
#the dictionary my_dict, you would write: del my_dict["key!"]
#Or, if the key was the variable my_key, you would write:
#del my_dict[my_key]
#
#Hint: If you try to delete items from the dictionary while
#looping through the dictionary, you'll run into problems!
#We should never change the number if items in a list or
#dictionary while looping through those items. Think about
#what you could do to keep track of which keys should be
#deleted so you can delete them after the loop is done.
#
#Hint 2: To check if a variable is an integer, use
#type(the_variable) == int. To check if a variable is a float,
#use type(the_variable) == float.


#Write your function here!

def clean_data(my_dict):
    del_list = []

#    x = my_dict.values()
#    for item in x:
 #       if (type(item) == int or type(item) == float) and item >= 0 and item <= 100:
#            if item > 0 and item <= 100:
 #               continue
#            del_list.append(item)
 #       else:
#            del_list.append(item)
            
#    print(del_list)

    x = my_dict.items()
    for x, y in x:
        if (type(y) == int or type(y) == float) and y >= 0 and y <= 100:
#            if item > 0 and item <= 100:
                continue
#            del_list.append(item)
        else:
            del_list.append(x)
            
    print(del_list)    
    
    for i in del_list:
        del my_dict[i]
    return my_dict

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{"20190101": 5, "20190103": 7.5, "20190104": 0, "20190107": 1}
rainfall = {"20190101": 5, "20190102": "6", "20190103": 7.5, 
           "20190104": 0, "20190105": -7, "20190106": 102,
           "20190107": 1}
print(clean_data(rainfall))

