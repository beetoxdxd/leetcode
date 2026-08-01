// Last updated: 1/8/2026, 5:29:26 p.m.
char* longestCommonPrefix(char** strs, int strsSize) {
    char i = 1, j = 0, *ans = (char*)malloc(sizeof(char)*201);

    while(strs[0][j]){
        while(i < strsSize && strs[0][j] == strs[i][j]) i++;
        if(i != strsSize) break;

        ans[j] = strs[0][j];
        i = 1; j++;
    }
    
    ans[j] = '\0';
    return ans;
}