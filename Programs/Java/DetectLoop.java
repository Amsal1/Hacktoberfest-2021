class DetectLoop
{
    static class Node
    {
        int data;
        Node next;

        Node(int data)
        {
            this.data = data;
        }
    }

    public static void main(String[] args)
    {
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);
        Node node5 = new Node(5);
        Node node6 = new Node(6);
        Node node7 = new Node(7);
        Node node8 = new Node(8);


        node1.next=node2;       
        node2.next=node3;
        node3.next=node4;
        node4.next=node5;
        node5.next=node6;      
        node6.next=node7;
        node7.next=node8;
        node8.next=null;

        System.out.println(hasLoop(node1));

    }

    private static boolean hasLoop(Node node)
    {
        if(node==null)
            return false;

        Node low = node ;
        Node high = node;
        while(high!=null && high.next!=null)
        {
            low=low.next;
            high = high.next.next;
            if(low==high)
            {
                return true;
            }
        }
        return false;
    }
}
