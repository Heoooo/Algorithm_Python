import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Solution {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	static boolean check(long num) {
		long t = (long) Math.sqrt(num);
		return t*t == num;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		for (int t=1; t<=T; t++) {
			long N = Long.parseLong(br.readLine());
			long rs = 0;
			while (true) {
				if (N==2) {
					break;
				}
				if (check(N)) {
					N = (long) Math.sqrt(N);
					rs += 1;
				}
				else {
					long tmp = (long) Math.sqrt(N);
					tmp += 1;
					long tp = tmp*tmp;
					rs += tp-N;
					N = tp;
				}
			}
			System.out.println("#"+t+" "+rs);
		}
	}

}