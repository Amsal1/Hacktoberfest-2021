import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author Sadiya Khatoon
 */
public class LCS {

    /**
     * @param s
     * @param t
     * @return 
     */
    
    
    public int lcss(String s,String t)
    {
        int op1,op2;
        if(s.length()==0 || t.length()==0)
            return 0;
        if(s.charAt(0) == t.charAt(0))
            return 1+ lcss(s.substring(1), t.substring(1));
        else
        {
        op1=lcss(s,t.substring(1));
        op2=lcss(s.substring(1),t);
        return Math.max(op1, op2);
        
        }
        
            
    }
    public static void main(String[] args)throws IOException  {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        // TODO code application logic here
        String s=br.readLine();
        String t=br.readLine();
        LCS ob =new LCS();
        int f=ob.lcss(s,t);
        System.out.println(+f);
    }
    
}
