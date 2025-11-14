# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a modular CFD website for a respiratory engineering consultancy with a JSON-driven content management system. The architecture separates development files from deployed files, using Python build scripts to generate static HTML pages from JSON content.

## Key Commands

### Development Workflow
```bash
# Edit content in JSON
nano dev/src/data/content.json

# Build and test locally (builds, restores CSS fixes, serves on localhost:8000)
python local_test.py

# Deploy to GitHub Pages (builds and pushes)
python deploy.py
```

### Build Only
```bash
# Build from dev directory
cd dev && python tools/build.py
```

### Manual Deployment
```bash
# Manual step-by-step deployment
cd dev && python tools/build.py
git add . && git commit -m "Update content" && git push
```

## Architecture

### Directory Structure
- `dev/src/data/content.json` - Single source of truth for all website content
- `dev/tools/build.py` - WebsiteBuilder class that generates multi-page HTML from JSON
- `local_test.py` - Local development server with build integration and CSS fixes
- `deploy.py` - Automated GitHub Pages deployment script
- Root directory - Generated HTML files served by GitHub Pages

### Build System
The WebsiteBuilder class (`dev/tools/build.py`) generates 5 HTML pages:
- `index.html` - Home with hero section and quick links
- `services.html` - Services grid (must be 2x2 layout)
- `about.html` - About with text and statistics
- `research.html` - Research publications with DOI links
- `contact.html` - Contact form and information

### CSS Architecture
- `styles/components.css` - Main component styles (services grid, navigation, etc.)
- `styles/main.css` - Base styles and variables
- `styles/responsive.css` - Responsive design rules

### Critical CSS Grid Configuration
Services page MUST use `grid-template-columns: repeat(2, 1fr)` for 2x2 layout. The system has a backup mechanism (`styles/components.css.fixed`) that `local_test.py` restores after builds to maintain consistent styling.

## JSON Content Structure

The `content.json` file has these sections:
- `site` - Global metadata (title, description)
- `hero` - Hero section (title, subtitle, CTA)
- `services.items[]` - Array of service objects with title, description, image, icon
- `about` - Paragraphs array and stats array
- `research.papers[]` - Research publications with DOI, abstract, categories
- `contact` - Contact information and form settings

## Important Constraints

### CSS Grid Consistency
When modifying services grid CSS, always use the codebase-consistency-guardian agent to ensure local and remote deployment consistency. The services page must display exactly 4 cards in a 2x2 grid.

### Deployment Pipeline
- Local builds output to root directory for GitHub Pages
- `local_test.py` includes CSS fix restoration mechanism
- Always test locally before deploying to catch layout issues

### Research Publications
When adding research papers, include full metadata: title, authors, journal, year, DOI, abstract, and categories array for proper formatting.

## Special Files

- `styles/components.css.fixed` - Backup CSS with correct grid configuration
- Generated HTML files in root - Never edit directly, always regenerate from JSON