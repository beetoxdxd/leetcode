// Last updated: 1/8/2026, 5:24:56 p.m.
int* replaceElements(int* arr, int arrSize, int* returnSize) {
    int i = 0, value = -1, aux;//, *ans = (int*)malloc(sizeof(int)*arrSize);
    *returnSize = arrSize;

    while(--arrSize >= 0){
        aux = arr[arrSize];
        arr[arrSize] = value;
        value = (value > aux) ? value : aux;
    }

    return arr;
}