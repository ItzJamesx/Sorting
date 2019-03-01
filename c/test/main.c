#include <stdio.h>

int main()
{
	int c;

	int n = 0;

	while ((c = getchar()) != EOF)
	{
		
        if (c == 'c')
		{
			printf("%s", "You paid respects");
		}

		printf("%1d\n", n);
		++n;
	}

}

