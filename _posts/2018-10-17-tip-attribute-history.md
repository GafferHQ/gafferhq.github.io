---
layout: post
title: "Attribute History"
icon: /resources/images/tip-attribute-history-icon.png
category: tips
tags: [nodes, scene]
---

Today's tip will be a bit longer than usual. We'll be taking a dive into a very powerful built-in feature of Gaffer: the attribute history.

Let's say you inherit a node graph in Gaffer, and you can't make heads or tails of it:

> **Note:** This graph is for demonstration purposes only, and is intentionally artificial and poorly built.

<img class="mb-30" src="/resources/images/tip-attribute-history-messy-graph.png" alt="A messy graph">

Let's also say that by the end of the graph, the asset has a particular attribute – in this case, an OpenGL shader that puts coloured points along its surface – and you'd like to find out which node in the graph assigned the particular value of this attribute. To accomplish this, you can use Gaffer's _Show History_ feature, which provides a list of each node in the graph that affected a particular scene attribute (or any scene property, in fact). With this powerful feature, you can clarify even convoluted graphs, and determine which nodes are affecting attributes, and then locate them in the _Graph Editor_.

### Viewing Attribute History ###
To view the attribute's history:

<img class="mb-30" src="/resources/images/tip-attribute-history-openAnimation.gif" alt="Demonstration of opening the attribute history">

1. Select the node at the part of the graph you wish to investigate.
2. Select the target location in the _Hierarchy View_.
3. In the _Scene Inspector_, under the _Selection_ tab, right-click the attribute's value, and select _Show History_.

The attribute's history window will open, and show all nodes that affected the attribute. If a node modified the attribute's value, the value will be highlighted in <span style="padding: 0 3px; background-color: #008800; border-radius: 3px; color: white">green</span>.

### Locating a Node in the Attribute History ###
You can also pin-point the location in the _Graph Editor_ of any node in the attribute history.

> **Note:** This feature does not currently focus on nodes inside of Box nodes.

<img class="mb-30" src="/resources/images/tip-attribute-history-drag-nodeAnimation.gif" alt="Demonstration of dragging nodes from the attribute history to the Graph Editor">

1. Click and drag the node name from the attribute history window. The cursor will change to ![node selection](/resources/images/gafferUI/nodes.png).
2. Release over the _Graph Editor_.

The node will be framed in the _Graph Editor_, at which point you could select the node and begin adjusting its plug values.
