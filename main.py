#!/usr/bin/env python3

import os

def update_custom_css():
    file_path = "assets/css/custom.css"
    
    content = '''/* Custom styles for MSBTEMadeEasy */

/* Featured posts styling */
.featured-posts {
    margin-bottom: 30px;
}

.featured-posts .card {
    border-left: 4px solid #17a2b8;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    height: 100%;
}

.featured-posts .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}

.featured-posts .card-img-top {
    max-height: 200px;
    object-fit: cover;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}

.featured-posts .card-title {
    font-size: 1.25rem;
    margin-bottom: 10px;
}

.featured-posts .card-text {
    font-size: 0.9rem;
    color: #6c757d;
}

.section-title {
    text-align: center;
    margin-bottom: 30px;
}

.section-title h2 {
    position: relative;
    display: inline-block;
    font-weight: 700;
    font-size: 1.4rem;
}

.section-title h2 span {
    background-color: #fff;
    padding: 0 15px;
    position: relative;
    z-index: 1;
}

.section-title h2:before {
    content: "";
    position: absolute;
    left: 0;
    top: 50%;
    width: 100%;
    height: 1px;
    background: #eee;
    z-index: 0;
}

/* Fix blog grid container images */
.blog-grid-container .card .img-thumb {
    height: 200px;
    object-fit: cover;
}

/* Iframe responsiveness */
iframe {
    max-width: 100%;
    border: 1px solid #eaeaea;
    border-radius: 5px;
    margin: 15px 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

/* Subject cards */
.subject-card {
    border: 1px solid #eaeaea;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 20px;
    background-color: #f9f9f9;
    transition: all 0.3s ease;
}

.subject-card:hover {
    background-color: #f0f0f0;
    transform: translateY(-3px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.subject-card h3 {
    color: #333;
    font-size: 1.2rem;
    margin-top: 0;
    margin-bottom: 10px;
}

.subject-card p {
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 0;
}

/* Program navigation */
.program-nav {
    background-color: #f8f9fa;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 30px;
}

.program-nav ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-wrap: wrap;
}

.program-nav li {
    margin-right: 15px;
    margin-bottom: 10px;
}

.program-nav a {
    display: inline-block;
    padding: 5px 15px;
    background-color: #e9ecef;
    border-radius: 20px;
    color: #495057;
    text-decoration: none;
    transition: all 0.2s ease;
}

.program-nav a:hover {
    background-color: #17a2b8;
    color: white;
}

/* Practical list styling */
.practical-list {
    counter-reset: practical-counter;
    list-style-type: none;
    padding-left: 0;
}

.practical-list li {
    position: relative;
    padding-left: 35px;
    margin-bottom: 15px;
}

.practical-list li:before {
    content: counter(practical-counter);
    counter-increment: practical-counter;
    position: absolute;
    left: 0;
    top: 0;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background-color: #17a2b8;
    color: white;
    text-align: center;
    line-height: 25px;
    font-size: 14px;
}

/* Heading enhancements */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}

h1 {
    font-size: 2rem;
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 10px;
}

h2 {
    font-size: 1.75rem;
    border-bottom: 1px solid #f0f0f0;
    padding-bottom: 5px;
}

h3 {
    font-size: 1.5rem;
}

/* Download button */
.download-btn {
    display: inline-block;
    padding: 8px 15px;
    background-color: #28a745;
    color: white;
    border-radius: 4px;
    text-decoration: none;
    margin: 10px 0;
    transition: all 0.3s ease;
}

.download-btn:hover {
    background-color: #218838;
    text-decoration: none;
    color: white;
}

.download-btn i {
    margin-right: 5px;
}

/* Responsive fixes */
@media (max-width: 768px) {
    .featured-posts .card-img-top {
        max-height: 180px;
    }
    
    .blog-grid-container .card .img-thumb {
        height: 180px;
    }
    
    iframe {
        height: 300px !important;
    }
}

@media (max-width: 576px) {
    .featured-posts .card-img-top {
        max-height: 160px;
    }
    
    .blog-grid-container .card .img-thumb {
        height: 160px;
    }
    
    iframe {
        height: 240px !important;
    }
}
'''
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated CSS file: {file_path}")

def update_index_html():
    file_path = "index.html"
    
    content = '''---
layout: default
title: Home
---

<!-- Featured Posts
================================================== -->
<section class="featured-posts">
    <div class="section-title">
        <h2><span>Featured Resources</span></h2>
    </div>
    <div class="row">
        {% for post in site.posts %}
            {% if post.featured == true %}
                <div class="col-md-6 mb-4">
                    <div class="card">
                        <a href="{{ site.baseurl }}{{ post.url }}">
                            <img class="card-img-top" src="{{ site.baseurl }}/{{ post.image }}" alt="{{ post.title }}">
                        </a>
                        <div class="card-body">
                            <h2 class="card-title"><a class="text-dark" href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
                            <p class="card-text">{{ post.excerpt | strip_html | truncatewords:20 }}</p>
                            <div class="metafooter">
                                <div class="wrapfooter small">
                                    <span class="post-date">{{ post.date | date_to_string }}</span>
                                    <span class="post-categories">
                                        {% for category in post.categories limit:1 %}
                                        <a class="badge badge-primary" href="{{ site.baseurl }}/categories#{{ category | replace: " ","-" }}">{{ category }}</a>
                                        {% endfor %}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            {% endif %}
        {% endfor %}
    </div>
</section>

<!-- Posts Index
================================================== -->
<div class="blog-grid-container">
    {% for post in paginator.posts %}
        {% if post.featured != true %}
            {% include postbox.html %}
        {% endif %}
    {% endfor %}
</div>

<!-- Pagination
================================================== -->
<div class="bottompagination">
<span class="navigation" role="navigation">
    {% include pagination.html %}
</span>
</div>
'''
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated index.html file")

def main():
    print("Fixing CSS for featured images...")
    update_custom_css()
    update_index_html()
    print("CSS and index.html updated successfully!")
    print("\nThe featured images should now be properly sized with these changes.")
    print("Make sure to commit and push these changes to your GitHub repository.")

if __name__ == "__main__":
    main()