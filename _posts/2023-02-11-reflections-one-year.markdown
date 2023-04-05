---
layout: post
title: "My first year of being a professional programmer"
date: 2023-02-26 21:30:26 +0800
categories: jekyll update
---

## I met my goal.

I posted a blog post on August 6, 2021 stating that I want to get a job before
april 2022. During that time, I was creating projects for my resume. I was
reading up on what people in the industry have to say about landing a job
without a degree. The most common advice is to have projects that demonstrate
my skills to potential employers.

It was an effective advice. By January I was started looking for local jobs.
February of 2022, I found a job that fit my criteria well. The interview went
well. I demonstrated some of my projects and one of their programmers asked me
programming questions. The questions were about programming best practices,
what I do when I can't solve a programming problem.

I was hired by a team of data scientists developing a product from their
university research. They're funded by the government and partnered with their
university.

Our core team is composed of 4 people. I'm the one in charged of programming the
product. Our project leader is a Cs doctorate and a professor in the university.
the working environment is what you'd expect from a government and academic
environment -- they're pretty formal, and buzzwords amaze them. Especially that
the project is focused on blockchain tech. It’s a unique experience to be
surrounded by non-programming (but otherwise technical) people speculating on
the technology.

In the office, I get to meet different kinds of people. It's great to be
surrounded by people smarter than me, especially programmers. I can ask them
advice on technical topics and most of the time that's when I learn new things.

## I have never made a complete system until now

Now that I'm hired, I realized I will be creating a complete system. I used to
only create scripts for my amusement and portfolio. Developing a whole system
-- one that should be able to perform its functions well and be easy to use is
different from programming simple scripts.

I remember being overwhelmed of how I will plan things out. As always, you'll
never realize how important planning is until you're in the middle of
development. In our case, I wasn't able to plan much because of uncertainties
on the hardware and its communications.

For context, The project is a renewable energy trading platform based on
blockchain.

The development of this project taught me a lot of things as a
programmer. I wrote code from low level hardware code, react js frontend code,
django backend code, solidity code, and bash. Bash was really useful for me
when it came to testing and automating things.

## x by example, x styleguide

Most of the software I wrote were new languages or concepts to me.

Being already familiar with multiple programming languages, reading `x by
example`, was the fastest way to get coding. Now, when I encounter a new
language, I'll read x by example. This works fine for small programs and
programming languages that I probably will not use much. Reading `solidity
by example` supplemented with the solidity style guide, I wrote decent smart
contracts (I think)

## TDD is great if the project is complex.

For complex projects such as our backend server (django), test-driven
devleopment helped a lot. I can't imagine how much time i saved by creating
tests to implement features in such a complex system. Compared to just using
`print()` like I'm used to. Now, If i'm going to work on a project where
printing will be cumbersome (solidity is another example), I will instead write
tests to develop software function by function. For simple scripts, I will
still stick to `print()`. BTW, using `debugger;` is great for frontend
javascript projects.

## Templates are great

For the frontend, we used an open source dashboard template written in react
and material-ui. This helped the project progress fast. It was better for our
small team to spend our time modifying the defaults of the template instead of
starting from scatch. Existing components were used as basis for creating our
own new components. Being written in react, any new member of the team will
most likely be able to contribute to the frontend.

## Thoughts on blockchain

Gas is still a problem. I think, currently that blockchain is great for
creating organizations because of its ability to store simple data and make it
available to everyone globally with not much infrastructure.

In my opinion, the current state of the art is only at the tip of the
iceberg of what blockchain can offer. Currently, we mostly see applications
that can theoretically be made using basic web architectures (server and
client). Blockchain only acts as improvement to the previous architectures.
Many people don't bother with it because the improvements it brings are not
worth the additional complexity that come with it.

More reasearch is needed. I can't say whether blockchain is a useless tool or
not because we still haven't discovered its true properties. The project
that I am working on made me see how it can be a useful innovation for
the technology of the incoming generation. I'll probably write a research
article about it soon.

## Failures

- Deciding architecture

  Back when we were starting to develop the project, I hit a roadblock.
  I didn't know how I would integrate the whole project. It's not that I didn't
  know what to do, I was stuck deciding which design was the best. My first
  choice was to put react inside of django so I can use django's templating
  capabilities with react. I tried that and modified a lot of code for the
  react material-ui frontend but in the end, it was janky. I realized that a
  backend server serving an api will be the better design. So I reverted most
  of the changes that I did and had the frontend and backend be separate
  entities. I'm glad that I did. The seperation made the program code cleaner
  and flexible.

  I was lucky that it was just mostly me and my other coworker doing
  development that time. the size of our team allowed us to flexibly change the
  architecture without anyone else complaining. I was really close to having a
  really bad developer experience for the rest of my time there.

- Not knowing lower-level side of computers

  Being a self-taught programmer who learned programming by creating simple
  python scripts for automation, I never really bothered to learn binary
  arithmetic and communications. That mistake hit me. I had to write programs
  for two kinds of devices which had different communications. Good thing some
  other developers created packages for easy communication with these
  hardware. I still had to learn their communication protocols and binary
  arithmetic to fully use and understand the hardware. It took me quite some
  time to learn.

- Plans after getting a job

  Before getting a job, I told myself that if I ever get one, I will work from 9
  to 5 then study more programming at home. That didn't happen. I told a
  programmer co-worker about this and they told me they actually had the same
  plans but were also not able to do it after getting hired. This led me to
  believe that having an onsite job is actually a lot more draining than working
  at home.

It's been a year now and the project is near completion. I met new people,
learned new things, encountered problems I was able to solve, and got paid. The
project is a one year contract so I'll be jobless again soon. I need to think
of another plan. Should I get a new job? Study in a university? Both?
