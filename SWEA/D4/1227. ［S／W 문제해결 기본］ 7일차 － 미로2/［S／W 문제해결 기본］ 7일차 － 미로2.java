import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    static int[] dy = {0, 1, 0, -1};
    static int[] dx = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int t = 1; t <= 10; t++) {
            int tc = Integer.parseInt(br.readLine());
            int[][] graph = new int[100][100];

            int startY = 0, startX = 0;

            for (int i = 0; i < 100; i++) {
                String line = br.readLine().trim();
                for (int j = 0; j < 100; j++) {
                    graph[i][j] = line.charAt(j) - '0';
                    if (graph[i][j] == 2) {
                        startY = i;
                        startX = j;
                    }
                }
            }

            boolean flag = false;
            Queue<int[]> que = new LinkedList<>();
            que.offer(new int[]{startY, startX});

            while (!que.isEmpty()) {
                int[] cur = que.poll();
                int y = cur[0];
                int x = cur[1];
                graph[y][x] = 1;

                for (int i = 0; i < 4; i++) {
                    int ny = y + dy[i];
                    int nx = x + dx[i];

                    if (ny >= 0 && ny < 100 && nx >= 0 && nx < 100) {
                        if (graph[ny][nx] == 0) {
                            que.offer(new int[]{ny, nx});
                        } else if (graph[ny][nx] == 3) {
                            flag = true;
                            break;
                        }
                    }
                }
                if (flag) break;
            }

            if (flag) {
                System.out.println("#" + t + " 1");
            } else {
                System.out.println("#" + t + " 0");
            }
        }
    }
}