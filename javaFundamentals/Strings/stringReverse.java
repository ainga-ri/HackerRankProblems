import java.io.*;
import java.util.*;

public class stringReverse {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        /* Enter your code here. Print output to STDOUT. */
        sc.close();
        String revA = "";
        for (int i = A.length() - 1; i >= 0; i--)
            revA = revA + A.charAt(i);
        if (A.compareTo(revA) == 0)
            System.out.println("Yes");
        else
            System.out.println("No");
    }
}
