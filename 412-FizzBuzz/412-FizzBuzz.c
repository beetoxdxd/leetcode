// Last updated: 1/8/2026, 5:26:53 p.m.
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) {
    int i;
    char **arr = (char **)malloc(sizeof(char*)*n);
    *returnSize = n;

    for(i = 1; i <= n; i++){
        arr[i-1] = (char *)malloc(sizeof(char)*9);
        if(i%3 == 0 && i%5 == 0) strcpy(arr[i-1], "FizzBuzz");
        else if(i%3 == 0) strcpy(arr[i-1], "Fizz");
        else if(i%5 == 0) strcpy(arr[i-1], "Buzz");
        else sprintf(arr[i-1], "%d", i);
    }

    return arr;
}