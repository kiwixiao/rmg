#!/usr/bin/env python3
"""
Simple static site generator for the CFD website.
Combines templates with JSON data to generate the final HTML.
"""

import json
import os
import shutil
import re
from pathlib import Path
import markdown

class SiteBuilder:
    def __init__(self, src_dir="src", dist_dir="dist"):
        self.src_dir = Path(src_dir)
        self.dist_dir = Path(dist_dir)
        self.templates_dir = self.src_dir / "templates"
        self.data_dir = self.src_dir / "data"
        self.components_dir = self.src_dir / "components"
        self.content_dir = self.src_dir / "content"
        
    def clean_dist(self):
        """Clean the distribution directory."""
        if self.dist_dir.exists():
            shutil.rmtree(self.dist_dir)
        self.dist_dir.mkdir(parents=True)
        
    def copy_assets(self):
        """Copy static assets to distribution directory."""
        # Copy styles
        styles_src = self.src_dir / "styles"
        styles_dest = self.dist_dir / "styles"
        if styles_src.exists():
            shutil.copytree(styles_src, styles_dest)
            
        # Copy scripts
        scripts_src = self.src_dir / "scripts"
        scripts_dest = self.dist_dir / "scripts"
        if scripts_src.exists():
            shutil.copytree(scripts_src, scripts_dest)
            
        # Copy assets
        assets_src = self.src_dir / "assets"
        assets_dest = self.dist_dir / "assets"
        if assets_src.exists():
            shutil.copytree(assets_src, assets_dest)
            
    def load_json_data(self, filename):
        """Load JSON data from the data directory."""
        with open(self.data_dir / filename, 'r') as f:
            return json.load(f)
            
    def load_markdown(self, filepath):
        """Load and convert markdown to HTML."""
        with open(filepath, 'r') as f:
            return markdown.markdown(f.read())
            
    def simple_template(self, template_content, data):
        """Simple template engine using {{variable}} syntax."""
        def replace_var(match):
            key = match.group(1)
            keys = key.split('.')
            value = data
            try:
                for k in keys:
                    value = value[k]
                return str(value) if value is not None else ''
            except (KeyError, TypeError):
                return f'{{{{{key}}}}}'  # Return original if not found
                
        # Replace simple variables
        template_content = re.sub(r'\{\{\s*([^}]+)\s*\}\}', replace_var, template_content)
        
        # Handle arrays (simple implementation)
        template_content = self.handle_arrays(template_content, data)
        
        return template_content
        
    def handle_arrays(self, content, data):
        """Handle simple array iteration."""
        # Pattern for {{#array}} content {{/array}}
        array_pattern = r'\{\{#([^}]+)\}\}(.*?)\{\{/\1\}\}'
        
        def replace_array(match):
            array_name = match.group(1)
            array_content = match.group(2)
            
            try:
                keys = array_name.split('.')
                array_data = data
                for key in keys:
                    array_data = array_data[key]
                    
                if isinstance(array_data, list):
                    result = ""
                    for item in array_data:
                        item_content = array_content
                        # Replace variables in the array content
                        item_content = self.simple_template(item_content, item)
                        result += item_content
                    return result
                else:
                    return ""
            except (KeyError, TypeError):
                return match.group(0)  # Return original if not found
                
        return re.sub(array_pattern, replace_array, content, flags=re.DOTALL)
        
    def load_component(self, component_name):
        """Load a component template."""
        component_path = self.components_dir / f"{component_name}.html"
        if component_path.exists():
            with open(component_path, 'r') as f:
                return f.read()
        return f"<!-- Component {component_name} not found -->"
        
    def build_page(self, template_name, output_name, data):
        """Build a single page."""
        # Load base template
        base_template_path = self.templates_dir / f"{template_name}.html"
        with open(base_template_path, 'r') as f:
            template_content = f.read()
            
        # Build main content from components
        components = [
            self.load_component('hero'),
            self.load_component('services'),
            self.load_component('about'),
            # Add blog component if needed
            '<section id="blog" class="blog"><div class="container"><h2 class="section-title">{{blog.title}}</h2><p class="section-subtitle">{{blog.subtitle}}</p></div></section>',
            # Add contact component
            '<section id="contact" class="contact"><div class="container"><h2 class="section-title">{{contact.title}}</h2><p class="section-subtitle">{{contact.subtitle}}</p></div></section>'
        ]
        
        main_content = '\\n'.join(components)
        
        # Replace content placeholder
        template_content = template_content.replace('{{content}}', main_content)
        
        # Apply template engine
        final_content = self.simple_template(template_content, data)
        
        # Write output
        output_path = self.dist_dir / output_name
        with open(output_path, 'w') as f:
            f.write(final_content)
            
        print(f"Generated: {output_name}")
        
    def build(self):
        """Build the entire site."""
        print("Building CFD Website...")
        
        # Clean and setup
        self.clean_dist()
        
        # Copy assets
        self.copy_assets()
        
        # Load data
        site_config = self.load_json_data('site-config.json')
        content_data = self.load_json_data('content.json')
        blog_data = self.load_json_data('blog.json')
        
        # Merge all data
        all_data = {**site_config, **content_data, **blog_data}
        
        # Build main page
        self.build_page('base', 'index.html', all_data)
        
        print("Build completed successfully!")
        print(f"Output directory: {self.dist_dir}")

if __name__ == "__main__":
    builder = SiteBuilder()
    builder.build()