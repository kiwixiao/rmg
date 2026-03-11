# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a modular CFD website for a respiratory engineering consultancy with a JSON-driven content management system. The architecture separates development files from deployed files, using Python build scripts to generate static HTML pages from JSON content.

## Key Commands

### Development Workflow
```bash
# Edit content in JSON or Markdown
nano dev/src/data/content.json
nano dev/src/data/content/services.md

# Build and test locally (builds HTML, serves on localhost:8000)
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

### Two-Folder Separation Pattern

**dev/** = Content management (what you edit)
- `dev/src/data/content.json` - Structured data (services, research papers, stats)
- `dev/src/data/content/*.md` - Markdown files for easy text editing (homepage, services, about, research, contact)
- `dev/tools/build.py` - WebsiteBuilder class that generates HTML from JSON + Markdown

**docs/** = Deployed website (what GitHub Pages serves)
- `docs/*.html` - Generated HTML pages (index, services, about, research, contact)
- `docs/styles/` - Static CSS files (never generated, manually maintained)
- `docs/scripts/` - Static JavaScript files (never generated, manually maintained)
- `docs/assets/` - Static media files (videos, images)

### Build System

The WebsiteBuilder class (`dev/tools/build.py`) generates 5 HTML pages:
- `index.html` - Home with hero section and quick links
- `services.html` - Services grid (2x2 layout with 4 service cards)
- `about.html` - About with text and statistics
- `research.html` - Research publications with DOI links
- `contact.html` - Contact form and information

**Key insight:** Only HTML is generated from dev/. CSS, JavaScript, and media files are static and live in docs/.

### What Gets Generated vs Static

| File Type | Generated? | Location | Edited Where |
|-----------|------------|----------|--------------|
| HTML (*.html) | ✅ Yes | docs/ | dev/src/data/ |
| CSS (*.css) | ❌ No | docs/styles/ | docs/styles/ |
| JavaScript (*.js) | ❌ No | docs/scripts/ | docs/scripts/ |
| Videos/Images | ❌ No | docs/assets/ | docs/assets/ |

## JSON + Markdown Content Structure

### content.json Structure
- `site` - Global metadata (title, description)
- `hero` - Hero section (title, subtitle, CTA) - text comes from homepage.md
- `services.items[]` - Array of service objects with title, icon, video/image paths - descriptions come from services.md
- `about` - Paragraphs array (from about.md) and stats array
- `research.papers[]` - Research publications with DOI, abstract, categories - page text from research.md
- `contact` - Contact information and form settings - page text from contact.md

### Markdown Files
The build script (`build.py`) loads Markdown files from `dev/src/data/content/`:
- `homepage.md` - Parsed by headers ("# Main Title", "# Subtitle")
- `services.md` - Parsed by headers ("# Page Title", "# Service 1: ...", etc.)
- `about.md` - Split by double newlines into paragraphs
- `research.md` - Parsed by headers ("# Page Title", "# Page Subtitle")
- `contact.md` - Parsed by headers ("# Page Title", "# Page Subtitle")

## Important Constraints

### Content Changes (Edit dev/)
When changing page text, service descriptions, or research papers:
1. Edit files in `dev/src/data/` (JSON or Markdown)
2. Run `python deploy.py` to rebuild HTML and deploy

### Design Changes (Edit docs/)
When changing colors, panel sizes, layouts, or styling:
1. Edit CSS files in `docs/styles/` directly
2. Run `python deploy.py` to deploy (no rebuild needed)

### Media Changes (Edit docs/)
When adding videos or images:
1. Add files to `docs/assets/videos/` or `docs/assets/images/`
2. Update `dev/src/data/content.json` to reference new files
3. Run `python deploy.py` to rebuild HTML and deploy

### CSS Panel Size Configuration
**Current settings in `docs/styles/components.css`:**
- Services grid: 1200px max-width, 2x2 layout (`grid-template-columns: repeat(2, 1fr)`)
- Service cards: 550px height
- Video/image containers: 300px height
- Videos use `object-fit: contain` to prevent distortion

These are permanent defaults - no backup/restore mechanism needed.

## Deployment Pipeline

### local_test.py Workflow
1. Runs `dev/tools/build.py` (generates HTML to docs/)
2. Starts HTTP server from `docs/` folder on port 8000
3. Opens browser to `http://localhost:8000`
4. Shows exactly what GitHub Pages will show

### deploy.py Workflow
1. Runs `dev/tools/build.py` (generates HTML to docs/)
2. `git add .` (stages all changes including HTML, CSS, videos, etc.)
3. `git commit -m "Update website content and rebuild"`
4. `git push` (pushes to GitHub)
5. GitHub Pages automatically deploys from docs/ folder

## Research Publications

When adding research papers to `content.json`, include full metadata:
- `title` - Full paper title
- `authors` - Author names (e.g., "Last, F; Last2, F")
- `journal` - Journal name
- `year` - Publication year
- `doi` - DOI identifier (e.g., "10.1234/example")
- `abstract` - Brief abstract
- `categories` - Array of category tags (e.g., ["CFD", "Clinical Applications"])
- `pdf_link` - Optional direct PDF link

## Service Videos

Videos in `docs/assets/videos/` are referenced in `content.json`:
```json
{
  "services": {
    "items": [
      {
        "title": "Service Name",
        "video": "assets/videos/service-video.mp4",
        "description": ""  // Filled from services.md
      }
    ]
  }
}
```

Videos use HTML5 `<video>` tags with `autoplay loop muted playsinline` attributes.
