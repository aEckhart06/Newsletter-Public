Title: Why CEO Matt Garman is willing to bet AWS on AI

Source: https://www.theverge.com/24338171/aws-ceo-matt-garman-ai-chips-anthropic-cloud-computing-trainium-decoder-podcast-interview

Finance: 5
Tech: 10
Job Market: 0
Stock Market: 5
Management: 10
Health Care: 0

AWS chief Matt Garman says Amazon is already seeing the benefits of its massive AI investments.

by  Nilay Patel

AWS chief Matt Garman says Amazon is already seeing the benefits of its massive AI investments.

by  Nilay Patel

Today, I’m talking with Matt Garman, the CEO of Amazon Web Services, or AWS. Matt took over as CEO last June — you might recall that we had his predecessor, Adam Selipsky, on the show just over a year ago. That makes this episode terrific Decoder bait, since I love hearing how new CEOs decide what to change and what to keep once they’ve settled into their role.

Matt has a really interesting perspective for that kind of conversation since he’s been at AWS for 20 years — he started at Amazon as an intern and was AWS’s original product manager. He’s now the third CEO in just five years, and I really wanted to understand his broad view of both AWS and where it sits inside an industry that he had a pivotal role in creating.

Listen to Decoder, a show hosted by The Verge’s Nilay Patel about big ideas — and other problems. Subscribe here!

You’ll hear Matt say that most companies are still barely in the cloud, and that opportunity remains massive for AWS, even though it’s been the market leader for years. If you’re a product manager or an aspiring product manager, you’ll catch Matt talking about these things exactly like the product manager he was from the start, only now with a broad view from the CEO chair.

But just acquiring new customers isn’t the game any longer: like every cloud provider, Amazon is reorienting its entire computing infrastructure for a world of generative AI. That includes more than $8 billion in funding for Anthropic, a huge push to build its own AI chips to compete with Nvidia, and even nuclear power investments as the energy demand for AI continues to grow. After Matt and I talked before the holidays, AWS announced an $11 billion investment to expand its data center operations in Georgia.

Matt’s perspective on AI as a technology and a business is refreshingly distinct from his peers, including those more incentivized to hype up the capabilities of AI models and chatbots. I really pushed Matt about Sam Altman’s claim that we’re close to AGI and on the precipice of machines that can do tasks any human could do. I also wanted to know when any of this is going to start returning — or even justifying — the tens of billions of dollars of investments going into it.

His answers on both subjects were pretty candid, and it’s clear Matt and Amazon are far more focused on how AI technology turns into real products and services that customers want to use and less about what Matt calls “puffery in the press.”

One note before we start — we recorded this episode just before the holidays, so I asked Matt about Netflix, one of AWS’s biggest customers, and whether it would hold up while streaming live events, especially the NFL games it streamed on Christmas. Turns out, Netflix did just fine with those, but the answers here were pretty interesting. Matt still checks in on his big customers, even as CEO.

Okay, AWS CEO Matt Garman. Here we go.

This transcript has been lightly edited for length and clarity.

Matt Garman, you’re the CEO of Amazon Web Services (AWS). Welcome to Decoder.

Thanks for having me.

I am very excited to talk to you. You’re like a perfect Decoder guest. You are, I believe, the first product manager at AWS, you started as an intern and now you’re the CEO. We have a lot of listeners who want to be on that journey, so there’s lots to talk to you about just in that.

You’re also the new CEO. We had your predecessor, Adam Selipsky, on the show just a little over a year ago. You’re about six months on the job now. So, there’s a lot of Decoder stuff in there — how you’re changing the organization and how you’re thinking about it. And then, obviously, we’re going to talk about AI. It’s going to happen. I hope you’re ready for it.

I’m ready for it. Shoot, fire away. I’m happy to go wherever you want.

All right. But I actually want to start with a very hot-button, deeply controversial topic. Are you ready?

Great. Fire away.

Okay, it’s Jake Paul. I want to start with Jake Paul. My understanding is Netflix is the prototypical AWS customer, right? They started on AWS, they made a big bet on AWS. They’re still the customer, right? They haven’t left AWS?

Yeah, Netflix is a great customer of ours. Absolutely.

They just had the live stream of Jake Paul fighting Mike Tyson. You can think anything you want about those two men fighting each other.

I was hoping Mike would win, honestly.

So was I.

I think most were, but that’s okay. It was fun to see him out there.

You’ve just set off a million more conspiracy theories about this fight. Anyhow, I told you it was controversial. All right, but the stream was pretty glitchy. I think everybody agrees on that. When I watched it, it degraded to 360p at some point for me. Netflix CEO Ted Sarandos was just on stage at a conference. Netflix said the demand is 108 million people globally, and here’s what Ted said about that stream: “We were stressing the limits of the internet itself that night. We had a control room up in Silicon Valley that was re-engineering the entire internet to keep it up during this fight because of the unprecedented demand that was happening.”

You’re the CEO of AWS, you’re the internet. Did they have to re-engineer the internet for the Jake Paul fight?

You’ve got to ask Ted about that. I think where they were stressed about the [content delivery network] they run, and you can ask Ted about that too. Netflix has its own homegrown CDN that it uses, and that’s the part that I think was stressed. I don’t know the details of exactly where they were running into barriers, but it wasn’t in the AWS infrastructure, it was in the Netflix-controlled part of their structure.

Yeah, their CDN is really fancy, right? They’ve got boxes and ISPs and everything. I was just curious because what we’re about to talk about, in a huge way, is how providers like AWS can meet the growing demand for compute everywhere and then get it to the people who need it. And it feels like most people in 2024 take video streaming for granted, but it’s still pretty hard.

It is. And I think in particular, there are a couple of things around that that are challenging, right? By the way, it’s a super hard thing that they did. Number one, it’s their first time doing a big, scaled live stream like that. The first time is actually what’s hard. Other people have done that before. We’ll stream Thursday Night Football and other places like that that have figured out how to do things at that scale, but it’s not the first time. So, I’m sure that the next time — I think they have a Christmas day game — they’ll probably work out some of those kinks and figure that piece out.

The first time you do it you’ll find those bottlenecks. And it’s true about any compute system where you have an order of magnitude more [to figure out]. They obviously have shows that have streamed more, but they’re spread across more time. So it’s this single spike up where everybody comes in a 30-minute window, and if it’s outside of what you planned for … If they planned for — I don’t know what their numbers were — 150 million and they got 180 million, it was outside of what they thought their upper limit was. We’ve seen this before in AWS and we’ve seen this in Amazon. The first time we did Prime Day we probably had issues across that too, of just people hitting the website and other things. So the first time you do events like this, it’s a learning process.

