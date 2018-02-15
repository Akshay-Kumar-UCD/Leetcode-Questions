def productExceptSelf(nums):
    ans = []
    z = 1
    for i in range(len(nums)):
        ans.append(z)
        z *= nums[i]
    z = 1
    for i in range(len(nums)-1,-1,-1):
        ans[i] *= z
        z *= nums[i]
    return ans

def test():
    answer = productExceptSelf([1,2,3,4])
    print(answer)

if __name__ == "__main__":
    test()