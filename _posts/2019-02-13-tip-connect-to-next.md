---
layout: post
title: "Connect to Next"
icon: /resources/images/2019-02-13-tip-connect-to-next/splash-connect-to-next.png
category: tips
tags: [nodes]
---

<!-- Add an image path macro for implicit page-based file paths -->
{% assign post-directory = page.path | remove: '_posts/' | remove: '.md' %}
{% assign images = site.images | append: "/" | append: post-directory %}

When constructing networks that use the Loop node, you'll often find yourself adding Dot nodes to connect the _previous_ plug to the returning _next_ plug, in order to give the connection proper visibility.

![Connecting a Loop node improperly.]({{ images }}/loop-network-bad.png)

<small>It's bad practice to directly connect the _previous_ plug to the _next_ plug, because the connection wraps around behind the nodes.</small>

The Loop node has a shortcut that will lay out a square of Dot nodes for you automatically:

1. Right-click the _previous_ plug. A plug context menu will open.
2. Select _Connect to Next_.
3. From there, you can complete the Loop network: ![Using Connect to Next in a Loop network]({{ images }}/connect-to-nextAnimation.gif)
