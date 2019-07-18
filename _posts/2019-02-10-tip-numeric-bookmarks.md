---
layout: post
title: Numeric bookmarks
author: Michael DuBelko
images: /content/images/2019-02-10-tip-numeric-bookmarks/
banner: splash-numeric-bookmark.png
tags: [tip, workflow]
---

A **numeric bookmark** is a node bookmark associated with a number key (<kbd>1</kbd> through <kbd>9</kbd>) on the keyboard.

Once assigned, hitting the key of a numeric bookmark will pin the currently focused editor to the node.

Unlike regular bookmarks, instead of having to find the bookmarked node from a list, you can use the number keys as shortcuts to bookmarks that are important to you, or that you use frequently. Also unlike regular bookmarks, numeric bookmarks are **not** stored when you save the graph.

> **Tip:** You can use the keys both on the main number row and the numpad.

The icon on the bookmarked node indicates the bookmark type:

- ![Regular bookmark]({{ page.images }}/regular-bookmark.png) Regular bookmark
- ![Numeric bookmark]({{ page.images }}/numeric-bookmark.png) Numeric bookmark (the number corresponds to the key)
- ![Regular and numeric bookmark]({{ page.images }}/regular-numeric-bookmark.png) Regular **and** numeric bookmark

### Assigning and unassigning a numeric bookmark ###

To assign/unassign a numeric bookmark to a node:

![Assigning and unassigning a numeric bookmark.]({{ page.images }}/assigning-unassigning-numeric-bookmarksAnimation.gif)

1. Select the node in the _Graph Editor_.
2. Hit <kbd>Ctrl</kbd> + <kbd>1</kbd>–<kbd>9</kbd> to assign a bookmark, or hit <kbd>Ctrl</kbd> + <kbd>0</kbd> to unassign the existing bookmark.

Alternatively, you can assign/unassign numeric bookmarks with the context menu:

1. Right-click the node in the _Graph Editor_. The node context menu will open.
2. Select _Numeric Bookmark_ > _1_–_9_, or _Numeric Bookmark_ > _Remove_.

After assignment, a numeric bookmark icon with the number you chose will appear on the node. After unassignment, the numeric bookmark icon will disappear from the node.

### Pinning and unpinning to a numeric bookmark ###

To pin or unpin an editor to an assigned numeric bookmark:

![Pinning and unpinning numeric bookmarks to various editors.]({{ page.images }}/pinning-unpinning-editor-to-numeric-bookmarkAnimation.gif)

1. Hover the cursor over the target editor.
2. Hit the number key of a numeric bookmark to pin, or hit <kbd>0</kbd> to unpin.

Alternatively, you can pin a numeric bookmark using the pin context menu:

1. Right-click the editor's ![pin icon]({{ site.images }}/gaffer-ui/targetNodesUnlocked.png). The pin context menu will open.
2. Select _Bookmark_ > _1_–_9_.

After pinning, the editor will stay locked to the node, and if you select a different node/object, the editor won't update. After unpinning, the editor will no longer be focused on the node, and will return its focus on the currently selected node/object, or, if there is no selection, go blank.