I think it’s probably overstating it to say that they had to re-architect the whole internet, but it is that key spike where a lot of applications are just not ... Particularly when you own the infrastructure, and this is one of the benefits of the cloud, by the way, is you get to ride on the law of large numbers where any one spike doesn’t overwhelm everything else. Netflix obviously has a huge number of customers, and I guess that they’ll be much more prepared for next time. But it’s a good learning experience for anybody even at a much smaller scale. When you’re planning an event that has the potential to be materially more than your average baseline, there are always risks that there are some scaling factors you don’t anticipate.

So it’s not a surprising problem to me. We’ve seen it over and over again and it’s one of those problems that the cloud helps to solve. But even in the cloud, planning is required and you have to think about how you scale ahead of it, and things like that.

When you were at home watching the fight, did your pager go off?

I was texting back and forth to our support team to make sure we were supporting the Netflix team as much as possible, yes.

How often does that happen to you as you use the internet and you think, “Boy, this is probably running on AWS. I had better make sure it’s going fast?”

More back in the day when we were scaling and learning — back in 2007 and 2008 where we were learning how to scale there. Today, we’re often at a broad scale and so everything, lots of things on the internet and around the world, run on AWS. And we usually run pretty reliably, so it comes up less than it used to, for sure.

Do you have Down Detector bookmarked on your laptop?

I don’t, no.

We’ve got to get the CEO of Down Detector on the show. That is a fascinating service across the board.

Let me ask the Decoder questions because I think this theme of “we are going to be more reliant on cloud infrastructure for compute in the world of AI,” and that’s got to reach all the people and hopefully make everybody some money and generate some useful products and services — that’s the theme. And I think whether or not we can stream people punching each other, and whether or not we can stream AI, the problems there are the same in the general sense.

But I want to ask the Decoder questions first so I can understand how you are solving those problems, having been at AWS for so long. So you are taking over for Adam who was on about just a little over a year ago. He stepped down about six months ago, you took over. You’ve been there a long time. You started as the first product manager of AWS, which is a pretty wild place to begin a career and end up as a CEO. How are you thinking about AWS, the organization, right now?

There are a couple of things that I’m thinking about. One, I have been here for 18 years, so I’ve been fortunate to learn a lot of the different parts of the business and have seen it from the early days until where we are now. Over 18 years we’ve grown to be a $110 billion business growing at 19 percent, so that’s great, and we’re just at the early stages of what that business can be. I’m pushing the teams to consistently think about how we innovate faster. How do we think bigger? And how do we support our customers?

As we think about the potential of AWS being a $200 billion, $300 billion, $500 billion business, or whatever size it gets to, we want to continuously think: What are the organizational structures? What are the mechanisms we use? What are the ways that we supported customers, which worked to get us to $100 billion, and may not work at $200 or $300 billion?

Some of that is just thinking about how we scale those aspects. And how do we think about supporting customers in a great way? How do we think about scaling our services in a great way? How do we think about continuously innovating across many different paths? And as you think about it, we have to really innovate along our core — the thing that got us here around compute, databases, storage, and networking. But we also have to innovate around AI, around some higher-level capabilities, and analytics.

We also have to innovate around helping customers who might be less technically savvy, so they can take advantage of the cloud. They may not be at Netflix-level sophistication, which is obviously a very sophisticated technology team, but want to take advantage of some of the cloud capabilities. I think we’re continuing to think about how we keep pushing that envelope to help more and more customers take advantage of what we have.

One of the things that I spend a lot of time thinking about is: how we organize so that our teams don’t lose agility and speed as we get bigger. That’s some of what I’m thinking about, and it’s nothing that’s broken today. Instead, it’s kind of like looking around corners to see when the business is twice as big as it is today, how do we make sure that we continue to execute and run as fast as possible?

Can I ask about that piece of the puzzle? Where does the next new customer come from?

Sure.

When you started at AWS they were all new customers. Now, most huge companies at least have an idea of what they might do with the cloud, whether they’re using AWS or something else. We have a lot of CEOs who come on here and say, “Look, I need to have multiple clouds so that I can go do rate negotiations with all of them.” Fine.

There is a new class of companies that assumes they don’t need any software support. They’re just going to hire a bunch of software as a service (SaaS) vendors, and they’ll run their business and use the SaaS products however they want to use them. And it seems very unlikely that they will become AWS customers themselves because they’ve outsourced a bunch of business functionality to a bunch of other software vendors. I’m just wondering if that’s a new class of potential customer, right? That kind of business didn’t exist until recently.

It’s true, and I think that there’s probably subtlety there. So I’ll take a couple of those, one at a time. Number one, we do have a lot of large customers that are running in AWS in the cloud today, and a huge number of them still have massive amounts of their estate on-premise. And so there’s a huge amount of growth available there. You can even take our largest customers, many of them only have 10, 20, 30, or 40 percent of their workloads in the cloud. There’s a massive amount of growth just helping them get to 70 or 80 percent, or whatever that number is going to be, and don’t even presume you get to a hundred. There’s a huge amount of business there.

I also think there’s a huge amount of business available with customers that only have one percent, or rounding to zero, of their estate in the cloud because they’re still running on-premise workloads, whether it’s IT or core business pieces. Some of it is running in data centers. Some of that is workloads that haven’t moved to a cloud world yet. Think telco networks, broadly. Most telco networks still run in traditional telco networks. There are a handful of customers, like the Dish networks of the world, who have thought about and have moved to building in the cloud. Since they got to start from zero, and have built it in the cloud, they get the benefits of that agility — but most haven’t.

Think about all of the compute that happens in a hospital today. It’s mostly in the hospital. And they’re just examples of where there’s an enormous amount of compute that could take advantage of these broad-scale cloud systems that haven’t yet moved there. So there’s a huge amount of potential in those additional businesses. There’s also just, as you think about new customers, every single year there are a huge number of startups that are created from scratch and they all start in the cloud too. There’s still lots of greenfield opportunity for us.

I think your observation about companies leaning more into SaaS is super interesting and it’s why they’re such a focus for us. It’s why we focus on deep partnerships. How do we make sure that AWS is the best place to run SAP, it’s the best place to run Workday, it’s the best place to run ServiceNow, it’s the best place to run ... Keep going down the list. And so, those SaaS independent software vendors (ISVs) have always been a really important customer base for us.

And increasingly, you see us build capabilities that make AWS even more powerful for SaaS vendors. At re:Invent, we announced a capability called Q Business Index where you can have all of your SaaS data pulled together into a single index that’s owned and controlled by the enterprise, but you can share across SaaS products. I think you’ll see more things like that where we can help customers not just say, “Okay, my data’s in a bunch of these SaaS islands and I can’t get benefits across them.”

