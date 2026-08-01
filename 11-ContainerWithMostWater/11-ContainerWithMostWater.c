// Last updated: 1/8/2026, 5:29:31 p.m.
int maxArea(int* height, int heightSize) {
    int i = 0, j = heightSize - 1, amount = 0, aux;

    while(i < j){
        if(height[j] > height[i]) aux = (j-i) * height[i++];
        else aux = (j-i) * height[j--];

        if(aux > amount)
            amount = aux;
    }

    return amount;
}
