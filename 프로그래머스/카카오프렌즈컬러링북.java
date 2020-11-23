import java.util.*;

class Solution {
    
    public int[][] matrix;
    
    public int dfs(int count, int x, int y, int m, int n){
        
        int current_color = matrix[x][y];
        matrix[x][y] = 0;
        
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        
        for(int i = 0 ; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx >= 0 && nx < m && ny >= 0 && ny < n){
                if (matrix[nx][ny] == current_color){
                    count = dfs(count+1, nx, ny, m, n);
                }
            } 
        }
        return count;
    }
    
    
    public int[] solution(int m, int n, int[][] picture) {
        matrix = new int[m][n];
        for(int i=0; i<m; i++){
            for(int k=0; k<n; k++){
                matrix[i][k]=picture[i][k];
            }
        }
        
        
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        ArrayList<Integer> colored = new ArrayList<>();
        
        
        for(int i = 0 ; i < m; i++){
            for(int j = 0 ; j < n; j++){
                if (matrix[i][j] != 0){
                    colored.add(dfs(1, i, j, m, n));
                }
            }
        }
    
        int[] answer = new int[2];
        answer[0] = colored.size();
        
        answer[1] = Collections.max(colored);
        return answer;
    }
}