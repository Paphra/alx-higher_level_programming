#include "lists.h"
#include <stdio.h>

/**
 * len - length of the linked list
 * @head: pointer to the start
 *
 * Return: number of items
 */
int len(listint_t **head)
{
	int l = 0;
	listint_t *elem = *head;

	while (elem != NULL)
	{
		l++;
		elem = elem->next;
	}
	return (l);
}

/**
 * is_palindrome - checkes whether a linked list is a palindrome
 * @head: the pointer to it's start
 *
 * Return: 0 if it is not, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j;
	int size = len(head);
	int *list;
	listint_t *elem;

	if (size == 0)
		return (1);

	list = malloc(sizeof(int) * size);
	if (list == NULL)
		return (0);
	elem = *head;
	while (elem != NULL)
	{
		list[i] = elem->n;
		elem = elem->next;
		i++;
	}

	i = 0;
	j = size - 1;
	while (i <= j)
	{
		/* printf("== %d <> %d ==\n", list[i], list[j]); checking one two*/
		if (list[i] != list[j])
			return (0);
		i++;
		j--;
	}

	free(list);

	return (1);

}
