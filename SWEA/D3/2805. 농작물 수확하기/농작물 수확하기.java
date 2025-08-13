import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for (int t=1; t<=T; t++) {
			int N = Integer.parseInt(br.readLine());
			int[][] graph = new int[N][N];
			
			for (int i=0; i<N; i++) {
				String line = br.readLine();
				for (int j=0; j<N; j++) {
					graph[i][j] = line.charAt(j) - '0';
				}
			}
			
			int rs = 0;
			int left = N/2;
			int right = N/2;
			for (int i=0; i<=N/2; i++) {
				for (int j=left; j<=right; j++) {
					rs += graph[i][j];
				}
				left -= 1;
				right += 1;
			}
			
			left += 2;
			right -= 2;
			for (int i=N/2+1; i<N; i++) {
				for (int j=left; j<=right; j++) {
					rs += graph[i][j];
				}
				left += 1;
				right -= 1;
			}
			System.out.println("#"+t+" "+rs);
			
		}
	}

}