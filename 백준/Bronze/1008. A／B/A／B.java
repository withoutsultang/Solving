import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in);
        String s = sc.nextLine();

        String[] sA = s.split(" ");

        Double a = Double.parseDouble(sA[0]);
        Double b = Double.parseDouble(sA[1]);

        System.out.println(a / b);


    }
}