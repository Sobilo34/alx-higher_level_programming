#include "lists.h"

/**
 * insert_node - Inserts a node with a given number into a sorted linked list
 * @head: A pointer to the head of the linked list
 * @number: The integer value to be added to the linked list
 *
 * Description: This function inserts a new node with the specified number
 *              into a sorted linked list while maintaining ascending order.
 *
 * Return: If successful, a pointer to the newly inserted node. If memory
 *         allocation fails or other errors occur, returns NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
