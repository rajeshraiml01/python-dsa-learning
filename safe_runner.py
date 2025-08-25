#!/usr/bin/env python3
"""
Safe execution wrapper for DSA learning code
Prevents worker process issues and handles cleanup properly
"""

import sys
import os
import signal
import atexit
import multiprocessing as mp
from contextlib import contextmanager

class SafeExecutor:
    def __init__(self):
        self.setup_signal_handlers()
        self.setup_multiprocessing()
    
    def setup_signal_handlers(self):
        """Setup proper signal handlers for graceful shutdown"""
        def signal_handler(signum, frame):
            print(f"\n🛑 Received signal {signum}, shutting down gracefully...")
            self.cleanup()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    def setup_multiprocessing(self):
        """Configure multiprocessing for safe execution"""
        try:
            mp.set_start_method('spawn', force=True)
        except RuntimeError:
            pass  # Already set
        
        # Register cleanup function
        atexit.register(self.cleanup)
    
    def cleanup(self):
        """Clean up resources and processes"""
        try:
            # Terminate any remaining child processes
            current_process = mp.current_process()
            for child in mp.active_children():
                child.terminate()
                child.join(timeout=1)
                if child.is_alive():
                    child.kill()
            print("✓ Cleaned up child processes")
        except Exception as e:
            print(f"⚠ Cleanup warning: {e}")
    
    @contextmanager
    def safe_execution(self):
        """Context manager for safe code execution"""
        try:
            yield
        except KeyboardInterrupt:
            print("\n🛑 Execution interrupted by user")
        except Exception as e:
            print(f"\n❌ Error during execution: {e}")
        finally:
            self.cleanup()

def run_dsa_code(module_name):
    """Safely run DSA code modules"""
    executor = SafeExecutor()
    
    with executor.safe_execution():
        if module_name == "hashtable":
            from dsa.hashtable import *
        elif module_name == "linkedlist":
            from dsa.linkedlist import *
        elif module_name == "graph":
            from dsa.graph import *
        elif module_name == "heap":
            from dsa.Heap import *
        elif module_name == "recursion":
            from dsa.recursion import *
        elif module_name == "findduplicate":
            from leetcode.findduplicate import *
        elif module_name == "identifynumber":
            from leetcode.identifynumber import *
        else:
            print(f"❌ Unknown module: {module_name}")
            print("Available modules: hashtable, linkedlist, graph, heap, recursion, findduplicate, identifynumber")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        module_name = sys.argv[1]
        print(f"🚀 Running {module_name} safely...")
        run_dsa_code(module_name)
    else:
        print("Usage: python safe_runner.py <module_name>")
        print("Available modules: hashtable, linkedlist, graph, heap, recursion, findduplicate, identifynumber")