I don’t think customers won’t be an AWS customer, because they’re still going to have a data lake of their own data, they’re still going to have their own applications, they’re still going to run their own websites. There are other things that customers are still going to want to do. And so I think more of their applications will be in SaaS as opposed to self-managed software, for sure. It’s hard to imagine many customers that won’t have their own compute storage database needs also.

When Adam was on the show, I asked him, “What’s the point of the airport ads? Who doesn’t know about AWS?” And his answer basically tracked with what you’re saying. There are still a lot of customers who we need to get thinking about moving to the cloud, and that’s why there are Thursday Night Football ads.

Is that your answer? When you get off the plane and you see the AWS logo, you’re like, “I’m going to get that guy?”

I mean, look, you can make that argument for lots of ads. Like, who doesn’t know that Coca-Cola exists? But you still see Coca-Cola ads. And so some of it is keeping it top of mind. Some of it is also … If you think about the advertising that we do together with some of the sports networks — whether it’s NFL, F1, or others — a lot of what that does is to help connect the dots. You may know that AWS exists, but helping see that in a context that you understand, which is football, F1, Bundesliga, or whatever the sport is, and how we’re helping do analytics for that sport, is one of those things that helps customers connect the dots.

And so, it’s not just an ad that says, “Hey, AWS exists,” but it is connecting those dots that says, “Okay, if we’re able to do analytics that can see how fast a football player can run, or see what the chance is that an F1 car can pass,” it helps customers just connect the dots as to where we might be able to help their business too. It also opens the door for us to do that next deep dive where we can dive in and understand that. And we find that that connection point is quite valuable even if people know that AWS exists already.

I do love the idea of some CEO coming to you and saying, “I need a win probability meter for my team every minute of the day in real time.”

That’s great.

Let me ask you about telco for one second. Just because telecommunications has long been a particular fascination of mine. Dish started from scratch. They announced loudly that they were going to use AWS as their cloud provider, that they wanted to do all the compute they needed for 5G and all that stuff to run that network in the cloud. Compare and contrast that to the other telcos.

When Verizon was launching 5G, for example, they told me that they were going to build a competitor to AWS because they needed the compute at the edge to run the network anyway. And they said they might as well just sell the excess capacity in their data centers to customers and say it would have a lower latency, or whatever you get from being very much at the edge. Did that pan out? Or are you saying, “Okay, that didn’t work, and I can go conquer those customers now. I can go get Verizon or AT&T or whoever else on the network?”

Well, Verizon was a little bit different. It was a partnership with us where we were talking about potentially selling some of that compute space together at the edge. I think that technology is probably a little bit ahead, and I still think that there’s an interesting eventual win there. But I think that the idea was a little bit ahead of the technology of really low-latency compute at the edge, mostly because a lot of that latency was taken up in the network, and so it’s hard to get that benefit of a small latency gap.

Look, if you go back 15 years, many companies were thinking that they would just go offer the cloud. It looked like it was easy. And then they said, “Oh, it’s just a hosting thing. I have a data center. I can sell that.” I think most companies today, outside of the handful of three or four companies that are really in the space, don’t think that they can provide a real cloud offering. It’s hard.

There are niche offerings in particular slices, but I think increasingly we view this as a partnership opportunity where we can add value together. So, I think our partnership with Verizon is great. We look at how we can add value together, and over time we’d love for more of the broader network. Because if you look globally, you’re starting to see other telcos start to lean into this model of, “Okay, maybe more of the core can be run in AWS” … Then maybe that part is, “Okay, that can be run in central data centers,” and so we’re starting to see more core. And then you think about, “Can the radio access network (RAN) be run in AWS? Maybe. Yeah, it can.” And they’re starting to see that piece in there.

I think it will be a transition over time. But I do think that as we add more value and show that we can give programmability to their networks, scale to the networks, and show benefits on patching and other things like that where there’s a lot more flexibility there — I think you’ll see more and more telcos leaning into to cloud-based place deployments.

I’m sure your partners at the traditional telco companies appreciate your support in the retconning of their promises around 5G. You’re doing great.

There’s a real split here. I hope people can hear it. We’re talking about still trying to get customers to come use cloud services. Step one: move some of your compute out of the basement of the hospital and into the cloud. And a lot of companies aren’t there yet, and it seems like you perceive that there’s still opportunity there.

Then we’re going to, in a minute, we’re going to talk about AI, which is the absolute cutting edge of, “How do we even run these companies? What do these computers even do? How does the cost work out?” How are you structuring the organization to deal with that split? “Don’t have your own servers in the basement?” versus, “Turn your decision-making over to some agentic AI system that we’re going to run for you.”

Well, in some ways it’s a much stronger carrot. If the pitch is, “Hey, run the exact same thing that you’re doing, but do it a little bit more efficiently and a little bit less expensively,” that is less of a value proposition than if you can do something that hasn’t been possible before. And so, I think that’s why many of the workloads that you’ve seen move to the cloud already are the super scalable ones, or the ones where they need lots of compute, or the ones where they have a really large footprint because they see the wins are enormous for those types of customers. For a server running in the basement of a hospital, maybe they can save a little bit of money, or maybe they can save a little bit of IT work or whatever, but the value proposition may not be there unless we can really deliver a lot of value.

You’re not going to be able to get a lot of the value that’s promised from AI from a server running in your basement, it’s just not possible. The technology won’t be there, the hardware won’t be there, the models won’t live there, et cetera. And so, in many ways, I think it’s a tailwind to that cloud migration because we see with customers, forget proof of concepts … You can run a proof of concept anywhere. I think the world has proven over the last couple of years you can run lots and lots and lots of proof of concepts, but as soon as you start to think about production, and integrating into your production data, you need that data in the cloud so the models can interact with it and you can have it as part of your system.

And I do think that that is going to be a tailwind over the next couple of years as people want to have these agentic systems. They want to have their data in a secure environment but integrated into an AI workflow. You can’t orchestrate an AI workflow pointing it on a mainframe. It’s not going to be possible. If you have the data going back and forth to some model, the security and control of making sure that that intellectual property (IP) stays with you is risky too.

But if you move the whole data into a secure cloud environment, you’ll have a modern data lake that has all your data. Your application will work there, you’ll be colocated with where the model, all the controls, and guardrails can run, and you can have a retrieval augmented generation (RAG) index that’s nearby to take advantage of all that data — that’s when you can really start integrating it into your production applications. And that’s where you’re going to see a lot of the really meaningful wins, not just kind of a cool, “Hey, that’s neat that I can have a chatbot,” but really integrate it into how your workflows change and how you can do business changes.

I have seen early signs that, to your question about organization, they’re very complementary. It’s not A or B, it is all pushing in the same place. So we’ll have to have different capabilities, we’ll have to have different motions to help all of that. But I do think that that move of getting your data into a cloud world is kind of a necessary condition to have a really, really successful, deeply integrated AI, I think, into your business processes.

