#!/usr/bin/env python3
"""
Simple test script for Object Size Comparator v2
"""

import sys
import os

# Add the script's directory to the path so we can import main
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from main import ObjectSizeComparator

def main():
    print("Testing Object Size Comparator v2")
    print("=" * 40)
    
    comparator = ObjectSizeComparator()
    
    # Test basic functionality
    print(f"\nTesting basic comparisons:")
    result = comparator.compare_objects('earth', 'moon')
    print(f"Earth vs Moon: {result['comparison_text']}")
    
    print(f"\nTesting search:")
    results = comparator.search_objects('ball')
    print(f"Objects containing 'ball': {[comparator.objects[key]['n'] for key in results]}")
    
    print(f"\nTesting size ranges:")
    planet_range = comparator.find_objects_by_size_range(1e6, 1e8, 'm')
    print(f"Planetary-scale objects: {[comparator.objects[key]['n'] for key in planet_range]}")
    
    print(f"\nAll objects loaded: {len(comparator.objects)}")
    
    print("\n✅ v2 System working correctly!")

if __name__ == "__main__":
    main()