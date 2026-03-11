# Respiratory System Modeling Consultancy Website

A modular static website for respiratory engineering research and services, powered by a JSON-driven content management system with GitHub Pages deployment.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Making Changes](#making-changes)
- [Testing & Deployment](#testing--deployment)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [FAQ](#faq)

## Project Overview

This website separates **content management** (dev/) from **deployed website** (docs/), making it easy to:

- Edit content in simple JSON and Markdown files
- Generate HTML pages automatically
- Test locally before deploying
- Deploy to GitHub Pages with one command

**Live website:** [GitHub Pages URL]

## Architecture

```
┌─────────────────────────────────────────────────┐
│ CONTENT SOURCE (dev/)                           │
│ - JSON data (services, research papers, etc.)  │
│ - Markdown text (page content)                  │
│ - Build script (converts to HTML)               │
└─────────────────────────────────────────────────┘
                      ↓
         python dev/tools/build.py
                      ↓
┌─────────────────────────────────────────────────┐
│ DEPLOYED WEBSITE (docs/)                        │
│ - Generated HTML pages                          │
│ - Static CSS styling                            │
│ - Static JavaScript                             │
│ - Media files (videos, images)                  │
└─────────────────────────────────────────────────┘
                      ↓
         GitHub Pages serves docs/
                      ↓
         Live website visitors see
```

### Key Concept

- **dev/** = Content management (what to say)
- **docs/** = Deployed website (how it looks)
- **Build process** = Converts content → HTML

## Getting Started

### Prerequisites

- Python 3.x
- Git
- Web browser

### Quick Start

1. **Clone the repository**
   ```bash
   git clone [your-repo-url]
   cd website
   ```

2. **Test locally**
   ```bash
   python local_test.py
   ```
   Opens browser to `http://localhost:8000`

3. **Make changes** (see [Making Changes](#making-changes))

4. **Deploy to GitHub Pages**
   ```bash
   python deploy.py
   ```

## Making Changes

### Content Changes (Edit dev/)

**What:** Page text, service descriptions, research papers, contact info

**Where to edit:** `dev/src/data/`

#### Change Page Text

Edit Markdown files in `dev/src/data/content/`:

```bash
# Edit homepage hero text
nano dev/src/data/content/homepage.md

# Edit service descriptions
nano dev/src/data/content/services.md

# Edit about page content
nano dev/src/data/content/about.md

# Edit research page content
nano dev/src/data/content/research.md

# Edit contact page content
nano dev/src/data/content/contact.md
```

#### Add/Edit Services or Research Papers

Edit `dev/src/data/content.json`:

```bash
nano dev/src/data/content.json
```

**Example: Add a new service**
```json
{
  "services": {
    "items": [
      {
        "title": "New Service Name",
        "description": "Service description here",
        "icon": "🎯",
        "video": "assets/videos/new-service.mp4"
      }
    ]
  }
}
```

**Example: Add a research paper**
```json
{
  "research": {
    "papers": [
      {
        "title": "Paper Title",
        "authors": "Author Names",
        "journal": "Journal Name",
        "year": "2024",
        "doi": "10.1234/example",
        "abstract": "Paper abstract...",
        "categories": ["CFD", "Research Area"]
      }
    ]
  }
}
```

**Then deploy:**
```bash
python deploy.py
```

### Design Changes (Edit docs/)

**What:** Colors, sizes, layouts, fonts, styling

**Where to edit:** `docs/styles/`

#### Change Panel Sizes

Edit `docs/styles/components.css`:

```css
/* Service grid container */
.services-grid {
    max-width: 1200px;  /* Change grid width */
}

/* Individual service cards */
.service-card {
    height: 550px;  /* Change card height */
}

/* Video/image containers */
.service-video,
.service-image {
    height: 300px;  /* Change media height */
}
```

#### Change Colors

Edit `docs/styles/main.css`:

```css
:root {
    --primary-color: #2563eb;    /* Main brand color */
    --secondary-color: #7c3aed;  /* Accent color */
    --text-dark: #1f2937;        /* Text color */
}
```

**Then deploy:**
```bash
python deploy.py
```

### Media Changes (Edit docs/)

**What:** Videos, images

**Where to edit:** `docs/assets/`

#### Add New Video

1. **Add video file:**
   ```bash
   cp new-video.mp4 docs/assets/videos/
   ```

2. **Reference in content.json:**
   ```json
   {
     "services": {
       "items": [
         {
           "video": "assets/videos/new-video.mp4"
         }
       ]
     }
   }
   ```

3. **Deploy:**
   ```bash
   python deploy.py
   ```

#### Add New Image

```bash
cp new-image.png docs/assets/images/
```

Reference it in your content as needed.

### JavaScript Changes (Edit docs/)

**What:** Interactive behavior, animations, menu functionality

**Where to edit:** `docs/scripts/main.js`

```bash
nano docs/scripts/main.js
```

Then deploy:
```bash
python deploy.py
```

## Testing & Deployment

### Local Testing

**Test before deploying to see exactly what visitors will see:**

```bash
python local_test.py
```

**What it does:**
1. Runs the build process (generates HTML from dev/)
2. Starts local web server on port 8000
3. Opens browser to `http://localhost:8000`
4. Shows EXACTLY what GitHub Pages will show

**Stop the server:** Press `Ctrl+C`

### Deployment to GitHub Pages

**Deploy changes to live website:**

```bash
python deploy.py
```

**What it does:**
1. Runs the build process
2. Stages all changes (`git add .`)
3. Creates commit ("Update website content and rebuild")
4. Pushes to GitHub (`git push`)
5. GitHub Pages automatically updates (takes 1-2 minutes)

**Important:** Always test locally first with `python local_test.py`

## Project Structure

```
website/
├── dev/                              # Content source (what you edit)
│   ├── src/data/
│   │   ├── content.json             # Structured data
│   │   └── content/                 # Markdown content
│   │       ├── homepage.md          # Hero section text
│   │       ├── services.md          # Service descriptions
│   │       ├── about.md             # About page content
│   │       ├── research.md          # Research page content
│   │       └── contact.md           # Contact page content
│   └── tools/
│       └── build.py                 # HTML generator script
│
├── docs/                             # Deployed website (GitHub Pages)
│   ├── index.html                   # Generated: Home page
│   ├── services.html                # Generated: Services page
│   ├── about.html                   # Generated: About page
│   ├── research.html                # Generated: Research page
│   ├── contact.html                 # Generated: Contact page
│   ├── styles/                      # Static: CSS styling
│   │   ├── main.css                 # Base styles, colors, variables
│   │   ├── components.css           # Component styles (cards, grid, etc.)
│   │   └── responsive.css           # Mobile/tablet responsiveness
│   ├── scripts/                     # Static: JavaScript
│   │   └── main.js                  # Interactive functionality
│   └── assets/                      # Static: Media files
│       ├── videos/                  # MP4 video files
│       │   ├── airway-modeling.mp4
│       │   ├── drug-delivery.mp4
│       │   ├── inhaler-device.mp4
│       │   └── flow-visualization.mp4
│       └── images/                  # PNG/JPG image files
│           ├── airway-modeling.png
│           ├── drug-delivery.png
│           ├── inhaler-device.png
│           └── flow-visulization.png
│
├── local_test.py                    # Test locally before deploying
├── deploy.py                        # Deploy to GitHub Pages
└── README.md                        # This file
```

### What Gets Generated vs What's Static

| File Type | Generated | Static | Location |
|-----------|-----------|--------|----------|
| HTML pages (*.html) | ✅ Yes | ❌ No | docs/ |
| CSS styling (*.css) | ❌ No | ✅ Yes | docs/styles/ |
| JavaScript (*.js) | ❌ No | ✅ Yes | docs/scripts/ |
| Videos (*.mp4) | ❌ No | ✅ Yes | docs/assets/videos/ |
| Images (*.png, *.jpg) | ❌ No | ✅ Yes | docs/assets/images/ |

**Key insight:** Only HTML is generated from dev/. Everything else is manually maintained in docs/.

## How It Works

### Build Process (build.py)

The build script converts content → HTML:

```python
# 1. Load content from dev/src/data/
content = load_content_from_json_and_markdown()

# 2. Generate HTML pages
for page in ['index', 'services', 'about', 'research', 'contact']:
    html = generate_page_html(content, page)
    write_to_file(f'../docs/{page}.html', html)

# 3. Done! HTML files ready in docs/
```

### Local Test Workflow (local_test.py)

```python
# 1. Build the website
run_build_script()

# 2. Start web server from docs/ folder
start_server(directory='docs', port=8000)

# 3. Open browser
open_browser('http://localhost:8000')
```

### Deploy Workflow (deploy.py)

```python
# 1. Build the website
run_build_script()

# 2. Git operations
git_add_all_changes()
git_commit('Update website content and rebuild')
git_push_to_github()

# 3. GitHub Pages automatically deploys
```

### GitHub Pages Hosting

GitHub Pages serves the `docs/` folder as a static website:

```
GitHub Repository docs/ folder
              ↓
   GitHub Pages builds site
              ↓
   https://[username].github.io/[repo]/
              ↓
        Live website
```

## FAQ

### Why separate dev/ and docs/ folders?

**Answer:** Clean separation of concerns:
- `dev/` = Content management (easy to edit JSON/Markdown)
- `docs/` = Deployed website (complete working website)
- Makes editing content much easier than editing raw HTML

### Do I need to run build.py manually?

**Answer:** No! Both `local_test.py` and `deploy.py` run the build automatically.

### What if I only change CSS/JS/media files?

**Answer:** Just run `python deploy.py` - it will deploy the changes without regenerating HTML.

### How do I see my changes before deploying?

**Answer:** Run `python local_test.py` to test locally first.

### Why do videos/images live in docs/ not dev/?

**Answer:** Media files are static assets that don't need to be "generated" - they're used as-is by the website. The dev/ folder is only for content that gets converted to HTML.

### Can I edit HTML directly in docs/?

**Answer:** Not recommended! HTML files are regenerated from dev/ content, so direct edits will be overwritten. Instead:
- Content changes → Edit dev/
- Design changes → Edit docs/styles/
- Behavior changes → Edit docs/scripts/

### How long does GitHub Pages take to update?

**Answer:** Usually 1-2 minutes after pushing. Check the "Actions" tab in your GitHub repository to see deployment status.

### What's the CSS panel size configuration?

**Current settings in `docs/styles/components.css`:**
- Services grid: 1200px max-width, 2x2 layout
- Service cards: 550px height
- Video/image containers: 300px height
- Videos use `object-fit: contain` to prevent distortion

### How do I add a new page?

**Answer:** You'll need to modify `dev/tools/build.py` to add a new page template and generation logic. This requires Python knowledge. For most use cases, the existing 5 pages are sufficient.

## Quick Reference

### Common Commands

```bash
# Test locally
python local_test.py

# Deploy to GitHub Pages
python deploy.py

# Build only (without deploying)
cd dev && python tools/build.py

# Check git status
git status

# Stop local server
Ctrl+C
```

### Common Edits

```bash
# Change homepage text
nano dev/src/data/content/homepage.md

# Add research paper
nano dev/src/data/content.json

# Change colors
nano docs/styles/main.css

# Change panel sizes
nano docs/styles/components.css

# Add video
cp video.mp4 docs/assets/videos/
nano dev/src/data/content.json
```

### Workflow Summary

```
Edit content → Test locally → Deploy
     ↓              ↓            ↓
   nano         local_test    deploy.py
```

---

**Questions or issues?** Check the FAQ section above or review the code in `dev/tools/build.py` to understand the build process.
