public class Node {
    int value;
    Node next;

    public Node(int val, Node next){
        this.value = val;
        this.next = next;
    }
}
public class SimpleLL {
    Node head;

    public SimpleLL(){
        this.head  = null;
    }

    public Node find(int value){
        var curr = head;
        if(head == null) return null;
        if(curr.value == value) return curr;
        while (curr.next != null) {
            if(curr.next.value == value){
                return curr.next;
            } else {
                curr = curr.next;
            }
        }
        return null;
    }

    public void insert(Node node){
        if(this.head == null){
            this.head = node;
            return;
        }
        var curr = this.head;
        while (curr.next != null) {
            curr = curr.next;
        }
        curr.next = node;
        return;
    }

       public void delete(Node node){
        if(this.head == null){
            return;
        }
        var curr = this.head;

        if(this.head == node){
            this.head = this.head.next;
            return;
        }

        while (curr.next != null) {
            if(curr.next.equals(node)){
                curr.next = curr.next.next;
            } else{
                curr = curr.next;
            }
        }
        return;
    }
}
