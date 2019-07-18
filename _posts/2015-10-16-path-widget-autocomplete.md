---
layout: post
title: Use autocomplete in path widgets
author: John Haddon
images: /content/images/2015-10-16-path-widget-autocomplete/
banner: tabComplete.png
tags: [tip, ui]
---

If you've spent much time in a UNIX shell, you probably already know and love tab completion, whereby hitting the tab key will autocomplete the current filename based on the first few characters entered. It's particularly handy for navigating the kind of deep directory structures that seem to typify VFX job structures. It's worth knowing that Gaffer's path widgets support the same tab complete mechanism - just **type part of the name, hit tab and if possible it'll be completed for you**. Here's an example.

Sometimes though, you don't know the first few characters of the name you're looking for, so tab complete is of no help. In this case you can **hit the down cursor to get an interactive listing** of all the files and directories at the current location.

![Cursor down animation]({{ page.images }}/cursorDownAnimation.gif)

You're not limited to doing this via the keyboard either. Just **double-click a name with the mouse to get the listing** at any time. If possible, the subdirectories below the selection are maintained when making a selection, which makes jumping between the same location in multiple shots pretty straightforward.

![Double-click animation]({{ page.images }}/doubleClickAnimation.gif)

Finally, you can **triple click** to select all the text, and **jump to any parent location**.

![Triple-click animation]({{ page.images }}/tripleClickAnimation.gif)
