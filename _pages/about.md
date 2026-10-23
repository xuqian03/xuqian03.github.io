---
permalink: /
title: "Welcome!"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div id="home"></div>

I am Qian Xu, currently a Master's student in Information and Communication Engineering at the [College of Electronics and Information Engineering](https://ceie.szu.edu.cn/), [Shenzhen University (SZU)](https://en.szu.edu.cn/), advised by [Prof. Shishun Tian](https://shishuntian.github.io/). I received my B.Eng. degree in Computer Science and Technology from [Dalian Polytechnic University](https://www.dlpu.edu.cn/).

My research focuses on light-field computer vision, with an emphasis on referring image segmentation, epipolar geometry, and multimodal reasoning with large language models. I am interested in building structure-aware frameworks that fuse natural language instructions with high-dimensional light-field cues for robust perception in complex, occluded scenes.

I welcome research discussions and collaborations related to light-field imaging, referring segmentation, and multimodal scene understanding.


## News
{: #news }
{% if site.data.news %}
<div class="news-scroller" role="region" aria-label="News">
  <ul>
    {% for item in site.data.news %}
      <li>{{ item.text }}</li>
    {% endfor %}
  </ul>
  <div class="news-hint" aria-hidden="true">scroll for more &darr;</div>
</div>
{% endif %}


## Publications {% if site.author.orcid %}[[ORCID]({{ site.author.orcid }})]{% endif %}
{: #publications }
{% assign pubs = site.data.publications %}
{% if pubs %}
<div class="pub-gallery">
  {% for pub in pubs %}
  {% assign has_image = pub.image | default: '' | strip %}
  {% if has_image != '' %}
  <article class="pub-card">
    <a class="pub-card__media" href="{{ pub.paper | default: pub.code | default: pub.project }}" target="_blank" rel="noopener">
      <img src="{{ pub.image | relative_url }}" alt="{{ pub.title }}">
    </a>
    <div class="pub-card__body">
      <div class="pub-list__title">
        {% if pub.paper %}
        <a href="{{ pub.paper }}" target="_blank" rel="noopener">{{ pub.title }}</a>
        {% else %}
        {{ pub.title }}
        {% endif %}
      </div>
      <div>{{ pub.authors }}</div>
      <div><em>{{ pub.venue }}</em></div>
      {% if pub.note %}<div>{{ pub.note }}</div>{% endif %}
      {% if pub.paper or pub.code or pub.project %}
        <div>
          {% if pub.paper %}[<a href="{{ pub.paper }}" target="_blank" rel="noopener">Paper</a>]{% endif %}
          {% if pub.code %}[<a href="{{ pub.code }}" target="_blank" rel="noopener">Code</a>]{% endif %}
          {% if pub.project %}[<a href="{{ pub.project }}" target="_blank" rel="noopener">Project</a>]{% endif %}
        </div>
      {% endif %}
    </div>
  </article>
  {% endif %}
  {% endfor %}
</div>
{% endif %}

{% assign has_text_only = false %}
{% assign has_gallery = false %}
{% for pub in pubs %}
  {% assign has_image = pub.image | default: '' | strip %}
  {% if has_image != '' %}
    {% assign has_gallery = true %}
  {% else %}
    {% assign has_text_only = true %}
  {% endif %}
{% endfor %}

{% if has_text_only %}
{% if has_gallery %}
### Additional Publications
{% endif %}
<ul>
  {% for pub in pubs %}
    {% assign has_image = pub.image | default: '' | strip %}
    {% if has_image == '' %}
    <li>
      <div>
        {% if pub.paper %}
        <a href="{{ pub.paper }}" target="_blank" rel="noopener">{{ pub.title }}</a>
        {% else %}
        {{ pub.title }}
        {% endif %}
      </div>
      <div>{{ pub.authors }}</div>
      <div><em>{{ pub.venue }}</em></div>
      {% if pub.note %}<div>{{ pub.note }}</div>{% endif %}
      {% if pub.paper or pub.code or pub.project %}
        <div>
          {% if pub.paper %}[<a href="{{ pub.paper }}" target="_blank" rel="noopener">Paper</a>]{% endif %}
          {% if pub.code %}[<a href="{{ pub.code }}" target="_blank" rel="noopener">Code</a>]{% endif %}
          {% if pub.project %}[<a href="{{ pub.project }}" target="_blank" rel="noopener">Project</a>]{% endif %}
        </div>
      {% endif %}
    </li>
    {% endif %}
  {% endfor %}
</ul>
{% endif %}

## Education
{: #education }

* **Shenzhen University, Sep. 2024 – Jun. 2027**
* **Dalian Polytechnic University, Sep. 2020 – Jun. 2024**



## Honors & Awards
{: #honors-awards }

* University Special Scholarship, Shenzhen University
* University First-Class Scholarship, Shenzhen University
* University First-Class Scholarship, Dalian Polytechnic University
