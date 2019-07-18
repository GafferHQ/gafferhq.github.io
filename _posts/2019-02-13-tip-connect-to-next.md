---
layout: post
title: Connect to Next
author: Michael DuBelko
images: /content/images/2019-02-13-tip-connect-to-next/
banner: splash-connect-to-next.png
tags: [tip, ui]
---

When constructing networks that use the Loop node, you'll often find yourself adding Dot nodes to connect the _previous_ plug to the returning _next_ plug, in order to give the connection proper visibility.

![Connecting a Loop node improperly.]({{ page.images }}/loop-network-bad.png)

<p class="text-muted px-3">It's bad practice to directly connect the <em>previous</em> plug to the <em>next</em> plug, because the connection wraps around behind the nodes.</p>

The Loop node has a shortcut that will lay out a square of Dot nodes for you automatically:

1. Right-click the _previous_ plug. A plug context menu will open.
2. Select _Connect to Next_.
3. From there, you can complete the Loop network: ![Using Connect to Next in a Loop network]({{ page.images }}/connect-to-nextAnimation.gif)
