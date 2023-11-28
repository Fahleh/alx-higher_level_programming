#include "lists.h"

/**
 * insert_node - A function that adds a node in a sorted list
 * @head: Pointer
 * @n: Data to add
 * Return: Pointer to new node.
 */

listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new, *temp, *old;

	if (!head)
		return (0);
	new = malloc(sizeof(*new));
	if (!new)
		return (0);
	new->n = n;
	if (!(*head))
	{
		*head = new;
		return (new);
	}
	temp = old = *head;
	while (temp && temp->n < n)
	{
		old = temp;
		temp = temp->next;
	}
	if (old == temp)
		*head = new;
	else
		old->next = new;
	new->next = temp;
	return (new);
}
