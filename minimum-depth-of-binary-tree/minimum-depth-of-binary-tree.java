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
    public int minDepth(TreeNode root) {
        
        if (root == null) return 0;
        
        Queue<TreeNode> q = new LinkedList<>();
        
        q.add(root);
    
        int i = 0;
        int level = 1;
        while(!q.isEmpty()){
            int len_q = q.size();
            for(int j = 0; j < len_q; j++){
                TreeNode currRoot = q.remove();
                
                if(currRoot.left == null && currRoot.right == null){
                   return level;
                }
                if(currRoot.left != null)q.add(currRoot.left);
                if(currRoot.right != null)q.add(currRoot.right);
            }
            level++;
            
        }
        return 0;
    }
    
    

    
}