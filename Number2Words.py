# Write a function to convert given number in the form of words.
# eg. Input: 1234 
# Output: One thousand two hundred thirty four

import inflect # pip3 install inflect

inf = inflect.engine()
no = int(input('Enter a number: '))
words = inf.number_to_words(no)

print("in words:", words)
