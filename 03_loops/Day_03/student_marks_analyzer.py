num_sub=int(input("enter num of subject:"))
marks=[]
Total_marks=0

for m in range(1,num_sub+1):
    mark=int(input(f"Enter mark {m}:"))
    marks.append(mark)

lowest_mark=marks[0]
highest_mark=marks[0]

for mark in marks:
    Total_marks=Total_marks+mark

    if lowest_mark>mark:
        lowest_mark=mark
        
    if highest_mark<mark:
        highest_mark=mark

Average=Total_marks/num_sub

print("="*34)
print("MARKS ANALYZER".center(34))
print("="*34)
print(f"{'Total Mark':<15}:{Total_marks}")
print(f"{'Average mark':<15}:{Average}")
print(f"{'Lowest mark':<15}:{lowest_mark}")
print(f"{'Highest Mark':<15}:{highest_mark}")
print("-"*34)