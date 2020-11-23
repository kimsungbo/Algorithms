import java.util.*;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        ArrayList<String> answer = new ArrayList<>();
        
        
        String format = "%0" + n + "d";
        
        for(int i = 0 ; i < n; i++){
            long a = Long.parseLong(Integer.toBinaryString(arr1[i]));
            long b = Long.parseLong(Integer.toBinaryString(arr2[i]));
            
            String a_ = String.format(format, a);
            String b_ = String.format(format, b);
                        
            String temp = "";
            for(int j = 0 ; j < n; j++){
                if (a_.charAt(j) == '1' || b_.charAt(j) == '1'){
                    temp = temp + "#";
                }
                else{
                    temp = temp + " ";
                }
            }
            answer.add(temp);
            
        }
        
 
        return answer.stream().toArray(String[]::new);

    }
}