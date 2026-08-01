// Last updated: 1/8/2026, 5:22:21 p.m.
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int *ans;
    *returnSize = numsSize*2;
    ans = (int*)malloc(sizeof(int)*(*returnSize));

    memcpy(ans, nums, numsSize*sizeof(int));
    memcpy(ans+numsSize, nums, numsSize*sizeof(int));

    return ans;
}