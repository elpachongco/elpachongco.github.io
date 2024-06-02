---
date: "2023-09-21T22:18:32Z"
title: Building a New Social Media Platform
---
I recently created a [/shorts/ page in my blog](https://elpachongco.github.io/shorts/). This page is intended for shorter content. It's a place I can use to share memes, tips, and small stories.

![](/img/uploads/elpachongco-shorts.png)

> My blog's shorts page.

I liked the idea of this. I thought it's a good way to use the blog as my own twitter of sorts.

And then I had an idea: If I encourage people to create a /shorts/ page on their blog, and I create a central hub for these pages, where they can interact, we basically have a new twitter!

And that's what I've been doing since August.

I've been building a website that will be a central hub for blogs. The website is called [bhread.com](https://bhread.com). Yes, it's pronounced like bread.

For this project, I wanted to try building a full-fledged application in Django. I have some experience with django rest framework so I thought plain Django would be familliar. I was wrong. Templates are hell.

Anyway, I found out about htmx and I really wanted to try it. I also wanted to  try [alpine.js](https://alpinejs.dev/) and tailwind. I'm used to plain css because I haven't done any project that requires a lot of styling. I usually use a UI library.

### Development

So I got into developing this project. I started with planning the application, and then I wrote it.

The planning part wasn't thorough enough as I didn't know what is needed to aggregate blogs. I don't have an idea about parsing feeds. But I knew I should store urls of feeds and posts.

At first I was conflicted whether to require accounts for feed submissions.  But I went straight to programming anyway. I figured that I should just write a kind of exploratory project to just know enough to be able to iterate to a better version. I wrote an initial version as fast as possible. In the end, I went through three iterations of data models to finally determine the best design.

The code was very unorganized but it helped me determine the requirements.

![](/img/uploads/bhread-initial-version.png)

> The initial bhread design. Thanks to water.css and material icons for its looks.

I showed it to some friends and there was not a lot of reaction. It's to be expected for an early product but it made me realize that this UI will not work for everyone. I like it because I like reading. It's my job to read. Hacker News looks like a big wall of text to other people. This looks like a wall of text.

To start the new iteration, I removed a lot of the code, and made new plans. This time, the UI is inspired by twitter and elk.zone (a mastodon client).

I tried a few designs. At first, I designed with CSS but I got tired easily and thought I needed to design it properly first before programming.

I used figma to design some components and the experience is really good. I used to do these things in Illustrator and I'm glad I tried out figma.

![](/img/uploads/bhread-design-figma.png)

> Bhread's prototype components. These are the basis for the current website's designs. I abandoned some of the ideas here as they're too distracting and it consumed a lot of space in the user's screen.

I discovered a youtube channel that's focused on recreating UI of famous sites. I watched his videos and I can highly recommend it. It's [Demistifying Design on Youtube](https://www.youtube.com/@DemystifyingDesign). I learned a lot of UX concepts by watching the videos.

After deciding on the look of the website, it was time to implement.

This is the first complicated project where I'm not using a UI library. CSS is too hard for me. I'm using tailwind to develop this site and I like it. Sure, it's discouraging to open an html file and see really long lines of tailwind classes but it's easier to debug because the style is directly in the html element. My only problem is that the tooling with django is not fully developed. The prettier plugin for arranging tailwind classes does not work on django templates.

Playing with HTMX for a bit, I realized how easy it makes the backend-frontend integration. It's amazing. Like everybody else, I used to build a frontend app and a json API for my web applications. I'm too tired of it. This is why I wanted to try HTMX. The only problem I see with using HTMX is if I want to create mobile apps for bhread, I will have to create a JSON API anyway.

I haven't used [[Alpine.js](Alpine.js)](Alpine.js) a lot as of now but I'm so excited to use it. Once I get the layout sorted, I'll start scripting.

### Deployment

I usually use python-poetry for development but I decided to learn docker for this project. It's amazing. The code will still work with poetry but it's so much easier to use docker. I decided to deploy with docker as well and apart from the mistakes I made while learning docker and deploying a django project at the same time, it's working pretty well. With a single command, I can start postgresql, redis, nginx, and gunicorn. The project runs on a $6 digital ocean droplet. I don't know how it will handle a lot of traffic but that's a problem I'm excited to have. Right now it's scary that it's using 800mb of ram on idle, with only me as the user. I'm still looking into it.

### To open source or not?

Initially, I planned on open sourcing it after a year of development. I didn't want to reveal the idea to the public until I'm sure it's ready. But I thought I should just get the site out there and build a community around it as early as possible.

One concern about open sourcing the project is monetization. I was scared that I might not be able to monetize it if I open source it. Sustainability is a big part of a project. I sure as hell won't be putting ads on it. It runs on a $6 machine, I can afford that. So that's not a problem right now.

![](/img/uploads/bhread-to-hn.png)

> Me doing a shameless plug on HN. It's a post about webrings. I couldn't resist.

That's it for now, this is what the website looks like right now (Sept 21, 2023):

![](/img/uploads/bhread-screenshot-09-21-2023.png)
It's getting pretty close :D

Bonus:

![](/img/uploads/bhread-styles-injected-fail.png)

> I forgot to sanitize the verification post. The wordpress theme of the post infected the whole site. Makes me think about the design of my code.

If you want to know more about the project, visit [[Bhread.com](Bhread.com)](https://bhread.com) or visit the [Bhread blog](https://blog.bhread.com).
