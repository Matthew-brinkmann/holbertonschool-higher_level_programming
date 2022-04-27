#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a node in a sorted list
 *
 * @head: the pointer to the first element in the list
 * @number: the valuse used to list place and to add as value into list element
 *
 * Return: address to new element or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *search1 = NULL, *search2 = NULL, *new = NULL;

	if (head == NULL)
		return (NULL);
	search1 = *head;
	search2 = *head;

	while (search2->n < number && search2 != NULL)
	{
		if (search2->next == NULL)
			break;
		search2 = search2->next;
		if (search2->n < number)
			search1 = search1->next;
	}

	if (search2->next == NULL)
		return(add_nodeint_end(head, number));

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	search1->next = new;
	new->next = search2;

	return (new);
}
