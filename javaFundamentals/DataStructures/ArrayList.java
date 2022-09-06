import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class ArrayList {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int lines = Integer.parseInt(scan.nextLine());
        ArrayList<ArrayList<Integer>> twoDim = new ArrayList<>(lines);
        for(int row = 0; row < lines; row++)
        {
            twoDim.add(new ArrayList<Integer>());
            String[] val = scan.nextLine().split(" ");
            List<String> values = new ArrayList<String>();
            values = Arrays.asList(val);
            System.out.println(values);
            for (int col  = 1; col <= Integer.parseInt(values.get(0)); col++)
            {
                twoDim.get(row).add(Integer.parseInt(values.get(col)));
            }
            
        }
        System.out.println(twoDim);
        scan.close();
        
    }
}

