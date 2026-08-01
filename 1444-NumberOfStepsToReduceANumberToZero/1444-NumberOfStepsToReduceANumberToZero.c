// Last updated: 1/8/2026, 5:24:19 p.m.
int numberOfSteps(int num) {
    int step = 0;
    
    while(num){
        if(!(num & 1)) num = num >> 1;
        else num--;
        step++;
    }

    return step;
}