import java.io.*;
import java.util.*;

class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] graph = new int[100][100];
    static int[] dx = {1, -1};

    public static void main(String[] args) throws IOException {

        for (int t = 1; t <= 10; t++) {
            int tc = Integer.parseInt(br.readLine());

            for (int i = 0; i < 100; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 100; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int endX = 0;
            for (int i = 0; i < 100; i++) {
                if (graph[99][i] == 2) {
                    endX = i;
                    break;
                }
            }

            int y = 99;
            int x = endX;

            while (y > 0) {
                boolean moved = false;

                for (int dir = 0; dir < 2; dir++) {
                    int nx = x + dx[dir];
                    if (nx >= 0 && nx < 100 && graph[y][nx] == 1) {
                        while (nx >= 0 && nx < 100 && graph[y][nx] == 1) {
                            graph[y][nx] = 0;
                            x = nx;
                            nx = x + dx[dir];
                        }
                        moved = true;
                        break;
                    }
                }

                if (!moved && y - 1 >= 0 && graph[y - 1][x] == 1) {
                    y--;
                }
            }
            System.out.println("#" + t + " " + x);
        }
    }
}
