---
title: "Programming tip: build trust on documentation"
date: 2024-11-18T10:50:00.000+08:00
draft: true
featured: false
---
There are comments I skip reading. What I found helpful was to make sure all comments are only the ones necessary to understand the context of a code.

\- Once trust is broken, documentation will be skipped.

\- As short as possible but still easy to understand. Concise

\- Mostly should be 'why' a code was added. E.g. a seemingly unnecessary log that was placed for data recovery purposes.

\- Can also be 'what' the code does. But strongly against it because it needs to be updated when the code is updated, it's more reliable to read the code (trusting the code more than docs is expected of programmers).

\- A format can make things easier to find, and thus increase trust. \`// Safety for path with spaces\` vs \`// safety for path with spaces\`. I find that starting with an uppercase letter makes the comment easier to spot and separates the two languages: code and English.
