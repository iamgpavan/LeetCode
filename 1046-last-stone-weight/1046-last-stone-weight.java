class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder()); 

        for(int x : stones){
            q.add(x); 
        }

        //8, 7, 4, 2, 1, 1 where 8 is the top element

        while(q.size() > 1){
            int x = q.remove(); 
            int y = q.remove(); 
            if(x == y){
                continue; 
            }
            else{
                if(x > y){
                    q.add(x - y); 
                }else{
                    q.add(y-x); 
                }
            }
        }

        return q.isEmpty() ? 0 : q.remove(); 

    }
}