#User function Template for python3

class Solution:
    
    def rev_num(self,num):
        rev=""
        while num>0:
            rev=rev+str((num%10))
            num=num//10
        return int(rev)
    
    def isSumPalindrome (self, n , c=1):
        # code here 
        reverse_number=self.rev_num(n)
        if n == self.rev_num(n):
            return n
        else:
            sum=n+reverse_number
            if c > 5:
                return -1
            return self.isSumPalindrome(sum,c=c+1)
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isSumPalindrome(n))
# } Driver Code Ends