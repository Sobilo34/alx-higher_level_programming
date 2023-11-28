#include "lists.h"

/**
 * insert_node - THis is a function that inserts a node
 * with a given number into a sorted linked list
 * @head: A pointer to the head of the linked list
 * @number: The integer value to be added to the linked list
 *
 * Description: This function inserts a new node with the specified number
 *              into a sorted linked list and maintaining ascending order.
 *
 * Return: If successful, a pointer to the newly inserted node. If memory
 *         allocation fails or other errors occur, returns NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_new;
	listint_t *present;

	node_new = malloc(sizeof(listint_t));
	if (node_new == NULL)
	{
		return (NULL);
	}
	node_new->n = number;

	present = *head;
	if (present == NULL || present->n >= number)
	{
		node_new->next = present;
		*head = node_new;
		return (node_new);
	}

	while (present && present->next && present->next->n < number)
		present = present->next;

	node_new->next = present->next;
	present->next = node_new;

	return (node_new);
}
