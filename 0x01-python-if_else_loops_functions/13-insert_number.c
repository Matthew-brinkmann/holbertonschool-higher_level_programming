#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * build_node - insert a node in a sorted list
 *
 * @too: when this node points too
 * @number: the valuse used to list place and to add as value into list element
 *
 * Return: address to new element
 */
listint_t *build_node(int number, listint_t *too)
{
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = too;

	return (new);
}

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
	if (*head == NULL)
	{
		new = build_node(number, NULL);
		*head = new;
		return (new);
	}

	search1 = *head;
	search2 = *head;
	if (search1->n >= number)
	{
		new = build_node(number, search1);
		*head = new;
		return (new);
	}

	while (search2->n < number && search2 != NULL)
	{
		if (search2->next == NULL)
			break;
		search2 = search2->next;
		if (search2->n < number)
			search1 = search1->next;
	}

	if (search2->next == NULL)
		return (add_nodeint_end(head, number));

	new = build_node(number, search2);
	search1->next = new;

	return (new);
}
