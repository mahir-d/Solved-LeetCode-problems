/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuffer sb = new StringBuffer();
        for(String s : dfs(root, new ArrayList<String>())){
            sb.append(s+",");
        }
        
        return sb.toString();
            
    }
    
    public static List<String> dfs(TreeNode root, List<String> currList){
        
        if(root == null){ 
            currList.add("x");
            return currList;
        }
        currList.add(Integer.toString(root.val));
        
        dfs(root.left, currList);
        dfs(root.right, currList);
        
        return currList;
        
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        
        Queue<String>queue = new LinkedList<>();
        for(String ch : data.split(",")){
            queue.add(ch);
        }
        return dfs(queue);
    }
    
    public static TreeNode dfs(Queue<String> queue){
        String currVal = queue.remove();
        if(currVal.equals("x")) return null; 
        
        TreeNode curr = new TreeNode(Integer.parseInt(currVal));
        if(!queue.isEmpty())curr.left =  dfs(queue);
        
        if(!queue.isEmpty())curr.right = dfs(queue);
        
        return curr;
        
        
        
    }
    
    
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));