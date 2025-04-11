class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dp = [0] * (len(pressedKeys)+1)

        # Only one way to interpret empty string
        dp[0] = 1

        # i+1 is the index of current element in dp array
        for i, c in enumerate(pressedKeys):
            # Pressed once case
            dp[i+1] = dp[i]
            
            # Pressed twice case
            if i and pressedKeys[i-1] == c: 
                dp[i+1] += dp[i-1]
                
                # Pressed thrice case
                if i >= 2 and pressedKeys[i-2] == c: 
                    dp[i+1] += dp[i-2]
                    
                    # Pressed 4 times case which is only possible in the case of 7 and 9
                    if i >= 3 and pressedKeys[i-3] == c:
                        if c in "79":
                            dp[i+1] += dp[i-3]
            
            # Store the remiander as it is the same thing as summing the dp array and then taking remainder
            dp[i+1] %= (10**9 + 7)
        
        return dp[-1]
