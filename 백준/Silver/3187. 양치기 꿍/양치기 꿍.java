import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Node{
	int y;
	int x;
	public Node(int y, int x) {
		this.y = y;
		this.x = x;
	}
}

public class Main {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer tokens;
	static StringBuilder sb;
	static char[][] graph;
	static boolean[][] check;
	static int[] dy = {0,1,0,-1};
	static int[] dx = {1,0,-1,0};
	static int R;
	static int C;
	static int V;
	static int K;
	
	
	static void bfs(Integer y, Integer x) {
		Queue<Node> que = new LinkedList<>();
		que.offer(new Node(y, x));
		check[y][x] = true;
		int v = 0;
		int k = 0;
		while (!que.isEmpty()) {
			Node node = que.poll();
			if (graph[node.y][node.x] == 'v') {
				v++;
			}
			else if (graph[node.y][node.x] == 'k') {
				k++;
			}
			for (int i=0; i<4; i++) {
				int ny = node.y + dy[i];
				int nx = node.x + dx[i];
				if ((0<=ny && ny < R) && (0<=nx && nx <C)) {
					if ((graph[ny][nx] != '#') && (check[ny][nx] == false)) {
						que.offer(new Node(ny, nx));
						check[ny][nx] = true;
					}
				}
			}
		}
		if (v >= k) {
			k = 0;
		}
		else {
			v = 0;
		}
		K += k;
		V += v;
	}
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		tokens = new StringTokenizer(br.readLine());
		R = Integer.parseInt(tokens.nextToken());
		C = Integer.parseInt(tokens.nextToken());
		graph = new char[R][C];
		check = new boolean[R][C];
		for (int i=0; i<R; i++) {
			String line = br.readLine();
			for (int j=0; j<C; j++) {
				graph[i][j] = line.charAt(j);
			}
		}
		
		V = 0;
		K = 0;
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				if ((graph[i][j] != '#') && (check[i][j] == false)) {
					bfs(i, j);
				}
			}
		}
		System.out.print(K+" "+V);
	}

}
