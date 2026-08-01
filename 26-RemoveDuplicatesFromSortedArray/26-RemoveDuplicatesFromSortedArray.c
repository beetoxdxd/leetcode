// Last updated: 1/8/2026, 5:29:01 p.m.
int removeDuplicates(int* nums, int numsSize) {
    int i = 1;

    for(int j = 1; j < numsSize; j++)
        if(nums[j] != nums[i-1])
            nums[i++] = nums[j];
        
    return i;
}