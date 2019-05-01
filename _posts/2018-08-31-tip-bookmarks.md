---
layout: post
title: "Bookmarked Nodes"
icon: /resources/images/tip-bookmarking-nodes-lead.jpg
category: tips
tags: [nodes]
---

Gaffer has a very useful node bookmarking feature, which can make working with large and complex graphs much easier. Today, we'll show you how to use it.

<img class="mtb-30" src="/resources/images/tip-bookmarking-nodes-lead.jpg" alt="A bookmarked node">

When a node is bookmarked, it becomes accessible from anywhere in the _Graph Editor_ (with one exception). This allows you to quickly connect to a bookmarked node from other nodes, even when not currently in frame in the Graph Editor.

<img class="mtb-30" src="/resources/images/tip-bookmarking-nodes.gif" alt="Demo of connecting to bookmarked nodes.">

To bookmark a node:

1. In the _Graph Editor_, right-click the node you wish to bookmark. The node context menu will appear.
2. Select _Bookmarked_. A red bookmark will appear on the node.

To connect to a bookmarked node:

1. In the _Graph Editor_, right-click the plug of a node. The plug context menu will appear.
2. Navigate to _Connect Bookmark_ and then select the bookmarked node from the list.

Two notes on bookmarking:

The target node and the bookmarked node must be at the same graph depth. For example, you cannot connect a node at the root of the graph to a bookmarked node inside of a Box node.

Furthermore, when connecting to a bookmarked node, the plugs must be compatible by data type (scene plug → scene plug; image plug → image plug; etc.) and direction (input plug → output plug; output plug → input plug).
