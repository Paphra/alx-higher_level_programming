#include "lists.h"

/**
 * check_cycle - checkes whether a linked list has a cycle in it
 * @list: the head of the list
 * Return: 0 if has no cycle
 *	1 - if it has one
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
