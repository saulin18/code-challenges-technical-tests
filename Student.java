import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;
public class Student {
    private String name;
    private double grade;
    private String department;
    private Gender gender;

    public static final double PASSING_GRADE = 70.0;

    public enum Gender {
        MALE, FEMALE
    }

    public Student(String name, double grade, String department, Gender gender) {
        this.name = name;
        this.grade = grade;
        this.department = department;
        this.gender = gender;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getGrade() {
        return grade;
    }

    public void setGrade(double grade) {
        this.grade = grade;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public Gender getGender() {
        return gender;
    }

    public void setGender(Gender gender) {
        this.gender = gender;
    }

    public static Map<String, Double> getAverageGradeByDepartment(Stream<Student> students) {
        var result = students.collect(Collectors.groupingBy(student -> student.department, 
                Collectors.averagingDouble(student -> student.grade)));

        return result;
    }

        public static Map<String, Long> getNumberOfStudentsByDepartment(Stream<Student> students) {
            var result = students.collect(Collectors.groupingBy(student -> student.getDepartment(),
            Collectors.counting()
            ));

            return result;
    }

         public static Map<String, List<String>> getStudentNamesByDepartment(Stream<Student> students) {
            Map<String, List<String>> result = students.collect(Collectors.groupingBy
            (student -> student.getDepartment(),
            Collectors.mapping(student -> student.getName(), Collectors.toList()
            )));

            return result;  
    }

        public static Map<String, Map<Student.Gender, Long>> getTheNumberOfStudentsByGenderForEachDepartment(Stream<Student> students) {

            var result = students.collect(Collectors.groupingBy(student -> student.getDepartment(),
            Collectors.groupingBy(student -> student.getGender(),
            Collectors.counting()
            )));

            return result;
    }
}