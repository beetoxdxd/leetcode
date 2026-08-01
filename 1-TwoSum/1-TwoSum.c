// Last updated: 1/8/2026, 5:29:49 p.m.
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *arr=(int *)malloc(sizeof(int)*2), i, j;
    *returnSize=2;
    
    for(i=0; i < numsSize-1 ; i++){
        for(j=i+1; j < numsSize; j++){
            if(nums[i]+nums[j]==target){
                arr[0]=i; arr[1]=j;
                return arr;
            }
        }
    }

    return arr;
}