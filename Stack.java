
import java.util.ArrayList;

public class Stack<T> {

    ArrayList<T> arr;

    public Stack() {
        this.arr = new ArrayList<>();
    }

    public void push(T item) {
        arr.add(item);
    }

    public T pop() {
        if (arr.isEmpty()) {
            return null;
        }
        return arr.remove(arr.size() - 1);
    }

    public T peek() {
        if (arr.isEmpty()) {
            return null;
        }
        return arr.get(arr.size() - 1);
    }

    public static void main(String[] args) {
        var stack = new Stack<Anuncio>();

        var anuncio1 = new Anuncio("121212", "title1", "description1");
        var anuncio2 = new Anuncio("sasasa", "title2", "description2");

        stack.push(anuncio1);
        stack.push(anuncio2);
        System.out.println(stack.peek().title);
        System.out.println(stack.pop().title);
        System.out.println(stack.peek().title);
    }
}

/**
 * No sabía la estructura exactamente que debía de tener
 */
public class Anuncio {

    String id;
    String title;
    String description;

    public Anuncio(String id, String title, String description) {
        this.id = id;
        this.title = title;
        this.description = description;
    }
}
