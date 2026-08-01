// Last updated: 1/8/2026, 5:27:50 p.m.
int maxProfit(int* prices, int pricesSize) {
    int i, min = INT_MAX, max = INT_MIN;

    for(i = 0; i < pricesSize; i++){
        if(min > prices[i]) min = prices[i];
        if(max < prices[i] - min) max = prices[i] - min;;
    }

    return max;
}