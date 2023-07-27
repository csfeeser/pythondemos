

menu= ["cheeseburger", "salad", "pizza", "tofu", "tostadas", "cheese sticks"]

for x,y in enumerate(menu):
    #print("x=", x)
    #print("y=", y)
    print(f"{x + 1}. {y}")

# DIFFERENCE TUPLE vs LIST
# BOTH ordered sequences
# BOTH be sliced by index tuple[0] or list[0]
# DIFFERENT, lists can be changed (mutable) ---> list.append(new_value)
#            tuples can NOT be changed (immutable)

