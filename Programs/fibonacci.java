import java.util.*;
public class Main
{  
   static int n1=0,n2=1,n3=0;   
   static void printFibonacci(int n)
   {    
        if(n>0)
        {    
            n3 = n1 + n2;    
            System.out.print(" "+n3);   
            n1 = n2;    
            n2 = n3;    
            printFibonacci(n-1);   
        }    
   }    
    public static void main(String args[])
    {    
       
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the number of terms: ");
        int n=sc.nextInt();   
        System.out.print("Fibonacci Series up to "+n+" terms: ");
        System.out.print(n1+" "+n2);    
        printFibonacci(n-2);
    }  
}  
