#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char alnum[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

int main()
{
	srand(time(NULL));

	char buf[6];
	char lower_buf[6];

	for (int i = 0; i < 5000000; i++) {
		for (int j = 0; j < 6; j++) {
			buf[j] = alnum[rand()%62];
			lower_buf[j] = (char)tolower(buf[j]);
		}

		if (strstr(lower_buf, "fail")) {
			printf("hit: %s pos: %d\n", buf, i);
		}
	}
}

