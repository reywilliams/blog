---
title: “My Favorite Tools (2025)”
date: "2025-12-30T18:28:22-08:00"
tags: [“tooling”, “lists”]
author: “Rey Williams”
description: “A quick rundown of tools I enjoyed using in 2025.”
summary: “A quick rundown of tools I enjoyed using in 2025.”
---

With 2025 wrapping up, I thought it would be fun to reflect on the tools I’ve enjoyed using this year. As a dev, these tools are a part of my daily workflows and make me _[some x %]_ better.

> These are in no particular order.

## 1. [Obsidian](https://obsidian.md/)

I am **very big** on notes (_and markdown_). I sometimes find that my mind moves a million times a minute, so writing things down gives me an opportunity to bring clarity to my thoughts and craft internal and external documentation that is cohesive and insightful.

I use Obsidian in both professional and personal settings, and I find its minimal yet feature-rich environment ideal for my use cases. I do have small gripes with it like [GraphQL syntax highlighting not rendering in the source editor due to it using a different library from the live preview editor](https://forum.obsidian.md/t/bug-of-syntax-highlighting-for-graphql-language-in-source-code-and-live-preview-mode/45110), but overall I enjoy the experience.

I don’t think I am a power user by any means, but I feel very productive with Obsidian and have patterns, templates, and such that work well for me in there. I can safely attribute at least 30% (:laughing:) of my professional success to Obsidian this year - I’ve technically scoped lots of epics, fixed a lot of hair-pulling bugs, and clearly documented lots of complex ideas in Obsidian. Next up on the docket is maybe using the [Obsidian MCP](https://hub.docker.com/r/mcp/obsidian), but I’ve tried to keep AI out of my notes as much as I can, as it’s sorta my “outlet” haha.

## 2. [DataGrip](https://www.jetbrains.com/datagrip/)

DataGrip is a more recent one for me, but it has quickly become one of my favorite tools this year in a short time. I was previously using [Beekeeper Studio](https://www.beekeeperstudio.io/) as it was recommended to me by a colleague,and it was great, _buttttttt_ DataGrip allows me to be so much more productive. DataGrip, like other JetBrains tools, are feature-rich and has so many quality-of-life (QOL) features and insight that make the experience so useful.

Some additional context about my use case: I use DataGrip professionally to:

- audit various (20+) PSQL databases
- test my own local databases with things like migrations and new entities
- gather metrics and information for (bug) investigations

A few things I’ve enjoyed in particular are:

- The data sources setup gives you lots of control and QOL settings for session management. A simple one I’ve enjoyed is [read-only mode](https://www.jetbrains.com/datagrip/features/executing.html#:~:text=how%20it%20works.-,Read%2Donly%20mode,-Read%2DOnly%20can).
- [^1] "Smart code completion, code inspections, on-the-fly error highlighting, quick-fixes, and refactoring capabilities. It saves you time by making the process of writing SQL code more efficient.”
- Quick expression evaluation
- The import/export options - I love any tool that supports markdown, haha.
- Easy navigation - I enjoy having a very clear separation between different DBs by using separate projects, colors, etc.
- Diagrams - these have helped me _sooo_ much as I’m sometimes dealing with a web of entities and would prefer not having to check for all the FKs and how they all relate.

[^1]: Directly from their [site](https://www.jetbrains.com/datagrip/features/) as I couldn't have said it better myself :tada:

## 3. [Ghostty](https://ghostty.org/)

Shout-out Mitchell!

Before Ghostty, I was an iTerm user, and it was fine, but Ghostty feels lightweight and quick, and now they’re taking this thing all the way as they’re now _[fiscally sponsored](https://ghostty.org/docs/sponsor#relationship-to-hack-club) by [Hack Club](https://hackclub.com/)_ :tada:!

I am currently using the [tip (nightly) release](https://mitchellh.com/writing/ghostty-non-profit) as I was really excited for find/search scrollback to be released, and it won’t be in a stable release until early 2026, I believe.

While Ghostty and its performance speaks for itself, I am also a big “fan” of Mitchell and find what he’s doing with Ghostty and has done with all of the HashiCorp product suite incredibly impressive.

## 4. Tailscale

Oh, Tailscale, what would I do without you! Tailscale is such an amazing tool, and I use it both personally (in my homelab) and professionally.

Tailscale has made itself so easy to use (let’s not talk about the NACLs editor), and it sorta let's me abstract away a lot of networking.

Most recently, I was saved by Tailscale from a tight deadline my team and I were facing due to their [exit node functionality](https://tailscale.com/kb/1103/exit-nodes). I am sure we would’ve been fine overall, but Tailscale made it easy.

I am super excited to use Tailscale more in my homelab as I continue to host more services and connect to them from any (allowed) device in my Tailnet.

## Notable Mentions

- Claude Code - I love taking notes, and the Frenchman loves to digest them, my favorite thought-partner.
- IntelliJ - for similar reasons as DataGrip.
