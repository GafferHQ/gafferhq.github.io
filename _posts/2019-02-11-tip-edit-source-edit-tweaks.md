---
layout: post
title: "Edit Source & Edit Tweaks"
icon: /resources/images/2019-02-11-tip-edit-source-edit-tweaks/splash-edit-source-edit-tweaks.png
category: tips
tags: [nodes, viewer]
---

When browsing a scene, it can be tricky to find and edit the node that generated or tweaked an object, especially if your graph is large, has many Box nodes, or depends on upstream components.

<!-- Add an image path macro for implicit page-based file paths -->
{% assign post-directory = page.path | remove: '_posts/' | remove: '.md' %}
{% assign images = site.images | append: "/" | append: post-directory %}

To make finding and editing upstream nodes more convenient, the following quick actions are available:

- **Edit Source** (<kbd>Alt</kbd> + <kbd>E</kbd>): Edits the node that generated the selected object.
- **Edit Tweaks** (<kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd>): Edits the most recent node that tweaked the selected object.

### Edit Source ###

![Edit Source in the Viewer and the Hierarchy View.]({{ images }}/edit-sourceAnimation.gif)

To edit an object's source node:

1. Select the object in the _Viewer_ or its location in the _Hierarchy View_.
2. Make sure to keep the cursor inside the _Viewer_ or _Hierarchy View_.
3. Hit <kbd>Alt</kbd> + <kbd>E</kbd>.

Alternatively, from the _Viewer,_ you can use the context menu:

1. Right-click the _Viewer_.
2. Select _History_ > _Edit Source..._.

In both methods, a _Node Editor_ window that is focused on the source node will open.

### Edit Tweaks ###

![Edit Tweaks in the Viewer and the Hierarchy View.]({{ images }}/edit-tweaksAnimation.gif)

Edit Tweaks searches for upstream ShaderTweaks and CameraTweaks nodes. It cannot search downstream.

To edit the most recent ShaderTweaks/CameraTweaks node that affected the shader of an object:

1. Select the object in the _Viewer_ or its location in the _Hierarchy View_.
2. Make sure to keep the cursor inside the _Viewer_ or _Hierarchy View_.
3. Hit <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>E</kbd>.

Alternatively, from the _Viewer,_ you can use the context menu:

1. Right-click the _Viewer_.
2. Select _History_ > _Edit Tweaks..._.

In both methods, a _Node Editor_ window that is focused on the relevant ShaderTweaks/CameraTweaks node will open.
