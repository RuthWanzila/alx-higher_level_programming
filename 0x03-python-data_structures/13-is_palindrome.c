#include "lists.h"

/**
* is_palindrome - function to call check_palindrome
* @head: ptr to the beginning of the list
* Return: 0 if not palindrome else 1
*/
int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
return (1);
return (check_palindrome(head, *head));
}

/**
* check_palindrome - function to check if the list is palindrome
* @head: ptr to the head of the list
* @last: ptr to the end of the list
* Return: 0 if not palindrome else 1
*/
int check_palindrome(listint_t **head, listint_t *last)
{
if (last == NULL)
return (1);
if (check_palindrome(head, last->nxt) && (*head)->n == last->n)
{
*head = (*head)->nxt;
return (1);
}
return (0);
}
