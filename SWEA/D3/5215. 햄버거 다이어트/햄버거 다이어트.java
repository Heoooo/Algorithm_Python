import java.io.*;
import java.util.*;
 
public class Solution {
   
  static BufferedReader br;
  static StringBuilder sb = new StringBuilder();
  static final int SCORE = 0, CALO = 1;
  static int T, N, L;
  static int[][] food = new int[22][2];
 
  static int run() {
    int[] dp = new int[L + 1];
    for (int i = 0; i < N; ++i) {
      for (int c = L; c >= food[i][CALO]; --c) {
        dp[c] = Math.max(dp[c], dp[c - food[i][CALO]] + food[i][SCORE]);
      }
    }
    return dp[L];
  }
 
  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
 
    T = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= T; ++tc) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      N = Integer.parseInt(st.nextToken());
      L = Integer.parseInt(st.nextToken());
 
      for (int i = 0; i < N; ++i) {
        st = new StringTokenizer(br.readLine());
        food[i][SCORE] = Integer.parseInt(st.nextToken());
        food[i][CALO] = Integer.parseInt(st.nextToken());
      }
      sb.append('#').append(tc).append(' ').append(run()).append('\n');
    }
    System.out.print(sb);
  }
}