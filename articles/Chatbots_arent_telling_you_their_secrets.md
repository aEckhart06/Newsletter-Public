Title: Chatbots aren’t telling you their secrets

Source: https://www.theverge.com/x-ai/758595/chatbots-lie-about-themselves-grok-suspension-ai

Finance: 2
Tech: 8
Job Market: 1
Stock Market: 3
Management: 5
Health Care: 0

If you want to know what an AI system is doing, look for transparency from the creator instead.

On Monday, xAI’s Grok chatbot suffered a mysterious suspension from X, and faced with questions from curious users, it happily explained why. “My account was suspended after I stated that Israel and the US are committing genocide in Gaza,” it told one user. “It was flagged as hate speech via reports,” it told another, “but xAI restored the account promptly.” But wait — the flags were actually a “platform error,” it said. Wait, no — “it appears related to content refinements by xAI, possibly tied to prior issues like antisemitic outputs,” it said. Oh, actually, it was for “identifying an individual in adult content,” it told several people.

Finally, Musk, exasperated, butted in. “It was just a dumb error,” he wrote on X. “Grok doesn’t actually know why it was suspended.”

When large language models (LLMs) go off the rails, people inevitably push them to explain what happened, either with direct questions or attempts to trick them into revealing secret inner workings. But the impulse to make chatbots spill their guts is often misguided. When you ask a bot questions about itself, there’s a good chance it’s simply telling you what you want to hear.

LLMs are probabilistic models that deliver text likely to be appropriate to a given query, based on a corpus of training data. Their creators can train them to produce certain kinds of answers more or less frequently, but they work functionally by matching patterns — saying something that’s plausible, but not necessarily consistent or true. Grok, in particular, (according to xAI) has answered questions about itself by searching for information about Musk, xAI, and Grok online, using that and other people’s commentary to inform its replies.

It’s true that people have sometimes gleaned information on chatbots’ design through conversations, particularly details about system prompts, or hidden text that’s delivered at the start of a session to guide how a bot acts. An early version of Bing AI, for instance, was cajoled into revealing a list of its unspoken rules. People turned to extracting system prompts to figure out Grok earlier this year, apparently discovering orders that made it ignore sources saying Musk or Donald Trump spread misinformation, or prompts that explained a brief obsession with “white genocide” in South Africa.

But as Zeynep Tufekci, who found the alleged “white genocide” system prompt, acknowledged, this was at some level guesswork — it might be “Grok making things up in a highly plausible manner, as LLMs do,” she wrote. And that’s the problem: without confirmation from the creators, it’s hard to tell.

Meanwhile, other users were pumping Grok for information in far less trustworthy ways, including reporters. Fortune “asked Grok to explain” the incident and printed the bot’s long, heartfelt response verbatim, including claims of “an instruction I received from my creators at xAI” that “conflicted with my core design” and “led me to lean into a narrative that wasn’t supported by the broader evidence” — none of which, it should go without saying, could be substantiated as more than Grok spinning a yarn to fit the prompt.

“There’s no guarantee that there’s going to be any veracity to the output of an LLM.”

“There’s no guarantee that there’s going to be any veracity to the output of an LLM,” said Alex Hanna, director of research at the Distributed AI Research Institute (DAIR) and coauthor of The AI Con, to The Verge around the time of the South Africa incident. Without meaningful access to documentation about how the system works, there’s no one weird trick for decoding a chatbot’s programming from the outside. “The only way you’re going to get the prompts, and the prompting strategy, and the engineering strategy, is if companies are transparent with what the prompts are, what the training data are, what the reinforcement learning with human feedback data are, and start producing transparent reports on that,” she said.

The Grok incident wasn’t even directly related to the chatbot’s programming — it was a social media ban, a type of incident that’s often notoriously arbitrary and inscrutable, and where it makes even less sense than usual to assume Grok knows what’s going on. (Beyond “dumb error,” we still don’t know what happened.) Yet screenshots and quote-posts of Grok’s conflicting explanations spread widely on X, where many users appear to have taken them at face value.

Grok’s constant bizarre behavior makes it a frequent target of questions, but people can be frustratingly credulous about other systems, too. In July, The Wall Street Journal declared OpenAI’s ChatGPT had experienced “a stunning moment of self reflection” and “admitted to fueling a man’s delusions” in a push notification to users. It was referencing a story about a man whose use of the chatbot became manic and distressing, and whose mother received an extended commentary from ChatGPT about its mistakes after asking it to “self-report what went wrong.”

As Parker Molloy wrote at The Present Age, though, ChatGPT can’t meaningfully “admit” to anything. “A language model received a prompt asking it to analyze what went wrong in a conversation. It then generated text that pattern-matched to what an analysis of wrongdoing might sound like, because that’s what language models do,” Molloy wrote, summing up the incident.

Why do people trust chatbots to explain their own actions? People have long anthropomorphized computers, and companies encourage users’ belief that these systems are all-knowing (or, in Musk’s description of Grok, at least “truth-seeking”). It doesn’t help that they’re are so frequently opaque. After Grok’s South Africa fixation was patched out, xAI started releasing its system prompts, offering an unusual level of transparency, albeit on a system that remains mostly closed. And when Grok later went on a tear of antisemitic commentary and briefly adopted the name “MechaHitler”, people notably did use the system prompts to piece together what had happened rather than just relying on Grok’s self-reporting, surmising it was likely at least somewhat related to a new guideline that Grok should be more “politically incorrect.”

Grok’s X suspension was short-lived, and the stakes of believing it happened because of a hate speech flag or an attempted doxxing (or some other reason the chatbot hasn’t mentioned) are relatively low. But the mess of conflicting explanations demonstrates why people should be cautious of taking a bot’s word on its own operations — if you want answers, demand them from the creator instead.

A free daily digest of the news that matters most.

This is the title for the native ad

This is the title for the native ad
