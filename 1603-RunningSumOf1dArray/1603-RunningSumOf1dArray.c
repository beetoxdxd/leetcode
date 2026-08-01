// Last updated: 1/8/2026, 5:23:40 p.m.
int* runningSum(int* nums, int numsSize, int* returnSize){
    int *arr=(int *)malloc(sizeof(int) * numsSize);
    short int i;
    
    arr[0]=nums[0];
    for(i=1; i < numsSize; i++) arr[i]=nums[i] + arr[i-1];

    *returnSize=i;
    return arr;
}