#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: first node of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *previous, *last_node = *head, *first_node = *head;
	int check, idx = 0, len = 1;

	if (*head == NULL)
		return (1);
	while (last_node->next != NULL)
	{
		len++;
		previous = last_node;
		last_node = last_node->next;
	}
	if (len == 1)
		return (1);
	if ((len % 2) != 0)
		return (0);
	for (; idx <= (len / 2); idx++)
	{
		if (first_node->n == last_node->n)
			check = 1;
		else
			return (0);
		if (first_node->next == NULL)
			break;
		first_node = first_node->next;
		last_node = previous;
		previous = *head;
		while (previous->next != last_node)
			previous = previous->next;
	}
	return (check);
}
