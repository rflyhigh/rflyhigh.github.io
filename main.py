#!/usr/bin/env python3

import os
import datetime

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def create_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Created file: {file_path}")

def create_chemistry_manual_post():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    file_path = f"_posts/{today}-311305-basic-science-chemistry-manual-answer.md"
    
    content = '''---
layout: post
title: "311305 Basic Science Chemistry Manual Answer"
author: flyhigh
categories: [AIML, "First Semester", "Manual Answers"]
tags: [chemistry, practical, manual, "k scheme"]
image: assets/images/chemistry-lab.jpg
featured: true
---

# 311305 Basic Science Chemistry Manual Answer

This post contains complete answers for the Basic Science Chemistry lab manual (311305) for MSBTE students. Each practical is provided with detailed solutions.

## Practical Solutions

### PracticalNo.1: Identification of Cations

<iframe src="https://drive.google.com/file/d/1SUR1lOXZawKqXpIJFKa8sB54Fw3oXUxO/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.2: Identification of anions

<iframe src="https://drive.google.com/file/d/1YqH2it4bni-DxycpmJFulZqLvTK-Gluv/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.3: Identification of States of Matter

<iframe src="https://drive.google.com/file/d/12ZCujGTN7_cArp2LVXNJbafW2woLRWKR/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.4: Electrode Potential of Copper Metal

<iframe src="https://drive.google.com/file/d/1M1v5XL-xGOssrSM9yrGQhXGYMEsdVzwl/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.5: Electrode potential of Iron Metal

<iframe src="https://drive.google.com/file/d/1YiSFkwQI-nysXA4vl3imvLrB3ZBK34f0/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.6: Daniel's cell

<iframe src="https://drive.google.com/file/d/1CK-VkY9NCT4qJEC4YGbJRxno7R-CTNGC/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.7: Electrochemical Equivalent of Cu

<iframe src="https://drive.google.com/file/d/1qmE045U4lcOWT3DHm5ZRseC1KjpjDOI3/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.8: Equivalent weight of metal

<iframe src="https://drive.google.com/file/d/1a60ZHyZgkanLF9feHr0uE8YWs_nsUbE6/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.9: Preparation of Corrosive Medium

<iframe src="https://drive.google.com/file/d/101HxJHNyCmnVPkuOUsrEUiqgWimTjCAS/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.10: Effect of temperature on the rate of corrosion

<iframe src="https://drive.google.com/file/d/16_4j1hdqTWmum1Tb-Ft8x8VcKxFqkrKI/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.11: Effect of temperature on Viscosity

<iframe src="https://drive.google.com/file/d/1WxAcQuTsAUknQjCWPVLmflFEylFxEZGX/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.12: Steam Emulsification Number

<iframe src="https://drive.google.com/file/d/1z8Z4N-VsUmfB2rJmOTmhVJEYbsQeOlbM/preview" width="100%" height="480" allow="autoplay"></iframe>

### Experiment No.13: Flash and fire point by Cleveland's open cup- apparatus

<iframe src="https://drive.google.com/file/d/1Pc45R9ve2ZEg37-hoNzvA-0A5IDFiQn6/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.14: Flashpoint by Abel's closed cup apparatus

<iframe src="https://drive.google.com/file/d/1g1mB0EH9no2UdH4-AZol5gwiWSFYWOop/preview" width="100%" height="480" allow="autoplay"></iframe>

### Practical No.15: Thinner content in oil paint

<iframe src="https://drive.google.com/file/d/1TH7KniYqTYM3xWLOC6eUWpe6pwQ8cYsg/preview" width="100%" height="480" allow="autoplay"></iframe>

More practical solutions will be added in a few days...

## Conclusion

This blog post shares the full answers to the Basic Science Chemistry lab manual. If you find this post useful, please share it with your friends.

## Related Resources

- [AIML First Semester Manuals](/aiml-first-semester-manuals)
- [AIML First Semester](/aiml-first-semester)
- [AIML Program](/aiml)
'''
    
    create_file(file_path, content)