So this leads right into the classic Decoder question: How is AWS structured now? What’s the org chart?

What do you mean? So say more about that. Just what is our org structure?

Yeah. How have you structured AWS? I mean you’re new, so I imagine you might change it, but how is it structured right now, and how are you thinking about changing it?

Well, I will say that an org structure, number one, is a living thing. So whatever I tell you today may not be true tomorrow, and I think you have to be agile there. But broadly, how we think about structuring our teams, I think, is pretty well documented in the industry around Amazon. We want single-threaded teams that can focus on a particular problem and move fast. And so what that means is you really want a team who can own a problem and not be matrixed across 10 different things where they have to coordinate a bunch.

In some ways, I think about it like a big monolithic computer program — it’s very efficient as long as that monolithic computer program is small. And as it gets bigger and you have multiple people working on that program, then you get a mainframe, and it’s very slow and you can’t iterate on it or move fast.

So what you do is decouple and build services that talk to each other through well-defined APIs. And then you continue to decouple those programs, you continue to refactor. That’s how to build modern technology systems. And you can think about containers as the current way of doing that, which are small, independently running systems that can talk to each other through APIs.

Now, if you think about org structure, it’s not that dissimilar from that. If you think about how do you have teams that can run really fast? There is going to be coordination, but what you want to do is minimize that coordination tax as much as possible. And so, if you have a well-defined API between them, which is like, “I build a service over here, you build a service over here,” we can innovate. Occasionally our teams will get together and make sure that we broadly know what our vision is. We want to know what the thing is that we’re running towards. But then I can go and my service, my organization, or my feature, can run independently and not have to have coordination.

High level, if the Amazon Elastic Compute Cloud (EC2) team and the Amazon Simple Storage Service (S3) team had to talk every time they were going to launch a feature to make sure it worked together, we would move really, really slow. But we don’t, and so the teams can move really fast.

Then we make sure we have … It’s kind of part of the leadership and the product leadership team to get together and say, “Okay, we think going after this space is super important. And some of that is customers are going onto this use case, and so broadly we’re going to have to go after this thing,” but we can still then have the teams go out and run fast. That is an organizing principle that ... And then there are other parts of the organization where we have teams that run kind of the data centers and other global, and some of those are our separate teams. But if you think about the product and organizing around the product and technology, that’s how we think about it.

This question is always bait for Amazon executives in particular because Amazon executives are raised in a culture to think exactly in this way and describe the company as a series of microservices. But how is AWS structured?

Just like that. I mean, even more so than Amazon.

Go through it, what are the services? What do you think about allocating the team for those services?

There are 200 different services, so I’m not going to go through all of them, but that is it. And we’ll continually refactor and re-think about them. From a technology point of view, we think about a compute service. You can think about EC2, and then you can think about EC2 networking, and then you can think about, “How do we make sure that it’s optimized around containers?” And then down at the bottom, you think about, “How do we have teams of 10 to 20 people that are focused on a subcomponent of that, that are fully separable?”

We have thousands of developers that are all organized on that principle. Sometimes we’ll move them around organizationally, but it’s not really the org structure. The key piece is really ownership at the bottom. The top part is just how efficient you are at management, and how do you make sure that you’re managing the teams well, and doing that high-level coordination bit. That’s actually where you move around. But at the core, those teams are pretty solid. As you find a new opportunity, you spin up a new team that goes after it and figure out where it makes the most sense in the org structure. But at the core, that is the organizing principle. We have those small teams and we continue to drive them. So that’s it.

And then we organize our sales, go-to-market, and marketing teams separate from that. But from the core product side, that’s how we think about it and it works well for us. I think the positives are ... Look, there are pros and cons to any organizational structure from our side. The pros significantly outweigh the cons. From the cons side, sometimes, and I’m sure you’ve heard this criticism or feedback of AWS, which is that sometimes it seems like it’s not perfectly consistent or this XYZ feature is not supported across every single service yet. And that is the downside of that organizational structure — your fit and finish across every single service is not always perfect, and sometimes it takes a little while to catch up to all of those things, which is expected as you have 1,000 different teams run at different paces on different things.

But the trade-off is we get to move really fast, we’re super agile, and we can respond to customer feedback really quickly. And I think that is the other secret — that it’s not just an organizing principle, but it is also that you teach those teams to really listen to the customer. I’m sure every leader you have on here says they listen to their customers, and I don’t believe that they ... Amazon does a really good job of actually internalizing that down to every individual contributor, and we think about how we go solve customer problems. And when you’re small, agile, and can make decisions, you can actually go solve customer problems really fast in your area. Those things play on each other and are helpful.

You did start as a product manager. As a product manager-

Technically an intern before AWS launched in 2005.

That’s true. But as a PM, you’re running some product and you’re probably thinking about the customer a lot. What were the frustrations you had as a PM that you think you can now reduce as the CEO?

Well, it was a very different business back in the day. I was the product manager for all of AWS, so ...

And so you still are is what you’re saying?

Yeah, exactly. I have the same job now. No, and I kid, there were a couple of other product managers at the time too. But the frustrations then and now are also similar, but different. It’s obviously a different scale that we’re operating at. But one of the things I was frustrated at back in 2006 was that I knew a ton of things that we just needed to go deliver for our customers. I just had a huge list and it was all about prioritizing that list, but I wish that we could deliver them faster and do more, and even at the scale that AWS is today that’s still true. I wish we could do more and do it faster, and that’s part of why we focus on that organizing principle of making sure that you can get out of the way of the teams to move fast. And so, my job today is a little bit more of, “How do I remove those barriers and help teams move fast?” But that’s it.

I think it’s a lot of we want to make sure that we’re innovating, we want to make sure that we’re leaning ahead. Some of the challenges we have today are different than we had in 2006. In 2006, we had to answer the question, “Why would a bookseller ever run my computers?” And that question, we get less and less today, actually. I don’t think I’ve gotten that one for a while.

But now we have to deal with scale, think about enterprise requirements, and about: How do I meet audit requirements? How do we support governments? How do we think about scale? And how do we make sure that we have enough electricity in the world? And all of those kinds of questions. But all good problems for us to solve so that we can take them on so the customers don’t have to.

This is the other big Decoder question and it’s going to lead us right into AI because I think you have a lot of decisions to make here. Amazon famously has the one-way door versus two-way door decision-making framework. Everyone applies it differently. Every Amazon executive I’ve ever talked to holds onto that idea and they apply it differently. What’s your decision-making framework? How do you make decisions?

Well, part of my job is to make the one-way door decisions. So I think that framework is, it’s a useful one to think about. And just to clarify, in case you’re not aware of it, largely that’s how you go fast. You try to define what those decisions are. They can be important decisions by the way. I think sometimes it’s misunderstood what are the important decisions and not important decisions. It’s not that.

