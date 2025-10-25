#!/usr/bin/env python3
"""
Demonstration script for the enhanced ObjectSizeComparator.
Shows the new features: float exponential notation, flexible unit assignment.
"""

from main import ObjectSizeComparator

def demo_unit_flexibility():
    """Demonstrate the flexible unit assignment system."""
    print("🔧 UNIT FLEXIBILITY DEMONSTRATION")
    print("=" * 50)
    
    comparator = ObjectSizeComparator()
    
    # Show how the same object can be displayed in different units
    objects_to_demo = ['virus', 'human_hair', 'golf_ball', 'earth', 'sun']
    
    for obj_key in objects_to_demo:
        obj_name = comparator.objects[obj_key]['name']
        size_in_meters = comparator.get_diameter_in_meters(obj_key, 'm')
        
        print(f"\n{obj_name}:")
        print(f"  Auto-format: {comparator.format_size(size_in_meters)}")
        
        # Try different unit representations
        units_to_try = ['nm', 'μm', 'mm', 'm', 'km']
        for unit in units_to_try:
            try:
                formatted = comparator.format_size(size_in_meters, unit)
                print(f"  In {unit:>2}: {formatted}")
            except:
                pass  # Skip if unit doesn't make sense for this magnitude

def demo_exponential_notation():
    """Show the exponential notation in the JSON data."""
    print("\n\n📊 EXPONENTIAL NOTATION IN DATA")
    print("=" * 50)
    
    comparator = ObjectSizeComparator()
    
    print("Sample of raw data values (using exponential notation):")
    sample_objects = ['virus', 'earth', 'sun']
    
    for obj_key in sample_objects:
        obj = comparator.objects[obj_key]
        print(f"\n{obj['name']}:")
        print(f"  diameter_average: {obj['diameter_average']}")
        print(f"  diameter_multiplier: {obj['diameter_multiplier']}")
        print(f"  Calculated size: {comparator.get_diameter_in_meters(obj_key, 'm')} meters")

def demo_custom_comparisons():
    """Demonstrate custom unit specifications in comparisons."""
    print("\n\n🎯 CUSTOM UNIT COMPARISONS")
    print("=" * 50)
    
    comparator = ObjectSizeComparator()
    
    # Example: Compare virus to red blood cell
    print("\n🦠 Virus as Red Blood Cell:")
    comparator.compare_objects('virus', 'red_blood_cell', num_comparisons=5)
    
    # Show what a human hair would look like if Earth was golf ball sized
    print("\n🌍➡️🏌️ Hair in Earth-as-Golf-Ball scale:")
    earth_to_golf_scale = (comparator.get_diameter_in_meters('golf_ball', 'm') / 
                          comparator.get_diameter_in_meters('earth', 'm'))
    hair_size = comparator.get_diameter_in_meters('human_hair', 'm')
    scaled_hair = hair_size * earth_to_golf_scale
    print(f"Human hair would be: {comparator.format_size(scaled_hair)}")

if __name__ == "__main__":
    demo_unit_flexibility()
    demo_exponential_notation()
    demo_custom_comparisons()
    
    print("\n\n✨ SUMMARY OF ENHANCEMENTS")
    print("=" * 50)
    print("✓ Float numbers with exponential notation (e.g., 1.27e7)")
    print("✓ No hardcoded 'unit' field in JSON objects")
    print("✓ Dynamic unit assignment from input arguments")
    print("✓ Flexible display formatting (nm, μm, mm, m, km)")
    print("✓ Automatic unit selection based on magnitude")
    print("✓ Precise floating-point calculations")
    print("✓ Scientific notation for very large/small numbers")
    print("✓ Flat database structure (no categories)")