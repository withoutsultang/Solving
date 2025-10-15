import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader I=new BufferedReader(new InputStreamReader(System.in));
        String[] st = I.readLine().split("/");

        int k = Integer.parseInt(st[0]);
        int d = Integer.parseInt(st[1]);
        int a = Integer.parseInt(st[2]);
        String r = "";

        if((k+a < d) || d == 0){
            r = "hasu";
        } else {
            r = "gosu";
        }


        System.out.print(r);
    }
}