You want the people that are owning those teams at the edges of the organization that really own those products to make important decisions because they know best about their product. But they’re also decisions that could be undone if we decide that it wasn’t the right thing to do. And then the bigger kind of, I’m going to go invest $1 billion, or some decision, or I’m going to launch a new service that is hard to pull back or is painful to pull back, those are the one-way door decisions that I think we want to have a little bit more inspection on. And even those, though, I think we are trying to figure out how do we make those faster too, and enable a broader swath of people to make those?

But you asked how I make decisions? I think for better or worse, my take is I am rarely, if ever, the expert on any particular subject that we’re working on. And whether we’re working on compute or on storage, talking about hypervisors, sales compensation, power contracts that we’re signing, go-to-market efforts, or marketing, I am rarely the expert in the room on those. And so I make sure that I listen and leave space for those experts who spend all of their days thinking about that to weigh in as to how they’ve come up with their recommendation, how they think about what we should do.

And then the part that I bring to that is to one, take a view of a non-expert and ask some questions and understand how they’re thinking about the problem. Then two, help connect the dots to the other part of the organization that they may not have visibility into and understand if there are trade-offs that they may not have thought about because they’re making a marketing decision and didn’t know about a new product that we were delivering over there. I try to make sure that, as an organization, we’ve connected those dots and then ask the right sets of questions. And then if there’s a tiebreaker decision I’ll have to do it so that we can move fast. I think the place we don’t want to be in is to sit there and just debate forever. At some point, you need a tiebreaker decision, and that’s what I view my job as doing as well.

All right, so I think this does bring us straight into AI because this is a bunch of decisions that everyone has to make and the outcomes are, I would say, still uncertain. As an industry, everyone is telling me this is the core enabling technology of the next generation of computing. This is a platform shift is the phrase that a bunch of CEOs have used with me. Do you think AI is a platform shift? Do you think it’s that big of a deal? Or is it just another suite of capabilities that AWS will offer people?

It’s a good question. I’ll start with how I believe that AI is incredibly transformational, whether you call it platform shift or not I can get to that in a second, but I think it’s an incredibly transformational technology that more than kind of … Look, these things come around every decade or so. I think it is one of the technologies that can be completely transformational. Whether it’s transforming industries, companies, jobs, workloads, or workflows, I think it has a real potential to have a material impact on every single piece of how we think about work, life, user experiences, and the like. I’m a full believer, that that is true. And I think there’s a timeline question: is that going to be in the next 12 months, 24 months, or the next five years? But I do think it is going to happen and it’s going to have a real change on a lot of pieces of business.

Platform shift is an interesting question because “platform” assumes that AI is not yet a platform and I think that that is a more open question. It’s a huge enabling technology. And whether you build on that AI or that AI is embedded in everything that you build with and is a core component of what you build with and how you think about … It’s a tool that is really meaningful and impactful. I think it remains to be seen as exactly what that means, but it is a transformational technology that-

Wait, can I make that simpler?

Yeah.

Can I put that on a spectrum for you, just to make this more concrete for the listener?

Do you think AI is more like multi-touch? Or do you think it’s more like the iPhone?

I don’t know if it’s really like either of those. I would bet that it-

Well, because multi-touch is like … You can’t make an iPhone without multi-touch, but that doesn’t imply that we’re all going to start using touchscreens all of the time.

Yeah. It’s not like multi-touch. It’s not like that. I don’t know if it’s an iPhone either, though. It may be more akin to the internet disruption. That’s what I’m saying. I don’t know if the internet is a platform, per se, it’s a shift in how you would deliver an application. So maybe it’s a platform. But I think it’s more akin to where there will be fundamental shifts in how you deliver products, offerings, and services, and how you do your work daily.

So the internet has been hugely transformational with how you do your work daily. You used to sit there on a typewriter or, I don’t know, write memos, or do whatever, and now you’re on a computer all day. You’re interacting on SaaS applications, emailing people, or there’s just fundamental connectivity. And I do think that AI is more akin to something like that, where it has that fundamental shift into how you’re going to get work done.

Yeah, I think you and I are both about the same age and you described the typewriter workforce with the same sort of, “I think that’s what it was like.”

Yeah. I don’t know. I never had a job like that.

It’s the same for me. I think, “Typewriters… people had them.” The timeline thing you brought up is really interesting: what is the timeline for this? It’s particularly interesting to me because I get a bunch of AI CEOs coming on the show telling me what their timeline for artificial general intelligence (AGI) is.

So Sam Altman recently said AGI would be possible on current hardware, and OpenAI is making a lot of noise about AGI for a variety of reasons that we can unpack at a later time. Mustafa Suleyman, who is the Microsoft AI CEO, was just on Decoder, and he said, “I don’t think we’re going to get to AGI on current hardware, but maybe within two to 10 years.” And he said we’re definitely not going to get there on Nvidia GB-200s.

You run data centers, you have a bunch of Nvidia chips in those data centers, and you are developing your own chips which I want to talk about. Where do you see yourself playing in that debate? Is it, “One of these vendors is going to light up AGI on someone’s data center, and I hope it’s AWS?” Is it, “I’m building this hardware to enable that to happen?” Is it, “This is what everyone’s talking about to goose their stock prices and I just need to sell more capabilities to more customers?”

Well, number one, it’s an impossible question to ask because there’s no definition of what AGI is. So when you reach is also an impossible definition because I don’t know. You can’t define when you reach an undefined thing.

What I would say is that I think that it’s just a continuum and I think that AI — we’ll call it AI inference, the ability to go do work — is going to continue to get more capable over time, and I think that there is a long road of this to get much, much, much more capable over time. And it’s going to get much less expensive to run over time, which I think then explodes the number of ways in which people will make it useful. Whether it’s running agents, doing other workflows, or performing long-running reasoning tasks, I think there’s a whole host of things that you can imagine. And so, there’s just a continuum of where the things eventually land and where you’re able to ask the computers to do more for you at lower costs.

I think hardware platforms are going to play a big part in that. I think software algorithms are going to play a big part in that and you’re going to need both of those. I don’t know when you reach AGI, I don’t know what that means, but I do think that the next generation of compute will be ... it’s going to deliver somewhere between. And whatever the current generation is that we just announced with Trainium 2, and eventually with Blackwells and GB-200s, I think we’ll give customers a 2–4x boost in compute capability per dollar. We announced Trainium 3, which will give another 2x boost to compute by the end of 2025.

That is going to help that goal. You will continue to get more and more, and you’re going to be able to do bigger and bigger things, and you’re going to need algorithmic improvements as well, which many of the teams, ours included, are very focused on doing.

