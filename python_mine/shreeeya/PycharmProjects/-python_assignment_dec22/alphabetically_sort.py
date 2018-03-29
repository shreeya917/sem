#Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them alphabetically.

sequence=str(input("Enter the sequence of word: "))
words=sequence.split(',')
print("The unsorted input is: \n",sequence)
words.sort()
print("The sorted output is:")
print(", ".join(words))