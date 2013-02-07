#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define LEN 6

/* letters are all lowercase so I don't need to convert to lower later */
char alnum[] = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789";

int main()
{
	srand(time(NULL));

	char buf[LEN];

	for (int i = 0; i < 5000000; i++) {
		for (int j = 0; j < LEN; j++) {
			buf[j] = alnum[rand()%62];
		}

		if (strstr(buf, "fail")) {
			printf("hit: %s pos: %d\n", buf, i);
		}
	}
}

