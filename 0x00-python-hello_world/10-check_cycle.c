#include "lists.h"

/**
 * check_cycle - A function that checks  if a singly linked list has a cycle in it.
 * @head: Head of the list
 * Return: 0 if no cycle present, 1 otherwise.
 */

int check_cycle(listint_t *head)
{
	listint_t *hare = head, *tortoise = head;

	if (!head || !(head->next))
		return (0);
	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