def create_aiml_first_semester_manuals_post():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    file_path = f"_posts/{today}-aiml-first-semester-manuals.md"
    
    content = '''---
layout: post
title: "AIML First Semester Manuals"
author: flyhigh
categories: [AIML, "First Semester"]
tags: ["manual answers", "k scheme", practical]
image: assets/images/aiml-manuals.jpg
featured: true
---

# AIML First Semester Manuals

This page contains links to all practical manual answers for AIML First Semester subjects under K Scheme.

## Available Manual Answers

### [311305 Basic Science Chemistry Manual Answer](/311305-basic-science-chemistry-manual-answer)
Complete solutions for all Chemistry practical experiments including:
- Identification of Cations and Anions
- Electrode Potential experiments
- Viscosity and Emulsification tests
- And more...

### 311301 English Manual Answer
*Coming soon...*

### 311302 Basic Mathematics Manual Answer
*Coming soon...*

### 311303 Basic Physics Manual Answer
*Coming soon...*

### 311304 Engineering Graphics Manual Answer
*Coming soon...*

### 311306 Fundamentals of ICT Manual Answer
*Coming soon...*

## How to Use These Manuals

1. Click on the subject you need help with
2. Find the specific practical number you're working on
3. Follow the step-by-step solutions provided
4. Use these as reference only - we recommend trying to solve the practicals yourself first!

## Need More Help?

If you need additional help with your AIML First Semester practicals, feel free to leave a comment below or check out our [AIML First Semester](/aiml-first-semester) page for more resources.
'''
    
    create_file(file_path, content)

def create_aiml_first_semester_post():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    file_path = f"_posts/{today}-aiml-first-semester.md"
    
    content = '''---
layout: post
title: "AIML First Semester"
author: flyhigh
categories: [AIML]
tags: ["first semester", syllabus, "manual answers", "guessing papers"]
image: assets/images/aiml-first-sem.jpg
featured: true
---

# AIML First Semester Resources

Welcome to the comprehensive resource page for AIML (Artificial Intelligence and Machine Learning) First Semester students. Here you'll find everything you need to excel in your studies.

## Syllabus

The AIML First Semester curriculum under K Scheme includes the following subjects:

1. **311301 - English**
   - Communication Skills
   - Grammar and Usage
   - Technical Writing

2. **311302 - Basic Mathematics**
   - Algebra
   - Trigonometry
   - Coordinate Geometry
   - Differential Calculus

3. **311303 - Basic Physics**
   - Units and Measurements
   - Force and Motion
   - Work, Power and Energy
   - Properties of Matter

4. **311304 - Engineering Graphics**
   - Drawing Equipment and Use of Instruments
   - Lettering and Dimensioning
   - Geometric Constructions
   - Projections

5. **311305 - Basic Science Chemistry**
   - Atomic Structure
   - Chemical Bonding
   - Electrochemistry
   - Fuels and Combustion

6. **311306 - Fundamentals of ICT**
   - Computer Fundamentals
   - Operating Systems
   - Office Automation Tools
   - Internet and Web Technologies

[Download Complete Syllabus (PDF)](#)

## Manual Answers

Get solutions to all your practical manuals:

- [AIML First Semester Manuals](/aiml-first-semester-manuals)
  - [311305 Basic Science Chemistry Manual Answer](/311305-basic-science-chemistry-manual-answer)
  - More coming soon...

## Guessing Papers

Prepare for your exams with our exclusive guessing papers:

- English Guessing Paper (Coming Soon)
- Basic Mathematics Guessing Paper (Coming Soon)
- Basic Physics Guessing Paper (Coming Soon)
- Engineering Graphics Guessing Paper (Coming Soon)
- Basic Science Chemistry Guessing Paper (Coming Soon)
- Fundamentals of ICT Guessing Paper (Coming Soon)

## Study Materials

- Subject Notes (Coming Soon)
- Important Questions (Coming Soon)
- Previous Year Question Papers (Coming Soon)
- Model Answer Papers (Coming Soon)

## Exam Preparation Tips

1. **Create a study schedule** - Allocate specific time slots for each subject
2. **Focus on practical knowledge** - MSBTE exams emphasize practical applications
3. **Practice previous year papers** - Understand the exam pattern and important questions
4. **Group study sessions** - Discuss difficult topics with classmates
5. **Regular revisions** - Review what you've learned weekly

## Need Help?

If you have any questions or need additional resources, feel free to leave a comment below or contact us directly.

[Back to AIML Program](/aiml)
'''
    
    create_file(file_path, content)

