class ReverseLinkedList
{
    static class Node
    {
        int data;
        Node next;

        Node(int data)
        {
            this.data = data ;
        }
    }

    public static void main(String[] args)
    {
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);
        Node node4 = new Node(4);


        node1.next=node2;
        node2.next=node3;
        node3.next=node4;
        node4.next=null;

        printList(reverseIterative(node1));
    }

    public static Node reverseIterative(Node node)
    {
        Node prev = null;
        Node current = node;
        Node next = null;

            while(current!=null)
            {
                next = current.next ;
                current.next = prev ;
                prev = current;
                current = next ;

            }

        node = prev;
        return node;
    }

    static void printList(Node node)
    {
        while(node!=null)
        {
            System.out.println(node.data + " ");
            node = node.next;
        }
    }
}
