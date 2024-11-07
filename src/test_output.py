"""Test script to verify Python execution and output"""
import sys
import time

def main():
    print("Starting test script...", flush=True)
    for i in range(5):
        print(f"Test output {i}", flush=True)
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    main()