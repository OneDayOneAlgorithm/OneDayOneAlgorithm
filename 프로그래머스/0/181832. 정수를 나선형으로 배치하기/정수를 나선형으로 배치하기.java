class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int[][] visited = new int[n][n];
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        int idx = 1;
        int x=0, y=0, nx=0, ny=0, dir_cnt=0;
        answer[x][y] = idx++;
        visited[x][y] = 1;
        for(int i=1; i<n*n; i++){
            for(int dir=0; dir<4; dir++){
                nx=x+dx[dir_cnt%4];
                ny=y+dy[dir_cnt%4];
                if(0<=nx && nx<n && 0<=ny && ny<n && visited[nx][ny]==0){
                    x=nx;
                    y=ny;
                    answer[x][y] = idx++;
                    visited[x][y] = 1;
                    break;
                }
                dir_cnt++;
            }
        }
        return answer;
    }
}