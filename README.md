# chunked

Split a list into pieces of `size`. The last piece may be shorter.

```python
from chunked import chunks, chunk_count

chunks([1, 2, 3, 4, 5], 2)
chunk_count([1, 2, 3, 4, 5], 2)  # 3
```

```bash
python -m unittest test_chunked.py
```

MIT
