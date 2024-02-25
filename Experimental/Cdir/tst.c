#include <stdio.h>
#include <string.h>

void printStr(char *str)
{
    printf("%s\n", str);
    for (int i = 0; i < (int)sizeof( str); i++)
    {
        char s[2];
        s[0] = str[i];
        s[1] = '\0';
        printf("{%c:%i, i:%i S:%s}, ", str[i], str[i], i, s);
    }
    putchar(10);
    printf(" size of str is: %i \n ", (int)sizeof( str));
    printf(" length of str is: %i \n ", (int)strlen( str));
    printf("\n▬▐▬▬▐▬▬▐▬▬▐▬▬▐▬▬▐▬▬▐▬▬▐▬▬▐▬▬▐▬▬▐▬▬▐▬▬▐▬▬▐▬\n");
}
int main(void)
{
    char strJap[] = "私は人生の何年も失った";
    char strArp[] = "انا ال ضاع من عمري سنين";
    char strEng[] = "I lost years of my life";

    printStr(strEng);
    printStr(strArp);
    printStr(strJap);

}