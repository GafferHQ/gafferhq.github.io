---
layout: base
---

<!-- Carousel -->
<section class="container mt-3 mb-3 px-0" id="carousel">
    <div class="carousel slide" data-ride="carousel" data-interval="10000" id="carousel-object">
        <ol class="carousel-indicators d-none d-md-flex">
            <li data-target="#carousel-object" data-slide-to="0" class="active"></li>
            <li data-target="#carousel-object" data-slide-to="1"></li>
            <li data-target="#carousel-object" data-slide-to="2"></li>
            <li data-target="#carousel-object" data-slide-to="3"></li>
            <li data-target="#carousel-object" data-slide-to="4"></li>
            <li data-target="#carousel-object" data-slide-to="5"></li>
        </ol>
        <div class="carousel-inner">
            {% include image-carousel.html img='https://image-engine.com/wp-content/uploads/2018/08/JFK_BO_JFK-BO-2740_ImageEngine_JurassicWorld_cineFX_v0001.001001.jpg' caption='LookDev and Lighting on Jurassic Park: Fallen Kingdom' active=true %}
            {% include image-carousel.html img='https://image-engine.com/wp-content/uploads/2017/06/featuredimage.jpg' caption='LookDev and Lighting on Lost in Space, season 1' %}
            {% include image-carousel.html img='https://image-engine.com/wp-content/uploads/2017/07/build_logan_lookDev_v236_0173.jpg' caption='LookDev on Logan' %}
            {% include image-carousel.html img='https://image-engine.com/wp-content/uploads/2018/01/704-0420-3500_ALT.1150.jpg' caption='Lighting and volumes on Game of Thrones, season 7' %}
            {% include image-carousel.html img='https://image-engine.com/wp-content/uploads/2018/08/JFK_NN_JFK-NN-0065_ImageEngine_JurassicWorld_cineFX_v0002.001001.jpg' caption='LookDev and Layout on Jurassic Park: Fallen Kingdom' %}
            {% include image-carousel.html img='https://image-engine.com/wp-content/uploads/2018/04/101_040_600_AO.1006.jpg' caption='Procedural layout in Lost in Space, season 1' %}
        </div>
        <a class="carousel-control-prev" href="#carousel-object" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carousel-object" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
</section>

<!-- Introduction -->
<section class="container mb-5" id="introduction">
    <div class="row justify-content-center mb-3">
        <div class="col col-md-9">
            <h1 class="text-center mb-3">Introducing <span class="text-primary">Gaffer</span></h1>
            <p><strong>Gaffer</strong> is a free, open-source, node-based VFX application that enables look developers, lighters, and compositors to easily build, tweak, iterate, and render scenes. Built with flexibility in mind, Gaffer supports in-application scripting in Python and OSL, so artists and technical directors can author shaders, automate processes, and design production workflows.</p>
            <p>With hooks in both C++ and Python, Gaffer's readily extensible API provides both professional studios and enthusiasts with the tools to add their own custom modules, nodes, and UI.</p>
            <p>The workhorse of the production pipeline at <a href="https://image-engine.com">Image Engine Design Inc.</a>, Gaffer has been used to build award-winning VFX for shows such as Jurassic World: Fallen Kingdom, Lost in Space, Logan, and Game of Thrones.</p>
        </div>
    </div>
    <div class="row">
        <div class="col text-center">
            <a class="btn btn-primary" href="/download/" role="button"><i class="fa fa-download"></i> Get Gaffer {{ site.latest-release }}</a>
            <a class="btn btn-primary ml-2" href="https://github.com/gafferHQ/gaffer"><i class="fab fa-github"></i> Follow Gaffer's Development</a>
        </div>
    </div>
</section>

<!-- Tour -->
<section class="container mb-3" id="tour">
    <div class="row mb-3">
        <div class="col-12 col-lg-6 mb-2 d-flex align-items-center">
            {% include image-lightbox.html img='/content/images/tour/gaffy-render.jpg' width='initial' height='initial' title='Build scenes' alt='Gaffy the robot, shaded in a scene containing procedural ref balls, Macbeth chart, and turntable rig.' %}
        </div>
        <div class="col-12 col-lg-6 p-lg-4">
            <h1 class="text-center">Build scenes</h1>
            <p>Import, build, and manipulate scenes non-destructively. Duplicate, combine, join, prune, split, and inspect scenes of arbitrary complexity using the robust node graph and scene hierarchy interfaces.</p>
        </div>
    </div>
    <div class="row mb-3">
        <div class="col-12 col-lg-6 mb-2 order-lg-last d-flex align-items-center">
            {% include image-lightbox.html img='/content/images/tour/shader-graph.jpg' width='initial' height='initial' title='Author shaders' alt='An OSL shader graph.' %}
        </div>
        <div class="col-12 col-lg-6 p-lg-4">
            <h1 class="text-center">Author shaders</h1>
            <p>With full support for <a href="https://www.solidangle.com/arnold">Arnold</a> and <a href="https://www.3delight.com">3Delight's</a> powerful industry-standard shaders, use the robust node plug-outs to quickly build compelling looks. For extra customization, arrange and write custom shaders using <a href="http://opensource.imageworks.com/?p=osl">Open Shading Language</a> nodes and code.</p>
        </div>
    </div>
    <div class="row mb-3">
        <div class="col-12 col-lg-6 mb-2 d-flex align-items-center">
            {% include image-lightbox.html img='/content/images/tour/workflow-graph.jpg' width='initial' height='initial' title='Design workflows' alt='A small component of a larger graph.' %}
        </div>
        <div class="col-12 col-lg-6 p-lg-4">
            <h1 class="text-center">Design workflows</h1>
            <p>Whether for 3D sequences, 2D image processing, or pipeline processes, design workflows all within a single tool. Use logic, filters, and expressions to make scalable node networks for automated and responsive VFX solutions.</p>
        </div>
    </div>