But just straightforwardly, if OpenAI declares that it has achieved AGI, which it seems very much poised to do, it will have done that on a bunch of Azure data centers. Do you think AWS needs to credibly claim, “Oh, we can do that too,” to compete with Azure? I mean, they’ve defined AGI down, to be clear. But they’re going to say it pretty soon.

Yeah, I understand there are contractual terms that they’re working through. But they have some motivation for reasons to do that, from my understanding. But it’s not about declaring anything. It is just, “Let’s figure out what you are as a customer.” I am less interested in puffery in the press and more interested in how I can help customers achieve actual outcomes. And so it’s fine, there can be marketing statements. They can be like, “I have the biggest compute cluster in the world,” or, “I have AGI.”

Okay, but at some point I want to help a bank figure out how they can reduce the amount of fraud that they’re seeing, or improve the speed at which they can approve loans, or whatever the thing is that actually goes and helps the business. I want to help a biotech find cancer cures faster and better and figure out how they can significantly shrink and or improve the efficacy of what they find.

So those to me are interesting and useful outcomes. And so if you tell me, “Hey, can you help a customer find cures for cancer faster?” Awesome. That is a thing that I’m focused on. Was that AGI that did it or not? I don’t know. I’m not interested in that, per se. I’m more interested in, “Can I actually help our customers deliver value to their businesses?” And a little bit less on, “Can I have a stake in the ground around marketing?” Because I think, at the end of the day, customers actually care about that first one, not that second one.

I think this leads right into the next piece of the AI puzzle that I’m seeing unfold. It’s where should the investment go? Is it training new models which might be hitting a sort of scaling law problem, and getting less capable at a slower rate than they were before with every successive model? Or is it in inference, which is what you’re describing? “Hey, we can bring the cost and speed of inference down on the existing models and make cheaper, better, more cost-effective products.” Where’s your emphasis right now?

I don’t think you can pick one or the other. You absolutely … The world is going to deliver more capable models and they are expensive. They require a lot of compute, and it’s an area of investment for us, and it’s an area of investment for many of our customers. And I think it’s the right area of investment for a lot of those because I do think … You don’t get more capable, smaller models if you don’t have the large model to start with. That is just how it works. You can’t come out with something that’s a really, really powerful small model if you didn’t also build a frontier model, or start with a frontier model. So you have to have those large frontier models and I think we’re going to need those to be more capable.

There’s a lot of innovation and inference in how you can drive costs down. Some of that is a systems problem, some of that is a hardware problem, and some of that is an algorithmic problem. You can think about model distillation. There’s a whole bunch of techniques that you can do to get these smaller, faster inference models, which I think are going to be hugely impactful and important to delivering real value to enterprises.

I think you go talk to customers now and they are no longer interested in bright, shiny AI proof of concepts. They want something with a real return on investment (ROI) associated with it. And the ways you deliver great ROI are that you either have more value and/or less cost. I think both of those are going to be important to keep raising the level of ROI that you can deliver. So, if we think there is this massive ability to transform organizations, we have to keep increasing what models can do and decreasing how much they can cost. I don’t see how you pick one of those. I think you have to do both.

If you had to pick one, it sounds like you would pick inference, right? Because that’s where the products are getting built.

Yeah. Well, what I’ll tell you is, in my keynote at re:Invent, I talked about another thing that I like to do in Amazon, and we do here, which is that we refuse a thing we call the “tyranny of the or,” which is forcing someone to pick A or B stifles innovation. It means that you don’t go out and invent how to do A and B. And so you can’t pick. I’m telling you, it is not an A or a B chance, it’s an A and B, and we have to push our teams to figure out how to do both, which includes bigger training — and we have to lower the cost of that, by the way. It can’t just keep scaling linearly, which is all part of the silicon investments that we’re making and networking, and things like that. How do you make the cost to train these really large models lower, so that you can train bigger models?

And I think we have to make that investment. We are making that investment and it’s a huge area of opportunity for us because today it’s too expensive to continue to ramp at the rates of the cost of the infrastructure. That’s a big part of Trainium, investing in how to get the cost down for training. I think the inference side has to drive costs down too, which is incredibly important for the adoption side of it. So you have to do both. It won’t work if you just do one side.

I did watch your keynote and you are welcome for that alley-oop on the “tyranny of ‘or.’” I knew it was coming because I wanted to ask about Trainium. This is a huge investment. You’ve been at it for several years, you announced Trainium 2 at re:Invent, it has additional capabilities in training and inference. It’s designed to be good at inference, so you can use the same chip everywhere.

Building these chips is a huge investment, and you are up against dedicated chip companies. You’re up against AMD, which is also making a huge investment. You’re up against Microsoft, which is making its own investments. You’re up against Nvidia, which is the leader and has a huge head start, not only in the chips but also in the software ecosystem around the chips. What do you think about that competition and that investment?

It’s less a competition and more an addition of choice. I don’t think it is GPUs or-

Oh, by the way, I forgot Google. I should probably point out that Google has an advanced data center and AI capabilities.

Yeah, Google does, that’s right. And so it turns out we’ve been making chips now for over a decade. So we’ve been making silicon chips, our own custom silicon for more than a decade. We’re actually … we have one of the most experienced teams in the industry doing this, and so it’s not a new thing. It’s not like we dove in here and said, “We have no idea what we’re doing,” By the way, some of those others are learning it for the first time. Not Nvidia of course, or AMD, and Google’s been making chips for a little while too. I think Microsoft is pretty new to this space. But we think that that is a big advantage for us as we understand how to do this at scale, and we understand how to do it in the cloud.

I think we have some advantages in that we don’t have to do it for a broad set of customers. We have to deploy our chips in exactly one environment. We have to deploy them in an AWS data center. We have to deploy them in exactly one server, or we don’t have to support a whole OEM infrastructure, a set of different drivers, or a bunch of different things. It’s just in our environment and we know exactly what that’s going to look like. And we think it’s a choice. We don’t think that it has to meet every single use case for every single customer.

We think that Nvidia GPUs, AMD GPUs, and others are going to be super interesting. They have good platforms. Both of them have very good teams that are executing really, really well, and I think they will continue to do that. I don’t see any reason why they wouldn’t. We plan to be a great partner of theirs for a really long time and support that and offer it to customers when it’s the right technology choice for their use case.

We think that we can offer interesting choices, and we’ve done it with Graviton. We’ve proven that we can launch a processor at a broad scale that is very useful for a set of workloads, a broad set of workloads for our customers. And in Graviton’s case, it doesn’t mean we don’t buy a ton of Intel and AMD chips and offer those to customers. We of course do, and those are growing businesses for us as well. It’s just more choice. And we think that choice makes AWS a more attractive platform for customers because they have more choices than they do other places. That additional choice is nice, and part of that choice is we want to really lean in and make sure it’s the best place to run Nvidia GPUs, AMD, Intel, and others.

