#include <stdio.h>
#include "lists.h"

/**
 * reverse_listint - reverse a list order.
 * @head: the list to reverse.
 *
 * Return: none
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *rev = NULL, *next = NULL;

	if (*head == NULL)
		return (NULL);

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = rev;
		rev = *head;
		*head = next;
	}
	*head = rev;

	return (*head);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the first element in the list
 *
 * Return: 0 if not palindrome or 1 if is palindrome)
 */
int is_palindrome(listint_t **head)
{
	listint_t *move1, *move2, *prev_move1, *half1, *half2;

	if (head == NULL || (*head) == NULL || ((*head)->next) == NULL)
		return (1);

	half1 = move1 = move2 = prev_move1 = *head;
	half2 = NULL;

	while (move1 != NULL && move2 != NULL && move2->next != NULL)
	{
		prev_move1 = move1;
		move1 = move1->next;
		move2 = move2->next->next;
	}

	if (move2 == NULL)
		half2 = move1;
	else
		half2 = move1->next;

	prev_move1->next = NULL;
	reverse_listint(&half2);

	while (half1 != NULL || half2 != NULL)
	{
		if (half1->n != half2->n || half1 == NULL || half2 == NULL)
			return (0);
		if (half1 != NULL)
			half1 = half1->next;
		if (half2 != NULL)
			half2 = half2->next;
	}
	return (1);
}
