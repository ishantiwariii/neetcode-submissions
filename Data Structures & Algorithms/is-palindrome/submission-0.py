class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pehle clean kro , fir reverse kro fir compare kro thats it

        clean = ""

        for i in s:
            if i.isalnum():
                clean += i.lower()
        
        reverse = clean[::-1]

        if clean == reverse:
            return True
        
        return False