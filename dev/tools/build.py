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
    
    def generate_html(self, content):
        """Generate complete HTML from content."""
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{content["site"]["title"]}</title>
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
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-background"></div>
        <div class="hero-content">
            <h1>{content["hero"]["title"]}</h1>
            <p>{content["hero"]["subtitle"]}</p>
            <a href="{content["hero"]["cta_link"]}" class="cta-button">{content["hero"]["cta_text"]}</a>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
        <div class="container">
            <h2 class="section-title">{content["services"]["title"]}</h2>
            <p class="section-subtitle">{content["services"]["subtitle"]}</p>
            
            <div class="services-grid">'''
        
        # Generate service cards
        for service in content["services"]["items"]:
            service_html = f'''
                <div class="service-card">
                    <div class="service-icon">{service["icon"]}</div>
                    <h3>{service["title"]}</h3>
                    <p>{service["description"]}</p>
                </div>'''
            html += service_html
        
        html += '''
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <div class="about-content">
                <div class="about-text">'''
        
        html += f'<h3>{content["about"]["title"]}</h3>'
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
        
        html += f'''
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2 class="section-title">{content["contact"]["title"]}</h2>
            <p class="section-subtitle">{content["contact"]["subtitle"]}</p>
            
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
                    <a href="#services">Respiratory Tract Modeling</a>
                    <a href="#services">Medical Device CFD</a>
                    <a href="#services">Biomedical Flow Analysis</a>
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
        return html
    
    def build(self):
        """Build the website."""
        print("🔨 Building website from JSON content...")
        
        # Load content
        content = self.load_content()
        
        # Generate HTML
        html = self.generate_html(content)
        
        # Write to parent directory index.html
        output_file = Path("../index.html")
        with open(output_file, 'w') as f:
            f.write(html)
            
        print(f"✅ Website built successfully!")
        print(f"📁 Output: {output_file}")
        print(f"🌐 Test locally: python -m http.server 8000")

if __name__ == "__main__":
    builder = WebsiteBuilder()
    builder.build()