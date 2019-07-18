---
layout: post
title: Plug-to-plug driving
author: Michael DuBelko
images: /content/images/2018-09-10-tip-plug-to-plug-driving/
banner: tip-plug-to-plug-driving-lead.jpg
tags: [tip, ui]
---

Sometimes, you want one plug's value to determine another plug's value. You could accomplish this with an Expression node and some Python, but today we'll show you a far easier method: create an auxiliary connection between them by dragging and dropping one plug onto another.

![Demo of driving a plug with another plug]({{ page.images }}/tip-plug-to-plug-driving.gif)

In most cases, the plugs must be of the same type: string, bool, float, V3i, V3f, etc. The exception is integer plugs, which can drive and be driven by floats and bools (the value will be converted automatically). As you would expect, the same two plugs cannot drive each other.

To make one plug drive another:

1. In the Graph Editor, double-click the source node, and then the destination node, which will open a new Node Editor window for each.

    > **Note:** For either source or destination node, you can instead use the _Node Editor_ in the top-right panel of the default layout.

2. Click and drag the source plug's label inside its Node Editor and drag it onto the destination plug inside its respective _Node Editor_.

Once the auxiliary connection is created, a green line will appear between the nodes, with an arrow pointing at the destination node. 
