// Last updated: 1/8/2026, 5:27:01 p.m.
bool canConstruct(char* ransomNote, char* magazine) {
    short int map[26] = {0};
    int i;

    while(*magazine){
        map[magazine[i]-97]++;
        magazine++;
    } 

    while(*ransomNote){
        if(map[ransomNote[i] - 97] == 0) return false;
        else map[ransomNote[i] - 97]--;
        ransomNote++;
    }

    return true;
}