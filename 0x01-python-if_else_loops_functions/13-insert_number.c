#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a new node at a given position
 * @head: pointer to the pointer of the first element of the list
 * @number: the data of the new node
 *
 * Return: address of the new node, else NULL if failed
 * - also return NULL if can not be added
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *elem;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
	} else
	{
		elem = *head;
		while (elem && elem->n < number)
			elem = elem->next;

		if (elem == NULL)
		{
			elem = new;
			new->next = NULL;
		} else
		{
			new->next = elem;
			elem = new;
		}
	}

	return (new);
}
