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
            for (int col  = 1; col <= Integer.parseInt(values.get(0)); col++)
                twoDim.get(row).add(Integer.parseInt(values.get(col)));
            
        }
        int queries = Integer.parseInt(scan.nextLine());
        for (int k = 0; k < queries; k++)
        {
            String[] pair = scan.nextLine().split(" ");
            List<String> pairList = new ArrayList<String>();
            pairList = Arrays.asList(pair);
            try
            {
                System.out.println(twoDim.get(Integer.parseInt(pairList.get(0))-1).get(Integer.parseInt(pairList.get(1))-1));
            } catch (IndexOutOfBoundsException e)
            {
                System.out.println("ERROR!");
            }
        }

        scan.close();
        
    } 
}

