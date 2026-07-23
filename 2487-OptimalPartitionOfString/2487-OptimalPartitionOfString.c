// Last updated: 22/7/2026, 11:36:02 p.m.
int partitionString(char* s) {
    int cont = 0;
    bool abc[26] = {0};

    while(true){
        while(*s != '\0' && !abc[*s - 'a']){
            abc[*s - 'a'] = true;
            s++;
        } 

        if(*s == '\0') break;
        memset(abc, false, sizeof(abc));
        cont++;
    }
    
    return cont+1;
}