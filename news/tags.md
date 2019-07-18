---
layout: base
title: Tags
---

{% capture tags %}
    {% for tag in site.tags %}
        {{ tag[0] }}
    {% endfor %}
{% endcapture %}
{% assign sorted-tags = tags | split:' ' | sort %}

<article class="container mt-3 mb-2" id="tags">
    <header>
        <p><a href="/news"><i class="fa fa-angle-double-left"></i> News</a></p>
        <h1 class="mb-3">{{ page.title }}</h1>
    </header>
    <div class="container">
        <div class="row">
            <section class="col-12 col-md-9 px-0 pr-md-3" id="sorted-tags">
                {% for tag in sorted-tags %}
                    <div class="mb-4">
                        <h2 class="mb-2 h5" id="{{ tag }}"><a class="text-normal" href="#{{ tag }}"><i class="fas fa-tags"></i> {{ tag }}</a></h2>
                        {% for post in site.tags[tag] %}
                        <div class="mb-3">
                            <p class="mb-0"><a href="{{ post.url }}">{{ post.title }}</a></p>
                            <p class="text-muted">{{ post.date | date: "%B %d, %Y" }}</p>
                        </div>
                        {% endfor %}
                    </div>
                {% endfor %}
            </section>
            {% include tags-sidebar.html %}
        </div>
    </div>
</article>
