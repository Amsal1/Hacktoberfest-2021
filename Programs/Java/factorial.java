import java.util.Scanner;

public class factorial {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a number to get factorial of it ");
		int n = input.nextInt();
		int m = 1;
		while(n>0){
			m = m*n;
			n-=1;
		}
		System.out.println("Fortorial is "+m);
	}
}
