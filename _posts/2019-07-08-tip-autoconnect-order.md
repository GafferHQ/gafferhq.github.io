---
layout: post
title: "Automatic Connections to New Nodes"
subtitle: "Tip of the Day"
icon: /resources/images/2019-07-08-tip-autoconnect-order/spaghetti.png
category: tips
tags: [nodes]
---

When creating Switch, Group, or Parent nodes in the _Graph Editor_, Gaffer will automatically connect your current selection to the new node. Sometimes, though, you will end up with an array of connections that are all out-of-order and crossed-up. Fortunately, there is a simple trick you can use to guarantee the correct order.

![Autoconnect with bad order](/resources/images/2019-07-08-tip-autoconnect-order/auto-connect-bad-orderAnimation.gif)

But first, why does this happen in the first place? It's because when you automatically connect to a newly created Switch, Group, or Parent node, the selected nodes will connect to it based on the order in which you selected them. If you select all the target nodes at once by dragging a marquee around them, the resulting connection won't always be predictable, because it's not clear to Gaffer how you want to order them.

So, in order to preserve sanity, if you instead <kbd>Shift</kbd>-click the nodes in the order you wish to connect them, the resulting connections will end up exactly as expected:

![Autoconnect with correct order](/resources/images/2019-07-08-tip-autoconnect-order/auto-connect-good-orderAnimation.gif)

Simple!
