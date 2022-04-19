static node splay(node root, int key)
{
    // Base cases: root is null or
    // key is present at root
    if (root == null || root.key == key)
        return root;

    // Key lies in left subtree
    if (root.key > key)
    {
        // Key is not in tree, we are done
        if (root.left == null) return root;

        // Zig-Zig (Left Left)
        if (root.left.key > key)
        {
            // First recursively bring the
            // key as root of left-left
            root.left.left = splay(root.left.left, key);

            // Do first rotation for root,
            // second rotation is done after else
            root = rightRotate(root);
        }

        // Zig-Zag (Left Right)
        else if (root.left.key < key)
        {
            // First recursively bring
            // the key as root of left-right
            root.left.right = splay(root.left.right, key);

            // Do first rotation for root.left
            if (root.left.right != null)
                root.left = leftRotate(root.left);
        }

        // Do second rotation for root
//         if (root.left == null)
//             return root;
//         else
//             return rightRotate(root);

        return (root.left == null) ?
                              root : rightRotate(root);
    }
    else // Key lies in right subtree
    {
        // Key is not in tree, we are done
        if (root.right == null) return root;

        // Zag-Zig (Right Left)
        if (root.right.key > key)
        {
            // Bring the key as root of right-left
            root.right.left = splay(root.right.left, key);

            // Do first rotation for root.right
            if (root.right.left != null)
                root.right = rightRotate(root.right);
        }
        else if (root.right.key < key)// Zag-Zag (Right Right)
        {
            // Bring the key as root of
            // right-right and do first rotation
            root.right.right = splay(root.right.right, key);
            root = leftRotate(root);
        }

        // Do second rotation for root
        return (root.right == null) ?
                               root : leftRotate(root);
    }
}