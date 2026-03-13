---
title: pain in the ascii
date: 2026-03-09
---
I spent most of my blog time today and yesterday trying to figure out the little ascii stamp symbol. It was rendering fine on desktop, but on mobile it was eating spaces, or so I thought. I assumed it was Jekyll doing some processing that collapsed empty spaces, but ultimately that wasn't it.

After fiddling with css and liquid templates for way too long, I realized that the spaces were all there, but my phone's monospace font doesn't have spaces that are actually monospace. So it was just monospaced block characters with regular spaces.

Anyway, the fix was to put monospace characers in for the spaces and style them insivible. A pain to be sure, but it worked. I also moved it to an include file so I don't need to worry about accidentally deleting part of it and breaking it. I thought ascii would be easier than making an svg, but I was so wrong. Now I have learned.