
import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 *
 * @author Sadiya Khatoon
 */
public class Min_path_sum {

    /**
     * @param grid
     * @return 
     */
    
    
    public int min_path(int [][]grid)
    {
        
        
        //dynamic programming (bottom up approach)
        if (grid==null || grid.length==0)
            return 0;
       int m=grid.length;
       int n=grid[0].length;
       int res[][]=new  int[m][n];
       res[m-1][n-1]=grid[m-1][n-1];//last cell
       //populating values in the latst column
       if(m>1)
       {
       for(int i=m-2;i>=0;i--)
       { 
           res[i][n-1]=grid[i][n-1]+res[i+1][n-1];
           
       }
       
       }
       //populating the values in the last row
       if(n>1)
       {
           for (int j=n-2;j>=0;j--)
           {
           res[m-1][j]=res[m-1][j+1]+grid[m-1][j];
           }
       }
       //rest of the cell
       for(int i=m-2;i>=0;i--)
       {
           for(int j=n-2;j>=0;j--)
           {
           res[i][j]=grid[i][j]+Math.min(res[i+1][j],res[i][j+1]);
           }
       }
           
       return(res[0][0]);
    }
    
   
    public static void main(String[] args)throws Exception {
        // TODO code application logic here
                BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
                int g[][]=new int[3][3];
           for(int i=0;i<3;i++)
           {
               for(int j=0;j<3;j++)
           {
              g[i][j]=Integer.parseInt(br.readLine());
           }
           }
           
           
           Min_path_sum ob=new  Min_path_sum ();
           System.out.println(ob.min_path(g));
    }
    
}
