
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author Sadiya Khatoon
 */
public class Roman_to_integer {

    /**
     * @param args the command line arguments
     */
    public int roman(String s)
    {
        Map <Character,Integer> hm=new HashMap<>();
        hm.put('I',1);
        hm.put('V',5);
         hm.put('X',10);hm.put('L',50);hm.put('C',100);hm.put('D',500);
         hm.put('N',1000);
         
         
         int res =hm.get(s.charAt(s.length()-1));
         for(int i=s.length()-2;i>=0;i--)
         {
            if(hm.get(s.charAt(i))<hm.get(s.charAt(i+1)))
            {
                res -=hm.get(s.charAt(i-1));
            }
            else res +=hm.get(s.charAt(i));
         }
          return res; 
            
    }
    public static void main(String[] args)throws IOException{
        // TODO code application logic here
        Roman_to_integer ob=new Roman_to_integer();
                BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
                System.out.println("Enter roman number using 'I' ,'V','X','L,'C','D' or 'N'  only");
                String s=br.readLine();
                
        System.out.println(ob.roman(s));
    }
    
}
