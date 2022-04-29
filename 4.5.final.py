

#In this problem, we're giving you a file containing some real data from
#the Marta (Atlanta's subway system) database. Each line of the file is
#a record of a single ride at a specific Marta station. Riders enter and
#exit the subway system by tapping a Breeze Card against a gate at a
#specific station.
#
#You can see a preview of what the file will look like in
#marta_sample.csv in the dropdown in the top left. Note, however, that
#the real dataset is massive: over 200,000 individual rides are recorded.
#So, you're going to be dealing with some pretty big data!
#
#Each line of the file contains six items, separated by commas:
#
# - the transit day, in MM/DD/YYYY format.
# - the transit time, in HH:MM:SS format.
# - the device ID, an identifer of the gate at which the rider entered.
# - the station ID, a numeric identifier the station.
# - the use type, whether the rider was entering, exiting, etc.
# - a serial number, the unique identifier of the rider's Breeze Card.
#
#Your goal is to use this file to answer three questions:
#
# - What is the average number of Breeze Card taps per station?
# - What is the station ID of the station whose traffic is the closest
#   to that average?
# - What station has the least overall amount of traffic?
#
#Note that you will answer these questions in the fill-in-the-blank
#problems below, _not_ in this coding exercise. So, you don't have to
#programmatically find the station ID closest to the average: you could
#just print all the stations and their averages, then visually check
#which is closest to the average.
#
#To get you started, we've gone ahead and opened the file:

marta_file = open('../resource/lib/public/marta_01-18-2016.csv', 'r')
myfile = marta_file.readlines()
#print(myfile.count('30'))
#for item in myfile:
#    print(item)
#myfiles = myfile.split(",")
mydict = {}
mylist = []
totcount = 0
#z = myfile.split(',')
for item in myfile:
    totcount = totcount + 1
#    print(item[3])
    x = item.split(',')
#    def myFunc(e):
#        return e(x[3])
#    x.sort(key = myFunc)
#    print(x[3])
 #   mydict.update({x[3]:x[1]})
    mylist.append(x[3])
 #   print(mylist)
#    print(mydict)
#    y = count(
mylist.sort()
y = 0
itemct = 1
unique = 0
#print(mylist)
for item in mylist:
#    y = item
    if itemct == 1:
        y = item
#        print(item)
#    print(y)
    if item == y:
        itemct = itemct + 1
#        y = item
        print(item)
        print(y)
        print(itemct)
    else:
        print("item" + str(itemct))
        unique = unique + 1
        continue


    #    print(item)
#You may add whatever code you want from here on to answer those three
#questions.
#
#HINT: although there are six items on each line of the file, you only
#need one of them: station ID. If you use split(",") to split up each
#line, station ID will be at index 3 on the list.
#
#HINT 2: You'll probably want to use a dictionary, with station IDs as
#the keys and 







