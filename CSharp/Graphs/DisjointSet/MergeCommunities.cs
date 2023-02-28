//Hackerrank Merging Communities
using System;
using System.Collections.Generic;
using System.IO;

class Solution
{
    static void Main(String[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */

        var settigns = Console.ReadLine().Split(' ');
        int n = int.Parse(settigns[0]);
        int q = int.Parse(settigns[1]);

        var ds = new DisjointSet(n);

        for (int i = 0; i < q; i++)
        {
            var line = Console.ReadLine();
            var items = line.Split(' ');
            var command = items[0];

            if (command == "Q")
            {
                int member = int.Parse(items[1]);
                Console.WriteLine(ds.NumberOfMembers(member));
            }
            else if (command == "M")
            {
                var member1 = int.Parse(items[1]);
                var member2 = int.Parse(items[2]);
                ds.Union(member1, member2);
            }
        }
    }

    public class DisjointSet
    {
        private int[] _connected;
        private int[] _numberOfMembers;
        private int _size;

        public DisjointSet(int size)
        {
            _size = size + 1;
            _connected = new int[_size];
            _numberOfMembers = new int[_size];

            for (int i = 0; i < _size; i++)
            {
                _connected[i] = i;
                _numberOfMembers[i] = 1;
            }
        }

        public int NumberOfMembers(int x)
        {
            return _numberOfMembers[Find(_connected[x])];
        }

        public int Find(int x)
        {
            if (x == _connected[x])
            {
                return x;
            }

            _connected[x] = Find(_connected[x]);
            return _connected[x];
        }

        public void Union(int x, int y)
        {
            var xRoot = Find(x);
            var yRoot = Find(y);

            if (xRoot != yRoot)
            {
                _connected[xRoot] = yRoot;
                _numberOfMembers[yRoot] += _numberOfMembers[xRoot];
            }
        }
    }
}