</section>

<!-- Video -->
<section class="container-fluid mb-3 py-4 bg-dark" id="video">
    <div class="row justify-content-center">
        <div class="col-sm-8 col-xs-12">
            <p class="h1 text-center text-white"><i class="fa fa-film"></i></p>
            <h1 class="text-center text-white mb-3">Gaffer in the studio</h1>
            {% include vimeo.html media='https://player.vimeo.com/video/201047816' %}
        </div>
    </div>
</section>

<!-- Features -->
<section class="container mb-3" id="features">
    <div class="row justify-content-center mb-2">
        <h1 class="text-center">Features</h1>
    </div>
    <div class="row">
        <div class="col-md-4 mb-4 px-3 px-md-1 px-lg-3">
            <p class="display-4 text-center"><i class="fas fa-smile"></i></p>
            <h2 class="h4 text-center">Free</h2>
            <p>Released under the BSD License. Free to use – at home or in a studio – and modify – be it a simple configuration tweak, or a complete application.</p>
        </div>
        <div class="col-md-4 mb-4 px-3 px-md-1 px-lg-3">
            <p class="display-4 text-center"><i class="fas fa-tachometer-alt"></i></p>
            <h2 class="h4 text-center">Powerful</h2>
            <p>Gaffer's multi-threaded, deferred evaluation engine enables work with large 3D and 2D data sets without slow-down.</p>
        </div>
        <div class="col-md-4 mb-4 px-3 px-md-1 px-lg-3">
            <p class="display-4 text-center"><i class="fa fa-cogs"></i></p>
            <h2 class="h4 text-center">Flexible</h2>
            <p>A renderer abstraction layer enables common workflows between several renderers. Supports <a href="https://www.solidangle.com/arnold">Arnold</a>, <a href="https://appleseedhq.net">Appleseed</a>, <a href="https://www.3delight.com">3Delight</a>, and <a href="https://renderman.pixar.com/products/tools/tractor.html">Tractor</a>.</p>
        </div>
    </div>
    <div class="row">
        <div class="col-md-4 mb-4 px-3 px-md-1 px-lg-3">
            <p class="display-4 text-center"><i class="fa fa-code"></i></p>
            <h2 class="h4 text-center">Extensible</h2>
            <p>Add UI, nodes, and modules. Integrate with new renderers and your render farm. Implement new datatypes to flow through the node graph.</p>
        </div>
        <div class="col-md-4 mb-4 px-3 px-md-1 px-lg-3">
            <p class="display-4 text-center"><i class="fa fa-users"></i></p>
            <h2 class="h4 text-center">Open Source</h2>
            <p>Built on a wealth of tested open-source VFX libraries, including <a href="https://www.openexr.com">OpenEXR</a>, <a href="https://sites.google.com/site/openimageio/home">OpenImageIO</a>, <a href="https://opencolorio.org">OpenColorIO</a>, <a href="http://opensource.imageworks.com/?p=osl">Open Shading Language</a>, and <a href="https://github.com/ImageEngine/cortex">Cortex</a>.</p>
        </div>
        <div class="col-md-4 mb-4 px-3 px-md-1 px-lg-3">
            <p class="display-4 text-center"><i class="fa fa-road"></i></p>
            <h2 class="h4 text-center">Ongoing</h2>
            <p>With new features constantly added by industry experts, development is further enhanced by VFX artists from around the world on <a href="https://github.com/gafferHQ/gaffer">GitHub</a>.</p>
        </div>
    </div>
</section>

<!-- Duplicate the call to action -->
<section class="container" id="download">
    <div class="row">
        <div class="col text-center">
            <a class="btn btn-primary" href="/download/" role="button"><i class="fa fa-download"></i> Get Gaffer {{ site.latest-release }}</a>
            <a class="btn btn-primary ml-2" href="https://github.com/gafferHQ/gaffer"><i class="fab fa-github"></i> Follow Gaffer's Development</a>
        </div>
    </div>
</section>
