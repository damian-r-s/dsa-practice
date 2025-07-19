package Applications.Java.Gerneral;

public class NumberOfStepsToReduceANumberToZero {
    public static int numberOfSteps(int num) {
        int steps = 0;
        int number = num;

        while(true)
        {
            if(number == 0)
                break;

            if(number % 2 == 0)
            {
                number = number / 2;
                steps++;
            }
            else
            {
                number -= 1;
                steps++;
            }
        }

        return steps;
    }
    public static void main(String[] args) {
        int num = 14;
        int steps = numberOfSteps(num);
        System.out.println(steps);

        num = 8;
        steps = numberOfSteps(num);
        System.out.println(steps);
    }
}
