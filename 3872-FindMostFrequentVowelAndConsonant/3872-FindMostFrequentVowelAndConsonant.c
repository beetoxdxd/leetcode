// Last updated: 22/7/2026, 5:56:51 p.m.
int maxFreqSum(char* s) {
    char abc[26] = {0}, max_vowel = 0, max_cons = 0, vowels[] = "aeiou", j;

    while(*s)
        abc[*(s++) - 'a']++;

    for(char i = 0; i < 26; i++){
        for(j = 0; j < 5; j++)
            if(i + 'a' == vowels[j]) break;

        if(j != 5 && abc[i] > max_vowel) max_vowel = abc[i];
        else if(j == 5 && abc[i] > max_cons) max_cons = abc[i];
    }

    return max_vowel + max_cons;
}