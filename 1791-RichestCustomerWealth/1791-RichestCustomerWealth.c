// Last updated: 1/8/2026, 5:23:08 p.m.
int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) {
    int i, j, max = 0, sum = 0;

    for(i = 0; i < *accountsColSize; i++) sum+=accounts[0][i];
    max = sum; sum = 0;

    for(i = 1; i < accountsSize; i++, sum = 0){
        for(j = 0 ; j < *accountsColSize; j++) sum += accounts[i][j];
        if(sum > max) max = sum;
    }

    return max;
}