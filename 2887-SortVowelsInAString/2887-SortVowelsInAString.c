// Last updated: 22/7/2026, 11:35:42 p.m.
#include <ctype.h>
#include <string.h>

char* sortVowels(char* s) {
    int hash[10] = {0}, len = strlen(s), j = 0, k = 0;
    char vowels[] = "AEIOUaeiou";

    for(int i = 0; i < len; i++){
        for(j = 0; j < 10; j++) if(vowels[j] == s[i]) break;
        if(j == 10) continue;

        hash[j]++;
    }

    for(int i = 0; i < len; i++){
        for(j = 0; j < 10; j++) if(vowels[j] == s[i]) break;
        if(j == 10) continue; // es consonante
    
        while(hash[k] == 0) k++;
        s[i] = vowels[k];
        hash[k]--;
    }

    return s;
}