
import java.util.Stack;

class AllTraversal
{
    static class Node
    {
        int data ;
        Node left , right ;

        Node(int data)
        {
            this.data = data ;
            left = right = null ;
        }
    }

    static Node root ;

    public static void main(String[] args)
    {
        root = new Node(1);

        root.left = new Node(2);
        root.right = new Node(3);

        root.left.left = new Node(4);
        root.left.right = new Node(5);

        root.right.left = new Node(6);
        root.right.right = new Node(7);

        preOrderRecursive(root);
        System.out.println();
        preOrderIterative(root);
        
        System.out.println();
        
        inOrderRecursive(root);
        System.out.println();
        inOrderIterative(root);
        
        System.out.println();
        
        postOrderRecursive(root);
        System.out.println();
        postOrderIterative(root);

    }

    private static void preOrderRecursive(Node root)
    {
        if(root == null)
            return;

        System.out.print(root.data + " ");
        preOrderRecursive(root.left);
        preOrderRecursive(root.right);
    }



    private static void preOrderIterative(Node root)
    {
        Stack<Node> stack = new Stack<>();
        stack.push(root);

        while(!stack.isEmpty())
        {
            Node temp = stack.pop();
            System.out.print(temp.data + " ");

            if(temp.right != null)
                stack.push(temp.right);

            if(temp.left != null)
                stack.push(temp.left);

        }

    }



    private static void inOrderRecursive(Node root)
    {
        if(root == null)
            return;

        inOrderRecursive(root.left);
        System.out.print(root.data + " ");
        inOrderRecursive(root.right);
    }


    private static void inOrderIterative(Node root)
    {
        Stack<Node> stack = new Stack<>();
        Node curr = root ;

        while(!stack.isEmpty() || curr != null)
        {
            if(curr!=null)
            {
                stack.push(curr);
                curr = curr.left;
            }
            else
            {
                curr= stack.pop();
                System.out.print(curr.data + " ");

                curr = curr.right ;
            }
        }
    }





    private static void postOrderRecursive(Node root)
    {
        if(root == null)
            return;

        postOrderRecursive(root.left);
        postOrderRecursive(root.right);
        System.out.print(root.data + " ");
    }



    private static void postOrderIterative(Node root)
    {
        Stack<Node> stack = new Stack<>();
        stack.push(root);

        Stack<Integer> dataStore = new Stack<>();

        while(!stack.isEmpty())
        {
            Node temp = stack.pop();
            dataStore.push(temp.data);

            if(temp.left != null)
                stack.push(temp.left);

            if(temp.right != null)
                stack.push(temp.right);

        }
        while(!dataStore.isEmpty())
        {
            System.out.print(dataStore.pop() + " ");
        }
    }

}
