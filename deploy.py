#!/usr/bin/env python3
"""
Deployment script for the modular CFD website.
Builds from JSON content and deploys to GitHub Pages.
"""
import os
import subprocess
import shutil
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
    print("🔨 Building website...")
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

def deploy_to_github():
    """Deploy to GitHub Pages."""
    print("🚀 Deploying to GitHub...")
    
    # Check if we're in a git repository
    if not Path(".git").exists():
        print("Error: Not in a git repository")
        return False
    
    # Add all changes
    if not run_command("git add ."):
        return False
    
    # Check if there are changes to commit
    result = subprocess.run("git diff --cached --quiet", shell=True)
    if result.returncode == 0:
        print("No changes to commit")
        return True
    
    # Commit changes
    commit_msg = "Update website content and rebuild"
    if not run_command(f'git commit -m "{commit_msg}"'):
        return False
    
    # Push to GitHub
    if not run_command("git push"):
        return False
    
    print("✅ Deployed to GitHub successfully")
    return True

def main():
    """Main deployment workflow."""
    print("🌐 Starting CFD Website Deployment")
    print("=" * 40)
    
    # Build the website
    if not build_website():
        print("❌ Build failed")
        return False
    
    # Deploy to GitHub
    if not deploy_to_github():
        print("❌ Deployment failed")
        return False
    
    print("\n🎉 Deployment completed successfully!")
    print("Your website should be live at GitHub Pages in a few minutes.")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        exit(1)