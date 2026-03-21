import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 1; i < N + 1; i++) {
            int mx = i * 2 - 1;
            String spaces = " ".repeat(N - i);
            String stars = "*".repeat(mx);
            System.out.println(spaces + stars);
        }

        for (int i = N - 1; i > 0; i--) {
            int mx = i * 2 - 1;
            String spaces = " ".repeat(N - i);
            String stars = "*".repeat(mx);
            System.out.println(spaces + stars);
        } 
    }
}