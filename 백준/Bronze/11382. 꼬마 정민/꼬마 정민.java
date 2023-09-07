import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");

        long d = Long.parseLong(s[0]);
        long e = Long.parseLong(s[1]);
        long f = Long.parseLong(s[2]);
        
        System.out.println(d + e + f);


    }
}