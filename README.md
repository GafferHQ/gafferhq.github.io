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

## Updates ##

The `update.py` script can be used to automatically update the site config to refer to the latest Gaffer release and the latest year for copyright. This is run daily as a GitHub action that produces pull requests, so generally shouldn't need to be run manually.

## Validation Process ##

We validate the site builds with a [GitHub Actions workflow](https://github.com/GafferHQ/gafferhq.github.io/blob/main/.github/workflows/check.yml). The primary motivation for this is to automatically check for dead URLs with the [html-proofer](https://github.com/gjtorikian/html-proofer) tool. These test builds have the added benefit of performing rudimentary [HTML validation](https://github.com/sparklemotion/nokogiri), but this has proved inaccurate for some of the HTML5 specs.
