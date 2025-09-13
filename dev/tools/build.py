#!/usr/bin/env python3
"""
Simple website builder that generates HTML from JSON content.
"""
import json
import os
from pathlib import Path

class WebsiteBuilder:
    def __init__(self):
        self.dev_dir = Path("dev")
        self.root_dir = Path(".")
        
    def load_content(self):
        """Load content from JSON file."""
        content_file = Path("src/data/content.json")
        with open(content_file, 'r') as f:
            return json.load(f)
    
    def generate_navigation(self, current_page="index"):
        """Generate navigation HTML."""
        nav_links = {
            "index": "Home",
            "services": "Services", 
            "about": "About",
            "research": "Research",
            "contact": "Contact"
        }
        
        nav_html = ""
        for page, title in nav_links.items():
            if page == current_page:
                nav_html += f'<li><a href="{page}.html" class="active">{title}</a></li>'
            else:
                if page == "index":
                    nav_html += f'<li><a href="index.html">{title}</a></li>'
                else:
                    nav_html += f'<li><a href="{page}.html">{title}</a></li>'
        
        return nav_html

    def generate_header_footer(self, content, current_page="index"):
        """Generate header and footer HTML."""
        nav_links = self.generate_navigation(current_page)
        
        header = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{current_page.title()} - {content["site"]["title"]}</title>
    <link rel="stylesheet" href="styles/main.css">
    <link rel="stylesheet" href="styles/components.css">
    <link rel="stylesheet" href="styles/responsive.css">
</head>
<body>
    <!-- Header -->
    <header>
        <nav>
            <div class="logo">{content["site"]["title"]}</div>
            <ul class="nav-links">
                {nav_links}
            </ul>
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </nav>
    </header>'''

        footer = f'''
    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>{content["site"]["title"]}</h4>
                    <p>{content["site"]["description"]}</p>
                </div>
                
                <div class="footer-section">
                    <h4>Services</h4>
                    <a href="services.html">Respiratory Tract Modeling</a>
                    <a href="services.html">Medical Device CFD</a>
                    <a href="services.html">Biomedical Flow Analysis</a>
                </div>
                
                <div class="footer-section">
                    <h4>Contact</h4>
                    <a href="mailto:{content["contact"]["email"]}">{content["contact"]["email"]}</a>
                    <a href="tel:{content["contact"]["phone"].replace(' ', '').replace('(', '').replace(')', '').replace('-', '')}">{content["contact"]["phone"]}</a>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2024 {content["site"]["title"]}. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="scripts/main.js"></script>
</body>
</html>'''
        return header, footer

    def generate_home_html(self, content):
        """Generate home page HTML."""
        header, footer = self.generate_header_footer(content, "index")
        
        return header + f'''
    <!-- Hero Section -->
    <section class="hero hero-page">
        <div class="hero-background"></div>
        <div class="hero-content">
            <h1>{content["hero"]["title"]}</h1>
            <p>{content["hero"]["subtitle"]}</p>
            <a href="contact.html" class="cta-button">{content["hero"]["cta_text"]}</a>
        </div>
    </section>

    <!-- Quick Links Section -->
    <section class="quick-links">
        <div class="container">
            <h2 class="section-title">Explore Our Expertise</h2>
            <div class="quick-links-grid">
                <a href="services.html" class="quick-link-card">
                    <h3>Our Services</h3>
                    <p>Advanced respiratory engineering solutions</p>
                    <span class="arrow">→</span>
                </a>
                <a href="research.html" class="quick-link-card">
                    <h3>Research Publications</h3>
                    <p>Scientific contributions and peer-reviewed research</p>
                    <span class="arrow">→</span>
                </a>
                <a href="about.html" class="quick-link-card">
                    <h3>About Our Lab</h3>
                    <p>Leading CFD expertise in respiratory systems</p>
                    <span class="arrow">→</span>
                </a>
                <a href="contact.html" class="quick-link-card">
                    <h3>Start Your Project</h3>
                    <p>Ready to optimize your respiratory system?</p>
                    <span class="arrow">→</span>
                </a>
            </div>
        </div>
    </section>
''' + footer

    def generate_services_html(self, content):
        """Generate services page HTML."""
        header, footer = self.generate_header_footer(content, "services")
        
        html = header + f'''
    <!-- Services Section -->
    <section class="services services-page">
        <div class="container">
            <h1 class="page-title">{content["services"]["title"]}</h1>
            <p class="page-subtitle">{content["services"]["subtitle"]}</p>
            
            <div class="services-grid">'''
        
        # Generate service cards
        for service in content["services"]["items"]:
            icon_or_image = ""
            if service["image"]:
                icon_or_image = f'<div class="service-image"><img src="{service["image"]}" alt="{service["title"]}"></div>'
            else:
                icon_or_image = f'<div class="service-icon">{service["icon"]}</div>'
            
            service_html = f'''
                <div class="service-card">
                    {icon_or_image}
                    <h3>{service["title"]}</h3>
                    <p>{service["description"]}</p>
                </div>'''
            html += service_html
        
        html += '''
            </div>
        </div>
    </section>
