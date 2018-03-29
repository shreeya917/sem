#3. Define a function that takes in a list arbitary_list = [1, 2, 4, 4, 3, 5, 6].
# Inside the function each element of the list is extracted and is cubed.
# Finally, The squared value is then appened to another list and is returned.

def f(arb_list):
    for arb in arb_list:
        arb=arb**3
        y.append(arb)

    arb_list.extend(y)
    return arb_list


arbitary_list = [1, 2, 4, 4, 3, 5, 6]
y=[]
f(arbitary_list)
print(arbitary_list)