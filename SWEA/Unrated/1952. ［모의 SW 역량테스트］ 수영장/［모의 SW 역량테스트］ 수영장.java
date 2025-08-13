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
			int[] nums = new int[4];
			st = new StringTokenizer(br.readLine());
			for (int i=0; i<4; i++) {
				nums[i] = Integer.parseInt(st.nextToken());
			}
			
			int[] use = new int[13];
			st = new StringTokenizer(br.readLine());
			for (int i=1; i<=12; i++) {
				use[i] = Integer.parseInt(st.nextToken());
			}
			
			int[] rs = new int[13];
			for (int i=1; i<=12; i++) {
				int tmp = 0;
				tmp = Integer.min(use[i]*nums[0], nums[1]);
				tmp += rs[i-1];
				
				if (i>=3) {
					tmp = Integer.min(tmp, rs[i-3]+nums[2]);
				}
				rs[i] = tmp;
				//System.out.println(tmp);
			}

			System.out.println("#"+t+" "+Integer.min(rs[12], nums[3]));
			
		}
	}

}