''' + footer
        return html

    def generate_about_html(self, content):
        """Generate about page HTML."""
        header, footer = self.generate_header_footer(content, "about")
        
        html = header + f'''
    <!-- About Section -->
    <section class="about about-page">
        <div class="container">
            <h1 class="page-title">{content["about"]["title"]}</h1>
            <div class="about-content">
                <div class="about-text">'''
        
        for paragraph in content["about"]["paragraphs"]:
            html += f'<p>{paragraph}</p>'
        
        html += '''
                </div>
                <div>
                    <div class="stats">'''
        
        # Generate stats
        for stat in content["about"]["stats"]:
            html += f'''
                        <div class="stat">
                            <div class="stat-number">{stat["number"]}</div>
                            <div class="stat-label">{stat["label"]}</div>
                        </div>'''
        
        html += '''
                    </div>
                </div>
            </div>
        </div>
    </section>
''' + footer
        return html

    def generate_contact_html(self, content):
        """Generate contact page HTML."""
        header, footer = self.generate_header_footer(content, "contact")
        
        return header + f'''
    <!-- Contact Section -->
    <section class="contact contact-page">
        <div class="container">
            <h1 class="page-title">{content["contact"]["title"]}</h1>
            <p class="page-subtitle">{content["contact"]["subtitle"]}</p>
            
            <div class="contact-content">
                <form class="contact-form">
                    <div class="form-group">
                        <label for="name">Full Name *</label>
                        <input type="text" id="name" name="name" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="email">Email Address *</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="company">Company/Organization</label>
                        <input type="text" id="company" name="company">
                    </div>
                    
                    <div class="form-group">
                        <label for="message">Project Description *</label>
                        <textarea id="message" name="message" placeholder="Please describe your project requirements..." required></textarea>
                    </div>
                    
                    <button type="submit" class="submit-btn">Send Message</button>
                </form>
                
                <div class="contact-info">
                    <h3>Get In Touch</h3>
                    
                    <div class="contact-item">
                        <span class="contact-item-icon">📧</span>
                        <span>{content["contact"]["email"]}</span>
                    </div>
                    
                    <div class="contact-item">
                        <span class="contact-item-icon">📞</span>
                        <span>{content["contact"]["phone"]}</span>
                    </div>
                    
                    <div class="contact-item">
                        <span class="contact-item-icon">📍</span>
                        <span>{content["contact"]["address"]}</span>
                    </div>
                    
                    <div class="contact-item">
                        <span class="contact-item-icon">🕒</span>
                        <span>{content["contact"]["hours"]}</span>
                    </div>
                </div>
            </div>
        </div>
    </section>
''' + footer
    
    def generate_research_html(self, content):
        """Generate research page HTML."""
        header, footer = self.generate_header_footer(content, "research")
        
        html = header + f'''
    <!-- Research Section -->
    <section class="research research-page">
        <div class="container">
            <h1 class="page-title">{content["research"]["title"]}</h1>
            <p class="page-subtitle">{content["research"]["subtitle"]}</p>
            
            <div class="research-grid">'''
        
        # Generate research papers
        for paper in content["research"]["papers"]:
            categories_html = ""
            for category in paper["categories"]:
                categories_html += f'<span class="category-tag">{category}</span>'
            
            paper_html = f'''
                <div class="research-paper">
                    <div class="paper-header">
                        <h3 class="paper-title">{paper["title"]}</h3>
                        <div class="paper-authors">{paper["authors"]}</div>
                        <div class="paper-meta">
                            <span class="journal">{paper["journal"]}</span> • 
                            <span class="year">{paper["year"]}</span>
                        </div>
                        <div class="paper-categories">{categories_html}</div>
                    </div>
                    <div class="paper-abstract">
                        <p>{paper["abstract"]}</p>
                    </div>
                    <div class="paper-links">
                        <a href="https://doi.org/{paper["doi"]}" class="doi-link" target="_blank">DOI: {paper["doi"]}</a>'''
            
            if paper["pdf_link"]:
                paper_html += f'<a href="{paper["pdf_link"]}" class="pdf-link" target="_blank">📄 PDF</a>'
            
            paper_html += '''
                    </div>
                </div>'''
            html += paper_html
        
        html += '''
            </div>
        </div>
    </section>
''' + footer
        return html

    def build(self):
        """Build the website."""
        print("🔨 Building multi-page website from JSON content...")
        
        # Load content
        content = self.load_content()
        
        # Generate all pages
        pages = {
            "index": self.generate_home_html(content),
            "services": self.generate_services_html(content),
            "about": self.generate_about_html(content), 
            "research": self.generate_research_html(content),
            "contact": self.generate_contact_html(content)
        }
        
        # Write all pages to parent directory
        output_files = []
        for page_name, page_html in pages.items():
            output_file = Path(f"../{page_name}.html")
            with open(output_file, 'w') as f:
                f.write(page_html)
            output_files.append(output_file)
            
        print(f"✅ Multi-page website built successfully!")
        print(f"📁 Generated pages: {', '.join([str(f) for f in output_files])}")
        print(f"🌐 Test locally: python -m http.server 8000")

if __name__ == "__main__":
    builder = WebsiteBuilder()
    builder.build()