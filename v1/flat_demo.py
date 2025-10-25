#!/usr/bin/env python3
"""
Demonstration of the flat database structure.
Shows how objects are now stored without categories for simplified access.
"""

from main import ObjectSizeComparator

def demo_flat_structure():
    """Demonstrate the flat database structure benefits."""
    print("📦 FLAT DATABASE STRUCTURE DEMONSTRATION")
    print("=" * 55)
    
    comparator = ObjectSizeComparator()
    
    print(f"\n✨ Simple Access: All {len(comparator.objects)} objects in one dictionary")
    print("-" * 55)
    
    # Show direct access without categories
    print("\n🔍 Direct object access examples:")
    sample_objects = ['planck_length', 'virus', 'earth', 'observable_universe']
    
    for obj_key in sample_objects:
        if obj_key in comparator.objects:
            obj = comparator.objects[obj_key]
            size = comparator.get_diameter_in_meters(obj_key, 'm')
            print(f"  {obj_key}: {obj['name']} = {comparator.format_size(size)}")
    
    print("\n📊 All objects sorted by size:")
    print("-" * 35)
    
    # Sort all objects by size
    sorted_objects = sorted(
        comparator.objects.items(),
        key=lambda x: comparator.get_diameter_in_meters(x[0], 'm')
    )
    
    for i, (obj_key, obj_data) in enumerate(sorted_objects):
        size = comparator.get_diameter_in_meters(obj_key, 'm')
        print(f"{i+1:2d}. {obj_data['name']:<25}: {comparator.format_size(size):>12}")

def demo_search_and_filter():
    """Demonstrate easy searching and filtering with flat structure."""
    print("\n\n🔎 SEARCH & FILTER DEMONSTRATION")
    print("=" * 45)
    
    comparator = ObjectSizeComparator()
    
    # Example: Find all objects with "atom" in the name
    print("\n🔬 Objects with 'atom' in name:")
    atom_objects = {k: v for k, v in comparator.objects.items() 
                   if 'atom' in v['name'].lower()}
    
    for obj_key, obj_data in atom_objects.items():
        size = comparator.get_diameter_in_meters(obj_key, 'm')
        print(f"  • {obj_data['name']}: {comparator.format_size(size)}")
    
    # Example: Find objects in a size range
    print("\n📏 Objects between 1 mm and 1 m:")
    size_range_objects = {}
    
    for obj_key, obj_data in comparator.objects.items():
        size = comparator.get_diameter_in_meters(obj_key, 'm')
        if 1e-3 <= size <= 1.0:  # Between 1 mm and 1 m
            size_range_objects[obj_key] = obj_data
    
    for obj_key, obj_data in size_range_objects.items():
        size = comparator.get_diameter_in_meters(obj_key, 'm')
        print(f"  • {obj_data['name']}: {comparator.format_size(size)}")
    
    # Example: Find objects by description keywords
    print("\n🌌 Objects with 'distance' in description:")
    distance_objects = {k: v for k, v in comparator.objects.items() 
                       if 'distance' in v['description'].lower()}
    
    for obj_key, obj_data in distance_objects.items():
        size = comparator.get_diameter_in_meters(obj_key, 'm')
        print(f"  • {obj_data['name']}: {comparator.format_size(size)}")

def demo_advantages():
    """Show advantages of flat structure."""
    print("\n\n⚡ FLAT STRUCTURE ADVANTAGES")
    print("=" * 40)
    
    print("\n✅ Benefits:")
    print("• Simpler JSON structure")
    print("• Direct object access: objects['earth']")
    print("• No nested loops needed")
    print("• Easier to search and filter")
    print("• More flexible data operations")
    print("• Reduced code complexity")
    print("• Better performance for lookups")
    
    print("\n🔧 Code Simplification:")
    print("Before (categorized):")
    print("  for category in data:")
    print("    for obj_key in data[category]:")
    print("      # process object")
    print()
    print("After (flat):")
    print("  for obj_key in objects:")
    print("    # process object")
    
    print("\n💡 Use Cases:")
    print("• Random object selection")
    print("• Size-based sorting")
    print("• Name/description searching")
    print("• Range filtering")
    print("• Statistical analysis")

if __name__ == "__main__":
    demo_flat_structure()
    demo_search_and_filter()
    demo_advantages()
    
    print("\n\n🎉 FLAT DATABASE STRUCTURE")
    print("=" * 35)
    print("✓ All objects in single dictionary")
    print("✓ Direct access without categories")
    print("✓ Simplified code structure")
    print("✓ Enhanced search capabilities")
    print("✓ Better performance")
    print("✓ More maintainable")
    print("\nReady for efficient object comparisons! 🚀")