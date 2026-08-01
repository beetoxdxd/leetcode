// Last updated: 1/8/2026, 5:28:11 p.m.
int lengthOfLastWord(char* s) {
    int i = strlen(s), cont = 0;

    while(s[--i] == ' ');
    while(i >= 0 && s[i--] != ' ')
        cont++;

    return cont;
}