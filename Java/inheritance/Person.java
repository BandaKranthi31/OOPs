public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void introduce(){
        System.out.println("Hi , Iam " + name + "and iam " + age + "Years ");
    }
}

class Student extends Person {
   private String school;

    public Student(String name, int age, String school) {
        super(name, age);
        this.school = school;
    }

    void study(){
        System.out.println("Iam studing in " + school);
    }
}
