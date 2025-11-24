---
title: Let Your Models Think
date: "2025-11-23T15:18:25-08:00"
tags: ["post", "ai", "research"]
author: Rey Williams
description: "Discussing the importance of letting your LLM models think."
summary: Remember to explore your configuration options and let your models think!
showtoc: true
---

## Discovery

In a recent project of mine, I had to investigate why an AI pipeline gave the output that it did. This is an exercise I am becoming increasingly familiar with, _unfortunately_. This pipeline primarily used [Claude](https://www.anthropic.com/news/introducing-claude) models, but I recently introduced the use of [Gemini](https://ai.google.dev/gemini-api/docs/models) models and thought it would be great to use the [Vertex AI Studio](https://cloud.google.com/generative-ai-studio) to compare a prompt from my pipeline in [Gemini 2.5 Pro](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro) vs the new [Gemini 3 Pro Preview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-pro).

While exploring the interface, I noticed that I could configure the thinking done by the Gemini models. The UI was actually really nice and let me see the thought chains, which I thought would be really useful for debugging why an LLM output what it did and a few providers concur that this is a viable approach [^1].

[^1]: Providers like [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/extended-thinking-tips#:~:text=then%20read%20Claude%27s%20thinking%20output) and [Google](https://ai.google.dev/gemini-api/docs/thinking#summaries) note that this _can_ and **should** be used in your prompt engineering process/iteration(s).

Transparently, I reviewed the [Google Gen AI SDK](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview) quite a bit for my implementation, but I did not realize that I could configure "thinking."

## "Enlightenment"

This led me down a rabbit hole where I realized that most model providers had configuration for thinking (or _reasoning_ as some of them call it). This made a lot of sense and I was quickly reminded of the advancements in [chain of thought](https://www.ibm.com/think/topics/chain-of-thoughts) (CoT) reasoning techniques that made the announcement of OpenAI's o1-preview model that could

> spend more time thinking through problems before they respond, much like a person would
>
> — <cite>Open AI [^2]</cite>

[^2]: This quote is from OpenAI's `o1-preview` announcement post in late (September) 2024

so interesting and "ground-breaking" at the time.

All in all, this was a great discovery for me and my pipelines, but honestly I feel as though it was another case of failing to _[RTFM](https://en.wikipedia.org/wiki/RTFM)_.

I thought it would be nice to explore this space a bit more and share my findings. We all know these LLMs and their tokens aren't cheap[^3] so it would definitely be great to get more value out of them.

[^3]: Take a look at this price-per-token tracker and lament at the ever increasing prices: https://pricepertoken.com/

## Thinking it Through

I think (pun intended) it would be best to focus on the "big three" providers and their primary models for my dive. I will primarily be covering:

- Anthropic Claude
- Google Gemini
- OpenAI GPT-5

### Claude

> Anthropic refers to thinking as "**extended thinking**"

Anthropic models are a bit interesting when it comes to thinking as they have two primary "entry points" when it comes to Claude:

- [Claude Code](https://www.claude.com/product/claude-code)
- [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)

For Claude Code, Anthropic introduced a progressive thinking model with the following hierarchy

> "think" < "think hard" < "think harder" < "ultrathink."
>
> — <cite>Anthropic [^4]</cite>

[^4]: This is from Anthropic's best practices guide - [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices)

This seems like a reasonable interface for thinking in Claude Code given that it's a CLI tool and adjusting per-message thinking budgets could be cumbersome.

Anthropic's Messages API follows an approach similar to other providers where they let you configure a thinking budget via a `thinking` object with a `budget_tokens` property in your request:

> To turn on extended thinking, add a `thinking` object, with the `type` parameter set to `enabled` and the `budget_tokens` to a specified token budget for extended thinking.
>
> — <cite>Anthropic [^5]</cite>

[^5]: Noted in Anthropic's guide on [how to use extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#how-to-use-extended-thinking)

Anthropic [notes](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/extended-thinking-tips#technical-considerations-for-extended-thinking) that there is a minimum budget of 1024 tokens and they recommend you bump this budget incrementally until you find a value that is ideal for your use-case. They do recommend, however, that workloads with a budget above 32k use [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing).

#### Honorable Mentions

Claude has a lot of interesting tidbits as it pertains to thinking. A few of them are:

- [Summarized thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#summarized-thinking) - Get a summary of Claude's full thinking process
- [Thinking encryption](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#thinking-encryption) and [Thinking redaction](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#thinking-redaction) as Claude's reasoning can sometimes be flagged by Anthropic's safety systems
- A [host of best practices](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#best-practices-and-considerations-for-extended-thinking)
- A useful [guide on chain-of-thought prompting engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought)

### Gemini

Google notes that

> thinking features are supported on all 3 and 2.5 series models.
>
> — <cite>Google [^6]</cite>

[^6]: Google's Gemini API [docs on thinking](https://ai.google.dev/gemini-api/docs/thinking#supported-models)

Google has followed a fairly standard thinking configuration with thinking budgets for Gemini models <= 2.5, but starting with Gemini 3 Pro that was [recently released](https://blog.google/products/gemini/gemini-3/) they're moving to "thinking levels."

You can still use the `thinkingBudget` parameter but Google warns you that this might lead to suboptimal performance.

For Gemini models, Google lets you:

- disable thinking (Pro models are excluded)
- use a set budget (within a [predefined range](https://ai.google.dev/gemini-api/docs/thinking#set-budget) for a specific model)
- use dynamic thinking (this lets the model "adjust the budget based on the complexity of the request")

The above can be a bit confusing as Google notes this about Gemini 2.5 and earlier models

> if `thinking_budget` is not set, the model automatically controls how much it thinks up to a maximum of `8,192 `tokens
>
> — <cite>Google [^7]</cite>

[^7]: Vertex AI [docs on thinking](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking)

The highest thinking budget for a Gemini model is Gemini 2.5 Pro's whopping `32768` thinking budget. Gemini 3 Pro's `thinking_level`s of `low` and `high` map to Gemini 2.5 Pro's `thinking_budget` as such:

| **reasoning_effort (OpenAI)** | **thinking_level (Gemini 3)** | **thinking_budget (Gemini 2.5)** |
| :---------------------------- | :---------------------------- | :------------------------------- |
| **minimal**                   | low                           | 1,024                            |
| **low**                       | low                           | 1,024                            |
| **medium**                    | high                          | 8,192                            |
| **high**                      | high                          | 24,576                           |

You can see that this is all based on the OpenAI's reasoning efforts (which we will touch on a bit later).

### OpenAI GPT-5

> OpenAI refers to thinking as "reasoning"

OpenAI's reasoning models use a `reasoning.effort` parameter to control reasoning (_thinking_). Similar to Gemini 3 models, you can use a `low`, `medium`, or `high` value.

There doesn't seem to be a way of specifying a thinking or reasoning budget, but you can control the cost of reasoning via the `max_output_tokens` [parameter](https://platform.openai.com/docs/api-reference/responses/create#responses-create-max_output_tokens) - this controls the total number of tokens generated by the model, which includes reasoning and output tokens (other models like Gemini consider thought tokens to be output tokens so tracks).

If you happen to hit the limit you've set via `max_output_tokens`, you'll get back a response with `incomplete` as its `status`.

Just like the other two providers, OpenAI's reasoning models offer [reasoning summaries](https://platform.openai.com/docs/guides/reasoning#reasoning-summaries).

## Final Thoughts

My final thoughts (again, pun intended) on this is that there is just so much to learn when it comes to using these LLM models and fully utilizing their abilities. Along with ensuring you _[RTFM](https://en.wikipedia.org/wiki/RTFM)_, you just need to do a good amount of experimentation and play around with these models and utilize all the available playgrounds (like Vertex AI Studio, and the [AWS Bedrock playgrounds](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock-playgrounds.html)).

Nonetheless, I am excited with what this means for my pipelines and workflows. Working with these tools have been nothing short of amazing (albeit frustrating).
