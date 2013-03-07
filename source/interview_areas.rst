Interview Areas
===============

Our engineering interview process covers several broad areas:

* **Technical chops:** the "software" part of software engineering

  * **Architecture:** working on complex systems as a whole
  * **Coding:** working on individual components
  * **Domain expertise:** specific knowledge of tools, languages, environments, etc.

* **Commercial software development:** the "engineering" part of software engineering

  * **Process:** commercial development processes and release cycles
  * **Team-sized projects:** tools and techniques for complex projects

* **Non-technical skills:** Will they enjoy working here? Will we enjoy having them work here?

* **The candidates' questions:** What they ask you can be as telling as how they answer your
  questions.

Obviously, there's no way that every interviewer could cover all these areas in an hour. The
areas are divided up between interviewers---as explained later in the
:doc:`"process" <interview_process>` section.


Technical
---------

Architecture
^^^^^^^^^^^^

Architecture interviews assess the candidates' ability to work and think at the "whole-system"
level.

Architecture is not just for senior-level engineers. Junior engineers should understand how the
pieces they worked on fit into the overall project, even if they wouldn't know how to design the
system from scratch.

* Ask them to select a complex system they've designed/worked on, and have them explain to you
  how the major pieces fit together.
* Get some sort of boxes-and-arrows diagram. What you're looking for is the ability to
  communicate the components of a complex system---not any particular diagramming methodology.
  (It's a good sign if they naturally gravitate to the whiteboard; if not, prompt them.)
* Find out what parts of the system they worked on, and how their pieces interfaced with the
  others.
* Dig deep into pieces they worked on, but also dig into pieces they didn't work on. It's a great
  sign if their knowledge extends beyond their own areas of responsibility.
* What were the requirements for the system? (You may not need to ask this---better engineers
  will slip requirements into the discussion along the way.)
* Propose a requirements change, and discuss how they'd adapt the system to the new requirements.
* Why did they make the design choices they did? What were the tradeoffs? (If they didn't design
  the system, can they explain the decisions that were made anyway?)
* Looking back, what would they change about the design? What parts worked particularly well or
  particularly poorly?

Using a design problem
""""""""""""""""""""""

Rarely, you may come across a candidate whose previous projects just aren't complex enough for a
meaningful architectural interview. In this case, you can give them a design problem. But this
is not ideal, for several reasons:

* It's tricky to find a good architectural problem where candidates can grok the requirements
  quickly and fit the design and discussion into a reasonable time.
* It's extremely high-stress for the candidate. Some highly-qualified candidates just won't do
  well on a design problem interview.
* Since you're not talking about a real system, you can't explore what went wrong or what they
  would change.

If you must use a design problem in an architectural interview, here are some tips:

* Deliberately under-specify the requirements. Do they ask you to clarify requirements,
  or do they just make assumptions?
* Give them time to think about their design---at least 10--15 minutes---before forcing them to
  explain it to you. Offer to leave the room so they can think (and draw at the whiteboard).
* Pick something you've worked on before, so that you know the parameters and pitfalls. (But make
  sure it's general enough that the candidate can understand it. And don't expect the candidate
  to immediately intuit something that took you weeks to figure out.)


Coding
^^^^^^

Coding interviews cover the candidates' ability to conceive and write great code. You can get
through an architectural interview without seeing a single line of (pseudo-)code; the opposite is
true for a coding interview.

Algorithms and logic
""""""""""""""""""""

Can they construct an algorithm? Do they understand basic logic?

* Design problems lasting about 10--15 minutes are completely appropriate here.
* How they approach the problem can be as interesting as whether the solution is correct.
  Under-specify the requirements and see if they prompt you for more details or just make
  assumptions.
* You can also get them to talk about an elegant algorithm they designed in a past project. Tip:
  confusing and baroque is not elegant. Good sign: complex problem, simple solution.
* Try to avoid questions where the answer is trivial if you know the trick---these don't tell you
  a lot about the candidate (other than what trick answers he or she already knows). A lot of
  "brain-teaser" type questions fall into this category.

Robustness
""""""""""

* How does their code account for errors and exception conditions? (Best to ask what they've
  actually done on past projects, rather than what they would do.)
* What are plusses and minuses of their approach? Did everyone on the team adopt it?
* When have they refactored code, and why? Have they made continuous,
  incremental improvements to the code they've touched, or do they like to replace things
  wholesale? Or do they prefer a copy-and-paste approach?
* Have they taken any steps or created any systems to prevent errors from occurring,
  or to detect them early? (The answer may involve unit testing, "asserts", debug-only code,
  test harnesses, internal self-validation, etc.)
* What approaches have they favored for tracking down bugs? (Their own or other coders' bugs.)
  Can they follow a coherent diagnostic plan to fix the root cause,
  or will they “play Whack-a-Mole" with our code and introduce as many bugs as they fix?

Programming
"""""""""""

* Are they religiously locked into a single language or platform, or have they demonstrated the
  ability to move between environments as the needs arise?
* How have they applied design patterns? Is the approach thoughtful and intended to address
  specific needs, or do they sprinkle inappropriate design patterns throughout their code in the
  hope of achieving magic results?
* Do they understand the differences between object-oriented, procedural, declarative,
  functional, and other types of programming? (Even if they don't use those terms.) Are they
  locked into a single approach, or more flexible? Have they created domain-specific languages to
  address particular problems?
* What do they understand (or not) about multithreading? Asynchronous processing,
  remote procedure calls, event-driven programming? [Other specific areas we'd like to dig into???]

Performance, scalability, and security
""""""""""""""""""""""""""""""""""""""

* What performance and scalability issues have they encountered? How did they discover them and
  track down the causes? How did they address them?
* When and how do they optimize their code? In the design stage? Everywhere throughout the code?
  Only in specific areas where they had problems? Based on rumors?
* Do they understand the difference between performance, availability, and scalability?
* What security concerns have been important in their coding? What's their level of awareness of
  security issues, and how have they avoided them? (There may also be specific security areas your
  team will want to dig into as part of "domain expertise", in the next interview. E.g., web
  engineers should be aware of SQL injection attacks as part of their web domain expertise.)


Domain Expertise
^^^^^^^^^^^^^^^^

Specific domain expertise is mainly useful as an indicator of what the candidate has learned in
the past, and what they are therefore capable of learning in the future.

Domain expertise goes stale quickly, and our business is constantly changing. Being (e.g.,)
an expert C# programmer who has a deep understanding of all of .Net's quirks is not sufficient
qualification to be a Rock Star Engineer. (What if we need to work in Java next month? Or
ActionScript?)

But having said that, it's definitely a red flag if the candidate shows a complete lack of
expertise in any relevant domain.

* Find out how they acquired their domain expertise. E.g., "what technical area have you learned
  about most recently, why did you need to learn it, and how did you learn it?" Good answer: "I
  realized Python was the best tool to build the management console, so I got a book and filled in
  details by searching online." Not-so-good answer: "my company sent me to two years of
  ActionScript classes."
* If you're going to ask about quirks of a particular environment, be certain that those quirks
  are ones that any engineer would *absolutely* have to know to be successful in that environment.
* "I don't know exactly, but here's where I'd find the answer" is often a fine answer to a
  domain-specific question.
* Does their knowledge cover a breadth of domains (tools, programming languages, environments,
  etc.)? Have they shown a consistent history of picking up new domains? These are some of the
  best predictors of a candidate's ability to succeed.


Commercial Software Development
-------------------------------

Commercial software development is all about the difference between tinkering and shipping. In
our industry, it doesn't matter how brilliant and elegant your code is if it never ships,
if it doesn't fill a real need,

Get the candidates talking about what they've actually done, not how things should be done.
Although you can learn about best development practices in school or from books,
you don't truly know them until you've been through the process.


Process and Schedule
^^^^^^^^^^^^^^^^^^^^

* Do they understand the commercial software development cycle? Do they use an Agile approach,
  or a waterfall one? (And are they religious about it?) How do they define "done" (or alpha,
  beta, release, etc., if those terms applied to their approach)?
* What kind of schedule was their last project on? Did it last weeks, months, or years?
* Have they ever worked on a project that shipped late? Failed to ship at all? What happened,
  and why? (And if all their projects shipped on time, to what do they credit that success?)
* How did specifications fit in? Who wrote them? How were changes handled? (Both too much and too
  little are bad. Really experienced engineers should understand how the process changes as
  companies and products mature.)
* What were QA's responsibilities? How did they interact with QA? What do they expect out of a QA
  team?
* Where did project management and/or program management fit in?
* What other groups in the company have they interacted with, and what was that experience like?
  Product management? Documentation? Marketing?
* How did their endgames work? What kind of effort did they (personally) have to put in to get
  the product out the door? How did they (team or personally) manage change and minimize risk
  during the endgame?
* What were some tradeoffs they had to make during the process? What bug did they feel worst
  about deferring, and why did they defer it anyway? (Candidates who think software ships without
  bugs won't be happy in the real world.)
* What have they learned from projects they've shipped? What would they change on their next
  project?


Team-Sized Projects
^^^^^^^^^^^^^^^^^^^

There are substantial differences between working alone and working on a team. You'll want to
make sure that candidates will be comfortable working on your code,
and you'll be comfortable working on theirs.

* Have they worked on team projects? How big was the team? How big was the codebase?
* What was the division of labor? Did it change between releases? During the course of a single
  release?
* What tools did they use to help manage team-sized projects and codebases? Did they (personally)
  create any tools or processes to improve team efficiency or code quality?
* What bug tracking systems have they used? Plusses and minuses?
* What revision control systems have they used? Positives and negatives? (Aside: using revision
  control even on non-team projects is a great sign.)
* How will they feel about working with existing code? (You won't get a real answer if you ask
  this outright. Try digging into past situations where they've inherited code and what that
  experience was like for them.)
* What tools and techniques did they use to assure quality? (Continuous integration? Code
  reviews? Debugging libraries? Etc.)
* Have they ever rewritten a major section of the code during a release (or over the course of
  multiple releases)? What kind of planning went into that? How did it work out?


Non-Technical Skills
--------------------

Team and Company "Fit"
^^^^^^^^^^^^^^^^^^^^^^

"Fit" is one of those areas that's tough to describe, but you'll know it when you see it.
Everyone on the interview schedule will be assessing team fit. And the team should discuss
(before the interviews begin) what qualities are important to them.

In addition, there are a few specific qualities that we're always looking for, in any engineer,
and the hiring manager should be sure to probe these areas:

* Passion: Does their enthusiasm for what they're been doing show? Is it infectious? Will they
  get as excited about working here? Or is it just a paycheck?

* Drive and endurance: We're a high-intensity company working in a competitive space. Do they
  thrive on that kind of environment, pace, and pressure? Or would they be happier at a larger,
  more-structured, slower-moving company? (Also, do they have the self-awareness to avoid burning
  out?)

* Self-direction (and leadership potential): How do they respond to unclear, conflicting,
  or missing direction? Will they set out to proactively resolve issues and drive their area of
  the product forward, or will they wait to be told what to do? Over time, will they establish an
  area of technical leadership and become a resource to the team?

  (Obviously there are different expectations here based on their seniority, but you should be on
  the lookout for leadership potential at any level.)

* The right blend of humility and arrogance: This is a tricky balance, and a well-functioning team
  can handle a variety of engineers throughout this spectrum. But you want to avoid the extremes.

  Some level of arrogance isn't uncommon---Rock Stars tend to be aware of their skills. But nobody
  wants to work with an engineer who won't listen to others' thoughts and who won't function as
  part of a team. At the opposite end, an engineer won't be effective if they're so humble that
  they'll never speak up and defend their own ideas.

  (But a big red flag: if you hear the candidate attacking people on a personal level, rather than
  attacking ideas, that's not going to work out. "That was an idiotic idea" is OK; but "she was an
  idiot for proposing that idea" has no place in our team.)


Communication
^^^^^^^^^^^^^

Everyone on the interview schedule should be looking at candidates' communication skills.

* Is their communication "high bandwidth"? Do they express their thoughts clearly? Do they get
  what you're saying quickly? Will you have to slow down to communicate with them? Will you try to
  avoid meetings with them?

* Do they listen to what you ask/say? Do their responses indicate they've understood you? Do they
  ask for clarification when they don't? Or do they make assumptions? Will the ideas of other
  engineers on the team get a fair hearing, or be immediately dismissed?

* Can they use the whiteboard effectively?

* Do you leave the interview feeling that you've had a conversation? A fruitful exchange of ideas?

* Our engineering teams are often split between locations and time zones. Have they worked with
  geographically-dispersed teams before? How did it work for them? What are their concerns about
  it?


Candidates' Questions
---------------------

Be sure to leave some time to answer the candidate's questions during the interview. Everyone
should allow 5--10 minutes for this, and hiring managers substantially more. (However, later
interviewers will tend to find the candidates' questions have been answered in earlier sessions.)

You can often learn as much about a candidate from the questions they ask as from the answers
they provide you. Candidates' questions will reflect their immediate concerns from their current
job. (People who are good at interviewing will also ask questions that point out their own
strengths, so don't necessarily read too much into what they ask.)

Candidates' questions are a good opportunity for you to sell the company and the position. Be
prepared to answer questions such as:

* "What's it like to work here?"
* "What do you see as most important for this job?" (Experienced candidates will ask this of
  everyone they talk to, and compare the answers.)
* "Why did you want to work here?"
* "What's it like to work for (the hiring manager)?"

Even as you're selling the company, you should represent things accurately. We can determine
whether candidates are a good match for us, but we largely rely on their judgment to figure out
whether our company is a good match for them. Candidates need an accurate picture of the company
to be able to make this decision for themselves.
