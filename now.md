---
layout: page
title: now
---

### mood: <a href="https://www.imood.com/users/jomolin" style="border-bottom: none;"><img src="{{ '/assets/imood/face.gif' | relative_url }}" alt="mood face" style="height: 1em; width: auto; vertical-align: middle; margin-right: 0.25em;"><span style="font-weight: 400; -webkit-text-stroke: 0;">{% if site.data.mood.current %}{{ site.data.mood.current }}{% endif %}</span></a>
{% if site.data.mood.personal %}<p style="font-style: italic; font-weight: normal;">{{ site.data.mood.personal }}</p>{% endif %}

### status

- Just trying to get to the end of the year with a little sanity intact. Working inside the systems without losing myself is much harder than the actual teaching.
- Went back to Korea in July 2025. Realized how much New Zealand doesn't agree with me.
- Korean language meetups stopped after the last venue closed confirming my suspicion that New Zealand can't support businesses. This means no regular physical meetups which is a bit depressing.

### reading

{% include currently_reading.html %}
