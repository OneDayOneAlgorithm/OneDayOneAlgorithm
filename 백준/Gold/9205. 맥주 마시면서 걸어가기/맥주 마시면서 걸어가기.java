import java.util.*;
import java.io.*;

public class Main{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int t, n, sr, sc, er, ec;
    static String answer;
    static int[][] convenienceStores;
    public static void main(String[] args) throws IOException{
        t = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < t; tc++) {
            n = Integer.parseInt(br.readLine());
            convenienceStores = new int[n][2];
            StringTokenizer st = new StringTokenizer(br.readLine());
            sr = Integer.parseInt(st.nextToken());
            sc = Integer.parseInt(st.nextToken());
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                convenienceStores[i] = new int[]{a, b};
            }
            st = new StringTokenizer(br.readLine());
            er = Integer.parseInt(st.nextToken());
            ec = Integer.parseInt(st.nextToken());
            answer = bfs();
            System.out.println(answer);
        } 
    }

    public static String bfs() {
        Queue<int[]> q = new LinkedList<int[]>();
        q.add(new int[] {sr, sc});
        Boolean[] visited = new Boolean[convenienceStores.length];
        Arrays.fill(visited, false);
        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int cr = curr[0];
            int cc = curr[1];            
            if (Math.abs(cr - er) + Math.abs(cc - ec) <= 1000) {
                return "happy";
            }
            for (int i = 0; i < convenienceStores.length; i++) {
                if (visited[i] == false) {
                    int nr = convenienceStores[i][0];
                    int nc = convenienceStores[i][1];
                    if (Math.abs(cr - nr) + Math.abs(cc - nc) <= 1000) {
                        visited[i] = true;
                        q.add(new int[] {nr, nc});
                    }
                }
            }
        }
        return "sad";
    }
}