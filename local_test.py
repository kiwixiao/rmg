#!/usr/bin/env python3
"""
Local test script for the modular CFD website.
Builds and serves the website locally for testing before deployment.
"""
import os
import subprocess
import time
import webbrowser
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running command: {cmd}")
            print(f"Error output: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Exception running command {cmd}: {e}")
        return False

def build_website():
    """Build the website from JSON content."""
    print("🔨 Building website for local testing...")
    dev_dir = Path("dev")
    if not dev_dir.exists():
        print("Error: dev/ directory not found")
        return False
    
    build_script = dev_dir / "tools" / "build.py"
    if not build_script.exists():
        print("Error: build script not found at dev/tools/build.py")
        return False
    
    # Run build from dev directory
    if not run_command("python tools/build.py", cwd=dev_dir):
        return False
    
    print("✅ Website built successfully")
    return True

def serve_locally():
    """Start local HTTP server from docs directory."""
    print("🌐 Starting local server...")
    print("📍 Website will be available at: http://localhost:8000")
    print("🔄 Press Ctrl+C to stop the server")
    print("=" * 50)

    # Try to open browser automatically
    try:
        webbrowser.open('http://localhost:8000')
        print("🌍 Opening browser automatically...")
    except:
        print("💡 Manually open: http://localhost:8000")

    # Start server from docs directory
    try:
        subprocess.run(["python", "-m", "http.server", "8000"],
                      cwd="docs",
                      check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
    except Exception as e:
        print(f"Error starting server: {e}")

def main():
    """Main local test workflow."""
    print("🧪 CFD Website Local Testing")
    print("=" * 30)
    
    # Build the website
    if not build_website():
        print("❌ Build failed")
        return False
    
    # Restore fixed CSS after build
    if Path("docs/styles/components.css.fixed").exists():
        if not run_command("cp docs/styles/components.css.fixed docs/styles/components.css"):
            print("⚠️  Warning: Could not restore CSS fix")
        else:
            print("✅ Restored CSS fix for 2x2 services grid")
    
    print("\n🎯 Local testing workflow:")
    print("1. Website built from dev/src/data/content.json and MD files")
    print("2. Generated files are in the docs/ directory")
    print("3. Your modular dev/ structure is preserved")
    print("4. When ready to deploy, run: python deploy.py")
    print()

    # Start local server from docs directory
    serve_locally()
    
    return True

if __name__ == "__main__":
    main()