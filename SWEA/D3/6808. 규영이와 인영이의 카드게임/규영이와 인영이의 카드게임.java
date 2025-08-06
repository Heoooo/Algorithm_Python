import java.io.*;
import java.util.*;

class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[] js = new int[9];
    static int[] gy = new int[9];
    static int[] arr = new int[9];
    static boolean[] select = new boolean[9];  // 전역 방문 배열
    static int winGy;
    static int winJs;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            winGy = 0;
            winJs = 0;

            st = new StringTokenizer(br.readLine());
            boolean[] check = new boolean[19];

            for (int i = 0; i < 9; i++) {
                js[i] = Integer.parseInt(st.nextToken());
                check[js[i]] = true;
            }

            int idx = 0;
            for (int i = 1; i <= 18; i++) {
                if (!check[i]) {
                    gy[idx++] = i;
                }
            }

            // 방문 배열 초기화
            for (int i = 0; i < 9; i++) {
                select[i] = false;
            }

            permutation(0);

            System.out.println("#" + t + " " + winJs + " " + winGy);
        }
    }

    static void permutation(int n) {
        if (n == 9) {
            int scoreGy = 0;
            int scoreJs = 0;

            for (int i = 0; i < 9; i++) {
                int sum = arr[i] + js[i];
                if (arr[i] > js[i]) {
                    scoreGy += sum;
                } else if (js[i] > arr[i]) {
                    scoreJs += sum;
                }
            }

            if (scoreGy > scoreJs) {
                winGy++;
            } else if (scoreJs > scoreGy) {
                winJs++;
            }
            return;
        }

        for (int i = 0; i < 9; i++) {
            if (!select[i]) {
                select[i] = true;
                arr[n] = gy[i];
                permutation(n + 1);
                select[i] = false;
            }
        }
    }
}