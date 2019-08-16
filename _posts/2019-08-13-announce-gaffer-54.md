---
layout: post
title: "Release: Gaffer 0.54"
subtitle: "Releases"
icon: /resources/images/2019-08-13-announce-gaffer-54/gaffer-54-splash.png
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

<img class="mb-30 show" style="margin: auto" src="{{ images }}/gaffer-54-splash.png" alt="Gaffer 0.54 release splash">

Another summer update, and another major release!

This latest update brings a medley of interface features, changes, and improvements to make the main Gaffer application that much friendlier to use. The most prominent changes are to the interface itself, which has received a visual overhaul, the addition of drag-and-dock tabs and multi-window layouts, different editor following states, and the new UV Inspector. A flexible window and tab system has been one of the most requested interface enhancements for a few years now, and we're very proud to have finally brought it to fruition.

On the node side of things, we've made notable improvements to the way you interact with OSLObject and OSLImage nodes. We've also added a few new nodes into the mix, such as the Arnold LightBlocker node.

As with our last major release, there are some breaking changes with older scripts that you should check up on, as well as some new articles for your perusal and edification in the documentation.

The [full changelog](https://github.com/GafferHQ/gaffer/releases/tag/0.54.0.0) for this update is quite a whopper. To save you some time, we've provided a summary of the most important changes below.

Enjoy!


### Interface updates ###

- <span class="changelog changelog-new">New</span>  Editor linking and following:
    - Editors can be linked. For example, editor A (![Editor link]({{ images }}/editor-link.png)) can be linked to editor B (![Editor linked]({{ images }}/editor-linked.png)) to match whichever node that editor B is viewing.
    - Editors can follow the scene selection (![Editor following scene]({{ images }}/editor-follow-scene.png)), viewing the node that generates the selected object.
    - [Demo <i class="fa fa-external-link"></i>](https://vimeo.com/354089521)
- <span class="changelog changelog-new">New</span>  _UV Inspector:_ ![UV Inspector]({{ images }}/uv-inspector-editor.png)
    - Displays the scene's unwrapped meshes and textures in UV space.
    - [Demo <i class="fa fa-external-link"></i>](https://vimeo.com/354089547)
- <span class="changelog changelog-updated">Updated</span>  Node menu search: ![Node menu]({{ images }}/node-menu-search.png)
    - Now uses improved fuzzy matching, giving you far better results.
        - Much improved detection of partial words: `lvlm` → `LevelSetToMesh`
        - Terms can be out-of-order: `osl mat`, `mat osl` → `oslMatrixTransform`
        - The order of search results is more intelligent, prioritising whole-word matches over partials.
    - Searches with no results appear red.
- <span class="changelog changelog-updated">Updated</span>  Window layouts: ![Window layouts]({{ images }}/window-layouts.png)
    - Each open graph now supports multiple editors in multiple windows.
    - You can now rearrange tabs, drag tabs between panels, drag tabs between windows, and detach panels and tabs into their own separate windows.
    - Saving a layout will now preserve the position, size, and full-screen state of all windows.
    - [Demo <i class="fa fa-external-link"></i>](https://vimeo.com/354089529)
- <span class="changelog changelog-updated">Updated</span>  _UI Editor_: 
    - You can now assign custom icons to a node: ![Node with icon]({{ images }}/node-with-icon.png)


### Node updates ###

- <span class="changelog changelog-new">New</span>  ![Arnold blocker node]({{ images }}/lightblocker-node.png)
    - An implementation of Arnold's scene-space light blocker.
    - [Example <i class="fa fa-download"></i>]({{ site.demos }}/example-lightblocker-node.gfr)
- <span class="changelog changelog-new">New</span>  ![Orientation node]({{ images }}/orientation-node.png)
    - Converts primvar orientation representations, and optionally randomizes their rotations.
    - Supports Euler angle, matrix, aim vector, quaternion, and axis-angle representations.
    - [Example <i class="fa fa-download"></i>]({{ site.demos }}/example-orientation-node.gfr)
- <span class="changelog changelog-new">New</span>  ![SetVisualiser node]({{ images }}/setvisualiser-node.png)
    - Shades objects in the _Viewer_ with colors based on their set memberships.
    - Supports both random and chosen colors.
    - [Demo <i class="fa fa-external-link"></i>](https://vimeo.com/354088506)
- <span class="changelog changelog-updated">Updated</span> ![OSLObject node]({{ images }}/oslobject-node.png)
    - Added a new interface for writing primvars. This replaces all of the OSL Out[Primvar] nodes. You no longer need to terminate OSL shader networks with an Out[Primvar] + OutObject node combination.
    - Added a _Use Attributes_ plug, which allows OSL shaders to query the scene's attributes.
    - [Example <i class="fa fa-download"></i>]({{ site.demos }}/example-oslobject-node.gfr)
- <span class="changelog changelog-updated">Updated</span>  ![OSLImage node]({{ images }}/oslimage-node.png)
    - The node's interface now supports image channel management. This replaces the OutImage, OutLayer, and OutChannel nodes.
    - Added the _Default Format_ plug. This allows OSLImage to be used to generate images/patterns without an input image.
    - [Example <i class="fa fa-download"></i>]({{ site.demos }}/example-oslimage-node.gfr)
- <span class="changelog changelog-updated">Updated</span>  ![Parent, Instancer, and Seeds nodes]({{ images }}/parent-instancer-seeds-nodes.png)
    - Added a filter input so that these nodes can operate on multiple locations in the input scene at once. For example, one Instancer node could instance an asset (`/assets/flower`) onto multiple point clouds (`/assets/bed1/points`, `/assets/bed2/points`) from a single scene input, whereas before you would need multiple Instancer nodes to accomplish this.
    - [Example <i class="fa fa-download"></i>]({{ site.demos }}/example-parent-instancer-seeds-node-filter.gfr)
- <span class="changelog changelog-removed">Deprecated</span>
    - OutColor
    - OutChannel
    - OutFloat
    - OutImage
    - OutInt
    - OutLayer
    - OutMatrix
    - OutNormal
    - OutObject
    - OutPoint
    - OutString
    - OutUV
    - OutVector


### Documentation updates ###

- <span class="changelog changelog-new">New</span>  [Light Linking]({{ site.docs }}/0.54.0.0/WorkingWithScenes/LightLinking/index.html)
- <span class="changelog changelog-new">New</span>  [Tutorial: Startup Configs]({{ site.docs }}/0.54.0.0/WorkingWithThePythonScriptingAPI/TutorialStartupConfig1/index.html)


### Breaking changes ###

- OSL networks saved in Gaffer 0.54 will not open in earlier versions. If you have critical production graphs built in 0.53 or earlier, do not open and save them with 0.54. **If you save a script with OSLObject/OSLImage nodes in Gaffer 0.54, they will only work with Gaffer 0.54** &ndash; there's no going back.
- OSL networks saved before Gaffer 0.45.0.0 are no longer compatible.
- For OSL networks saved before Gaffer 0.54.0.0 that query object transforms, the OSLObject's new `useTransform` plug must be checked.
- Removed support for the `scene:path` context variable in all shader and OSL networks. To enable temporary backwards compatibility for rendering, use the following environment variables: 
    - ShaderAssignment node: Set `GAFFERSCENE_SHADERASSIGNMENT_CONTEXTCOMPATIBILITY` to `1`.
    - OSLObject node: Set the `GAFFEROSL_OSLOBJECT_CONTEXTCOMPATIBILITY` to `1`.

