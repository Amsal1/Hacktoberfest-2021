import java.util.Scanner;

public class factor{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("------------------Program to print factor of n numbers------------------");
		System.out.print("Enter N number ");
		int n = input.nextInt();
		System.out.print("Factor of "+n+" is: ");
		for (int i = 1;i<=n;i+=1 ) {
			if (n%i==0) {
				System.out.print(" "+i+" ");
			}
			
		}
	}
}