But it’s a big opportunity for us. And if you do think, which we do, that AI is going to disrupt all of those different industries, it’s a massive opportunity where it’s not one player that is going to be the only compute platform that all of those things run in over time. We think that we have an opportunity to build some of that and provide differentiated choices for customers who choose to run AWS.

Chips and chip investment is a long-term decision. You’re making decisions now and allocating capital that might not pay off for a decade or more. Do you think that model training is hitting a scaling limit? That it’s going to plateau the way that some people are saying it’s plateauing?

I think people like to talk about scaling laws because again, it sounds fun to talk about. But I think that it probably just means there have to be more levels of invention. I think if you look over any technology ramp, you see one particular technique ramping up like this and then it slows down, and then somebody says, “Oh, how about you try this?” And then it goes back up again, and then you try something else. And so there’s going to have to be software and algorithmic changes. I think it’s not a blind dump of more data, add more compute, close your eyes, and then you get a bigger model next year. You’re going to need smart people looking at it, driving it, and figuring out new ways to help that. But that doesn’t mean that you’ve hit a limit. I think it’s just that you’re going to have to keep innovating in different ways.

Think about, number one, how long, and it was longer than a decade, that people were saying that we were hitting Moore’s Law of scaling limits. That was, “Can you take 17 nanometers and make it 15 nanometers and 13 nanometers?” And you’re saying, “Okay, there’s going to be a limit.” They had to figure out the technology to get past a couple of those. I remember somewhere around 10 nanometers, people were like, “I don’t think you can get past this,” and now we’re building three-nanometer chips. And so you keep getting smaller because there are new technologies in there.

You had to figure out how you deal with interference, and you had to think about actually stacking the memory, different structures of the chips, and other things like that — but you work through those. In the meantime, you kind of figured out how to do more compute on an accelerator like a GPU, which then gave you a huge step change in compute. And so, no longer are people worried about whether we are hitting the limits of what a 17-nanometer Intel chip from 10 years ago is doing, right? Now we’re orders of magnitude more compute than that.

Well, hold on, hold on. I mean, this is the real limit. One company figured that out. Taiwan Semiconductor Manufacturing Company (TSMC) figured that out using an EV machine from one company in the Netherlands. And they’re the provider for everyone, which means you are now asking TSMC for capacity in competition with Nvidia, Apple, Qualcomm, AMD, and even, to some extent, in competition with Intel, right?

They figured out parts of that. I mean, they figured out the layout chip. And by the way, [TSMC CEO] C.C. Lei and the team did a fantastic job of figuring it out. So yes, but the world figures it out, right?

But Intel famously did not figure this out.

They didn’t.

I mean, that’s where they are right now.

But others have.

I’m saying right now the bottleneck in the chip industry, in the investment, is one company can provide this product. Is that something that you actively think about? Like, “Do they have the capacity to let us compete?”

I mean, they’re making lots of investments and I think they’re scaling. I think others are looking to catch up in that space too. They have a great lead, and this is also true in technology and has been for a long time. Somebody jumps ahead and figures it out, gets a lead, and it’s a benefit for them for a while and others catch up. I think you can look at some of the High Bandwidth Memory (HBM), and some of those other fabrications that are coming up, and they’re catching up and finding other new ways to do that. There will be other inventions that leapfrog over time. But obviously, fabs are hugely capital-intensive investments. And so, I am sure that others will eventually find new and different ways to innovate around that too. It has always been true in technology.

Are you making any bets on any non-TSMC fabs?

I wouldn’t have anything to announce there, but we partner with lots of folks. We partner with Samsung, Intel, and others that have their own fabs as well, and buy lots of other stuff from them. From memory to CPUs, we buy parts from lots of different fabs around the world.

The other big constraint is power. You have said two to three generations from where we are in AI we’re going to need one to five gigawatts of power, about a medium city. This led you to talk about nuclear power and how we’re going to need that. That’s a big deal to say, “Okay, we’re going to need so much AI capacity that we’re going to build nuclear power plants.” Microsoft and other companies have said the same thing. Is that still where your mind is? This is going to be so successful that Amazon is going to try to build some power plants?

Yes. It is. We’ve made significant investments there. And that’s a range of things, by the way. It’s a portfolio. This is not a new plan for us. Over the last five years, we have commissioned more renewable power projects than ... Each year for the last five years we’ve commissioned more than any company in the world. And that’s bringing on new power into the grids, and whether they’re new solar farms or the new wind farms, and now we’re adding nuclear to that. So it’s just a portfolio of that. I think the world is going to need more carbon-free energy, and compute and data centers are a big portion of that. We are pushing hard to make sure that the world has enough sources of that. I do think that nuclear power will be an important component of that plan over the next couple of decades.

And so, we are excited about small modular reactors. I think that it’s a technology that’s a little ways away. By the way, it’s not a solve for the next couple of years, but past 2030 and beyond, I think it could be a very important component. One, you can actually put it near where you need the power to be.

Another of the bottlenecks that we run into is around transmission. It’s not just power generation, but it’s transmission. So you can have a solar farm out in the desert, but if you don’t have transmission to get it to where your data centers are, then it doesn’t do a lot of good. Those are both problems that need to be solved. And it’s not just data centers, it’s electric cars, it’s electrification of all of our businesses. There’s a bunch of these things that are going to need to happen, and so I think nuclear power is going to be an important part of that, and small modular reactors.

I think the world’s going to have to build more of these large industrial-scale nuclear plants as well. I think a lot of people’s heads are in the “That was scary back in the ‘50s when the technology wasn’t as safe.” Today, it’s a very safe, scalable technology, but it’s something that we have to keep spending on and scaling.

We’re going to have you back for another full hour on nuclear power plants. That’s a whole rabbit hole that I want to talk about at some point in the future. But we’re running out of time here. And I just want to ask the biggest question of all. This is a lot of huge forward investment. You’re designing chips, we’re investing in TSMC’s capacity. We’re talking about nuclear power plants, we’re building bigger data centers. There’s an $8 billion investment in Anthropic to help build a data center and then run Anthropic and Claude.

When is any of this going to make a dollar? You need a product in the consumer or enterprise market that throws off enough margin at enough scale to fund all of this investment and still make money for the people making the product. And ideally, the people paying for the product are using it to make more money on the other side. The economics of this are still very unclear to me unless you are Nvidia. When does all of this make a dollar for you?

Yeah. Well, AWS is a nice, profitable business for Amazon.

Right, you’ve got the margin to spend on it, but at some point, it has to return.

