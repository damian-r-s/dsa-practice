public class Solution
{
    public int[] TopKFrequent(int[] nums, int k)
    {
        var heap = new MaxHeap(nums.Length);

        for (int i = 0; i < nums.Length; i++)
        {
            heap.Add(nums[i]);
        }

        var result = new int[k];
        for (int i = 0; i < k; i++)
        {
            var current = heap.Pop();
            result[i] = current.Number;
        }

        return result;
    }

    private class MaxHeap
    {
        public class Item
        {
            public Item(int number)
            {
                Number = number;
                Frequency = 1;
            }

            public int Number { get; private set; }
            public int Frequency { get; private set; }

            public void IncreaseFrequency()
            {
                Frequency++;
            }
        }

        private int _size = 0;
        private int _ptr = 0;
        private Item[] _elements;
        public MaxHeap(int size)
        {
            _size = size;
            _elements = new Item[size + 1];
        }

        public void Add(int element)
        {
            if (_ptr == _size)
                throw new ArgumentOutOfRangeException($"Cannot have more than {_size}");

            var idx = FindIndex(element);
            if (idx == -1)
            {
                _ptr = _ptr + 1;
                _elements[_ptr] = new Item(element);
                idx = _ptr;
            }
            else
            {
                var item = _elements[idx];
                item.IncreaseFrequency();
            }

            var parent = idx / 2;
            while (parent > 0 && _elements[parent].Frequency < _elements[idx].Frequency)
            {
                var father = _elements[parent];
                _elements[parent] = _elements[idx];
                _elements[idx] = father;

                idx = parent;
                parent = idx / 2;
            }
        }

        int FindIndex(int element)
        {
            int result = -1;
            for (int i = 1; i <= _ptr; i++)
            {
                var item = _elements[i];
                if (item == null)
                {
                    break;
                }

                if (item.Number == element)
                    return i;
            }

            return result;
        }

        public Item Pop()
        {
            if (_ptr > _size)
                throw new ArgumentOutOfRangeException($"Cannot have more than {_size}");

            var result = _elements[1];
            _elements[1] = _elements[_ptr];
            _elements[_ptr] = null;
            _ptr = _ptr - 1;

            var idx = 1;
            while (idx <= _ptr / 2)
            {
                var left = 2 * idx;
                var right = 2 * idx + 1;
                var ele = _elements[idx];

                if (_elements[right] == null && ele.Frequency < _elements[left].Frequency)
                {
                    _elements[idx] = _elements[left];
                    _elements[left] = ele;
                    idx = left;
                }
                else if (_elements[right] != null && (ele.Frequency < _elements[left].Frequency || ele.Frequency < _elements[right].Frequency))
                {
                    if (_elements[right].Frequency < _elements[left].Frequency)
                    {
                        _elements[idx] = _elements[left];
                        _elements[left] = ele;
                        idx = left;
                    }
                    else
                    {
                        _elements[idx] = _elements[right];
                        _elements[right] = ele;
                        idx = right;
                    }
                }
                else
                {
                    break;
                }
            }

            return result;
        }
    }
}