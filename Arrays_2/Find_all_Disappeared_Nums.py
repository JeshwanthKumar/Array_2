#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = [] #Initialize an empty array as result
        
        for i in range(len(nums)):  #Contiue till the length of nums
            index = abs(nums[i])-1  #Initialize index as absolute value of nums[i]-1
            
            if nums[index] < 0: #If the nums[index] is less than 0 continue
                continue
            nums[index] *= -1   #Multiply nums[index] with -1
                
        for j in range(len(nums)):  #Continue till the length of nums
            if nums[j] > 0: #If nums[j] is greater than 0 
                result.append(j+1)  #Append the value into the array
        return result   #Return the result
        



       