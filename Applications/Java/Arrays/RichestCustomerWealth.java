package Applications.Java.Arrays;

public class RichestCustomerWealth {
    public int maximumWealth(int[][] accounts) {
        int maximum = 0;

        for(int []customer: accounts)          
        {
            int current = 0;
            for(int bank: customer)
            {
                current += bank;
            }
            maximum = Math.max(maximum, current);
        }

        return maximum;
    } 
}