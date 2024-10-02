---
title: Programming tip
date: 2024-10-02T09:00:00.000+08:00
draft: false
featured: false
---
Programming tip: differentiate indexes and counts in code.
Index starts at 0, count starts at 1.
Count is also equal to array length.
In python, one can do this
```py
for count, fruit in enumrate(fruits, start=1):
```
This has saved me a lot of confusion.
