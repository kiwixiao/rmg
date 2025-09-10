# CFD Website - Modular Static Site

A modern, modular static website for CFD consultancy services. Built with a component-based architecture for easy maintenance and content updates.

## 🏗️ Architecture

```
src/
├── components/          # Reusable HTML components
├── templates/           # Base HTML templates
├── styles/             # Modular CSS files
├── scripts/            # JavaScript modules
├── data/               # JSON configuration and content
├── content/            # Markdown content files
└── assets/             # Images, icons, documents

tools/                  # Build tools
dist/                   # Generated website (build output)
```

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   make install
   ```

2. **Build the website:**
   ```bash
   make build
   ```

3. **Serve locally:**
   ```bash
   make serve
   ```
   Then open http://localhost:8000

4. **Development mode (build + serve):**
   ```bash
   make dev
   ```

## 📝 Content Management

### Easy Content Updates

1. **Update text content:** Edit `src/data/content.json`
2. **Change site configuration:** Edit `src/data/site-config.json`
3. **Add blog posts:** Create markdown files in `src/content/blog/`
4. **Update images:** Place images in `src/assets/images/` and reference in JSON

### Example: Updating Hero Section

Edit `src/data/content.json`:
```json
{
  "hero": {
    "title": "Your New Title",
    "subtitle": "Your new description",
    "background_image": "assets/images/new-hero.jpg"
  }
}
```

Then run `make build` to regenerate the site.

## 🎨 Styling

- **CSS Variables:** Global design tokens in `src/styles/variables.css`
- **Base Styles:** Typography and layout in `src/styles/base.css`
- **Components:** Component-specific styles in `src/styles/components.css`
- **Responsive:** Mobile styles in `src/styles/responsive.css`

## 🔧 Modern Web Development Practices

This structure follows industry standards:

### ✅ What We Use (Modern Best Practices)

1. **Component-Based Architecture**
   - Reusable HTML components
   - Modular CSS organization
   - JavaScript ES6 modules

2. **Content as Data**
   - JSON for structured content
   - Markdown for blog posts
   - Separation of content and presentation

3. **Build Process**
   - Simple Python-based static site generator
   - Asset optimization and copying
   - Template engine for dynamic content

4. **Version Control Friendly**
   - Separate content from code
   - Easy to track changes
   - Team collaboration friendly

### 🌟 Real-World Alternatives

**For larger projects, consider:**

1. **Static Site Generators:**
   - **Next.js** (React-based, most popular)
   - **Gatsby** (React + GraphQL)
   - **Hugo** (Go-based, very fast)
   - **Jekyll** (Ruby-based, GitHub Pages)

2. **Headless CMS:**
   - **Strapi** (open-source)
   - **Contentful** (cloud-based)
   - **Sanity** (developer-friendly)
   - **Ghost** (blogging-focused)

3. **Full-Stack Frameworks:**
   - **Next.js** with headless CMS
   - **Nuxt.js** (Vue-based)
   - **SvelteKit** (Svelte-based)

## 📁 File Organization Benefits

### ✅ Advantages of This Structure

1. **Easy Updates:** Change JSON files → rebuild → done
2. **Team Friendly:** Designers can edit JSON, developers handle templates
3. **Scalable:** Add new components and pages easily
4. **Maintainable:** Clear separation of concerns
5. **Version Control:** Track content changes separately from code

### 🔄 Workflow for Content Updates

1. **Content Team:** Updates JSON files and adds images
2. **Build Process:** Runs automatically (can be automated with GitHub Actions)
3. **Deployment:** Generated HTML/CSS/JS deployed to hosting

## 🚀 Deployment Options

- **Static Hosting:** Netlify, Vercel, GitHub Pages
- **CDN:** CloudFlare Pages, AWS S3 + CloudFront
- **Traditional:** Any web server (Apache, Nginx)

## 🛠️ Available Commands

```bash
make install   # Install dependencies
make build     # Build website to dist/
make serve     # Serve locally on port 8000
make dev       # Build and serve
make clean     # Clean build artifacts
make rebuild   # Clean and rebuild
```

## 🔧 Customization

### Adding New Sections

1. Create component in `src/components/new-section.html`
2. Add styles in `src/styles/components.css`
3. Add data structure in `src/data/content.json`
4. Update build process in `tools/build.py`

### Adding New Pages

1. Create template in `src/templates/`
2. Update build script to generate new page
3. Add navigation links in `src/data/site-config.json`

This structure provides the perfect balance of simplicity and scalability for modern web development!