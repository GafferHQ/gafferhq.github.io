---
layout: post
title: "Release: Gaffer 0.53.1.0"
subtitle: "Releases"
icon: /resources/images/2019-02-14-announce-gaffer-53/gaffer-53-splash.png
---

<!-- Add an image path macro for implicit page-based file paths -->
{% assign post-directory = page.path | remove: '_posts/' | remove: '.md' %}
{% assign images = site.images | append: "/" | append: post-directory %}

<style type="text/css">
    span.changelog {
        border: 1px solid;
        padding: 0 1px; 
        border-radius: 2px;
    }
    span.changelog-new {
        background-color: #ccf7cc;
        border-color: #b4f7b4;
    }
    span.changelog-updated {
        background-color: #f7f7cc;
        border-color: #f7f784;
    }
    span.changelog-removed {
        background-color: #f7cccc;
        border-color: #f7cccc;
    }
    span.changelog-deleted {
        border: none;
        border-bottom: 1px dotted red;
    }
    li {
        margin-bottom: 10px;
    }
    li > ul li:first-child {
        margin-top: 10px;
    }
    h3 {
        margin-top: 2em;
    }
</style>

<img class="mb-30 show" style="margin: auto" src="{{ images }}/gaffer-53-splash.png" alt="Gaffer 0.53.1.0 release splash">

Recently, we reached a development milestone: **Gaffer 0.53.1.0**. This is a huge update, filled with nifty new features and nodes. You will find some of them very useful in your day-to-day Gaffer use.

However, we have replaced some of the core nodes, leading to several breaking changes. We've summarized the relevant differences for you below (for the dry details, you can view the full changelogs [here](https://github.com/GafferHQ/gaffer/releases/tag/0.53.0.0) and [here](https://github.com/GafferHQ/gaffer/releases/tag/0.53.1.0)).

<!-- Interface Updates -->

### Interface updates ###
We've made a fair number of interface improvements based on user feedback:

- <span class="changelog changelog-new">New</span> [Numeric bookmarks]({% post_url 2019-02-10-tip-numeric-bookmarks %}): ![Numeric bookmark on a node]({{ images }}/gaffer-53-numeric-bookmark.png)
    - Navigate to nodes and pin them to editors using the number keys!
- <span class="changelog changelog-new">New</span> [Edit Source and Edit Tweaks]({% post_url 2019-02-11-tip-edit-source-edit-tweaks %}): ![Edit Source and Edit Tweaks menu actions]({{ images }}/gaffer-53-edit-source-edit-tweaks.png)
- <span class="changelog changelog-new">New</span>  [Edit color connection components]({% post_url 2019-02-12-tip-shader-connection-components %}) in shader networks: ![Node with a split colour connection]({{ images }}/gaffer-53-color-components.png)
- <span class="changelog changelog-new">New</span> [Connect to Next]({% post_url 2019-02-13-tip-connect-to-next %}) on Loop nodes: ![Connect to Next menu action]({{ images }}/gaffer-53-connect-to-next.png)
- <span class="changelog changelog-updated">Updated</span> Bookmarks menu shortcut is now <kbd>B</kbd> (was <kbd>Ctrl</kbd> + <kbd>B</kbd>).

<!-- Node Updates -->

### Node updates ###
Many nodes have had breaking changes or have been replaced. You can open existing scripts that have the old versions of the nodes, but they will be update on load. **If you save a script with any of these new nodes in Gaffer 53, they will only work with Gaffer 53** &ndash; there's no going back.

- <span class="changelog changelog-new">New</span> ![ShaderTweaks node]({{ images }}/gaffer-53-shadertweaks-node.png)
    - A node for tweaking shaders and lights.
    - This node is still in development. Feel free to give us your feedback on its interface!
    - [Demo]({{ site.demos }}/gaffer-53-shadertweaks-node-public.gfr)
- <span class="changelog changelog-new">New</span> ![Loop node]({{ images }}/gaffer-53-loop-node.png)
    - Replaces: SceneLoop and ImageLoop nodes.
    - [Demo]({{ site.demos }}/gaffer-53-loop-node-public.gfr)
- <span class="changelog changelog-new">New</span> ![TimeWarp node]({{ images }}/gaffer-53-timewarp-node.png)
    - Replaces: SceneTimeWarp and ImageTimeWarp nodes.
    - [Demo]({{ site.demos }}/gaffer-53-timewarp-node-public.gfr)
- <span class="changelog changelog-new">New</span> ![ContextVariables node]({{ images }}/gaffer-53-contextvariables-node.png)
    - Replaces: SceneContextVariables, ImageContextVariables, DeleteSceneContextVariables, and DeleteImageContextVariables nodes.
    - [Demo]({{ site.demos }}/gaffer-53-contextvariables-node-public.gfr)
- <span class="changelog changelog-new">New</span> ![ArnoldTextureBake node]({{ images }}/gaffer-53-arnoldtexturebake-node.png)
    - For baking Arnold shaders on meshes into textures.
    - [Demo]({{ site.demos }}/gaffer-53-arnoldtexturebake-node-public.gfr)
- <span class="changelog changelog-updated">Updated</span> ![Box node]({{ images }}/gaffer-53-box-node.png)
    - [Boxes can now be disabled]({{ site.docs }}/0.53.4.0/WorkingWithTheNodeGraph/Box/index.html#setting-up-a-box-for-pass-through) (<kbd>D</kbd>) when their new `passThrough` plug is connected.

<!-- Breaking Changes -->

### Other breaking changes ###

- <span class="changelog changelog-updated">Updated</span> Updated shader caching. New shader caches will not be compatible with previous Gaffer versions. Old caches will update on read.
- <span class="changelog changelog-updated">Updated</span> Renamed the _Script Editor_ to the _Python Editor_ (UI) / `PythonEditor` (API). If you have custom layouts saved, they will be preserved.
- <span class="changelog changelog-removed">Removed</span> The `parent` variable is no longer available in the _Python Editor_. You can no longer paste serialized graphs (the contents of .gfr files) into the _Python Editor_. Instead, you must paste them into the _Graph Editor_. The parent variable is still available in Expression nodes.
- <span class="changelog changelog-updated">Updated</span> In the _Python Editor_, the `script` variable is now the `root` variable.
