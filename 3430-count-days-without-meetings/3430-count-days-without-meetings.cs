public class Solution {
    public int CountDays(int days, int[][] meetings) {
        /// Merge all days
        Array.Sort(meetings, (a, b) => a[0].CompareTo(b[0]));    
        int[] cur = new int[2];   
        cur[0] = meetings[0][0];
        cur[1] = meetings[0][1];
        List<int[]> new_merge = new List<int[]>();

        for(int i = 0;i<meetings.Length;i++)
        {
            if (meetings[i][0] <= cur[1])
                cur[1] = Math.Max(cur[1], meetings[i][1]);
            else{
                new_merge.Add(cur.ToArray());
                cur[0] = meetings[i][0];
                cur[1] = meetings[i][1];
            }
        }        
        new_merge.Add(cur);

        int res = 0;
        foreach(var item in new_merge)
        {
            res+= item[1]-item[0]+1     ;       
        }
        
        return days-res;
    }
}