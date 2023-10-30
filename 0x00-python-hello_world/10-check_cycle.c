#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks efficiently if a linked list has a loop
 * @list: pointer to the head node of the list
 * Return: 0 if no cycle found, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list->next, *fast = (list->next)->next;
	int flag = 0;

	if (!list || !list->next)
		return (-2);

	while (fast)
	{
		if (slow == fast)
		{
			slow = list;
			while (slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}
			return (flag++);
		}
		slow = slow->next;
		fast = (fast->next)->next;
	}
	return (flag);
}
