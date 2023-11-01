#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node in a sorted
 * linkedlist
 * @head: pointer to the first node in the list
 * @number: value to store the node number memeber
 * Return: pointer to the newly created node
 */
listint_t *insert_node(listint_t **head, int number)
{
	/**
	 * steps
	 * -----
	 * Make a new node with the members having the values
	 * first traverse through the whole list
	 * at each node compare the current and the next node number member
	 * if it falls between the range insert the node inside that range
	 * update the linked list
	 * if the current->number <= new_node->number && new_node <= ahead->number
	 * then insert the new_node there
	 * temp = current->next
	 * current->next = new_node
	 * new_node->next = temp
	 */
	listint_t *current = *head, *ahead = (*head)->next, *temp = NULL;
	listint_t *insert_new_node = malloc(sizeof(listint_t));
	/*   current      ahead   */
	/*|---Node---||---Node---||---Node---||---Node---|*/
	if (!insert_new_node)
	{
		perror("malloc failed");
		return (NULL);
	}

	insert_new_node->n = number;
	insert_new_node->next = NULL;

	while (current->next && ahead->next)
	{
		if (current->n <= insert_new_node->n && insert_new_node->n <= ahead->n)
		{
			temp = current->next;
			current->next = insert_new_node;
			insert_new_node->next = temp;
			return (insert_new_node);
		}
		current = current->next;
		ahead = ahead->next;
	}
	return (NULL);
}
