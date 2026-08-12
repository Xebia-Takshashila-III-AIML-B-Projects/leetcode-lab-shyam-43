# Editorial

## Idea

The minimum changes only when a smaller value is inserted.

Instead of searching every time,

store the minimum seen so far along with every value.

Each stack element stores:

```
(value, minimum_until_here)
```

Example

```
push(5)

[(5,5)]

push(2)

[(5,5),
 (2,2)]

push(4)

[(5,5),
 (2,2),
 (4,2)]
```

Now,

Top

```
O(1)
```

Pop

```
O(1)
```

Minimum

```
O(1)
```

---

## Complexity

| Operation | Time |
|-----------|------|
| push | O(1) |
| pop | O(1) |
| top | O(1) |
| getMin | O(1) |

Space:

```
O(n)
```

---

## Learning Outcome

This problem teaches:

- Stack design
- Auxiliary information
- Constant-time retrieval
- Space-Time tradeoff
