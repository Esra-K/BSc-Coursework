package Q1;

    public class BST<T extends Comparable> {
        private BSTNode root;
        private int size;
        public class BSTNode
        {
            // Local variables
            public T data;			// The data in the node
            BSTNode left;	// Pointer to the left child
            BSTNode right;	// Pointer to the right child

            public BSTNode(T elem)
            {
                data = elem;
                left = null;
                right = null;
            }
            public BSTNode(T elem, BSTNode lt, BSTNode rt)
            {
                data = elem;
                left = lt;
                right = rt;
            }

            public BSTNode getLeft() {
                return left;
            }

            public BSTNode getRight() {
                return right;
            }

            public T getData() {
                return data;
            }

            public void setData(T data) {
                this.data = data;
            }

            public void setLeft(BSTNode left) {
                this.left = left;
            }

            public void setRight(BSTNode right) {
                this.right = right;
            }
        }

        public BST() {
            root = null;
            size = 0;
        }
        public void add(T data) {
            if (data == null) {
                throw new IllegalArgumentException("Data cannot be null");
            }
            if (root == null) {
                root = new BSTNode(data);
                size++;
            } else {
                add(data, root);
            }
        }
        private void add(T data, BSTNode cur) {
            int comparison = data.compareTo(cur.getData());
            if (comparison > 0) {
                if (cur.getRight() == null) {
                    cur.setRight(new BSTNode(data));
                    size++;
                } else {
                    add(data, cur.getRight());
                }
            } else if (comparison < 0) {
                if (cur.getLeft() == null) {
                    cur.setLeft(new BSTNode(data));
                    size++;
                } else {
                    add(data, cur.getLeft());
                }
            }
        }

        public boolean contains(T data) {
            if (data == null) {
                throw new IllegalArgumentException("Data cannot be null");
            }
            if (root == null) {
                return false;
            }
            return find(data, root) != null;

        }

        public T find(T data, BSTNode cur) {
            int comparison = data.compareTo(cur.getData());
            if (comparison > 0) {
                if (cur.getRight() == null) {
                    return null;
                } else {
                    return (T)find(data, cur.getRight());
                }
            } else if (comparison < 0) {
                if (cur.getLeft() == null) {
                    return null;
                } else {
                    return (T)find(data, cur.getLeft());
                }
            } else {
                return cur.getData();
            }
        }
        public int size() {
            return size;
        }

        public T getMinElement() throws IllegalStateException{
            if (root == null) throw new IllegalStateException("Exception");
            return min(root);
        }
        private T min(BSTNode x){
            if(x.left == null) return (T)x.data;
            else               return min(x.left);
        }

        public T getMaxElement() throws IllegalStateException{
            if (root == null) throw new IllegalStateException("Exception");
            return max(root);
        }
        private T max(BSTNode x){
            if(x.right == null) return (T)x.data;
            else               return max(x.right);
        }
    }