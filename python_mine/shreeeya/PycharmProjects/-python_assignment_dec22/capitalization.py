#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

lines=str(input("Enter sequence of lines: "))
lines.upper()
for line in lines:
    upper_lines= line.upper()
    print(upper_lines,end='')