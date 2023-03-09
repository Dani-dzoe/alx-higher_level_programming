#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly-linked list
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert
 * Return: if the functions fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new:

	new = malloc(sizeof(listint_t));	
