#include <stdio.h>
#include <unistd.h>
#include <string.h>

char data[0x100];
FILE *notebook;

void setup() {
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

void printNotebook() {
    printf("Here's what you wrote.\n");
    printf(data);
}

void readToNotebook() {
    printf("Share your deep thoughts with me > ");
    read(0, data, 0x100);
}

void printMenu() {
    puts("1) Zapostit' thread");
    puts("2) Read thread");
    puts("3) Poiti v shkolu.");
}

int main() {
    setup();
    printf("Dobro pojalovat. Snova.\n");
    notebook = fopen("./notebook.txt", "w+");
    int option = 0;

    if (!notebook) {
        fprintf(stderr, "%s", "Too bad\n");
        return 1;
    }

    do {
        printMenu();
        printf("> ");
        scanf("%d", &option);
        switch (option) {
            case 1:
                readToNotebook();
                break;
            case 2:
                printNotebook();
                break;
            default:
                goto final;
        }
    } while (option != 3);

final:
    printf("I'm not really sure, how to write to a file, I guess that's the correct way...\n");
    memcpy(&notebook, data, 0x100);
    fclose(notebook);
    return 0;
}
