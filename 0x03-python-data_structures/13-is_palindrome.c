#include "lists.h"

/**
 * is_palindrome - Checks if a list is a palindrome
 *
 * @list: Pointer to list
 * Description: List is a palindrom if it's first half
 * is the same as a reverse of its other half.
 *
 * Return: 1 if true 0 otherwise
 */

int is_palindrome(listint_t **list)
{
	int result = 1;
	listint_t *hare, *tortoise, *h1, *h2, *temp;

	if (!list)
		return (0);

	if (!(*list) || !((*list)->next))
		return (1);

	tortoise = hare = *list;
	while (hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	if (hare)
		tortoise = tortoise->next;

	h2 = reverse_listint(&tortoise);
	temp = h2;

	h1 = *list;
	while (h2)
	{
		if (h2->n != h1->n)
		{
			result = 0;
			break;
		}
		h1 = h1->next;
		h2 = h2->next;
	}

	reverse_listint(&temp);
	return (result);
}

/**
 * reverse_listint - Reverses a list
 * @h: Head
 *
 * Return: Pointer to the listt
 */

listint_t *reverse_listint(listint_t **h)
{
	listint_t *temp1, *temp2;

	if (!h || !(*h))
		return (NULL);
	temp1 = (*h)->next;
	(*h)->next = NULL;
	while (temp1)
	{
		temp2 = *h;
		*h = temp1;
		temp1 = (*h)->next;
		(*h)->next = temp2;
	}
	return (*h);
}
