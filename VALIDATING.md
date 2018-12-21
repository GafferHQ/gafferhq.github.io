# Validating Site Builds #

We validate the site builds with Travis CI. The primary motivation for this is to automatically check for dead URLs between the internal pages and to external sites with the [html-proofer](https://github.com/gjtorikian/html-proofer) tool. These test builds have the added benefit of performing rudimentary [HTML validation](https://github.com/sparklemotion/nokogiri), but this has proved inaccurate for some of the HTML5 specs.

For compatibility with local builds at Image Engine, we are currently running a [Travis config](https://github.com/GafferHQ/gafferhq.github.io/blob/master/.travis.yml) with an older Ruby version:
```yml
rvm:
  - 2.3.7
```

If there are major problems validating the site build with Travis, it's best to debug locally. This requires reconstructing an Ubuntu-like environment with `sudo` access and Ruby locked to this same version. Consider doing this only as a last resort, and an indicator that something has gone very wrong.

## Testing Locally with Docker ##
For the time being, consider replicating Travis with Docker unfeasible.

As of 2018-12-11, the Travis group has [migrated away](https://blog.travis-ci.com/2018-11-19-required-linux-infrastructure-migration) from container Linux test builds, in favour of VM builds. The [latest container image](https://hub.docker.com/r/travisci/ci-garnet/tags) for Ruby builds was updated in 2017. From looking at recent Travis build logs, the container instances are no longer taken from this hub. On 2018-12-16, the Travis devs removed the documentation on the Travis site for local builds, and have so far not replaced it with a description as to how a user could use the new setup.

## Testing Locally by Hand ##
The alternative to Docker is to test on a local machine (or VM), and try to replicate the Travis build as best as possible.

To do this, we will replicate an Ubuntu distro with a particular Ruby version and gem bundle. Since the site config is mostly Ruby-dependent, running on an 18.04 LTS distro doesn't cause any conflicts.

### Package requirements ###
During this installation process, you will install:
- `nodejs`
- `rbenv` (for recent security reasons, `rvm` is no longer safe to use)
- `ruby-build` (enables the `rbenv install` command)

### Installation ###
We cannot guarantee that the Ruby version for the test builds will stay static. So, for this installation, you will need to refer to a Travis build log – preferably the one that failed – in order to replicate its Ruby setup.
1. If you haven't already, clone the GafferHQ site repo:
    ```bash
    $ git clone https://github.com/gafferhq/gafferhq.github.io.git ~/dev/
    ```
2. [Remove all traces of rvm](https://richonrails.com/articles/uninstalling-rvm).
3. Install nodejs:
    ```bash
    $ sudo apt install nodejs
    ```
4. Clone rbenv:
    ```bash
    $ git clone https://github.com/rbenv/rbenv.git ~/.rbenv
    ```
5. Build rbenv:
    ```bash
    $ cd ~/.rbenv && src/configure && make -C src
    ```
6. Add rbenv's path and init to your shell startup script:
    ```bash
    $ echo 'PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
    $ echo 'eval "$(rbenv init -)"' >> ~/.bashrc
    $ reset
    ```
    **Note:** You may need to comment out `export GEM_HOME=` from your startup script.
7. Install ruby-build:
    ```bash
    mkdir -p "$(rbenv root)"/plugins
    git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build
    ```
8. Install the static version of Ruby set by the `.travis.yml` config.
    1. Ruby < 2.4.0 requires `libssl`, which newer distros likely won't have:
        1. Check which older versions are available:
        ```bash
        $ sudo apt-cache policy libssl-dev
        Version table:
        ...
        ```
        2. Choose an old version from the list, and install it:
        ```bash
        $ sudo apt install libssl-dev=1.0.2g-1ubuntu4.14
        ```
    2. Install the same Ruby version as seen in the Travis build log (look for the `rvm use` line). Use `--disable-install-doc` to speed up the process significantly:
        ```bash
        $ RUBY_CONFIGURE_OPTS=--disable-install-doc rbenv install 2.3.7
        $ rbenv rehash
        ```
        Check that the version installed successfully:
        ```bash
        $ rbenv versions
        * system
        2.3.7
        ```
9. Set the Ruby version for the site repo directory. This creates a `.ruby_version` file in the repo root. It can be overridden/removed later. 
    ```bash
    $ cd ~/dev/gafferhq.github.io
    $ rbenv local 2.3.7
    $ rbenv local
    2.3.7
    ```
    Check that the rbenv `$PATH` overrides are working and that the gems will install to the right place:
    ```bash
    $ ruby --version
    ruby 2.3.7p456 (2018-03-28 revision 63024) [x86_64-linux]
    $ which ruby
    /home/michaeldu/.rbenv/shims/ruby
    $ rbenv which gem
    /home/michaeldu/.rbenv/versions/2.3.7/bin/gem
    $ gem env home
    /home/michaeldu/.rbenv/versions/2.3.7/lib/ruby/gems/2.3.7
    ```
10. Install the version of `bundler` that the Travis Build used (look for the `Using bundler` line):
    ```bash
    $ gem install bundler -v 1.17.2
    $ gem which bundler
    /home/michaeldu/.rbenv/versions/2.3.7/lib/ruby/gems/2.3.0/gems/bundler-1.17.2/lib/bundler.rb
    $ whereis bundle
    bundler: /home/michaeldu/.rbenv/shims/bundle /home/michaeldu/gems/bin/bundle
    ```
11. Build the gem bundle:
    ```bash
    $ bundle install
    ```
    If all goes well, you should have no errors, and the installed gem versions should match the Travis build log exactly:
    ```bash
    $ gem list
    ...
    jekyll (3.6.2)
    github-pages (177)
    ...
    ```
You should now be ready to build and test the site as if you were using the Travis build environment.

### Testing ###
The site is built and validated with:
```bash
$ bundle exec jekyll build && bundle exec htmlproofer ./_site --only-4xx --check-html --empty-alt-ignore --url-ignore "/vimeo.com/"
```

### Switching between Ruby versions ###
If you've built another version of Ruby (say, `2.5.2`), and want to run a comparison build, make sure to remove the `Gemfile.lock` from the local site repo and rebuild the bundle:
```bash
$ rm Gemfile.lock
$ rbenv local 2.5.2
$ bundle install
```
