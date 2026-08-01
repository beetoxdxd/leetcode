// Last updated: 1/8/2026, 5:28:22 p.m.
double myPow(double x, int n) {
    if(n == 0) return 1;
    if(n == 1) return x;
    if(n == -1) return 1/x;
    
    double half = myPow(x, n/2), aux = (n > 0) ? x : 1/x;
    if(n % 2 == 0) return half * half;
    return half * half * aux;
}