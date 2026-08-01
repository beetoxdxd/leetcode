// Last updated: 1/8/2026, 5:28:08 p.m.
int factorial(int n){
    if(n == 1 || n == 0) return 1;
    return n * factorial(n-1);
}

char* getPermutation(int n, int k) {
    static int size = 0;
    static bool hash[9];
    if(size == 0){
        size = n;
        memset(hash, false, 9);
    }

    if(k == 0){
        char *empty = malloc(sizeof(char) * (size+1)); *empty = 0;
        char *digit = malloc(sizeof(char) * 2);

        for(int i = size - 1; i >= 0; i--){
            if(!hash[i]){
                snprintf(digit, 2, "%d", i+1);
                strcat(empty, digit);
            }

        }

        free(digit);
        size = 0;
        return empty;
    }

    int div = factorial(n-1), aux = 0;
    char *res = malloc(sizeof(bool) * (n+1)), *perm, begin = 0, index = 0;

    while(aux < k)
        aux = div * (++begin);

    for(int i = 0; i < begin; i++, index++)
        if(hash[i]) index++;

    aux = index;
    // checa los posibles elementos entre la diferencia de indices
    for(int i = begin; i < aux; i++){
        if(hash[i]) index++;
        if(index > aux && hash[index-1]) // detecta si el nuevo index esta ocupado 
            index++;
    }
    
    // recorre hasta encontrar el siguiente elemento en orden
    while(hash[index - 1]) index++;

    hash[index-1] = true;
    snprintf(res, n+1, "%d", index);
    perm = getPermutation(n-1, k % div);
    strcat(res, perm);
    free(perm);

    return res;
}