//Classic min heap
using System;
class MaxHeap
{
    int[] _nodes;
    int _size = 0;
    int _ptr = 0;
    public MaxHeap(int size)
    {
        _nodes = new int[size];
        _size = size;
    }
    public void Add(int value)
    {
        _ptr = _ptr + 1;
        if (_ptr > _size)
            throw new ArgumentOutOfRangeException("Added too many elements!");

        _nodes[_ptr] = value;

        var index = _ptr;
        var parent = index / 2;
        while (parent > 0 && _nodes[parent] < _nodes[index])
        {
            var node = _nodes[parent];
            _nodes[parent] = _nodes[index];
            _nodes[index] = node;
            index = parent;
            parent = index / 2;
        }
    }

    public int Peak() => _nodes[1];

    public int Pop()
    {
        if (_ptr == 0)
            throw new ArgumentOutOfRangeException("The heap is empty!");

        var result = _nodes[1];
        _nodes[1] = _nodes[_ptr];
        _ptr = _ptr - 1;

        var index = 1;
        while (index <= _ptr / 2)
        {
            var leftChild = 2 * index;
            var rightChild = leftChild + 1;

            if (_nodes[index] < _nodes[leftChild] || _nodes[index] < _nodes[rightChild])
            {
                if (_nodes[rightChild] < _nodes[leftChild])
                {
                    var value = _nodes[leftChild];
                    _nodes[leftChild] = _nodes[index];
                    _nodes[index] = value;
                    index = leftChild;
                }
                else
                {
                    var value = _nodes[rightChild];
                    _nodes[rightChild] = _nodes[index];
                    _nodes[index] = value;
                    index = rightChild;
                }
            }
            else
                break;
        }

        return result;
    }
}