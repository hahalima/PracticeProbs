
public class TreeMain {
	public static void main(String[] args) {
		
	}
	
	public Node build123() {
		Node first = new Node(1);
		Node second = new Node(2);
		Node third = new Node(3);
		second.left = first;
		second.right = third;
		return second;
	}
	
	public int size(Node node) {
		if (node == null) return 0;
//		int count = 0;
//		while (true) {
//			if (node.left != null) {
//				count++;
//				node = node.left;
//			}
//			if (node.right != null) {
//				count++;
//				node = node.right;
//			}
//			if (node.left == null || node.right == null) break;
//		}
//		return count;
		return size(node.left) + 1 + size(node.right);
	}
	
	public int maxDepth(Node node) {
		
		if (node == null) return 0;
		else {
			int left = 1 + maxDepth(node.left);
			int right = 1 + maxDepth(node.right);
			if (left < right) return right;
			else return left;
		}
	}
	
	public int minValue(Node node) {
//		while (node.left != null) {
//			node = node.left;
//		}
//		return node.data;
		if (node.left == null) return node.data;
		return minValue(node.left);
	}
	
	public void printTree(Node node) {
		if (node.left != null) printTree(node.left);
		System.out.println(node.data);
		if (node.right != null) printTree(node.right);
	}
	
	public void printPostorder(Node node) {
		if (node.left != null) printPostorder(node.left);
		if (node.right != null) printPostorder(node.right);
		System.out.println(node.data);	
	}
	
	public boolean hasPathSum(Node node, int sum) {
		if (sum == 0 && (node.left == null && node.right == null)) return true;
		else {
			sum = sum - node.data;
			hasPathSum(node.left, sum);
			hasPathSum(node.right,sum);
		}
		return false;
	}

	public void mirror(Node node) {
		Node temp = node.left;
		node.left = node.right;
		node.right = temp;
		if (node.left != null) mirror(node.left);
		if (node.right != null) mirror(node.right); 

	}
}
