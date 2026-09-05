
class Node {
    Node next;
    Node prev;
    int data;

    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

public class LL {
    Node head;
    Node tail;

    public LL() {
        this.head = null;
        this.tail = null;
    }

    public void insert(int data) {

        if (this.head == null) {
            this.head = new Node(data);
            this.tail = this.head;
            this.head.prev = this.tail;
            this.tail.next = this.head;
            return;
        }

        var newNode = new Node(data);
        newNode.next = this.head;
        this.head.prev = newNode;
        this.tail.next = newNode;
        newNode.prev = this.tail;
        this.tail = newNode;

        return;
    }

    public Node getFirst() {
        return this.head;
    }

    public Node getLast() {
        return this.tail;
    }

    public Node popLeft() {

        if (this.head == null) {
            return null;
        }

        if (this.head == this.tail) {
            var node = this.head;
            this.head = null;
            this.tail = null;
            return node;
        }

        var node = this.head;
        this.head = node.next;
        this.head.prev = this.tail;
        this.tail.next = this.head;
        return node;
    }

    public Node popRight() {

        if (this.tail == null) {
            return null;
        }

        if (this.tail == this.head) {
            var node = this.tail;
            this.tail = null;
            this.head = null;
            return node;
        }

        var node = this.tail;
        this.tail = node.prev;
        this.tail.next = this.head;
        this.head.prev = this.tail;

        return node;
    }

    public Node find(int data) {
        if (this.head == null) {
            return null;
        }

        var head = this.head;
        do {
            if (head.data == data) {
                return head;
            }
            head = head.next;
        } while (head != this.head);
        return null;
    }

    public void print() {
        var head = this.head;
        do {
            System.out.print(head.data + " ");
            head = head.next;
        } while (head != this.head);
        System.out.println();
    }
}

class Main {
    public static void main(String[] args) {
        
    }
}
