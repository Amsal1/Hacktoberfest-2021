import java.util.Scanner;
import java.util.Stack;

public class BalanceBrackets
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        System.out.println(ispar(str));
    }
    static boolean ispar(String x)
    {
        Stack<Character> stack = new Stack<>();

        if(x.length()%2 != 0)
        {
            return false;
        }

        for(int i = 0 ; i < x.length() ; i++)
        {
            char ch = x.charAt(i);
            switch (ch) {
                case '(' -> stack.push(')');
                case '[' -> stack.push(']');
                case '{' -> stack.push('}');
                default -> {
                    if(!stack.isEmpty() || ch==stack.peek())
                    {
                        stack.pop();
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }
        return (stack.isEmpty());
    }
}
