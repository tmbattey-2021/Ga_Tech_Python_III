


#In the Pokemon video game series, every Pokemon has six
#stats: HP, Attack, Defense, Special Attack, Special Defense,
#and Speed.
#
#Write a function called total_stats that will take as input
#a list of dictionaries. Each dictionary will have seven
#key-value pairs:
#
# - name: a Pokemon's name
# - hp, attack, defense, special attack, special defense,
#   and speed: an integer representing that Pokemon's stat
#   in that category
#
#Your function should return a single dictionary. The keys
#of the dictionary should be the Pokemon names from the
#original list, and the values should be the _total_ stats
#for each Pokemon (add HP, Attack, Defense, Special Attack,
#Special Defense, and Speed).
#
#For example, if this was one of the dictionaries in the
#original list:
#
#{"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49,
#"special attack": 65, "special defense": 65, "speed": 45}
#
#Then one of the key-value pairs in the dictionary you
#return would be: "Bulbasaur": 318 (45 + 49 + 49 + 65 + 65 +
#45 = 318).


#Add your function here!
def total_stats(starters):
    tot_pok = 0
    tot_pop = 0
    hp_list = []
    attack_list = []
    def_list = []
    spe_attack_list = []
    spec_def_list = []
    speed_list = []
    final_dict = {}
    
#    y = starters.keys()
#    keys_as_list = list(y)
 #   keys_as_list.sort()
 #   print(keys_as_list)
 #   for item in keys_as_list:
 #       b = item
 #       final_dict.append[item]
  #      print(final_dict)
    #    outstr = (item + ": " + str(the_dictionary[b]) + "\n")
     #   final_str = final_str + outstr
#    return(final_str)
    
    #for key in starters:
    count = 0
    lenlist = len(starters)
    print(type(starters))
    if count < lenlist:
        for dict in starters:
#            x = car.get("model")
            print(dict)
            print(type(dict))
#            x = dict.find("hp")
 #           print(x)
#            print(dict[1])
 #           x = dict.split()
 #           print(x)       
  #          print(dict[1])
            name_var = dict.get("name")
            hp_var = dict.get("hp")
            print(hp_var)
            attack_var = dict.get("attack")
            defense_var = dict.get("defense")
            spec_attack_var = dict.get("special attack")
            spec_defense_var = dict.get("special defense")
            speed_var = dict.get("speed")
#            hp_list.append(dict['attack'])
#            hp_list.append(dict['defense'])
 #           hp_list.append(dict['special attack'])
#            hp_list.append(dict['special defense'])
#            hp_list.append(dict['speed'])       
#            print(hp_list)
#            count = count + 1
            tot_var = hp_var + attack_var + defense_var + spec_attack_var + spec_defense_var + speed_var
            print(tot_var)
            final_dict[name_var] = tot_var
            print(final_dict)
    return final_dict
#    for i in hp_list:
 #       tot_pok = tot_pok + i
 #   print(tot_pok)
    
#    p = []
#    for value in country_list:
#        p.append(value['population'])
#    print(p)
#    for pop in p:
#        tot_pop = tot_pop + pop
#    print(tot_pop)
#    dens = tot_pop/tot_area
#    return dens




#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Bulbasaur': 318, 'Charmander': 309, 'Squirtle': 314}
starters = [{"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49, "special attack": 65, "special defense": 65, "speed": 45},
            {"name": "Charmander", "hp": 39, "attack": 52, "defense": 43, "special attack": 60, "special defense": 50, "speed": 65},
            {"name": "Squirtle", "hp": 44, "attack": 48, "defense": 65, "special attack": 50, "special defense": 64, "speed": 43}]
print(total_stats(starters))




