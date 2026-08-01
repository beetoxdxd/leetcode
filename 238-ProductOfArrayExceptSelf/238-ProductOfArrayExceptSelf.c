// Last updated: 1/8/2026, 5:27:17 p.m.
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int i, left, right, *ans;
    ans = (int*)malloc(sizeof(int)*numsSize);

    left = right = 1;

    for(i = 0; i < numsSize; i++){
        ans[i] = left;
        left *= nums[i];
    }

    for(i = numsSize-1; i >= 0; i--){
        ans[i] *= right;
        right *= nums[i];
    }

    *returnSize = numsSize;
    return ans;
}