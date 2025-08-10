import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb;
	
	static int N;
	static int M;
	static ArrayList<Integer>[] graph;
	static Queue<Integer> que;
	static int[] rs;
	
	static public int bfs(int i) {
		boolean check[] = new boolean[N+1];
		que = new ArrayDeque<>();
		que.add(i);
		check[i] = true;
		int cnt = 0;
		
		while (!que.isEmpty()) {
			int node = que.poll();
			for (int next_node : graph[node]) {
				if (check[next_node] == false) {
					que.add(next_node);
					check[next_node] = true;
					cnt += 1;
				}
			}
		}
		return cnt;
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		graph = new ArrayList[N+1];
		for (int i=0; i<=N; i++) {
			graph[i] = new ArrayList<Integer>();
		}
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph[b].add(a);
		}
		
		rs = new int[N+1];
		int max_value = 0;
		for (int i=1; i<=N; i++) {
			rs[i] = bfs(i);
			max_value = Integer.max(max_value, rs[i]);
		}
		
		for (int i=1; i<=N; i++) {
			if (rs[i] == max_value) {
				System.out.print(i+" ");
			}
		}
	}

}
