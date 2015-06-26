import java.util.ArrayList;
import java.util.List;


public class Arrays {
	public static void main(String[] args) {
		List<ArrayList<Integer>> A = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> row1 = new ArrayList<Integer>();
		row1.add(1);
		row1.add(2);
		ArrayList<Integer> row2 = new ArrayList<Integer>();
		row2.add(3);
		row2.add(4);
		ArrayList<Integer> row3 = new ArrayList<Integer>();
		row3.add(5);
		row3.add(6);
		A.add(row1);
		A.add(row2);
		A.add(row3);
		
		ArrayList<Integer> ans = spiralOrder(A);
		System.out.println(ans.toString());
	}
	
	public static ArrayList<Integer> spiralOrder(List<ArrayList<Integer>> A) {
		 ArrayList<Integer> result = new ArrayList<Integer>();
		 // Populate result;
       int top = 0; 
       int bot = A.size()-1;
       int left = 0;
       int right = A.size()-1;
       
       while (top <= bot && left <= right) {
               for (int i=left; i<= right; i++) {
                   result.add((A.get(top).get(i)));
               }
               top++;
               
               for (int i=top; i<=bot; i++) {
                   result.add(A.get(i).get(right));
               }
               right--;
               
               for (int i = right; i>=left ; i--) {
                   result.add(A.get(bot).get(i));
               }
               bot--;
               
               for (int i = bot; i>=top; i--) {
                   result.add(A.get(i).get(left));
               }
               left++;
       }
		 return result;
	}
}
