import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> time = new ArrayList<Integer>();
        
        for(int i = 0 ; i < progresses.length; i++){
            if((100 - progresses[i]) % speeds[i] == 0){
                time.add((100-progresses[i]) / speeds[i]);
            }
            else{
                time.add((100-progresses[i]) / speeds[i] + 1);
            }
        }
        
        int start = 0;
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(int i = 0 ;i < time.size(); i++){
            if(time.get(start) < time.get(i)){
                answer.add(i-start);
                start = i;
            }
        }
        answer.add(time.size() - start);
        
        
        return answer.stream().mapToInt(i->i).toArray();

    }
}