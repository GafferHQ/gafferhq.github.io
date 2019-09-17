---
layout: default
title: Download
---

# Pre-built packages #

**Gaffer {{ site.latest-release }}** (stable) compiled, containing Appleseed {{ site.appleseed-version }}. Compatible with Arnold {{ site.arnold-version }}, 3Delight {{ site.delight-version }}, and Tractor {{ site.tractor-version}}.

<div class="container">
    <div class="row">
        <div class="col-md-4 px-0 mr-md-2 mb-2" id="linux">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Linux</h5>
                    <a class="btn btn-primary d-block mb-2" href="https://github.com/gafferhq/gaffer/releases/download/{{ site.latest-release }}/gaffer-{{ site.latest-release }}-linux.tar.gz"><i class="fab fa-linux"></i> Download <small>(.tar.gz)</small></a>
                    <p>Requires CentOS 7.5 or newer</p>
                    <p class="small mb-0">Other Linux distributions may work, but Gaffer has not been rigorously tested on them.</p>
                </div>
            </div>
        </div>
        <div class="col-md-4 px-0 mb-2" id="macos">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">macOS</h5>
                    <a class="btn btn-primary d-block mb-2" href="https://github.com/gafferhq/gaffer/releases/download/{{ site.latest-release }}/gaffer-{{ site.latest-release }}-osx.tar.gz"><i class="fab fa-apple"></i> Download <small>(.tar.gz)</small></a>
                    <p class="mb-0">Requires Mavericks 10.9 or newer</p>
                </div>
            </div>
        </div>
    </div>
</div>

[Install instructions](https://www.gafferhq.org/documentation/{{ site.latest-release }}/GettingStarted/InstallingGaffer)

[Changelog](https://github.com/GafferHQ/gaffer/releases/tag/{{ site.latest-release }})

[Older releases](https://github.com/gafferhq/gaffer/releases)

# Source #

**Gaffer {{ site.latest-release }}** (stable) source.

<a href="https://github.com/gafferhq/gaffer/archive/{{ site.latest-release }}.zip"><i class="fa fa-download"></i> Download <small>(.zip)</small></a>

[Build instructions](https://github.com/GafferHQ/gaffer/blob/master/README.md#building)

For the most recent changes, you can grab and build the [latest source](https://github.com/GafferHQ/gaffer/releases/latest), but please note that the latest changes are not always production-ready.

#### Build Requirements ####

Package Name | Minimum Version
|-
**General** | -
[gcc](https://gcc.gnu.org/index.html) | 6.3.1
[scons](https://www.scons.org) |
**OpenGL** | -
[libX11-devel](https://www.x.org) |
[libXi-devel](https://www.x.org) |
[libXmu-devel](https://www.x.org) |
[mesa-libGL-devel](https://www.mesa3d.org) |
[mesa-libGLU-devel](https://www.mesa3d.org) |
