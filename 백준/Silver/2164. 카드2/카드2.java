import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException {
		Queue<Integer> que = new ArrayDeque<>();
		int N = Integer.parseInt(br.readLine());
		for (int i=1; i<=N; i++) {
			que.offer(i);
		}
		
		int t = 0;
		while (true) {
			if (que.size() == 1) {
				break;
			}
			if (t % 2 == 0) {
				que.poll();
			}
			else {
				que.offer(que.poll());
			}
			t += 1;
		}
		System.out.println(que.peek());
	}
}
