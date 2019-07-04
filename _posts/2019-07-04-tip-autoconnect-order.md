---
layout: post
title: "Automatic Connections to New Nodes"
subtitle: "Tip of the Day"
category: tips
tags: [nodes]
---

<img width="200" class="float-left" style="margin-right: 20px;" src="{{ site.baseurl }}/resources/images/2019-07-04-tip-autoconnect-order/spaghetti.png" alt="Spaghetti">
When creating Switch, Group or Parent nodes in the _Graph Editor_, Gaffer
will automatically connect your current selection up to the new node.
Sometimes though, you end up with something similar to the picture to the left.
But why would it do such a thing? <br><br>
Gaffer will connect to the new node's plugs from left to right, based on the
order of your selection.  If you drag-selected the nodes, this isn't always
predictable. So in order to preserve sanity, if you instead <kbd>Shift</kbd>
click the nodes you wish to connect, in a left-to-right order, it should end
up just as you expect!

