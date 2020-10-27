def longer_than_five(list_of_names):
    for name in list_of_names: # iterate over the list to look at each name
        if len(name) > 5: # as soon as you see a name longer than 5 letters,
            return True # then return True!
            # If Python executes that return statement, the function is over and the rest of the code will not run -- you already have your answer!
    return False # You will only get to this line if you
    # iterated over the whole list and did not get a name where
    # the if expression evaluated to True, so at this point, it's correct to return False!

# Here are a couple sample calls to the function with different lists of names. Try running this code in Codelens a few times and make sure you understand exactly what is happening.

list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))

#Write a function that reverses
# its string argument.

#Escriba una función que refleje su argumento de cadena, generando una cadena que contenga la cadena original y la cadena al revés.
#Escribe una función que elimine todas las apariciones de una letra determinada de una cadena.
#Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:

def replace(s,old, new):
    return

def test():
    return

test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
test(replace(s, 'om', 'am'),
       'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')