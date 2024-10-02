---
title: "TIL: `tac` command"
date: 2024-09-30T09:20:00.000+08:00
draft: false
featured: false
---
`tac` is like `cat` but the output is reversed.

I used it for finding the most recent error log:

```

tac err.log | grep -m 1 ERROR

```

[source](https://www.unix.com/shell-programming-and-scripting/140254-grep-only-last-occurred-error-error-log.html)
