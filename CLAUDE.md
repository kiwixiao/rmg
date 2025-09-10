# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a modern, modular static website for a CFD (Computational Fluid Dynamics) consultancy specializing in respiratory airflow modeling. The website follows modern web development practices with component-based architecture and content management through JSON files.

## Architecture

- **Component-Based Structure**: Modular HTML components in `src/components/`
- **Template System**: Base templates with content injection
- **Modular CSS**: Organized stylesheets with CSS variables
- **JavaScript Modules**: ES6 modules for functionality
- **Content as Data**: JSON files for all content management
- **Build Process**: Python-based static site generator

## File Structure

```
src/
├── components/          # Reusable HTML components (hero.html, services.html, etc.)
├── templates/           # Base HTML templates
├── styles/             # Modular CSS files
│   ├── variables.css   # CSS custom properties
│   ├── base.css        # Base styles and typography
│   ├── components.css  # Component-specific styles
│   └── responsive.css  # Mobile responsive styles
├── scripts/            # JavaScript modules
│   ├── main.js         # Application entry point
│   └── modules/        # Individual feature modules
├── data/               # JSON configuration and content
│   ├── site-config.json    # Site navigation and footer
│   ├── content.json        # Main page content
│   └── blog.json           # Blog posts metadata
├── content/            # Markdown content files
│   └── blog/           # Blog post markdown files
└── assets/             # Images, icons, documents

tools/                  # Build tools
├── build.py           # Python static site generator

dist/                  # Generated website (build output)
public/                # Public assets
```

## Development Workflow

### Common Development Tasks

1. **Build the website:**
   ```bash
   make build
   ```

2. **Development mode (build + serve):**
   ```bash
   make dev
   ```

3. **Serve locally:**
   ```bash
   make serve
   ```

4. **Clean build artifacts:**
   ```bash
   make clean
   ```

5. **Install dependencies:**
   ```bash
   make install
   ```

### Content Updates

1. **Update main content:** Edit `src/data/content.json`
2. **Change navigation:** Edit `src/data/site-config.json`
3. **Add blog posts:** 
   - Create markdown file in `src/content/blog/`
   - Add metadata to `src/data/blog.json`
4. **Update images:** Place in `src/assets/images/` and reference in JSON

## Content Management System

The website uses a JSON-based content management system:

### Primary Content File: `src/data/content.json`
- Hero section (title, subtitle, CTA, background image)
- Services (6 services with titles, descriptions, icons, images)
- About section (title, paragraphs, image, statistics)
- Contact information

### Site Configuration: `src/data/site-config.json`
- Site title and navigation
- Footer sections and links
- Global site settings

### Blog System: `src/data/blog.json` + Markdown files
- Blog post metadata and excerpts
- Markdown files for full blog content
- Support for tags, authors, dates

## Styling System

- **CSS Variables**: Centralized design tokens in `variables.css`
- **Modular CSS**: Separate files for different concerns
- **Color Scheme**: Primary blue (#2563eb), secondary (#1e40af), accent (#3b82f6)
- **Responsive Design**: Mobile-first approach
- **Component Styles**: Scoped styling for each component

## JavaScript Architecture

- **ES6 Modules**: Modern JavaScript with import/export
- **Feature Modules**: Separate modules for navigation, smooth scroll, header effects
- **Event-Driven**: Clean event handling and DOM manipulation
- **No Build Dependencies**: Runs directly in modern browsers

## Build Process

The site uses a custom Python-based static site generator (`tools/build.py`):

1. **Template Processing**: Combines base templates with components
2. **Content Injection**: Merges JSON data with HTML templates
3. **Asset Copying**: Copies CSS, JS, and assets to dist/
4. **Markdown Processing**: Converts blog markdown to HTML

## Testing and Quality Assurance

1. **Local Testing**: Use `make dev` for development server
2. **Browser Testing**: Test in modern browsers (Chrome, Firefox, Safari)
3. **Responsive Testing**: Use browser dev tools for mobile testing
4. **Content Validation**: Ensure JSON files are valid before building

## Deployment

The build process generates static files in `dist/` that can be deployed to:
- Static hosting (Netlify, Vercel, GitHub Pages)
- CDN (CloudFlare Pages, AWS S3 + CloudFront)
- Traditional web servers (Apache, Nginx)

## Modern Web Development Practices Used

This project demonstrates industry-standard practices:
- Component-based architecture
- Separation of content and presentation
- Build automation
- Version control friendly structure
- Asset optimization
- Responsive design
- Accessibility considerations

## Browser Compatibility

- Modern browsers with ES6 module support
- Mobile browsers (iOS Safari, Chrome Mobile)
- Graceful degradation for older browsers