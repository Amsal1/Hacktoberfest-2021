class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int res = 0;
      
        Queue<Character> queue = new LinkedList<>();
        
        for(char c : s.toCharArray())
        {
            if(queue.contains(c))
            {
                while(queue.contains(c))
                {
                    queue.poll();
                }
            }
            queue.add(c);
            
            res = Math.max(res, queue.size());
            
        }
        return res;
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int result = lengthOfLongestSubstring(s);
        System.out.println(res);
    }
}