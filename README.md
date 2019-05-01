# GafferHQ.org #

This repository contains the website for http://gafferhq.org. It is published to the web via [GitHub Pages](https://pages.github.com/). Any changes pushed to the upstream master branch go live immediately.

## Local Testing ##

When editing the site it is useful to preview your changes before making them live. The easiest way to do this is to run a local server using Docker. From the root of your git clone:

```bash
docker run -t --rm -v "$PWD":/usr/src/app -p "4000:4000" starefossen/github-pages
```

You can then view the site by navigating to http://0.0.0.0:4000 in your web browser. Changes made to the site will be automatically picked up by the server and visible upon a refresh in the browser.

If docker is unavailable to you, you can use ruby directly instead. `cd` to the root of your build, and run:

```bash
bundle exec jekyll serve
```

## Categories and Tags ##

When authoring posts, the `category` and `tags` [FrontMatter](https://jekyllrb.com/docs/posts/#categories-and-tags) can be used. Categories are used to differentiate between 'news' and 'tips'. Only ever use a singular `category` (not `categories`). Tags can be used to create sub-groups of content under any particular category. Posts will be linked to/from relevant archive pages.

### Build note ###

Because of the GitHub Page's [plugin whitelist](https://help.github.com/en/articles/configuring-jekyll-plugins), we sadly can't use something like [jekyll-archives](https://github.com/jekyll/jekyll-archives). As such, we have to roll our own. We also can't run any build steps on commit. So, if you author a new post and add a new `tag` or `category` that hasn't been used before, you need to run `buildPostArchives.py`. This will rebuild the stub pages in the `_post_categories` and `_post_tags` directories. 

*NOTE: Never edit the contents of these directories manually, they will be overwritten by the script when next run.*.

The contents of `_post_categories` and `_post_tags` _must_ be committed along with the post to prevent `404` errors when linking to the archive pages.

## Validation Process ##

We use Travis CI to automatically validate the site's pages and build on PRs and merges. For more details, and information on validating locally, see [Validating Site Builds](VALIDATING.md). 
