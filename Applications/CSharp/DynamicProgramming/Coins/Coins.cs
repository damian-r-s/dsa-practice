//322. Coin Change
// You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
// Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
// You may assume that you have an infinite number of each kind of coin.

public class Solution
{
    public int CoinChange(int[] coins, int amount)
    {
        var n = amount + 1;
        int[] array = Enumerable.Repeat(n, n).ToArray();
        array[0] = 0;

        for (int i = 1; i < n; i++)
        {
            foreach (var coin in coins)
            {
                if (i - coin >= 0)
                {
                    array[i] = Math.Min(array[i], 1 + array[i - coin]);
                }
            }
        }

        return array[n - 1] == n ? -1 : array[n - 1];
    }
}