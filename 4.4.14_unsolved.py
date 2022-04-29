
#We've given you a file called "top500.txt" which contains
#the name and lifetime gross revenue of the top 500
#films at the time this question was written. 
#
#Each line of the given file is formatted like so:
# <name>\t<gross revenue in dollars>
#
#In other words, you should call .split("\t") to split
#the line into the movie name (the first item) and the
#gross (the second item).
#
#Unfortunately, these movies are not in order. Write a 
#function called "sort_films" that accepts two parameters:
#a string of a source filename and a string of a
#destination filename. Your function should open the
#source file and sort the contents from greatest gross
#revenue to least gross revenue, and write the sorted
#contents to the destination filename. You may assume the
#source file is correctly formatted.
#
#Hint: one common issue on this problem is that every line
#in the input file ends with a line break except the last
#one. If the autograder gives you an index error, open
#top500result.txt and make sure there are 500 lines in your
#output file!

#Write your function here!

def sort_films(input1, output1):
    
#def multiply_file_by_index(out1, in1):
    count = 0
    filea = open(input1)
    fileb = open(output1, "w")
    filea = filea.readlines()
    filea = str(filea.split("\t"))
    
    def myFunc(e):
        return e[int(filea[1])]
    filea.sort(key=myFunc)
#    filea.readline()
    for line in filea:
        line = line.rstrip()
        count = count + 1
#        inta = int(line) * count
        strout = filea[0] + " " + filea[1]
        fileb.write(strout + "\n")
        print(strout)

#        def myFunc(e):
#  return e['year']

#cars = [
#  {'car': 'Ford', 'year': 2005},
#  {'car': 'Mitsubishi', 'year': 2000},
#  {'car': 'BMW', 'year': 2019},
 # {'car': 'VW', 'year': 2011}
#]

#cars.sort(key=myFunc)

#The line of code below will test your function and put
#your results in top500result.txt. Then, it will print
#"Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")





