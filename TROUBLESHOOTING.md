# Worker Process Issue - Troubleshooting Guide

## Problem Description
The error "brutally killing workers" and matplotlib temporary file cleanup issues typically occur due to:

1. **Multiprocessing conflicts** in Jupyter environments
2. **Improper process cleanup** during shutdown
3. **Matplotlib backend issues** in headless environments
4. **Race conditions** in temporary file management

## Quick Fixes

### 1. Run the Fix Script
```bash
python fix_worker_issue.py
```

### 2. Use Safe Runner
```bash
python safe_runner.py hashtable
python safe_runner.py linkedlist
python safe_runner.py graph
```

### 3. Environment Setup
```bash
# Install requirements
pip install -r requirements.txt

# Set environment variables
set MPLBACKEND=Agg
set PYTHONHASHSEED=0
```

## Detailed Solutions

### For Jupyter Notebook Users:
1. **Restart Kernel**: Kernel → Restart & Clear Output
2. **Add to first cell**:
   ```python
   import matplotlib
   matplotlib.use('Agg')
   import multiprocessing as mp
   mp.set_start_method('spawn', force=True)
   ```

### For VS Code Users:
1. **Restart Python interpreter**
2. **Use integrated terminal** instead of external terminals
3. **Set Python interpreter** to your virtual environment

### For Command Line Users:
1. **Use the safe_runner.py script**
2. **Set proper environment variables**
3. **Avoid Ctrl+C during multiprocessing operations**

## Prevention Tips

1. **Always use proper process cleanup**:
   ```python
   import atexit
   import multiprocessing as mp
   
   def cleanup():
       for p in mp.active_children():
           p.terminate()
           p.join()
   
   atexit.register(cleanup)
   ```

2. **Set matplotlib backend early**:
   ```python
   import matplotlib
   matplotlib.use('Agg')  # Before importing pyplot
   ```

3. **Use context managers** for resource management

4. **Avoid nested multiprocessing** in Jupyter

## If Issues Persist

1. **Clear Python cache**:
   ```bash
   python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
   ```

2. **Clear matplotlib cache**:
   ```bash
   python -c "import matplotlib; print(matplotlib.get_cachedir())"
   # Delete the directory shown
   ```

3. **Reinstall packages**:
   ```bash
   pip uninstall matplotlib multiprocessing
   pip install matplotlib multiprocess
   ```

4. **Use a fresh virtual environment**

## Still Having Issues?

If you continue to see these errors:

1. Share the specific code that triggers the error
2. Mention your environment (Jupyter, VS Code, command line)
3. Include your Python version and OS
4. Try running individual files instead of importing modules

## Testing

Run this to verify the fix:
```bash
python -c "
import multiprocessing as mp
import matplotlib
matplotlib.use('Agg')
print('✓ Configuration successful')
"
```
