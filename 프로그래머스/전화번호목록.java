import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        
        for(int i = 0 ; i < phone_book.length - 1; i++){
            int length = phone_book[i].length();
            
            for(int j = i + 1; j < phone_book.length; j++){
                if(phone_book[i].startsWith(phone_book[j]) || phone_book[j].startsWith(phone_book[i])){
                    return false;
                }
            }
        }
        
        
        return answer;
    }
}