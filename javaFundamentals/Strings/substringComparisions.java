import java.util.Scanner;

public class substringComparisions {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        String aux = "";
        smallest = s.substring(0, k);
        for (int i = 0; i < s.length() - k + 1; i++)
        {
            aux = s.substring(i, i+k);
            if (aux.compareTo(smallest) < 0)
                smallest = aux;
            if (aux.compareTo(largest) > 0)
                largest = aux;
        }
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
