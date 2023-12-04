#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - THis function checks if a linked list is a palindrome
 * @head: Pointer to pointer, to the head of a list
 * Return: 0 if not else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *present = *head;
	int index[2400], count = 0;

	if (head == NULL || present == NULL || present->next == NULL)
		return (1);

	while (present != NULL)
	{
		index[count++] = present->n;
		present = present->next;
	}

	count--;
	present = *head;

	while (present != NULL)
	{
		if (present->n != index[count--])
			return (0);
		present = present->next;
	}

	return (1);
}

