
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;
import java.util.Queue;

public class stackQueues {

    public static void main(String[] args) {
        var myLinkedL = new LinkedList<Student>();

        var student1 = new Student("121212", 100, List.of("mat", "prog"));
        var student2 = new Student("sasasa", 55, List.of("mat", "prog", "discret"));

        myLinkedL.add(student1);
        myLinkedL.add(student2);
        System.out.println(myLinkedL.peek());
        System.out.println(myLinkedL.offer(student2));
        System.out.println(myLinkedL.poll());
    }

    private static class Student {

        String id;
        int score;
        List<String> classes;

        public Student(String id, int i, List<String> classes) {
            this.id = id;
            this.score = i;
            this.classes = classes;
        }

    }

}
