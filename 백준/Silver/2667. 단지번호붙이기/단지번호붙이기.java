import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb;
	
	static class Pair {
		int y;
		int x;
		
		public Pair(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}
	
	public static void main(String[] args) throws IOException {
		Queue<Pair> que = new ArrayDeque<>();
		int dy[] = {0,1,0,-1};
		int dx[] = {1,0,-1,0};
		
		int N = Integer.parseInt(br.readLine());
		int[][] graph = new int[N][N];
		boolean[][] check = new boolean[N][N];
		
		for (int i=0; i<N; i++) {
			String line = br.readLine();
			for (int j=0; j<N; j++) {
				graph[i][j] = line.charAt(j) - '0';
			}
		}
		
		int cnt = 0;
		ArrayList<Integer> rs = new ArrayList<>();
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				if (graph[i][j] == 1 && check[i][j] == false) {
					int tmp = 1;
					check[i][j] = true;
					que.offer(new Pair(i, j));
					while (!que.isEmpty()) {
						Pair cur = que.poll();
						int y = cur.y;
						int x = cur.x;
						for (int k=0;k<4;k++) {
							int ny = y + dy[k];
							int nx = x + dx[k];
							if(ny >= 0 && ny < N && nx >= 0 && nx < N) {
								if (graph[ny][nx]==1 && check[ny][nx] == false) {
									check[ny][nx] = true;
									que.offer(new Pair(ny, nx));
									tmp += 1;
								}
							}
						}					
					}
					rs.add(tmp);
					cnt += 1;
				}
			}
		}
		System.out.println(cnt);
		rs.sort(null);
		for (int i=0; i<rs.size();i++) {
			System.out.println(rs.get(i));
		}
		
	}
}
