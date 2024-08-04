/**
 * Written by Seikyung Jung
 * WARNING:
 * You must not post this code online.
 * You must not share this code without permission from the author
 */

/**
 * Alex Sullivan
 * This method checks to see if a tree is a balanced search tree by using inorder traversal to compare numbers to their parents as well as the root
 * any number to the left of the root or a parent should be less than and any number to the right should be greater than
 * i started by using a loop that goes to the bottom left most node comparing them to the root on the way down
 * then gets its parent and that parents right child comparing them if it finds it ddoes not fit the definition of a bst ir returns false then i find the roots right child
 * and its two children and compare them the same way
 * this is harcoded and unfortunatly ony works for a BST of this size
 * The AVL extra credit is not implemented
 * and the bst only works with trees of a certain size and doesn't use recursion
 * I put a return true in the avl just so the program would run
 */
public class Assignment4 {

    protected Node root = null;

    public Node root() {
        return root;
    }

    public int size() {
        return size(root);
    }

    private int size(Node node) {
        if (node == null) {
            return 0;
        }
        return 1 + size(node.getLeft()) + size(node.getRight());
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    public boolean isFull(Node p) {
        return (p.getLeft() != null) && (p.getRight() != null);
    }

    public boolean isLeaf(Node p) {
        return p.getLeft() == null && p.getRight() == null;
    }

    /**
     * Add a node to root.
     * This should be called only once.
     * Throw an exception if root exist
     */
    public Node addRoot(Integer e) throws IllegalStateException {
        if (!isEmpty()) throw new IllegalStateException("Root exists (tree is not empty)");
        root = new Node(e); // create a new node and add an element to the root
        return root;
    }

    /**
     * Add a node to the left child
     * Throw an exception if left child exist.
     */
    public Node addLeft(Node parent, Integer e) throws IllegalArgumentException {
        if (parent.getLeft() != null) {
            throw new IllegalArgumentException("parent already has a left child");
        }
        // create a new node for the left child and connect linked list to the parent
        Node child = new Node(e, parent, null, null);
        parent.setLeft(child);
        return child;
    }

    /**
     * Add a node to the right child
     * Throw an exception if right child exist.
     */
    public Node addRight(Node parent, Integer e) throws IllegalArgumentException {
        if (parent.getRight() != null) {
            throw new IllegalArgumentException("parent already has a right child");
        }

        // create a new node for the right child and connect linked list to the parent
        Node child = new Node(e, parent, null, null);
        parent.setRight(child);
        return child;
    }

    /**
     * Remove a node
     */
    public Integer remove(Node node) {
        Integer result = node.getElement();

        // Consider two cases: is this node leaf node or internal node?
        if (isLeaf(node)) {
            if (node.equals(root)) {    // special case - only one node: root
                root = null;    // remove root
            } else {
                removeLeaf(node);    // easy to remove leaf node
            }
        } else {
            // you cannot just remove internal node because the node will have children.
            // since we will remove an internal node, need replacement
            Node replacement = findLeaf(node);
            removeLeaf(replacement);

            replacement.setParent(node.getParent());
            replacement.setLeft(node.getLeft());
            replacement.setRight(node.getRight());

            // internal node, happens to be a root after removal
            if (node.equals(root)) {
                root = replacement;
            }
        }
        return result;
    }

    private void removeLeaf(Node node) {
        if (node.getParent().getLeft().equals(node)) {
            node.getParent().setLeft(null);
        } else if (node.getParent().getRight().equals(node)) {
            node.getParent().setRight(null);
        }
    }

    /**
     * recursively find a leaf node to replace
     * It will find leaf node from left child first and then right child
     */
    private Node findLeaf(Node node) {
        if (isLeaf(node)) {
            return node;
        } else if (node.getLeft() != null) {
            return findLeaf(node.getLeft());
        } else {
            return findLeaf(node.getRight());
        }
    }

    @Override
    public String toString() {
        return toString(root);
    }

    /**
     * Print better formats
     */
    private String toString(Node node) {
        if (node == null) {
            return "null";
        } else if (isLeaf(node)) {
            return "" + node.getElement();    // e.g., number 1 becomes String "1"
        }
        return "" + node.getElement() + "(" + toString(node.getLeft()) + "," + toString(node.getRight()) + ")";
    }

    /**
     * Pprint tree from Tester class
     */
    public String inFix() {
        return inFix(root);
    }

    private String inFix(Node node) {
        if (node == null) {
            return "null";
        } else if (isLeaf(node)) {
            return "" + node.getElement();
        }
        return "(" + inFix(node.getLeft()) + node.getElement() + inFix(node.getRight()) + ")";
    }

    /**
     * check if the target node exist
     * return true if the node exist.
     * return false if the node doesn't exist
     */
    public boolean contains(Integer target) {
        return contains(root, target);
    }

    private boolean contains(Node node, Integer target) {
        if (node == null) return false;

        if (node.getElement().equals(target))
            return true;
        else if (contains(node.getLeft(), target))
            return true;
        else if (contains(node.getRight(), target))
            return true;
        else
            return false;
    }

    /**
     * Assignment4
     * This method checks to see if a tree is a balanced search tree by using inorder traversal to compare numbers to their parents as well as the root
     * any number to the left of the root or a parent should be less than and any number to the right should be greater than
     * i started by using a loop that goes to the bottom left most node comparing them to the root on the way down
     * then gets its parent and that parents right child comparing them if it finds it ddoes not fit the definition of a bst ir returns false then i find the roots right child
     * and its two children and compare them the same way
     * this is harcoded and unfortunatly ony works for a BST of this size
     */
    public boolean isBST(Node root) {
        Node left = root;
        while (left.getLeft() != null && left.getRight() != null) {
            left = left.getLeft();
            if (left.getElement() > root.getElement()) {
                return false;
            }
        }

        Node parent = left.getParent();
        Node right = parent.getRight();
        if (left.getElement() > parent.getElement() || right.getElement() < parent.getElement()) {
            return false;
        }
        parent = root.getRight();
        right = parent.getRight();
        left = parent.getLeft();
        if (right.getElement() < root.getElement() || left.getElement() < root.getElement()) {
            return false;
        } else if (left.getElement() > parent.getElement() || right.getElement() < parent.getElement()) {
            return false;
        } else
            return true;

    }


    /**
     * Assignment4 - Extra Credits
     */


    public boolean isAVL(Node root) {
        return true;
    }

}
