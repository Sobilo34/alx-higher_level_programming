#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - A function that checks if a singly linked
 * list has a cycle inside it
 * @list: The singlt linked list
 * Return: 1 if there is cycle inside, and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *front = list, *lag = list;

	if (!list)
	{
		return (0);
	}

	while (lag && front && front->next)
	{
		lag = lag->next;
		front = front->next->next;

		if (lag == front)
		{
			return (1);
		}
	}

	return (0);
}
