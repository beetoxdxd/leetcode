// Last updated: 1/8/2026, 5:22:47 p.m.
char * mergeAlternately(char * word1, char * word2){
    char *p, *ans = (char*)malloc(sizeof(char)*(strlen(word1)+strlen(word2)+1));
    p = ans;

    while(*word1 || *word2){
        if(*word1) *(p++) = *(word1++);
        if(*word2) *(p++) = *(word2++);
    }

    *p = 0;
    return ans;
}