set_num1={1,2,3,23,45}
set_num2={1,2,9,67}
ans=set_num1.difference(set_num2)
print(ans)
ans=set_num2.difference(set_num1)
print(ans)

ans=set_num1.union(set_num2)
print(f"Union {ans}")

ans=set_num1.intersection(set_num2)
print(f"Intersection {ans}")

ans=set_num1.symmetric_difference(set_num2)
print(f"Symatric {ans}")

# set_num1+set_num2
# set_num1&set_num2
# set_num1-set_num2

set1={i*i for i in set_num1 }
print(set1)

for i in range(len(set1)):
    print(set1[i])