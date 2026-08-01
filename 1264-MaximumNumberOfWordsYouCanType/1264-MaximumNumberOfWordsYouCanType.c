// Last updated: 1/8/2026, 5:24:51 p.m.
int canBeTypedWords(char* text, char* brokenLetters) {
    bool hash[26] = {0};
    int words = 0;

    while(*brokenLetters) hash[*(brokenLetters++) - 'a'] = true;
    while(*text != 0){
        if(*text == ' ') words++;
        else if(hash[*text - 'a']){
            words--;
            while(*text && *text != ' ') text++;
            continue;
        }

        text++;
    }

    return ++words;
}