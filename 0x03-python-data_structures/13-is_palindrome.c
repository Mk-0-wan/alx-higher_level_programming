#include "lists.h"

/**
 * is_palindrome - checks whether the list is a
 * palindrome or not (if it mirrors itself)
 * @head: pointer to the first node in the list
 * Return: 0 if true 1 if false
 */
int is_palindrome(listint_t **head)
{
	/**
	 * make a reversed list first
	 * and an original list
	 * now loop
	 *            s_head == r_head
	 * 1 -> 2 -> 3 -> 4 <- 4 <- 3 <- 2 <- 1
	 *
	 */
	listint_t *head_node = *head;
	listint_t *tail_node = *head;
	listint_t *rev_head = NULL, *prev = NULL;
	/* for reverse list */
	if (!*head)
		return (1);
	/* start from the last point of the list */
	while (tail_node)
	{
		rev_head = tail_node->next;
		tail_node->next = prev;
		prev = head_node;
		tail_node = rev_head;
	}
	tail_node = prev; /* move to the last node in the list */
	while (head_node != NULL && tail_node != NULL)
	{
		if (head_node->n != tail_node->n)
			/* yes it's not a palindrome*/
			return (0);
		head_node = head_node->next;
		tail_node = tail_node->next;
	}
	return (1);
}
