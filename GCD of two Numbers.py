class Solution:
    def GCD(self, n1, n2):
        count1=[]
        count2=[]
        for i in range(1,n1+1):
            if n1%i==0:
                count1.append(i)
        for j in range(1,n2+1):
            if n2%j==0:
                count2.append(j)
        return max(set(count1) & set(count2))
print(Solution().GCD(4,6))
