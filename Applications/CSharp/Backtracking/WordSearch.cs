// 79. Word Search
// Given an m x n grid of characters board and a string word, return true if word exists in the grid.
// The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution
{
    private char[][] _board;
    private string _word;
    private HashSet<(int, int)> _path;
    private int _n = 0;
    private int _m = 0;

    public bool Exist(char[][] board, string word)
    {
        _board = board;
        _word = word;
        _path = new HashSet<(int, int)>();

        _m = _board.Length;
        _n = _board[0].Length;

        return Search(0, 0, 0);
    }

    private bool Search(int i, int j, int l)
    {
        if (l == _word.Length)
            return true;

        if (i < 0 || j < 0 || i >= _m || j >= _n || _word[l] != _board[i][j] || _path.Contains((i, j)))
            return false;

        _path.Add((i, j));

        var res = Search(i + 1, j, l + 1) || Search(i - 1, j, l + 1) || Search(i, j + 1, l + 1) || Search(i, j - 1, l + 1);
        _path.Remove((i, j));

        return res;
    }
}