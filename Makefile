# CFD Website Build System

.PHONY: build serve clean install dev

# Install dependencies
install:
	pip install -r requirements.txt

# Build the website
build:
	python tools/build.py

# Serve the website locally (requires Python 3)
serve:
	cd dist && python -m http.server 8000

# Development mode - build and serve
dev: build serve

# Clean build artifacts
clean:
	rm -rf dist/

# Full rebuild
rebuild: clean build

# Help
help:
	@echo "Available commands:"
	@echo "  install  - Install Python dependencies"
	@echo "  build    - Build the website to dist/"
	@echo "  serve    - Serve the website locally on port 8000"
	@echo "  dev      - Build and serve (development mode)"
	@echo "  clean    - Clean build artifacts"
	@echo "  rebuild  - Clean and build"