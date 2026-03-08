
import java.io.File;
import java.io.IOException;

public class fileIO {

    public static void main(String[] args) {

        try {
            var isCreated = new File("example.txt").createNewFile();
            if (!isCreated) {
                System.out.println("File already exists.");
            }
        } catch (IOException e) {
            System.err.println("Error creating file: " + e.getMessage());
        }

        File file = new File("example.txt");

        try (var writer = new java.io.FileWriter(file)) {
            writer.write("Hello, World!");
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }

        try (var reader = new java.io.FileInputStream(file)) {
            int c;
            while ((c = reader.read()) != -1) {
                System.out.print((char) c);
            }
        } catch (IOException e) {
            System.err.println("Error reading from file: " + e.getMessage());
        }
    }

}
