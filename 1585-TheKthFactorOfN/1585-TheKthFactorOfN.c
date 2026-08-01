// Last updated: 1/8/2026, 5:23:42 p.m.
int kthFactor(int n, int k) {
    int i, j, *factors = (int*)calloc(k, sizeof(int));

    for(i = 1, j = 0; i <= n/2 && j < k; i++){
        if(n % i == 0) factors[j++] = i;
    }

    if(j == k) return factors[k-1];
    
    factors[j++] = n;
    return (j < k) ? -1: factors[k-1];
}