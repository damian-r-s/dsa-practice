int[] MergeSort(int[] nums) => MergeSort(nums, 0, nums.Length - 1);

int[] MergeSort(int[] nums, int first, int last)
{
    if (first >= last)
        return nums;

    int middle = first + (last - first) / 2;
    MergeSort(nums, first, middle);
    MergeSort(nums, middle + 1, last);

    var left = new int[middle - first + 1];
    for (int i = 0; i < left.Length; i++)
    {
        left[i] = nums[first + i];
    }
    var right = new int[last - middle];
    for (int i = 0; i < right.Length; i++)
    {
        right[i] = nums[middle + 1 + i];
    }

    var idxL = 0;
    var idxR = 0;
    while (idxL < left.Length && idxR < right.Length)
    {
        if (left[idxL] <= right[idxR])
        {
            nums[first] = left[idxL];
            idxL++;
        }
        else
        {
            nums[first] = right[idxR];
            idxR++;
        }

        first++;
    }

    while (idxL < left.Length)
    {
        nums[first] = left[idxL];
        idxL++;
        first++;
    }

    while (idxR < right.Length)
    {
        nums[first] = right[idxR];
        idxR++;
        first++;
    }

    return nums;
}