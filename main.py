#!/usr/bin/env python3

import os

def update_related_posts_html():
    file_path = "_includes/related-posts.html"
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} does not exist. Creating new file.")
    
    content = '''<!-- Related Posts
================================================== -->
<div class="{% unless page.categories == empty %} related-posts {% endunless %}">  

    {% unless page.categories == empty %}
    <h2 class="text-center mb-4">Explore more like this</h2>
    {% endunless %}
    
    <div class="d-flex flex-wrap justify-content-center align-items-center">
    
    <!-- Categories -->
    {% assign sortedCategories = page.categories | sort %}
    {% for category in sortedCategories limit:3 %}
    <a class="smoothscroll badge badge-primary text-capitalize m-1" href="{{site.baseurl}}/categories#{{ category | replace: " ","-" }}">{{ category }}</a>                
    {% endfor %}
    {% if page.categories.size > 3 %}
    <span class="badge badge-light m-1">+{{ page.categories.size | minus: 3 }} more</span>
    {% endif %}

    <!-- Tags -->  
    {% assign sortedTags = page.tags | sort %}
    {% for tag in sortedTags limit:4 %}                
    <a class="smoothscroll badge badge-primary text-capitalize m-1" href="{{site.baseurl}}/tags#{{ tag | replace: " ","-" }}">{{ tag }}</a>               
    {% endfor %}
    {% if page.tags.size > 4 %}
    <span class="badge badge-light m-1">+{{ page.tags.size | minus: 4 }} more</span>
    {% endif %}

    </div>

    {% assign maxRelated = 3 %}
    {% assign minCommonTags =  1 %}
    {% assign maxRelatedCounter = 0 %}
    <div class="blog-grid-container">
        {% for post in site.posts %}
        
            {% assign sameTagCount = 0 %}
            {% assign commonTags = '' %}
        
            {% for category in post.categories %}
            {% if post.url != page.url %}
                {% if page.categories contains category %}
                {% assign sameTagCount = sameTagCount | plus: 1 %}
                {% capture tagmarkup %} {{ category }} {% endcapture %}
                {% assign commonTags = commonTags | append: tagmarkup %}
                {% endif %}
            {% endif %}
            {% endfor %}
        
            {% if sameTagCount >= minCommonTags %}
            {% include postbox.html %}
            {% assign maxRelatedCounter = maxRelatedCounter | plus: 1 %}
            {% if maxRelatedCounter >= maxRelated %}
                {% break %}
            {% endif %}
            {% endif %}
        
        {% endfor %}
        </div>        
</div>
'''
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {file_path}")

def update_custom_css():
    file_path = "assets/css/custom.css"
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} does not exist. Creating new file.")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("/* Custom styles for MSBTEMadeEasy */\n\n")
    
    # Read existing content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Add new CSS for related posts
    related_posts_css = '''
/* Related posts badges */
.related-posts .badge {
    margin: 0.25rem;
    padding: 0.5rem 0.75rem;
    font-size: 0.75rem;
    font-weight: 500;
    border-radius: 20px;
}

.related-posts .badge-primary {
    background-color: #17a2b8;
    transition: all 0.2s ease;
}

.related-posts .badge-primary:hover {
    background-color: #138496;
    transform: translateY(-2px);
}

.related-posts .badge-light {
    background-color: #f8f9fa;
    color: #6c757d;
}

.related-posts h2 {
    font-size: 1.25rem;
    color: #6c757d;
    margin-bottom: 1rem;
}

.related-posts .d-flex {
    flex-wrap: wrap;
    max-width: 100%;
    overflow: hidden;
}
'''
    
    # Check if the CSS already exists
    if "/* Related posts badges */" not in content:
        content += related_posts_css
        
        # Write the updated content back
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {file_path} with related posts CSS")
    else:
        print(f"Related posts CSS already exists in {file_path}")

def main():
    print("Fixing category overflow in 'Explore more like this' section...")
    update_related_posts_html()
    update_custom_css()
    print("\nFixes applied successfully!")
    print("\nChanges made:")
    print("1. Limited categories to 3 with a '+X more' indicator if there are more")
    print("2. Limited tags to 4 with a '+X more' indicator if there are more")
    print("3. Added proper spacing and margins to prevent overflow")
    print("4. Made the badges wrap to the next line when they exceed the container width")
    print("5. Added hover effects for better user experience")
    print("\nMake sure to commit and push these changes to your GitHub repository.")

if __name__ == "__main__":
    main()