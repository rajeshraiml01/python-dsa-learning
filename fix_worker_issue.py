#!/usr/bin/env python3
"""
Fix for worker process and matplotlib temporary file issues
"""

import os
import sys
import tempfile
import shutil
import matplotlib
import multiprocessing as mp

def fix_matplotlib_backend():
    """Set matplotlib to use a non-interactive backend"""
    matplotlib.use('Agg')  # Use Anti-Grain Geometry backend (no GUI)
    print("✓ Matplotlib backend set to 'Agg'")

def fix_multiprocessing():
    """Configure multiprocessing for better process management"""
    if __name__ == '__main__':
        # Set start method to 'spawn' for better process isolation
        try:
            mp.set_start_method('spawn', force=True)
            print("✓ Multiprocessing start method set to 'spawn'")
        except RuntimeError:
            print("⚠ Multiprocessing start method already set")

def clean_temp_files():
    """Clean up matplotlib temporary files"""
    temp_dir = tempfile.gettempdir()
    matplotlib_dirs = []
    
    for item in os.listdir(temp_dir):
        if item.startswith('matplotlib-'):
            matplotlib_dirs.append(os.path.join(temp_dir, item))
    
    for dir_path in matplotlib_dirs:
        try:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path, ignore_errors=True)
                print(f"✓ Cleaned up: {dir_path}")
        except Exception as e:
            print(f"⚠ Could not clean {dir_path}: {e}")

def setup_environment():
    """Setup environment variables for better process management"""
    # Disable matplotlib font cache rebuilding
    os.environ['MPLBACKEND'] = 'Agg'
    os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()
    
    # Set multiprocessing start method
    os.environ['PYTHONHASHSEED'] = '0'
    
    print("✓ Environment variables configured")

if __name__ == "__main__":
    print("🔧 Fixing worker process issues...")
    
    # Apply fixes
    setup_environment()
    fix_matplotlib_backend()
    fix_multiprocessing()
    clean_temp_files()
    
    print("\n✅ Fixes applied successfully!")
    print("\nRecommendations:")
    print("1. Restart your Python kernel/environment")
    print("2. If using Jupyter, restart the kernel")
    print("3. Run your code again")