def create_aiml_program_post():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    file_path = f"_posts/{today}-aiml.md"
    
    content = '''---
layout: post
title: "AIML Program - MSBTE"
author: flyhigh
categories: [AIML]
tags: [program, syllabus, "k scheme"]
image: assets/images/aiml-program.jpg
featured: true
---

# AIML Program - Artificial Intelligence and Machine Learning

Welcome to the AIML (Artificial Intelligence and Machine Learning) program resource page. This diploma program prepares students for careers in the rapidly growing field of AI and ML.

## Program Overview

The AIML diploma is a 6-semester program designed to provide students with a strong foundation in artificial intelligence and machine learning concepts, along with practical skills needed for industry applications.

## Semesters

### [First Semester](/aiml-first-semester)
Foundation courses including Basic Mathematics, Physics, Chemistry, and ICT fundamentals.

### Second Semester
Introduction to programming concepts and data structures.

### Third Semester
Core computer science subjects and introduction to AI concepts.

### Fourth Semester
Advanced programming and database management systems.

### Fifth Semester
Specialized AI and ML algorithms and applications.

### Sixth Semester
Industry projects and advanced AI implementations.

## K Scheme Syllabus

Access the complete syllabus for all semesters:

- [First Semester Syllabus](/aiml-first-semester)
- Second Semester Syllabus (Coming Soon)
- Third Semester Syllabus (Coming Soon)
- Fourth Semester Syllabus (Coming Soon)
- Fifth Semester Syllabus (Coming Soon)
- Sixth Semester Syllabus (Coming Soon)

## Manual Answers

Find practical manual solutions for all semesters:

### K Scheme Manual Answers
- [First Semester Manuals](/aiml-first-semester-manuals)
- Second Semester Manuals (Coming Soon)
- Third Semester Manuals (Coming Soon)
- Fourth Semester Manuals (Coming Soon)
- Fifth Semester Manuals (Coming Soon)
- Sixth Semester Manuals (Coming Soon)

## Guessing Papers

Prepare for your exams with our exclusive guessing papers:
- [MSBTE AIML Guessing Papers](#) (Coming Soon)

## Career Opportunities

AIML diploma graduates can pursue careers in:
- AI Application Development
- Machine Learning Engineering
- Data Analysis
- Computer Vision
- Natural Language Processing
- Robotics
- And many more emerging fields

## Industry Partners

Our program is designed in collaboration with industry leaders to ensure the curriculum meets current industry demands.

## Resources

- [MSBTE Official Website](https://msbte.org.in/)
- [AIML Community Forum](#)
- [Recommended Books](#)
- [Online Learning Resources](#)

Stay tuned for regular updates and additional resources to help you succeed in your AIML diploma program!
'''
    
    create_file(file_path, content)

def create_custom_css():
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
}

.featured-posts .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
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
'''
    
    create_file(file_path, content)

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
                            <p class="card-text">{{ post.excerpt | strip_html | truncatewords:30 }}</p>
                            <div class="metafooter">
                                <div class="wrapfooter">
                                    <span class="meta-footer-thumb">
                                        <img class="author-thumb" src="{{ site.baseurl }}/{{ site.authors[post.author].avatar }}" alt="{{ site.authors[post.author].display_name }}">
                                    </span>
                                    <span class="author-meta">
                                        <span class="post-name">{{ site.authors[post.author].display_name }}</span><br/>
                                        <span class="post-date">{{ post.date | date_to_string }}</span>
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
    
    create_file(file_path, content)

def update_default_html():
    file_path = "_layouts/default.html"
    
    # Check if file exists first
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} does not exist. Skipping update.")
        return
    
    # Read the current content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Add custom CSS link in the head section
    if '<link href="{{ site.baseurl }}/assets/css/custom.css" rel="stylesheet">' not in content:
        content = content.replace('</head>', '<link href="{{ site.baseurl }}/assets/css/custom.css" rel="stylesheet">\n</head>')
        
        # Write the updated content back
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {file_path} to include custom CSS")
    else:
        print(f"Custom CSS already included in {file_path}")

def create_placeholder_images():
    # Create assets/images directory if it doesn't exist
    create_directory_if_not_exists("assets/images")
    
    # List of required images
    images = [
        "chemistry-lab.jpg",
        "aiml-manuals.jpg",
        "aiml-first-sem.jpg",
        "aiml-program.jpg"
    ]
    
    # Check if images exist, if not create placeholder text files
    for image in images:
        image_path = f"assets/images/{image}"
        if not os.path.exists(image_path):
            with open(image_path + ".txt", 'w') as f:
                f.write(f"Placeholder for {image}. Please replace with an actual image file.")
            print(f"Created placeholder for {image}")

def main():
    print("Starting to create MSBTEMadeEasy posts and structure...")
    
    # Create necessary directories
    create_directory_if_not_exists("_posts")
    create_directory_if_not_exists("assets/css")
    
    # Create posts
    create_chemistry_manual_post()
    create_aiml_first_semester_manuals_post()
    create_aiml_first_semester_post()
    create_aiml_program_post()
    
    # Create CSS file
    create_custom_css()
    
    # Update index.html
    update_index_html()
    
    # Update default.html to include custom CSS
    update_default_html()
    
    # Create placeholder images
    create_placeholder_images()
    
    print("\nAll files have been created successfully!")
    print("\nNext steps:")
    print("1. Replace the placeholder images in assets/images/ with actual images")
    print("2. Make sure your _layouts/default.html includes the custom CSS")
    print("3. Commit and push these changes to your GitHub repository")
    print("4. GitHub Pages will rebuild your site with the new content")

if __name__ == "__main__":
    main()