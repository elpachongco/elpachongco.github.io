---
date: "2023-11-11T23:35:37Z"
title: I should have used the debugger
---
A week ago I was implementing a dynamic logo in a website which would change if the navbar has a dark background and change back if it's light. 

My approach was to add two `<img>` tags, overlapping each other and toggling the front element (greater z-index) when the conditions are right.

Seems good right? 

Well, It worked as expected but after some testing, I noticed something: scrolling up would lag the browser on my 4-core i7 8550u 16gb memory machine. It's probably half a second of the browser refusing to do anything before allowing me to scroll up.

Of course I immediately assumed it was the logo. Because previously, the site used plain text as its only branding. 

I immediately thought that the CSS may be causing a [DOM reflow]([https://developer.mozilla.org/en-US/docs/Glossary/Reflow](https://developer.mozilla.org/en-US/docs/Glossary/Reflow)). So I changed the logo toggle logic to use opacity, instead of `display: none`. My thinking was that it could be triggering the browser to re-validate the DOM tree every time the element is removed. I tested this, but the lag is still present with no noticeable change.

Next, I searched for ideas. The one that stood out was that maybe my selectors are too complex for this. This gave me an idea.

The implementation for the logo toggling depended on a single class that is added everytime the background changes. This behavior is handled by jquery.

My idea was to move the toggle from CSS to the jquery.

I spent some time with that and then tested it. Still no change. At this point, I'm out of ideas.

I called it a day maybe I just need to rest. 

The next day, I had an idea: why not debug this with the devtools?

I've never used the more complicated tools because honestly, flame graphs intimidate me.

Hoping to finally fix the bug, I used the performance tab and recorded a sample interaction where I scroll up and then stop the recording. The timeline shows an interesting data: when I scroll up, a task happens. This task takes a good 460ms to finish. The task is `Image Decode`.

That's when I realized what was really happening. It's doing some processing on the logo because the file I used was a PNG file. I rushed to a random svg download site and downloaded two random SVGs, replaced the image sources, and tested. I was right, the lag is gone. 


What's the takeaway from this?

Reach for the most effective tool you have before doing trial-and-error. Often times, it's easy to resort to trial-and-error approach when debugging. But knowing how long a debugging task is going to take you is a skill you should master. if you think it's going to take a long time, use the tool for the job. Use the debugger.

More importantly, keeping track of the [tools available to you](https://alan.norbauer.com/articles/browser-debugging-tricks) and being WILLING to use them when appropriate is a good habit to have. Expect yourself to resist using a debugger because it's usually not as quick to do as trial-end-error.
