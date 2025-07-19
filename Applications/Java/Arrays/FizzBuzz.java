package Applications.Java.Arrays;

import java.util.ArrayList;

public class FizzBuzz 
{
    public static ArrayList<String> fizzBuzz(int n)
    {
        ArrayList<String> result = new ArrayList<>(n);
        String divisibleBy3 = "Fizz";
        String divisibleBy5 = "Buzz";

        for (int i = 1; i <= n; i++)
        {
            String str = "";
            if (i % 3 == 0) {
                str = divisibleBy3;
            }
            if (i % 5 == 0) {
                str += divisibleBy5;
            } 
            if (str.isEmpty()){
                str = String.valueOf(i);
            }
            result.add(str);
        }

        return result;
    }

    public static void main(String[] args) {
        int n = 15;    
        ArrayList<String> output = fizzBuzz(n);

        for (String val : output) {
            System.out.println(val);
        }
    }   
}
