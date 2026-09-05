import java.util.LinkedList;
import java.util.List;

class TreeNode {
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

    public void insert(int data) {
        if (this.root == null) {
            this.root = new TreeNode(data);
            return;
        }
        var current = this.root;
        while (current != null) {
            if (data < current.data) {
                if (current.left != null) {
                    current = current.left;
                } else {
                    current.left = new TreeNode(data);
                    return;
                }
            } else {
                if (current.right != null) {
                    current = current.right;
                } else {
                    current.right = new TreeNode(data);
                    return;
                }
            }
        }
    }

    public void preOrder(TreeNode TreeNode) {
        if (TreeNode == null) {
            return;
        }
        System.out.print(TreeNode.data + " ");
        preOrder(TreeNode.left);
        preOrder(TreeNode.right);
    }

    public void inOrder(TreeNode TreeNode) {
        if (TreeNode == null) {
            return;
        }
        inOrder(TreeNode.left);
        System.out.print(TreeNode.data + " ");
        inOrder(TreeNode.right);
    }

    public void postOrder(TreeNode TreeNode) {
        if (TreeNode == null) {
            return;
        }
        postOrder(TreeNode.left);
        postOrder(TreeNode.right);
        System.out.print(TreeNode.data + " ");
    }

    public void doDFS(TreeNode TreeNode) {
        if (TreeNode == null) {
            return;
        }
        System.out.print(TreeNode.data + " ");
        doDFS(TreeNode.left);
        doDFS(TreeNode.right);
    }

    public void doBFS(TreeNode TreeNode) {
        var queue = new LinkedList<TreeNode>();
        queue.add(TreeNode);
        while (!queue.isEmpty()) {
            var size = queue.size();

            for (int i = 0; i < size; i++) {
                var current = queue.pop();
                System.out.print(current.data + " ");
                if (current.left != null) {
                    queue.add(current.left);
                }
                if (current.right != null) {
                    queue.add(current.right);
                }
            }

        }
    }

    public void delete(int data) {

        var root = this.root;

        TreeNode parent = null;
        while (root != null) {

            if (root.data == data) {
                var isLeaf = root.left == null && root.right == null;
                var hasOneChild = root.left == null || root.right == null;
                var hasTwoChildren = root.left != null && root.right != null;

                var isRootOfTree = this.root == root;

                if (isLeaf) {
                    if (isRootOfTree) {
                        this.root = null;
                    } else if (parent.left == root) {
                        parent.left = null;
                    } else {
                        parent.right = null;
                    }
                    return;
                } else if (hasOneChild) {
                    TreeNode child = root.left != null ? root.left : root.right;
                    if (isRootOfTree) {
                        this.root = child;
                    } else if (parent.left == root) {
                        parent.left = child;
                    } else {
                        parent.right = child;
                    }
                    return;
                } else if (hasTwoChildren) {
                    var succesorAndParent = findSuccessor(root);
                    var successor = succesorAndParent.get(0);
                    var parentOfSuccessor = succesorAndParent.get(1);
                    var succesorIsLeaf = successor.left == null && successor.right == null;
                    var succesorHasOneChild = successor.left == null || successor.right == null;

                    root.data = successor.data;

                    if (succesorIsLeaf) {
                        if (parentOfSuccessor.left == successor) {
                            parentOfSuccessor.left = null;
                        } else {
                            parentOfSuccessor.right = null;
                        }
                    } else if (succesorHasOneChild) {
                        if (parentOfSuccessor.left == successor) {
                            parentOfSuccessor.left = successor.left != null ? successor.left
                                    : successor.right;
                        } else {
                            parentOfSuccessor.right = successor.left != null ? successor.left
                                    : successor.right;
                        }
                    }
                    return;
                }
            }

            if (data < root.data) {

                if (root.left != null) {
                    parent = root;
                    root = root.left;

                } else {
                    return;
                }
            } else {

                if (root.right != null) {
                    parent = root;
                    root = root.right;

                } else {
                    return;
                }
            }
        }

    }

    /*
     * Maximum in the left subtree
     */
    public List<TreeNode> findLeftSuccesor(TreeNode node) {
        assert node.left != null;

        var current = node.left;
        var parent = node;
        if (current.right == null)
            return List.of(current, parent);

        while (current.right != null) {
            parent = current;
            current = current.right;
        }

        return List.of(current, parent);
    }

    /*
     * Minimum in the right subtree
     */
    public List<TreeNode> findRightSuccesor(TreeNode node) {
        assert node.right != null;
        var current = node.right;
        var parent = node;

        if (current.left == null)
            return List.of(current, parent);

        while (current.left != null) {
            parent = current;
            current = current.left;
        }

        return List.of(current, parent);

    }

    public List<TreeNode> findSuccessor(TreeNode node) {
        if (node.right != null) {
            return findRightSuccesor(node);
        } else {
            return findLeftSuccesor(node);
        }
    }
}
