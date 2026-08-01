// Last updated: 1/8/2026, 5:29:23 p.m.
int romanToInt(char* s) {
    int ans = 0;

    while(*s){
        switch(*s){
            case 'I':
                if(*(s+1) == 'V'){ s++; ans += 4; }
                else if(*(s+1) == 'X'){ s++; ans += 9; }
                else ans += 1;
                break;
            case 'V':
                ans += 5;
                break;
            case 'X':
                if(*(s+1) == 'L'){ s++; ans += 40; }
                else if(*(s+1) == 'C'){ s++; ans += 90; }
                else ans += 10;
                break;
            case 'L':
                ans += 50;
                break;
            case 'C':
                if(*(s+1) == 'D'){ s++; ans += 400; }
                else if(*(s+1) == 'M'){ s++; ans += 900; }
                else ans += 100;
                break;
            case 'D':
                ans += 500;
                break;
            case 'M':
                ans += 1000;
                break;
        }
        
        s++;
    }

    return ans;
}