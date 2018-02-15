"""
def powerset(nums):
    soln = [[], nums]
    for index, e in enumerate(nums):
        if [e] not in soln:
            soln.append([e])
            print(e)
        for new_index, f in enumerate(nums[index+1:]):
            if [e, f] not in soln:
                soln.append([e, f])
                print([e, f])
            if nums[index+1:] not in soln:
                soln.append(nums[index+1:])
                print(nums[index+1:])
 
    return soln
    
nums = [1,2,3]
soln = powerset(nums)
print(soln)
"""