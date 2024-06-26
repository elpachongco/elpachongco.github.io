---
layout: post
title: Process
date: 2024-06-15T21:32:00.000+08:00
draft: false
featured: true
---
I've been developing applications for around 3 years now. Mostly just for fun, and for my personal use. But now, with a new job, I have to work with a team.

In this job, I noticed myself making a lot of small mistakes repeatedly: Forgetting to push commits before asking for code review, forgetting to set a variable to False before pushing, or outright forgetting to test before pushing.

A kind coworker, understandably, probably got tired of me making these small mistakes and offered help. We did a one-on-one chat, and he asked some questions. It basically felt like being debugged.

![stick figure man standing beside human lying in the bed with a 'bug' coming out.](img/human-debugging-human.jpg "Human debugging human")

The most important part of our conversation was when he asked me to outline what I do when I work, from start to finish. So I thought it through, outlined my rough steps when working, and came up with the steps on the fly by thinking of what I always do.

Why am I telling this? Because he asked me exactly if I just came up with it from memory. I did, and that's the problem. I was only relying on memory - which is unpredictable (well, it's probably predictable by how much sleep I had). 

From my outline he mentioned things that I missed and gave me an example. We wrote it down, and turned the steps into checklist items. This file is now known as 'workflow.md'. It contains a simple checklist of the ideal process:

```
- [ ] When starting a task, create a Trello card.
- [ ] After creation of a card, create a Slack thread.
- [ ] Ask questions/gather data:
  - [ ] How often will this be used?
  - [ ] How many users will use this feature?
 ...
 - [ ] After working on a task, list all features added
 - [ ] Test all the features
 - [ ] List all existing features that are affected of the changes
 - [ ] Test them as well
 - [ ] If a test fails, revise code
   - [ ] Test feature again after revising
 - [ ] If all tests succeed, review the code
 - [ ] Ask questions
   - [ ] Are the variables named properly
   - [ ] Are the comments formatted according to standard
   
```

When I start a new task, I copy this file to /tmp/ and go through the items one by one. By following a document, and not relying on memory or instinct, mistakes are lessened.

But the best part is that this file can be enhanced. Whenever we make a mistake, we ask ourselves, is this a mistake that could have been prevented by a better process? If yes, we revise the workflow file.

For example, a task I worked on nearly required a redo because there's a step I missed. I forgot about it and it's not in the workflow file. So I added it to the file. By doing this we're reducing the amount of small issues that could easily be prevented by not relying on memory alone. 

If you're going to build a workflow/process file, here's a tip:

* Consider previous mistakes and add a check for what caused the mistake. 

Some examples:

* If you're forgetful or careless, like me, then add a double check to your process. 
* If you tend to over engineer stuff, then add a part where you gather data (i.e. ask questions) and define requirements before working on a task.

Having a defined process improves efficiency. It's much better than relying on memory alone because it can easily be replicated, improved and reviewed. It's not a solution for everyone or every scenario but I think it's worth trying out.
