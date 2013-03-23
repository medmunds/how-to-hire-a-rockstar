.. _coding-interview:

The Coding Interview
====================

Coding interviews cover the candidates' ability to conceive and write great code. You can get
through an architectural interview without seeing a single line of (pseudo-)code; the opposite is
true for a coding interview.


Algorithms and Logic
--------------------

Can they construct an algorithm? Do they understand basic logic?

* Design problems lasting about 10--15 minutes are completely appropriate here.

* How they approach the problem can be as interesting as whether the solution is correct.
  Under-specify the requirements, and see if they prompt you for more details
  or just make assumptions.

* You can also get them to talk about an elegant algorithm they designed in a past project.
  Note: confusing and baroque is not elegant. Good sign: complex problem, simple solution.

* Try to avoid questions where the answer is trivial if you know the trick.
  These don't tell you a lot about the candidate,
  other than what trick answers he or she already knows.
  (A lot of "brain-teaser" type questions fall into this category.)


.. sidebar:: Open-Source Projects

    If a candidate has contributed to an open-source project, this can be a great way for you to
    get a first-hand look at their actual code.

    But don't just let them point you at GitHub and leave it at that.
    Use their public code as the basis for this coding interview.

    (Think of it a bit like you're conducting a code review with a new engineer.)


Robustness and Maintainability
------------------------------

* How does their code smell? (Try to start with what they've *actually done* on past projects,
  not just what they *would* or *should* do. Hypotheticals tend to be rose-scented.)

* How does their code account for errors and exception conditions?

* When, how, and why have they refactored code?
  Have they made continuous, incremental improvements to the code they've touched?
  All-at-once replacements of major subsystems?
  (With the rest of the team's cooperation? When they weren't looking?)
  Or do they prefer coding by copy-and-paste?

* Have they taken any steps or created any systems to prevent errors from occurring,
  or to detect them early? (Answers might involve unit testing, "asserts," debug-only code,
  test harnesses, internal self-validation, etc.)

* What approaches have they favored for tracking down bugs? (Their own or other coders' bugs.)
  Can they follow a coherent diagnostic plan to fix the root cause,
  or will they "play Whack-a-Mole" with our code and introduce as many bugs as they fix?

* Some of these questions veer toward engineering religion.
  (And candidates' past teams may have been more or less religious than our own.)
  Ask about the pluses and minuses of the approaches they took.
  Did everyone on their team adopt those approaches?


Programming
-----------

* Are they locked into a single language or platform, or have they demonstrated the
  ability and willingness to move between environments as the needs arise?
  Have they created domain-specific languages to address particular problems?

* How have they applied design patterns? Is the approach thoughtful and intended to address
  specific needs, or do they sprinkle inappropriate design patterns throughout their code in the
  hope of achieving magic results?

* Do they understand the differences between object-oriented, procedural, declarative,
  functional, and other types of programming? (Even if they don't use those terms.) Are they
  locked into a single approach, or more flexible?

* Do they have a working understanding of fundamental computer science concepts?
  What do they understand (or not) about multithreading? Asynchronous processing,
  remote procedure calls, event-driven programming? Memory allocation, garbage collection?
  (Not so much the specifics of any given environment, but an understanding of the underlying
  mechanisms in general.)


Performance, Scalability, and Security
--------------------------------------

* What performance and scalability issues have they encountered? How did they discover them and
  track down the causes? How did they address them?

* When and how do they optimize their code? In the design stage? Everywhere throughout the code?
  Only in specific areas where they had problems? Based on rumors?

* Do they understand the difference between performance, availability, and scalability?

* What security concerns have been important in their coding? What's their level of awareness of
  security issues, and how have they avoided them?

There may also be specific performance, scalability, and security areas your
team will want to dig into as part of the
:ref:`domain expertise interview <domain-expertise-interview>`. E.g., web
engineers should be aware of SQL injection attacks as part of their web domain expertise.
