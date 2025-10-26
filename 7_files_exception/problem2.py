
f1=open('/Users/algo trading 2025/batch34/7_files_exception/number.txt','r')
d=f1.read()
print(d)
f1.close()


nums=d.split('\n')
print(nums)


try:
    num1=int(nums[0])
    num2=int(nums[1])
    print(num1,num2)
    ans=num1/num2
    print(ans)
except Exception as e:
    print(e)