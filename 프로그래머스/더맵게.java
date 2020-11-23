import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
        
        for(Integer i: scoville){
            queue.add(i);
        }
        
        while (queue.peek() < K){
            if (queue.size() == 1){
                return -1;
            }
            
            int x = queue.poll();
            
            if(x < K){
                int y = queue.poll();
                queue.add(x + 2 * y);
                answer++;
            }
            
        }
        return answer;
    }
}