// Last updated: 22/7/2026, 11:36:06 p.m.
int findClosestNumber(int* nums, int numsSize) {
    int i, min = nums[0];

    for(i = 1; i < numsSize; i++){
        if(abs(nums[i]) < abs(min)) min = nums[i];
        else if(abs(nums[i]) == abs(min)) min = (nums[i] > min) ? nums[i] : min;
    }

    return min;
}