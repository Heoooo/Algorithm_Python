import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb;
	
	static int L;
	static int N;
	static int rs;
	static int[] tscore, tcal;
	
	static void dfs(int n, int score, int cal) {
		if (cal > L) {
			return;
		}
		
		if (n == N) {
			rs = Integer.max(score, rs);
			return;
		}
		
		dfs(n+1, score+tscore[n], cal+tcal[n]);
		dfs(n+1, score, cal);
		
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for (int i=1; i<=T; i++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			tscore = new int[N];
			tcal = new int[N];
			
			for (int j=0; j<N; j++) {
				st = new StringTokenizer(br.readLine());
				tscore[j] = Integer.parseInt(st.nextToken());
				tcal[j] = Integer.parseInt(st.nextToken());
			}
			
			rs = 0;
			dfs(0,0,0);
			System.out.println("#"+i+" "+rs);
		}
	}

}
