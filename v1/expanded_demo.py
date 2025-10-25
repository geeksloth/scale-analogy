#!/usr/bin/env python3
"""
Comprehensive demonstration of expanded metric prefix coverage.
From Planck length (10^-35 m) to Observable Universe (10^26 m).
"""

from main import ObjectSizeComparator

def demo_extreme_scales():
    """Demonstrate the full range of metric prefixes."""
    print("🌌 EXTREME SCALE DEMONSTRATION")
    print("=" * 60)
    
    comparator = ObjectSizeComparator()
    
    # Show objects across the entire scale spectrum
    extreme_objects = [
        'planck_length',
        'proton',
        'hydrogen_atom',
        'virus',
        'human_hair',
        'golf_ball',
        'earth',
        'sun',
        'earth_sun_distance',
        'light_year',
        'milky_way_diameter',
        'observable_universe'
    ]
    
    print("\n📏 Scale Spectrum (smallest to largest):")
    print("-" * 60)
    
    for obj_key in extreme_objects:
        if obj_key in comparator.objects:
            obj_name = comparator.objects[obj_key]['name']
            size_in_meters = comparator.get_diameter_in_meters(obj_key, 'm')
            formatted_size = comparator.format_size(size_in_meters)
            
            print(f"{obj_name:<25}: {formatted_size:>15}")

def demo_all_metric_prefixes():
    """Show examples using all available metric prefixes."""
    print("\n\n🔢 ALL METRIC PREFIXES DEMONSTRATION")
    print("=" * 60)
    
    comparator = ObjectSizeComparator()
    
    # Sample size in meters to convert to different prefixes
    sample_size = 1.0  # 1 meter
    
    # All supported prefixes
    prefixes = [
        'ym', 'zm', 'am', 'fm', 'pm', 'nm', 'μm', 'mm', 'cm', 'dm', 
        'm', 'dam', 'hm', 'km', 'Mm', 'Gm', 'Tm', 'Pm', 'Em', 'Zm', 'Ym'
    ]
    
    print(f"\n1 meter expressed in different prefixes:")
    print("-" * 40)
    
    for prefix in prefixes:
        try:
            formatted = comparator.format_size(sample_size, prefix)
            print(f"{prefix:>3}: {formatted}")
        except Exception as e:
            print(f"{prefix:>3}: Error - {e}")

def demo_scale_comparisons_extreme():
    """Show extreme scale comparisons."""
    print("\n\n⚖️  EXTREME SCALE COMPARISONS")
    print("=" * 60)
    
    comparator = ObjectSizeComparator()
    
    # If Planck length was the size of a proton
    if 'planck_length' in comparator.objects and 'proton' in comparator.objects:
        print("\n🔬 If Planck Length were the size of a Proton:")
        comparator.compare_objects('planck_length', 'proton', num_comparisons=6)
    
    # If Earth was the size of a hydrogen atom
    if 'hydrogen_atom' in comparator.objects:
        print("\n🌍 If Earth were the size of a Hydrogen Atom:")
        comparator.compare_objects('earth', 'hydrogen_atom', num_comparisons=8)
    
    # If Observable Universe was the size of Earth
    if 'observable_universe' in comparator.objects:
        print("\n🌌 If Observable Universe were the size of Earth:")
        comparator.compare_objects('observable_universe', 'earth', num_comparisons=8)

def demo_cosmic_distances():
    """Demonstrate cosmic scale distances with appropriate units."""
    print("\n\n🚀 COSMIC DISTANCE DEMONSTRATIONS")
    print("=" * 60)
    
    comparator = ObjectSizeComparator()
    
    cosmic_objects = [
        'earth_moon_distance',
        'earth_sun_distance', 
        'solar_system_diameter',
        'light_year',
        'milky_way_diameter',
        'observable_universe'
    ]
    
    print("\nCosmic distances in various units:")
    print("-" * 50)
    
    for obj_key in cosmic_objects:
        if obj_key in comparator.objects:
            obj_name = comparator.objects[obj_key]['name']
            size_m = comparator.get_diameter_in_meters(obj_key, 'm')
            
            print(f"\n{obj_name}:")
            print(f"  Auto:  {comparator.format_size(size_m)}")
            print(f"  km:    {comparator.format_size(size_m, 'km')}")
            print(f"  Mm:    {comparator.format_size(size_m, 'Mm')}")
            print(f"  Gm:    {comparator.format_size(size_m, 'Gm')}")
            
            if size_m >= 1e12:  # For very large distances
                print(f"  Tm:    {comparator.format_size(size_m, 'Tm')}")
            if size_m >= 1e15:  # For extremely large distances
                print(f"  Pm:    {comparator.format_size(size_m, 'Pm')}")

def demo_quantum_scale():
    """Demonstrate quantum and subatomic scales."""
    print("\n\n⚛️  QUANTUM SCALE DEMONSTRATIONS")
    print("=" * 60)
    
    comparator = ObjectSizeComparator()
    
    quantum_objects = [
        'planck_length',
        'proton',
        'atomic_nucleus',
        'electron',
        'hydrogen_atom',
        'carbon_atom',
        'dna_helix'
    ]
    
    print("\nQuantum and atomic scales:")
    print("-" * 40)
    
    for obj_key in quantum_objects:
        if obj_key in comparator.objects:
            obj_name = comparator.objects[obj_key]['name']
            size_m = comparator.get_diameter_in_meters(obj_key, 'm')
            
            print(f"\n{obj_name}:")
            print(f"  Auto:  {comparator.format_size(size_m)}")
            print(f"  fm:    {comparator.format_size(size_m, 'fm')}")
            print(f"  pm:    {comparator.format_size(size_m, 'pm')}")
            print(f"  nm:    {comparator.format_size(size_m, 'nm')}")

if __name__ == "__main__":
    demo_extreme_scales()
    demo_all_metric_prefixes() 
    demo_scale_comparisons_extreme()
    demo_cosmic_distances()
    demo_quantum_scale()
    
    print("\n\n✨ EXPANDED METRIC PREFIX COVERAGE")
    print("=" * 60)
    print("Range: 10^-35 meters (Planck length) to 10^26 meters (Observable Universe)")
    print("Prefixes: ym, zm, am, fm, pm, nm, μm, mm, cm, dm, m, dam, hm, km, Mm, Gm, Tm, Pm, Em, Zm, Ym")
    print("Total coverage: 61 orders of magnitude!")
    print("Applications: Quantum physics → Human scale → Cosmic structures")