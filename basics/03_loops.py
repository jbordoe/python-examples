###########################
# A simple while loop
###########################
print('')
a = 0  # initialize the variable
while a < 10: # the loop stops when this condition is no longer true
    print(a, '', end='')
    a = a+1
else: # executes once the loop is finished
    print('done.')


###########################
# while loop with break
###########################
print('')
b = 0
while True: # will loop indefinitely
    print(b, '', end='')
    b = b+1

    if b > 5:
        break # end the loop here, move to next statement

###########################
# while loop with continue
###########################
print('')
c = 0
while c <= 10:
    c = c +1
    if c % 2 == 0:
        continue # skip the remainder of the loop bodu

    print(c, '', end='')

###########################
# for loop with array
###########################
print('')
animals = ['cat', 'dog', 'bear']
for animal in animals:
    print(animal, '', end='')
else: # executes once the loop is finished
    print('done.')

###########################
# for loop with String
###########################
print('')
for letter in 'String':
    print(letter, '', end='')

###########################
# for loop with range
###########################
print('')
for n in range(5,15):
    print(n, '', end='')

