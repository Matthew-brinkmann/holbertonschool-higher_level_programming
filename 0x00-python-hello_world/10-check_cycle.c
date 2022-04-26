#include "lists.h"
/**
 * check_cycle - checks if list has a cycle in it
 *
 * @list: the list to check if cycle occurs
 *
 * Return: 1 if list has cycle, 0 if list has NO cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *l1 = NULL, *l2 = NULL;

	if (list == NULL)
		return (0);

	l1 = list;
	l2 = list;

	while (l1 != NULL && l2 != NULL && l1->next != NULL && l2->next != NULL)
	{
		l1 = l1->next;
		l2 = l2->next->next;
		if (l2 == NULL || l1 == NULL)
			return (0);
		if (l2->next == l1)
			return (1);
	}

	return (0);
}
