---
permalink: /
title: "Welcome!"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---



I am Qian Xu, currently a Master's student in Information and Communication Engineering at the [College of Electronics and Information Engineering](https://ceie.szu.edu.cn/), [Shenzhen University (SZU)](https://en.szu.edu.cn/), advised by [Prof. Shishun Tian](https://shishuntian.github.io/).

My research focuses on light-field computer vision, with an emphasis on referring image segmentation, epipolar geometry, and multimodal reasoning with large language models. I am interested in building structure-aware frameworks that fuse natural language instructions with high-dimensional light-field cues for robust perception in complex, occluded scenes.

I am currently seeking a position as a doctor.

## 📢 News

{: #news }
{% if site.data.news %}

- {% for item in site.data.news %}
- {{ item.text }}
- {% endfor %}

scroll for more ↓

 {% endif %}

## Publications

{: #publications }
{% assign pubs = site.data.publications %}
{% if pubs %}

{% for pub in pubs %} {% assign has_image = pub.image | default: '' | strip %} {% if has_image != '' %}

![{{ pub.title }}]({{ pub.image | relative_url }})

 {% if pub.paper %} [{{ pub.title }}]({{ pub.paper }}) {% else %} {{ pub.title }} {% endif %}

{{ pub.authors }}

*{{ pub.venue }}*

 {% if pub.note %}

{{ pub.note }}

{% endif %} {% if pub.paper or pub.code or pub.project %}

 {% if pub.paper %}[[Paper]({{ pub.paper }})]{% endif %} {% if pub.code %}[[Code]({{ pub.code }})]{% endif %} {% if pub.project %}[[Project]({{ pub.project }})]{% endif %}

 {% endif %}

 {% endif %} {% endfor %}

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

- {% for pub in pubs %} {% assign has_image = pub.image | default: '' | strip %} {% if has_image == '' %}
- {% if pub.paper %} [{{ pub.title }}]({{ pub.paper }}) {% else %} {{ pub.title }} {% endif %}

  {{ pub.authors }}

  *{{ pub.venue }}*

   {% if pub.note %}

  {{ pub.note }}

  {% endif %} {% if pub.paper or pub.code or pub.project %}

   {% if pub.paper %}[[Paper]({{ pub.paper }})]{% endif %} {% if pub.code %}[[Code]({{ pub.code }})]{% endif %} {% if pub.project %}[[Project]({{ pub.project }})]{% endif %}

   {% endif %}
- {% endif %} {% endfor %}

 {% endif %}


## Honors & Awards

{: #honors-awards }

* University Special Scholarship, Shenzhen University
* University First-Class Scholarship, Shenzhen University
* University First-Class Scholarship, Dalian Polytechnic University