I think, look, and for customers, they’re increasingly looking at it this way. It’s not just us. And I said this a little bit ago. If you talk to customers they are very focused on how they can have ROI-positive AI projects. I think the cloud has already proven to be ROI positive across a broad swath of industries. We’re moving your data to the cloud, your compute to the cloud, and you gain agility. And so I think we’ve proven that we can deliver great ROI for customers in moving to the cloud broadly and taking AI aside.

And so, what we’re increasingly seeing customers say is, “I want to see the ROI of these AI projects.” And I do think that that is an important shift where it is not just the cool, it’s not just the shiny object factor, it is a, “How do I make sure this makes sense?” And we are spending time with customers thinking about that. How do you work through the use cases that are enabled today that can deliver real value? Some of those are broadly reported around things like modernizing your contact center, and we think Connect is a great offering for customers to do that. We’re actually seeing a huge number of customers move to Connect in a cloud contact center to take advantage of many of those AI capabilities. You see some of that in optimizing your back-office projects.

And I think increasingly, as the agentic workflows really get much more powerful, and as we think about collaborative agentic workflows and longer running agentic workflows, you’re going to see more and more value come up through these. As the models get more capable you’re going to see more value coming up through those. And so I think it’s on us. It’s incumbent on us to make sure that these are very profitable for end customers to go and implement.

But let me just put that in a framework that makes it maybe a little bit sharper.

You’ve been at AWS since the beginning. AWS started, and I’m going to flatten this narrative, you can correct me for it being a little too flat, but just in the flattest possible way: Amazon is building a bunch of these services. “Hey, we have excess capacity. Hey, we want to build microservices for our own components. We can resell those.”

So you get a bunch of benefits along the way of just building Amazon, and then you can turn that into a business. AI, right now, feels like there are a bunch of ideas for products that might be useful. Inside Amazon, outside of Amazon, for AWS’s customers, whoever, but it requires a massive amount of forward investment.

It’s not just, “We’re kind of doing it anyway.” It’s much more, “Hey, there’s a huge opportunity here. We need to leapfrog ahead and maybe get some more customers.” Or maybe there’s a platform shift or whatever it is. We all see the huge promise that is happening at a subsidy, and that subsidy seems dangerous.

It’s not the right characterization of it. So there are a couple of things I would say. Number one is that AWS was never about excess capacity of Amazon. Just like math doesn’t work. You can imagine that I’ve heard that narrative, it sounds nice. And as soon as Christmastime comes around, if I have to take Netflix’s servers away so that we can support retail traffic, that doesn’t really work as a business. So that was never the idea, intent, or goal of AWS.

And we built the businesses from scratch. They weren’t reusing Amazon components. We learned from that. They’re an incredible early customer to learn from the components that they would need. But we built them from the ground up to support a broad range of customers. AWS itself was a big investment by Amazon to go after a broad new business. As you think about it now, we had Amazon as a big customer of ours, for sure, and they were a super helpful customer for us to learn about what large enterprises would need from services like AWS and they continue to be.

I think AI is not that dissimilar. Amazon needs AI. You mentioned that you watched my re:Invent keynote, Andy was up there for 25 minutes talking about all of the cool things that the rest of Amazon is doing with regards to AI. And you’re talking about Rufus, you’re talking about how we’re thinking about our supply chain and fulfillment centers, and across the whole scope of ... And Alexa. That business desperately needs AI capabilities to, again, reimagine our business, get more efficiencies, and deliver new experiences for customers. Amazon is customer number one for a bunch of these capabilities. So if AWS can build them and Amazon can take advantage of them, that’s fantastic and both of those things are true.

So yes, it’s a big forward investment, but we also have Amazon still using them, and we are in a different place now. When we started in 2006, we had zero external customers, and we now have a million external customers or multiple millions of external customers. That is a huge customer base that is ready, willing, and excited to buy and use the products that we have. So that investment is a forward investment, but you also have a really big base that you can amortize it across and go offer it to, which makes that investment thesis a little bit easier to get over.

All right. So I’m going to ask you the same question again to wrap up with all this context. When do you think all this investment will become ROI positive?

I think it’s a positive ROI. Well, it depends on what you mean by ROI positive. I think there’s a lot of investment in the world.

Right. But this is a lot of investment in AI across the industry. When do you think it’s going to start returning?

I mean, if you think globally, I think it’s ROI positive now. I think the question is when does it become more evenly distributed? Look, I think the hardest question of that, honestly, is for the model producers. I think that’s the single hardest question. I actually think today, or if not today, very soon, it is going to be ROI positive for the broad swath of customers using AI and building it in, like banks, insurance companies, pharmaceuticals, and others. You can make that ROI-positive story today, and I think it will continue to get better. And I think for infrastructure providers like Nvidia, of course, it’s very ...

They’re doing fine.

I think the question is when does … The folks who are making the huge investments are the ones who are building foundational models from a software perspective and then reselling those foundational models. It’s a good question. I don’t know the answer to when that investment kind of fully pays off for an OpenAI or an Anthropic. I think Amazon and Google probably have a different math of when we can make those pay off because you get internal usage of them from your own use. I don’t know that. But there’s a lot of smart people investing in, continuing to put investment in a broad swath of AI companies. And you have to believe, which we do, that there is a massive economic benefit from many of these AI capabilities that are orders of magnitude bigger.

I do think it really plays into that math equation. As inference gets cheaper and more capable there are multiple orders of magnitude more inference to be done. And that is when it ultimately starts to pay off, I think, for a lot of those model providers, and in a huge, massive way.

All right, you are clearly in the weeds of all these products, which is fun to hear. Let’s end here. Last question. When you’re trying out all these AI products, which is the one that you use that makes you think, “Okay, is this investment worth it”?

That’s a good question. I don’t know if there was any one product that I got excited about. The first product that I ever used that I said, “Hey, I think this is real,” is just like everybody else. I think ChatGPT was just a transformational product. It was a great UI and it really unlocked for everyone what was possible. So the first time that I really realized that this was going to take off. We were making investments internally, but I think we were hopeful that they would get there. I think that’s the first one that I used that I really understood.

Now it’s hard because I use thousands of them and I think all of them are really cool. And I think there are a lot of startups from people that are building AI products. People who are making new proteins — which is incredible — folks like Perplexity who are making search engines that are much more interesting, contact centers, and banking applications. There’s a whole host of them now that are incredible. I think Amazon makes some, and many of our partners make many, so those are all incredible. But it really was, just like the rest of the world, I think ChatGPT was the first one that really helped solidify it.

Got it. Very diplomatic answer. Matt, this was great. You’ve got to come back. I really enjoyed this conversation.

Great. Thanks for having me.

A podcast from The Verge about big ideas and other problems.

A weekly newsletter by David Pierce designed to tell you everything you need to download, watch, read, listen to, and explore that fits in The Verge’s universe.
