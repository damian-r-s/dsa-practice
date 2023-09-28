#include <iostream>

#include "MinHeap.h"

using namespace std;

int main() {

    MinHeap heap;
    heap.Insert(100);
    heap.Insert(20);
    heap.Insert(40);
    heap.Insert(15);

    cout << "Is it empty: " << heap.IsEmpty() << endl;
    cout << "Extract minimum: " << heap.ExtractMin() << endl;

    return 0;
}