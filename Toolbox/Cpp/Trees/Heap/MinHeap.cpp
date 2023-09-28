#include <stdexcept>

#include "MinHeap.h"

MinHeap::MinHeap() {}

bool MinHeap::IsEmpty() const {
    return heap.empty();
}

int MinHeap::Size() const {
    return heap.size();
}

int MinHeap::ExtractMin()
{
    if (IsEmpty()) {
        throw std::runtime_error("Heap is empty");
    }

    int result = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    HeapifyDown(0);
    
    return result;
}

void MinHeap::Insert(int value)
{
    heap.push_back(value);
    int index = heap.size() - 1;
    HeapifyUp(index);
}

void MinHeap::HeapifyDown(int index)
{
    int smallest = index;
    int left = 2 * smallest + 1;
    int right = 2 * smallest + 2;   

    if(left < this->Size() && heap[left] < heap[smallest])
    {
        smallest = left;
    }

    if(right < this->Size() && heap[right] < heap[smallest])
    {
        smallest = right;
    }

    if(smallest != index)
    {
        std::swap(heap[index], heap[smallest]);
        HeapifyDown(smallest);
    }
}

void MinHeap::HeapifyUp(int index)
{
    int parent = (index - 1) / 2;
    int current = index;
    while(current > 0 && heap[current] < heap[parent])
    {
        std::swap(heap[parent], heap[current]);
        current = parent;
        parent = (current - 1) / 2;
    }
}