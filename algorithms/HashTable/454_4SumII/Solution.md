# 454_4SumII

This question can be simply use Hash Table to fix it. Using conventional thinking, it needs traverse four arrays, and calculate each sum of elements from these four arrays. Therefore, the time complexity is O($n^4$). However, use hash table can square root the question (and the time complexity). To set the sum of any two arrays (To generally speaking, suppose these two arrays are A, B) in a hash table. The key of the hash table is the sum of the combination elements of these two arrays, and the value is the number of occurrences of the key. It likes:

```python
hash_table = dict()
for a in A:
	for b in B:
    hash_table[a+b] = hash_table.get(a+b, 0) + 1
```

After set the hash_table, use the remaining half arrays to match the hash_table's value. To calculate the sum of the combination elements of array C, D. If the sum is the opposite value of any key in hash table, add the corresponding value in the hash table to the accumulated number.

```python
count = 0
for c in C:
	for d in D:
    count += hash_table.get(-(c+d), 0)
        
return count
```

