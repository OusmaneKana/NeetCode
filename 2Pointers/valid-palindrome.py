class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0 , len(s) -1

        while l<r:
            print(s[l], s[r])
            if l<r and not self.is_alphanum(s[l]):
                l+=1
            
            if r>l and not self.is_alphanum(s[r]):
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l+1, r-1
            
        return True
        
    

    def is_alphanum(self, c):
        return(
            ord("Z")>=ord(c) >= ord("A") or
            ord("z")>=ord(c) >= ord("a") or
            ord("9")>=ord(c) >= ord("0")
        )
    


test = Solution()

test.isPalindrome("Was it a car or a cat I saw?")