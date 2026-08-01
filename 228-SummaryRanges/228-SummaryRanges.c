// Last updated: 1/8/2026, 5:27:21 p.m.
char** summaryRanges(int* nums, int numsSize, int* returnSize) {
    int i = 1, j = 1, cont = 1, start;
    char **ans = (char**)malloc(sizeof(char*));

    if(numsSize > 0) start = nums[0];
    else {
        *returnSize = 0;
        return ans;
    }

    while(i <= numsSize){
        if(i != numsSize && start == nums[i] - cont) cont++;
        else {
            ans = realloc(ans, sizeof(char*)*j);

            if(cont == 1){ 
                ans[j-1] = (char*)malloc(sizeof(char)*12);
                sprintf(ans[j-1], "%d", start);
            } else {
                ans[j-1] = (char*)malloc(sizeof(char)*25);
                sprintf(ans[j-1], "%d->%d", start, nums[i-1]);
            }
            
            if(i != numsSize){
                start = nums[i];
                cont = 1; j++;
            } 
        }

        i++;
    }
    
    *returnSize = j;
    return ans;
}