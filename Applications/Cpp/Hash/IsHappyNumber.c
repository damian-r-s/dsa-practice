#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int digitSquareSum(int n)
{
    int sum = 0;
    while (n > 0)
    {
        int digit = n % 10;
        sum += digit * digit;
        n /= 10;
    }

    return sum;
}

typedef struct node_t
{
    int val;
    struct node_t *next;
} node;

typedef struct
{
    node **buckets;
    int size;
} hashset;

hashset *create_hashset(int size)
{
    hashset *hs = malloc(sizeof(hashset));
    hs->buckets = calloc(size, sizeof(node *));
    hs->size = size;
    return hs;
}

void remove_hashset(hashset *hs)
{
    for (int i = 0; i < hs->size; i++)
    {
        node *cur = hs->buckets[i];
        while (cur != NULL)
        {
            node *tmp = cur;
            cur = cur->next;
            free(tmp);
        }
    }

    free(hs->buckets);
    free(hs);
}

void hashset_add(hashset *hs, int val)
{
    int hash = abs(val) % hs->size;
    node *cur = hs->buckets[hash];
    while (cur != NULL)
    {
        if (cur->val == val)
        {
            return;
        }
        cur = cur->next;
    }
    node *new_node = malloc(sizeof(node));
    new_node->val = val;
    new_node->next = hs->buckets[hash];
    hs->buckets[hash] = new_node;
}

bool hashset_contains(hashset *hs, int val)
{
    int hash = abs(val) % hs->size;
    node *cur = hs->buckets[hash];
    while (cur != NULL)
    {
        if (cur->val == val)
        {
            return true;
        }
        cur = cur->next;
    }
    return false;
}

bool isHappy(int n)
{
    hashset *seen = create_hashset(2000);

    while (n != 1)
    {
        n = digitSquareSum(n);
        if (hashset_contains(seen, n))
        {
            remove_hashset(seen);
            return false;
        }

        hashset_add(seen, n);
    }

    remove_hashset(seen);
    return true;
}

int main(void)
{
    return 0;
}