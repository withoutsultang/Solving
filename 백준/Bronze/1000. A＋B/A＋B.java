import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in);
        String s = sc.nextLine();

        String[] sA = s.split(" ");

        int a = Integer.parseInt(sA[0]);
        int b = Integer.parseInt(sA[1]);

        System.out.println(a + b);


    }
}