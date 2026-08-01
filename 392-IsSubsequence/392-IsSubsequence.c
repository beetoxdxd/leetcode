// Last updated: 1/8/2026, 5:27:03 p.m.
bool isSubsequence(char* s, char* t) {
    while(*t && *s){
        s += *s == *t++;
    }

    return !*s;
}