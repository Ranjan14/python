from functools import reduce
nums=[1,34,3,25,56,2,5]

result=reduce(lambda a,b:a+b,nums)
print(result)
