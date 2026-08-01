// Last updated: 1/8/2026, 5:29:45 p.m.
int lengthOfLongestSubstring(char* s) {
    int abc[128]; 
    int i = 0, start = -1, maxLength = 0;
    char *aux; 
    memset(abc, -1, sizeof(abc));

    while(s[i] != '\0'){
        if(abc[s[i]] > start)
            start = abc[s[i]];

        abc[s[i]] = i;
        if(i-start > maxLength) maxLength = i-start;
        i++;
    }

    return maxLength;
}