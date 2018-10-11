---
layout: post
title: "Clipping Planes"
subtitle: "Tip of the Day"
icon: /resources/images/tip-clipping-planes-icon.png
---

Like other DDCs, Gaffer uses clipping planes in its viewport (the _Viewer_) for selective rendering. The clipping planes can be set to confine the current view to a selection of scene locations.

<img class="mtb-30" src="{{ site.baseurl }}/resources/images/tip-clipping-planesAnimation.gif" alt="Demonstration of the clipping planes">

To set the clipping plane to enclose one or more locations:

1. Select the location(s):
    - In the _Graph Editor,_ select one or more locations, or
    - In the _Viewer,_ select one or more locations' objects.
2. Right-click inside the _Viewer_.
3. Select _Clipping Planes_ > _Fit to Selection_.

> **Tip:** After the location(s) are selected, you can also hover the cursor over the _Viewer_ and hit <kbd>Control</kbd> + <kbd>K</kbd>.

To reset the clipping planes back to default:

1. Right-click inside the _Viewer_.
2. Select _Clipping Planes_ > _Default_.
