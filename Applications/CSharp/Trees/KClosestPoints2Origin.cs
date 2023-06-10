// 973. K Closest Points to Origin
// Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
// The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
// You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        var items = points.Select(point => {
            long x = point[0];
            long y = point[1];

            return (point, x * x + y * y);
        });

        int[][] result = new int[k][];
        // T: O(n)
        PriorityQueue<int[], long> queue = new(items);

        // T: O(k log(n))
        for (int i = 0; i < k; i++) {
            result[i] = queue.Dequeue();
        }

        return result;
    }
}
