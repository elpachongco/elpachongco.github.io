---
layout: post
title: Design for HTML, not JS
date: 2025-04-25T20:24:00.000+08:00
draft: true
featured: false
---
__this is a draft. thoughts are not final.__

The only thing separating you from the pain of JS and the joy of HTML is the way you design web applications.

Web developers dream of native app like behavior for their websites by designing  SPAs that mimic native apps. But the reality is, web has a different architecture and it should have its own design. In fact, it already has. It's forms. Everything should be a form.

HTML is very easy to work with. Anecdotally, I use Django to create web applications. With it, one only has to create a route, create data models, create logic, create templates and the web app is finished. UI may be boring, but it is finished. Boring is good anyway.

Developers don't seem to realize how perfect this workflow is. In pursuit of a flashy UI and the fear of not having enough control, they resort to ignoring most of the conveniences given by the framework to roll custom validation, fetching, error handling and so much more.

At first it would be difficult to imagine this. Most modern apps today are designed with JS in mind. It may require a rewire to think differently.

Here's how a notes app will be made normally:
1. A page listing all the notes 
2. A button showing 'add note' in the page
3. Clicking the button will add a new note entry to the page with a 'title' and a 'body' field.
4. Buttons showing 'Save' and 'Cancel' appears while editing the page
5. Clicking 'Save' will save the note and add it to the list of notes.

All of these is done without a single page refresh. 

Now let's redesign this app but this time keeping in mind to not use JS
1. A page listing all the notes
2. A button showing 'add note' in the page
3. Clicking the button will redirect you to the 'Add note' page
4. The page has 'title' and 'body' fields
5. Buttons showing 'Save' and 'Discard' are also in the page
6. Clicking 'Save' will save the note, and redirect you back to the page listing the notes containing the newly-created note.

Now the first app may seem smooth and straightforward. But realize this, it will only be smooth and straightforward if you make it to be. It is smooth in the planning phase. You'll have to take care of each functionality to make sure these work smoothly. 

More importantly, the amount of work to do it is not sustainable for a single-person. The notes app may seem simple but scale that to a more complex app, and you'll be spending half your time debugging every code you write and then debugging it again every time you touch it.

Doing it in plain HTML does not need that amount of effort because it utilizes code that have already been written by others and behavior that come with the browser.

I'm not saying everyone should use this model but try it and you'll realize just how much time you're wasting.

I have recently tried to contact a repair shop and one of the ways to do it was through their FB messenger chat bots. I didn't expect a good UX but it was straightforward and did what I needed it to do.
