def productExceptSelf(nums):
    res=[1]*len(nums)

    pre=1
    for i in range(1,len(nums)):
        res[i]=pre*nums[i-1]
        pre=res[i]
    post=nums[-1]

    for i in range(len(nums)-2,-1,-1):
        res[i]=post*res[i]
        post=post*nums[i]

    return res

n = int(input("Enter number of elements : "))
nums=[]
for i in range(0, n):
    ele = int(input())
    nums.append(ele)
    
print(productExceptSelf(nums))