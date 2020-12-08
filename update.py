#!/usr/bin/env python

import github
import yaml

import argparse
import datetime
import distutils.util
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
	"--github-access-token",
	dest = "githubAccessToken",
	default = os.environ.get( 'GITHUB_ACCESS_TOKEN', None ),
	help = "A suitable access token to authenticate the GitHub API."
)
parser.add_argument(
	"--set-outputs",
	dest = "setOutputs",
	type = distutils.util.strtobool,
	default = "0",
	help = "Echo the outputs needed by `.github/workflows/update.yml`."
)
args = parser.parse_args()

def __versionFromString( s ) :

	# We use a list of ints for the version, as it
	# can be compared usefully.
	try :
		return [ int( n ) for n in s.split( "." ) ]
	except :
		# We don't care about non-numeric releases
		# like betas etc.
		return [ 0, 0, 0, 0 ]

def __versionToString( v ) :

	return ".".join( str( s ) for s in v )

# Find the latest release

client = github.Github( args.githubAccessToken )
repo = client.get_repo( "GafferHQ/gaffer" )

latestRelease = None
latestReleaseVersion = __versionFromString( "0.0.0.0" )

for release in repo.get_releases() :

	if release.prerelease :
		continue

	releaseVersion = __versionFromString( release.tag_name )
	if releaseVersion > latestReleaseVersion :
		latestRelease = release
		latestReleaseVersion = releaseVersion

# Update the config with the latest release and year

with open( "_config.yml" ) as configFile :
	config = yaml.safe_load( configFile )

newConfig = config.copy()
newConfig.update(
	latestGafferVersion = __versionToString( latestReleaseVersion ),
	copyrightYear = datetime.datetime.now().year
)

if newConfig == config :
	sys.stderr.write( "Up to date\n" )
	sys.exit( 0 )

with open( "_config.yml", "w" ) as configFile :
	yaml.dump( newConfig, configFile, sort_keys = True )

# Create output variables for use in the rest of the workflow

if args.setOutputs :

	changes = []
	if newConfig["latestGafferVersion"] != config["latestGafferVersion"] :
		changes.append( "Gaffer to {}".format( newConfig["latestGafferVersion"] ) )
	if newConfig["copyrightYear"] != config["copyrightYear"] :
		changes.append( "Copyright to {}".format( newConfig["copyrightYear"] ) )

	title = "Update {}".format( " and ".join( changes ) )
	print( "::set-output name=title::{}".format( title ) )