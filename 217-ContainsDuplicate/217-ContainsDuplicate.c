// Last updated: 1/8/2026, 5:27:28 p.m.
int compare(const void* a, const void* b)
{
  int va = *(const int*) a;
  int vb = *(const int*) b;
  return (va > vb) - (va < vb);
}

bool containsDuplicate(int* nums, int numsSize) {
    int i;
    qsort(nums, numsSize, sizeof(int), compare);

    for(i = 1; i < numsSize; i++){
        if(nums[i] == nums[i-1]) return true;
    }

    return false;
}