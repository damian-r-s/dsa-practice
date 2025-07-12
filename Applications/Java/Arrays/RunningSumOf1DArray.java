package Applications.Java.Arrays;

import java.util.Scanner;

public class RunningSumOf1DArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the numbers separated by spaces: ");
        String inputLine = scanner.nextLine();

        String[] tokens = inputLine.split(" ");
        int[] nums = new int[tokens.length];
        for (int i = 0; i < tokens.length; i++) {
            nums[i] = Integer.parseInt(tokens[i]);
        }

        int[] result = runningSum(nums);
        System.out.print("Running Sum: ");
        for (int num : result) {
            System.out.print(num + " ");
        }

        scanner.close();
    }

    private static int[] runningSum(int[] nums) {
        for(int i = 1; i < nums.length; i++){
            nums[i] += nums[i -1];
        }
        return nums;
    }
}