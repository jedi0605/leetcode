public class Solution {
    public int HeightChecker(int[] heights) {
        
        List<int> tmp = new List<int>(heights);
        tmp.Sort();
        
        int res = 0;
        for(int i=0; i<heights.Length;i++)
        {
            if(heights[i]!=tmp[i])
                res++;
        }
        return res;
    }
}