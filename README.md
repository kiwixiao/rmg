# CFD Website - Modular Development Workflow

A modern, modular website for Respiratory Airflow Modelling consultancy with easy content management through JSON files.

## Quick Start

### 1. Edit Content
Edit the JSON file to update website content:
```bash
# Edit the main content file
nano dev/src/data/content.json
```

### 2. Build & Deploy
Run the deployment script to build and push to GitHub Pages:
```bash
python deploy.py
```

That's it! Your website will be updated automatically.

## Project Structure

```
website/
├── dev/                          # Development files
│   ├── src/data/content.json    # Main content configuration
│   └── tools/build.py           # Build script
├── deploy.py                     # Automated deployment script
├── index.html                    # Generated website (GitHub Pages serves this)
└── styles/                      # CSS files (copied from build)
```

## Manual Workflow

If you prefer step-by-step control:

1. **Edit content**: Modify `dev/src/data/content.json`
2. **Build**: `cd dev && python tools/build.py`
3. **Deploy**: `git add . && git commit -m "Update content" && git push`

## Content Structure

The `content.json` file contains all website content:

- `site`: Global site information (title, description)
- `hero`: Hero section content (title, subtitle, CTA)
- `services`: Services section with array of service items
- `about`: About section with paragraphs and statistics
- `contact`: Contact information and form settings

## Development Notes

- The build system generates a complete HTML file from the JSON data
- GitHub Pages automatically serves the built files
- Asset paths are optimized for GitHub Pages deployment
- The deployment script handles git operations automatically