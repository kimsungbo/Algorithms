import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        List<Integer> answer = new ArrayList<Integer>();
        
        
        for(int i = 0 ; i < prices.length; i++){
            boolean flag = false;
            
            for(int j = i+1 ; j < prices.length; j++ ){
                if (prices[j] < prices[i]){
                    answer.add(j-i);
                    flag = true;
                    break;
                }
            }
            if(flag == false ){
                answer.add(prices.length - i - 1);
            }
        }
        
        int[] answer2 = answer.stream().mapToInt(i->i).toArray();
        
        return answer2;

    }
}