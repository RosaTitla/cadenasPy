print("This will execute first")

for _ in range(3):
    print("This line will execute three times")
    print("This line will also execute three times")

print("Now we are outside of the for loop!")

#How many times will the for loop iterate in
# the following statements?

p = [3, 4, "Me", 3, [], "Why", 0, "Tell", 9.3]
for ch in p:
   print(ch)

print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))

# Note: `range` function is already casted as `list` in the textbook
print(range(5))

accum = 0
for w in range(11):
    accum = accum + w
print(accum)

# or, if you use two inputs for the range function

sec_accum = 0
for w in range(1,11):
    sec_accum = sec_accum + w
print(sec_accum)

# It will print out 10 instead of 55
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for w in nums:
   accum = 0
   accum = accum + w
print(accum)



#Write code to create a list of integers
# from 0 through 52 and assign that list to the variable numbers. You should use a special Python function – do not type out the whole list yourself. HINT: You can do this in one line of code!

numbers=[x for x in range(0,53)]
print(numbers)

#Count the number of characters in string str1.
# Do not use len(). Save the number in variable numbs.
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs=0
for letra in str1:
    numbs+=1
print(numbs)
#Create a list of numbers
# 0 through 40 and assign this list to
# the variable numbers. Then,
# accumulate the total of the list’s values and assign that sum to the variable sum1

sum1=0
for numbers in range(41):
    sum1=sum1+numbers
print(sum1)

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(5):
    print(n, fruits[n])

fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n], end="\t")
#How many times is the letter p
# printed by the following statements?
s = "python"
for idx in range(len(s)):
   print(s[idx % 2])



