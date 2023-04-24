import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

/**
 *
 * @author Sadiya Khatoon
 */
public class Longest_substring_without_repeating_characters {

    /**
     * @param args the command line arguments
     */
    public int length(String s)
    { char c;
        HashSet<Character> h=new HashSet<>();
        int max=0;
        for(int i=0;i<s.length();i++)
        {
            c=s.charAt(i);
            if(!h.contains(c))
            {
                h.add(c);
            }
            else{
                max=Math.max(max, h.size());
                h.clear();
                
            }
        }
        return max;
    }
    public static void main(String[] args)throws IOException {
        // TODO code application logic here
          BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        // TODO code application logic here
        String s=br.readLine();
        Longest_substring_without_repeating_characters  ob=new Longest_substring_without_repeating_characters ();
        System.out.print(ob.length(s));
    }
    
}
