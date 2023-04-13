#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

typedef struct DiaryEntry{
    int mark;
    char *comment;
} DiaryEntry;

DiaryEntry *diary[0x20];

void prompt() {
    puts("Sina-korzina, a ti uroki sdelal? Nu-ka davai suda dnevnik...");
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

void printMenu() {
    puts("1) Add");
    puts("2) Edit");
    puts("3) View");
    puts("4) Remove");
    puts("5) Exit");
}

char *getCommentAndGrade(int *grade) {
    int entrySize = 0;

    printf("Enter your mark: ");
    scanf("%d", grade);

    printf("Enter size of comment: ");
    scanf("%d", &entrySize);
    if (entrySize <= 0)  {
        puts("ERROR: Incorrect size!");
        return NULL;
    }

    char *comment = (char *)malloc(entrySize);
    if (comment == NULL) {
        puts("ERROR: Incorrect size!");
        return NULL;
    }
    printf("Enter comment: ");
    int rb = read(0, comment, entrySize);
    if (rb == 0) {
        return NULL;
    }

    return comment;
}

int getIndex(int min, int max) {
    int index = 0;
    printf("Enter index: ");
    scanf("%d", &index);
    if (index < min || index > max) {
        puts("ERROR: Incorrect index");
        return -1;
    }
    return index;
}

void addGrade(int *markCount) {
    if (*markCount >= 0x20) {
        puts("ERROR: You've graduated!");
        return ;
    }
    DiaryEntry *entry= (DiaryEntry *) malloc(sizeof(DiaryEntry));
    int entrySize = 0;

    entry -> comment = getCommentAndGrade(&entry -> mark);
    if (entry -> comment == NULL) {
        return ;
    }

    diary[*markCount] = entry;
    *(markCount) += 1;
}


void viewGrade() {
    int index = getIndex(0, 0x1f);
    if (index < 0) {
        return ;
    }
    printf("Mark: %d", diary[index] -> mark);
    printf("Comment: %s", diary[index] -> comment);
}

void editGrade() {
    int index = getIndex(0, 0x1f);
    if (index < 0) {
        return ;
    }

    int entrySize = 0;
    int grade = 0;

    printf("Enter your mark: ");
    scanf("%d", &grade);

    printf("Enter size of comment: ");
    scanf("%d", &entrySize);
    if (entrySize <= 0)  {
        puts("ERROR: Incorrect size!");
        return ;
    }
    diary[index] -> comment = realloc(diary[index] -> comment, entrySize);

    printf("Enter comment: ");
    int rb = read(0, diary[index] -> comment, entrySize);
}

void deleteGrade() {
    int index = getIndex(0, 0x1f);
    if (index < 0) {
        return ;
    }
    if (diary[index] == NULL) {
        puts("ERROR: No such entry in diary");
        return ;
    }
    free(diary[index] -> comment);
    free(diary[index]);
} 


int main() {
    prompt();

    int markCount = 0, choice = 0;
    do {
        printMenu();
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                addGrade(&markCount);
                break;
            case 2:
                editGrade();
                break;
            case 3:
                viewGrade();
                break;
            case 4:
                deleteGrade();
                break;
        }
    } while (choice != 5);

    return 0;
}
