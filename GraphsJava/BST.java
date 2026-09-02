public class TreeNode {
    TreeNode left;
    TreeNode right;
    int data;
    public TreeNode(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

public class BST {
    TreeNode root;
    public BST() {
        this.root = null;
    }

    public void insert(int data){
        if(this.root == null){
            this.root = new TreeNode(data);
            return;
        }
        var current = this.root;
        while(current != null){
            if(data < current.data){
                if(current.left != null){
                current = current.left;
                } else {
                    current.left = new TreeNode(data);
                    return;
                }
            }else{
                if(current.right != null){
                    current = current.right;
                } else {
                    current.right = new TreeNode(data);
                    return;
                }
            }
        }
    }

    public void preOrder(TreeNode TreeNode){
        if(TreeNode == null){
            return;
        }
        System.out.print(TreeNode.data + " ");
        preOrder(TreeNode.left);
        preOrder(TreeNode.right);
    }

    public void inOrder(TreeNode TreeNode){
        if(TreeNode == null){
            return;
        }
        inOrder(TreeNode.left);
        System.out.print(TreeNode.data + " ");
        inOrder(TreeNode.right);
    }

    public void postOrder(TreeNode TreeNode){
        if(TreeNode == null){
            return;
        }
        postOrder(TreeNode.left);
        postOrder(TreeNode.right);
        System.out.print(TreeNode.data + " ");
    }   

    public void doDFS(TreeNode TreeNode){
        if(TreeNode == null){
            return;
        }
        System.out.print(TreeNode.data + " ");
        doDFS(TreeNode.left);
        doDFS(TreeNode.right);
    }

    public void doBFS(TreeNode TreeNode){
        var queue = new Queue<TreeNode>();
        queue.enqueue(TreeNode);
        while(!queue.isEmpty()){
            var size = queue.size();
        
            for(int i = 0; i < size; i++){
                var current = queue.dequeue();
                System.out.print(current.data + " ");
                if(current.left != null){
                    queue.enqueue(current.left);
                }
                if(current.right != null){
                    queue.enqueue(current.right);
                }
            }
            
        }
    }
 
}