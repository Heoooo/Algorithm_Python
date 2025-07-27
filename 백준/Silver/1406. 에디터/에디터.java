import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException {
		Stack<Character> stack1 = new Stack<>();
		Stack<Character> stack2 = new Stack<>();
		String line = br.readLine();
		for (int i=0; i<line.length();i++) {
			stack1.push(line.charAt(i));
		}
		
		int T = Integer.parseInt(br.readLine());
		for (int i=0; i<T; i++) {
			StringTokenizer tokens = new StringTokenizer(br.readLine());
			String cmd = tokens.nextToken();
			
			if (cmd.equals("L")) {
				if (!stack1.isEmpty()) {
					stack2.push(stack1.pop());
				}
			}
			else if (cmd.equals("D")) {
				if (!stack2.isEmpty()) {
					stack1.push(stack2.pop());
				}
			}
			else if (cmd.equals("B")) {
				if (!stack1.isEmpty()) {
					stack1.pop();
				}
			}
			else {
				Character x = tokens.nextToken().charAt(0);
				stack1.push(x);
			}
		}
		
		sb = new StringBuilder();
		while (!stack1.isEmpty()) {
			stack2.push(stack1.pop());
		}
		while (!stack2.isEmpty()) {
			sb.append(stack2.pop());
	
		}
		System.out.println(sb);
	}
}
