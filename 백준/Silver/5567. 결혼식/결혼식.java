import java.io.*;
import java.util.*;

public class Main {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		Queue<Integer> que = new ArrayDeque<>();
		boolean check[] = new boolean[N+1];
		List<Integer> edge[] = new ArrayList[N+1];
		for (int i=1; i<=N; i++) {
			edge[i] = new ArrayList<>();
		}
		
		for (int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			edge[a].add(b);
			edge[b].add(a);
		}
		
		que.add(1);
		check[1] = true;
		int rs = 0;
		for (int i=0; i<2; i++) {
			int size = que.size();
			for (int j=0; j<size; j++) {
				int node = que.poll();
				for (int next_node : edge[node]) {
					if (!check[next_node]) {
						que.add(next_node);
						check[next_node] = true;
						rs += 1;
					}
				}
			}
		}
		System.out.println(rs);
	}

}
