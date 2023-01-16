import numpy as np
alpha_dict = {
    "A":0,
    "B":1,
    "C":2,
    "D":3,
    "E":4,
    "F":5,
    "G":6,
    "H":7,
    "I":8,
    "J":9,
    "K":10,
    "L":11,
    "M":12,
    "N":13,
    "O":14,
    "P":15,
    "Q":16,
    "R":17,
    "S":18,
    "T":19,
    "U":20,
    "V":21,
    "W":22,
    "X":23,
    "Y":24,
    "Z":25
}


array = [[ [0 for col in range(26)] for col in range(26)] for row in range(26)]

with open("3letter.txt") as textFile:
       lines = [line.strip().split(" ", 1) for line in textFile]



letters = []
for i in lines:
    letters.append(i[0])

defs = []

for i in lines:
    defs.append(i[1])

zipo = zip(letters,defs)
dictionary = dict(zipo)

def __converter(str1):
    temp = []
    for word in str1:
        word = word.upper()
        temp.append(alpha_dict[word])
    return temp

for row in letters:
    temp = __converter(row)
    array[temp[0]][temp[1]][temp[2]] = row 


def search(word):
    if word.lower():
        word = word.upper()
    if len(word) == 3:
        if word in dictionary:
            res = "{} - {}".format(word,dictionary[word])
            return res
        else:
            return "word doesn't exist in the dictionary!\n"
    else:
        return "you have inputted wrong number of word!\n"
    

def add_to_dict(word, meaning):
    if word.lower():
        word = word.upper()
    if len(word) == 3:
        if word not in dictionary:
            tmp = __converter(word)
            array[tmp[0]][tmp[1]][tmp[2]] = word
            dictionary.update({word:meaning})
            return "the word {} has been added.\nthe meaning of the word is {}\n".format(word, meaning)

        else:
            return "the word already exists.\n"
    else :
        return "Please insert a 3 letter word!\n"

def delete_from_dict(word):
    if word.lower():
        word = word.upper()
    res = ""
    if word in dictionary:
        tmp = __converter(word)
        del array[tmp[0]][tmp[1]][tmp[2]]
        #array[tmp[0][tmp[1]]].pop(tmp[2])
        res = dictionary.pop(word)
        return "the word {} - {} has been deleted.\n".format(word,res)
        
    else:
        return "the word doesn't exist in the dictionary.\n"


res = True
while res:
    
    print('''The below is a implemetation of a hashing.
    Please select a option from below by typing either 1 or 2 or 3.
    1) Insert a word into the dictionary 
    2) Delete a word from a dictionary
    3) Search a word from a dictionary
    4) Exit from the program.
    ''')
    option = int(input("please select the option!\n"))

    match (option):
        case (1):
            inp_add = input("Please insert a word.\n")
            inp_add_meaning = input("Please insert the meaning of the word.\n")
            print(add_to_dict(inp_add,inp_add_meaning))
            print(array)
            #print(dictionary)
        
        case (2):
            inp_del = input("Input a word that you would like to delete.\n")
            print(delete_from_dict(inp_del))
            print(array)

        case (3):
            inp = (input("please search a word in our dictionary and the definition will come up\n"))
            print(search(inp))

        case (4):
            res = False
            break





    
       




#with open("3letter.txt") as textFile:
 #   for lines in textFile:
  #      lines = lines.strip().split(" ", 1)
   #     print(lines)
    #    break

'''

with open("3letter.txt") as textFile:
       lines = [line.split(" ", 1) for line in textFile]

#print(lines)

letters = []
for i in lines:
    letters.append(i[0])


remaining = []
for i in lines:
    remaining.append(i[1:])


zipo = zip(letters,remaining)
dictionary = dict(zipo)
print(dictionary)



'''
'''
with open("3letter.txt") as textfile:
            for inputline in textfile:
                key, value = inputline.split()
                dictionary[key] = value
print(dictionary)
'''


'''with open("3letter.txt") as textfile:
            for inputline in textfile:
                   dictionary[inputline[0]][inputline[1]][inputline[2]] = inputline[3:]

print(array)
'''
'''

#print(lines) 



#print(letters)


#def __converter(str1):
 #   temp = []
  #  for word in str1:
   #     word = word.upper()
    #    #print(dict[col])
     #   temp.append(dict[word])
return temp


def search(find):
    temp = __converter(find)

    result = array[temp[0]][temp[1]][temp[2]] 



defs = []
for i in lines:
    new_str = ""
    for j in i[1:]:
        new_str += j + " "

    
    defs.append(new_str)
    

print(defs)
*/
#for row in letters:
 #   temp = ""
  #  for col in row:
   #     temp.append(dict[col])
#print(temp)        

for row in letters:
    temp = __converter(row)
    array[temp[0]][temp[1]][temp[2]] = row
    
#print(array)
#print(temp) 
'''