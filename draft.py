array = [9,2,3,4,5, None] #pretend last index is empty
print(f"Before shift: {array}")
inserted_head_element= 10
for i in reversed(range(5)):
    array[i+1]= array[i]
    
array[0] = inserted_head_element
print(f"After shift: {array}")