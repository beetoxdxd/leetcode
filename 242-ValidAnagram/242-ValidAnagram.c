// Last updated: 1/8/2026, 5:27:11 p.m.
bool isAnagram(char* s, char* t) {
    int hash[26] = {0};

    while(*s != 0)
        hash[*s++ - 'a']++;
    

    while(*t != 0){
        if(hash[*t - 'a'] == 0) return false;
        hash[*t++ - 'a']--;
    }

    for(int i = 0; i < 26; i++)
        if(hash[i] != 0) return false;

    return true;
}