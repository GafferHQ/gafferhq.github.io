Overview
--------

This repository contains the website for http://gafferhq.org. It is published to the web via [GitHub Pages](https://pages.github.com/); any changes pushed to the upstream master branch go live immediately.

Local Testing
-------------

When editing the site it is useful to preview your changes before making them live. The easiest way to do this is to run a local server using Docker. From the root of your git clone :

```
docker run -t --rm -v "$PWD":/usr/src/app -p "4000:4000" starefossen/github-pages
```

You can then view the site by navigating to http://0.0.0.0:4000 in your web browser. Changes made to the site will be automatically picked up by the server and visible upon a refresh in the browser.

If docker is unavailable to you, you can use ruby directly instead :

```
bundle exec jekyll serve
```
