#!/usr/bin/env python

# A helper script to build Jekyll pages for the Gaffer blog Categories/Tags.
#
# As we're limited to the sub-set of Jekyll plugins supported by GitHub Pages
# we can't use the jekyll-archive plugin. So we have to roll our own.
#
# This requires us to manually create stubs in _post_categories and _post_tags
# to ensure an index pages exists.
#
# This script parses all posts and ensures that we have matching pages

import os
import re

def run() :

	tags = set()
	categories = set()

	for post in getPosts() :
		collectCategoryAndTags( post, categories, tags )

	regenerateFiles( "tag", tags, '_post_tags' )
	regenerateFiles( "category", categories, '_post_categories' )

##############################################################################

def getPosts() :

	postsDir = os.path.join( os.path.dirname( __file__ ), '_posts' )
	allFiles = os.listdir( postsDir )
	return [ os.path.join( postsDir, f ) for f in allFiles if f.endswith('.md') ]


def collectCategoryAndTags( filePath, outCategoriesSet, outTagSet ) :

	f = open( filePath, "r" )
	try :
		inFrontMatter = False
		for l in f.readlines():

			if l.startswith( "---" ) :
				if inFrontMatter :
					# We're past the front-matter block so
					# we don't need to read any more
					return
				else :
					inFrontMatter = True

			if not inFrontMatter :
				continue

			if l.startswith( 'category:' ) :
				c = l.replace( 'category:', '' ).strip()
				outCategoriesSet.add( c )

			elif l.startswith( 'categories:' ) :
				raise ValueError(
					"%s: Found '%s'. Posts should only use the singular 'category:'."
					% ( filePath, l )
				)

			elif l.startswith( 'tags:' ) :
				m = re.search( 'tags:\s*?\[\w*?([^\]]+)\w*?]', l )
				if m :
					tags = m.group(1).split(',')
					for t in tags :
						outTagSet.add( t.strip() )
	finally :
		f.close()


def generateStub( archiveType, key ):
	return \
"""---
title: Blog | %s
archive_%s: %s
---""" % ( key.title(), archiveType, key )


def regenerateFiles( archiveType, keys, dirName ) :

	outputDir = os.path.join( os.path.dirname( __file__ ), dirName )

	for f in os.listdir( outputDir ) :
		if f.endswith( ".md" ) :
			os.remove( os.path.join( outputDir, f ) )

	for k in keys :
		contents = generateStub( archiveType, k )
		f = open( os.path.join( outputDir, "%s.md" % k ), "w" )
		try :
			f.write( contents )
		finally :
			f.close()


if __name__ == "__main__" :
	run()

