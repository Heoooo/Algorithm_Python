import java.io.*;
import java.util.*;
 
public class Solution {
    static int N, W, H, min;
    static int[][] arr, map;
    static int[] dy = { -1, 0, 1, 0 };
    static int[] dx = { 0, 1, 0, -1 };
 
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());
            min = Integer.MAX_VALUE;
            arr = new int[H][W];
            for (int i = 0; i < H; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < W; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            map = new int[H][W];
            pick(0, arr);
            System.out.println("#"+t+" "+min);
        } 
    }
 
    private static void pick(int depth, int[][] arr) {
        check(arr);
        if (depth == N) {
            return;
        }
 
        map = new int[H][W];
        for (int i = 0; i < W; i++) {
            for (int k = 0; k < map.length; k++) {
                System.arraycopy(arr[k], 0, map[k], 0, arr[k].length);
            }
            for (int j = 0; j < H; j++) {
                if (map[j][i] != 0) {
                    bomb(map[j][i], j, i);
                    zero();
                    pick(depth+1, map);
                    break;
                }
            }
        }
    }
 
    private static void bomb(int V, int row, int col) {
        map[row][col] = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 1; j < V; j++) {
                int nr = row + j * dy[i];
                int nc = col + j * dx[i];
                if (nr >= 0 && nr < H && nc >= 0 && nc < W && map[nr][nc] != 0) {
                    bomb(map[nr][nc], nr, nc);
                }
            }
        }
    }
 
    private static void zero() {
        for (int i = 0; i < W; i++) {
            for (int j = H - 1; j >= 1; j--) {
                if (map[j][i] == 0) {
                    for (int k = j-1; k >= 0; k--) {
                        if (map[k][i] != 0) {
                            map[j][i] = map[k][i];
                            map[k][i] = 0;
                            break;
                        }
                    }
                }
            }
        }
    }
    private static void check(int[][] map2) {
        int cnt = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (map2[i][j] != 0)
                    cnt++;
            }
        }
        if (min > cnt)
            min = cnt;
         
    }
}