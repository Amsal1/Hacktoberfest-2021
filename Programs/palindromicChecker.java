package programpalindrome;
import java.util.Scanner;
import java.util.Stack;
public class programpalindrome {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Scanner in=new Scanner(System.in);

		System.out.print("enter a sentence : ");
        String kalimat = in.nextLine();
        Stack stack = new Stack();

        for (int i = 0; i < kalimat.length(); i++) {
           stack.push(kalimat.charAt(i));
      }

        String reverseString = "";
        while (!stack.isEmpty()) {
            reverseString = reverseString+stack.pop();
      }
        System.out.println(reverseString);
        if (kalimat.equals(reverseString))
            System.out.println("This sentence is a palindrome sentence");
        else
            System.out.println("This sentence is not a palindrome");
	}

}
