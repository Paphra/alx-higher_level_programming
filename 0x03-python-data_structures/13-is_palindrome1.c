#include "lists.h"

/**
 * is_palindrome - checks to see whether a list a a palindrome
 * @head: the pointer to the pointer of the first element in the list
 *
 * Return: 0, if it is not, and 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *next;

	if (*head == NULL)
		return (1);

	slow = *head;
	fast = *head;
	prev = NULL;
	next = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
		slow = slow->next;
	while (slow != NULL)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	slow = *head;
	while (prev != NULL)
	{
		if (slow->n != prev->n)
			return (0);
		slow = slow->next;
		prev = prev->next;
	}

	return (1);
}
