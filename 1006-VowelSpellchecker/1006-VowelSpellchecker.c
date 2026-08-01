// Last updated: 1/8/2026, 5:25:16 p.m.
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <ctype.h>
#include <string.h>

char* copy_string(char *src){
    char *dest = malloc(sizeof(char) * strlen(src));
    strcpy(dest, src);
    return dest;
}

char* capitalization(char* wordlist, char* query){
    int j, len = strlen(wordlist);

    for(j = 0; j < len && wordlist[j] && query[j]; j++)
        if(tolower(wordlist[j]) != tolower(query[j])) break;

    if(j == len) return wordlist; // se encontró coincidencia
    return NULL;
}

bool is_vowel(char x){
    int i = 0; char vowels[] = "aeiou"; x = tolower(x);
    for(i = 0; i < 5; i++)
        if(x == vowels[i]) return true;

    return false;
}

char* vowel_errors(char* wordlist, char* query){
    int j, len = strlen(wordlist); 
    char *empty = malloc(sizeof(char)); *empty = 0;
    
    for(j = 0; j < len && wordlist[j] && query[j]; j++){
        if(is_vowel(wordlist[j]) && is_vowel(query[j])) continue;
        if(tolower(wordlist[j]) != tolower(query[j])) break;
    }

    if(j == len) return wordlist; // se encontró coincidencia
    return empty;
}

char** spellchecker(char** wordlist, int wordlistSize, char** queries, int queriesSize, int* returnSize) {
    char **res = malloc(sizeof(char*) * queriesSize); *returnSize = queriesSize;
    int i, j, **hash = malloc(sizeof(int*) * 26), index[26] = {0};

    for(i = 0; i < 26; i++) hash[i] = malloc(sizeof(int));
    for(i = 0; i < wordlistSize; i++){
        int aux = tolower(wordlist[i][0]) - 'a';
        hash[aux] = realloc(hash[aux], sizeof(int) * (index[aux] + 1));
        hash[aux][index[aux]++] = i;
    }

    for(i = 0; i < queriesSize; i++){
        int aux = tolower(queries[i][0]) - 'a';
        res[i] = NULL;

        for(j = 0; j < index[aux]; j++){ // recorre todas las coincidencias
            if(strcmp(wordlist[hash[aux][j]], queries[i]) == 0){
                res[i] = queries[i];
                break;
            }
        }

        if(res[i]) continue;
        for(j = 0; j < index[aux]; j++){
            char* element = capitalization(wordlist[hash[aux][j]], queries[i]);
            if(element){
                res[i] = element;
                break;
            }
        }

        if(res[i]) continue;
        if(is_vowel(queries[i][0])){
            for(j = 0; j < wordlistSize; j++){
                if(!is_vowel(wordlist[j][0])) continue;
                res[i] = vowel_errors(wordlist[j], queries[i]);
                if(res[i] && res[i][0]) break;
            }
        } else {
            for(j = 0; j < index[aux]; j++){
                res[i] = vowel_errors(wordlist[hash[aux][j]], queries[i]);
                if(res[i][0]) break;
            }
        } 
        
        if(res[i]) continue;
        char *empty = malloc(sizeof(char)); *empty = 0;
        res[i] = empty;       
    }

    return res;
}