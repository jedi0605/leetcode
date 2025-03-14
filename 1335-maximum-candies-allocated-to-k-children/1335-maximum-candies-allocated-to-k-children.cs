public class Solution {
    
    private bool Work(List<int> candies2,long c, long k){
        long res = 0;
        foreach(var i in candies2)
        {
            res += (i/c);
        }
        return true? res>=k :false;
    }
    
    public int MaximumCandies(int[] candies, long k) {
        List<int> candies2 = new List<int>(candies);
        
        long l = 1; 
        long r = candies2.Max();
        
        while(l<=r)
        {
            long mid = (l+r) / 2;
            if(Work(candies2,mid,k))
                l = mid+1;
            else
                r = mid-1;
        }
        return (int)r;
    }
}