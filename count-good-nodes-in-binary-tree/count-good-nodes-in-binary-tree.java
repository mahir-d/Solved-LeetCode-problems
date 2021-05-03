/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int goodNodes(TreeNode root) {
        if(root == null) return 0;
        
        return dfs(root, root.val);
        
        
    }
    
    public static int dfs(TreeNode root, int max_val){
        
        if (root == null)return 0;
        int count = 0;
        
        if(root.val >= max_val) count++;
        
        count += dfs(root.left, Math.max(max_val, root.val));
        count += dfs(root.right, Math.max(max_val, root.val));
        
        return count;
        
        
        
    }
}