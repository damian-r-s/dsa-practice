#ifndef MIN_HEAP_H
#define MIN_HEAP_H

#include <vector>

class MinHeap 
{
private:
    std::vector<int> heap;
    void HeapifyUp(int index);
    void HeapifyDown(int index);
public:
    MinHeap();
    void Insert(int value);
    int ExtractMin();
    int Size() const;
    bool IsEmpty() const;
};

#endif // MIN_HEAP_H