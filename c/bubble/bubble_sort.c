#include <stdio.h>

int main()
{
	int values[] = {5, 6, 7, 9, 2};
	int size = (int)sizeof(values);
	int length = (int) ( sizeof(values) / sizeof(values[0]) );

	printf("Size of Values: %d\n", size);
	printf("Length of Values: %d\n", length);

	for (int i = 0; i < length; i++)
	{
		printf("%d\n", values[i]);
	}

}

/*
int getLength(int inputArr[])
{
	int length = (int) ( sizeof(inputArr) / sizeof(inputArr[0] );
	return length;
}
*/
