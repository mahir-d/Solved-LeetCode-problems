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
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        return dfs(root, null, null);
    }
    
    public static boolean dfs(TreeNode root, Integer max_val, Integer min_val){
        
        if(root == null)return true;
        
        if ((min_val != null && root.val <= min_val) || (max_val != null && root.val >= max_val)) return false;
        
        
        return dfs(root.left, root.val, min_val) && dfs(root.right, max_val, root.val); 
        
    } 
}