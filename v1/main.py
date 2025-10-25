import json
import math
from typing import Dict, List, Tuple, Optional

class ObjectSizeComparator:
    def __init__(self, json_file_path: str = "objects.json"):
        """Initialize the comparator with object data from JSON file."""
        with open(json_file_path, 'r') as file:
            self.objects = json.load(file)
    
    def assign_unit_from_magnitude(self, diameter_meters: float, 
                                  preferred_unit: str = None) -> Tuple[float, str]:
        """
        Assign appropriate unit based on magnitude or use preferred unit.
        Supports full range of metric prefixes from yocto (10^-24) to yotta (10^24).
        
        Args:
            diameter_meters: Diameter value in meters
            preferred_unit: Optional preferred unit (e.g., 'nm', 'μm', 'Gm', 'Tm')
        
        Returns:
            Tuple of (converted_value, unit_string)
        """
        # Complete metric prefix conversion table
        unit_conversions = {
            # Small units (negative powers of 10)
            'ym': (1e24, 'ym'),    # yoctometer (10^-24)
            'zm': (1e21, 'zm'),    # zeptometer (10^-21)
            'am': (1e18, 'am'),    # attometer (10^-18)
            'fm': (1e15, 'fm'),    # femtometer (10^-15)
            'pm': (1e12, 'pm'),    # picometer (10^-12)
            'nm': (1e9, 'nm'),     # nanometer (10^-9)
            'μm': (1e6, 'μm'),     # micrometer (10^-6)
            'um': (1e6, 'μm'),     # micrometer (alternative)
            'mm': (1e3, 'mm'),     # millimeter (10^-3)
            'cm': (1e2, 'cm'),     # centimeter (10^-2)
            'dm': (1e1, 'dm'),     # decimeter (10^-1)
            
            # Base unit
            'm': (1.0, 'm'),       # meter (10^0)
            
            # Large units (positive powers of 10)
            'dam': (1e-1, 'dam'),  # decameter (10^1)
            'hm': (1e-2, 'hm'),    # hectometer (10^2)
            'km': (1e-3, 'km'),    # kilometer (10^3)
            'Mm': (1e-6, 'Mm'),    # megameter (10^6)
            'Gm': (1e-9, 'Gm'),    # gigameter (10^9)
            'Tm': (1e-12, 'Tm'),   # terameter (10^12)
            'Pm': (1e-15, 'Pm'),   # petameter (10^15)
            'Em': (1e-18, 'Em'),   # exameter (10^18)
            'Zm': (1e-21, 'Zm'),   # zettameter (10^21)
            'Ym': (1e-24, 'Ym'),   # yottameter (10^24)
        }
        
        if preferred_unit and preferred_unit in unit_conversions:
            multiplier, unit = unit_conversions[preferred_unit]
            return diameter_meters * multiplier, unit
        
        # Auto-assign based on magnitude with expanded ranges
        if diameter_meters < 1e-21:      # Less than 1 zm
            return diameter_meters * 1e24, 'ym'
        elif diameter_meters < 1e-18:    # Less than 1 am
            return diameter_meters * 1e21, 'zm'
        elif diameter_meters < 1e-15:    # Less than 1 fm
            return diameter_meters * 1e18, 'am'
        elif diameter_meters < 1e-12:    # Less than 1 pm
            return diameter_meters * 1e15, 'fm'
        elif diameter_meters < 1e-9:     # Less than 1 nm
            return diameter_meters * 1e12, 'pm'
        elif diameter_meters < 1e-6:     # Less than 1 μm
            return diameter_meters * 1e9, 'nm'
        elif diameter_meters < 1e-3:     # Less than 1 mm
            return diameter_meters * 1e6, 'μm'
        elif diameter_meters < 1e-2:     # Less than 1 cm
            return diameter_meters * 1e3, 'mm'
        elif diameter_meters < 1e-1:     # Less than 1 dm
            return diameter_meters * 1e2, 'cm'
        elif diameter_meters < 1.0:      # Less than 1 m
            return diameter_meters * 1e1, 'dm'
        elif diameter_meters < 1e1:      # Less than 1 dam
            return diameter_meters, 'm'
        elif diameter_meters < 1e2:      # Less than 1 hm
            return diameter_meters * 1e-1, 'dam'
        elif diameter_meters < 1e3:      # Less than 1 km
            return diameter_meters * 1e-2, 'hm'
        elif diameter_meters < 1e6:      # Less than 1 Mm
            return diameter_meters * 1e-3, 'km'
        elif diameter_meters < 1e9:      # Less than 1 Gm
            return diameter_meters * 1e-6, 'Mm'
        elif diameter_meters < 1e12:     # Less than 1 Tm
            return diameter_meters * 1e-9, 'Gm'
        elif diameter_meters < 1e15:     # Less than 1 Pm
            return diameter_meters * 1e-12, 'Tm'
        elif diameter_meters < 1e18:     # Less than 1 Em
            return diameter_meters * 1e-15, 'Pm'
        elif diameter_meters < 1e21:     # Less than 1 Zm
            return diameter_meters * 1e-18, 'Em'
        elif diameter_meters < 1e24:     # Less than 1 Ym
            return diameter_meters * 1e-21, 'Zm'
        else:                            # 1 Ym or more
            return diameter_meters * 1e-24, 'Ym'
    
    def get_diameter_in_meters(self, obj_key: str, base_unit: str = 'm') -> float:
        """
        Get object diameter in meters, with option to specify the base unit 
        the data is stored in. Now supports full metric prefix range.
        
        Args:
            obj_key: Key of the object in the database
            base_unit: Unit that the stored values are in (supports all metric prefixes)
        
        Returns:
            Diameter in meters
        """
        obj = self.objects[obj_key]
        diameter = obj['diameter_average']
        multiplier = obj.get('diameter_multiplier', 1.0)
        
        # Apply multiplier first
        actual_diameter = diameter * multiplier
        
        # Extended unit conversion table to meters
        unit_to_meters = {
            # Extremely small units
            'ym': 1e-24,    # yoctometer
            'zm': 1e-21,    # zeptometer
            'am': 1e-18,    # attometer
            'fm': 1e-15,    # femtometer
            'pm': 1e-12,    # picometer
            
            # Common small units
            'nm': 1e-9,     # nanometer
            'μm': 1e-6,     # micrometer
            'um': 1e-6,     # micrometer (alternative)
            'mm': 1e-3,     # millimeter
            'cm': 1e-2,     # centimeter
            'dm': 1e-1,     # decimeter
            
            # Base unit
            'm': 1.0,       # meter
            
            # Large units
            'dam': 1e1,     # decameter
            'hm': 1e2,      # hectometer
            'km': 1e3,      # kilometer
            'Mm': 1e6,      # megameter
            'Gm': 1e9,      # gigameter
            'Tm': 1e12,     # terameter
            'Pm': 1e15,     # petameter
            'Em': 1e18,     # exameter
            'Zm': 1e21,     # zettameter
            'Ym': 1e24,     # yottameter
        }
        
        if base_unit in unit_to_meters:
            return actual_diameter * unit_to_meters[base_unit]
        else:
            raise ValueError(f"Unknown base unit: {base_unit}. Supported units: {', '.join(unit_to_meters.keys())}")
    
    def determine_base_unit_from_magnitude(self, obj_key: str) -> str:
        """
        Determine the most likely base unit for stored data based on magnitude.
        This helps maintain backward compatibility and sensible defaults.
        """
        obj = self.objects[obj_key]
        diameter = obj['diameter_average']
        
        # Use heuristics based on typical object sizes and scientific notation
        if diameter < 1e-4:  # Very small values, likely in meters already
            return 'm'
        elif diameter < 1.0:  # Small values, could be meters or mm
            # Check if it's a celestial object (would be in meters)
            if any(keyword in obj['name'].lower() for keyword in ['earth', 'sun', 'moon', 'mars', 'venus', 'mercury', 'jupiter']):
                return 'm'
            else:
                return 'm'  # Default to meters for consistency
        elif diameter < 1000:  # Medium values
            return 'm'
        else:  # Large values
            return 'm'
    
    def find_best_comparison(self, target_object: str, reference_object: str, 
                           exclude_objects: Optional[List[str]] = None,
                           target_unit: str = 'm', reference_unit: str = 'm') -> List[Tuple[str, float, str]]:
        """
        Find objects that would be good size comparisons when scaling target to reference size.
        
        Args:
            target_object: The object to scale (e.g., 'earth')
            reference_object: What to scale it to (e.g., 'golf_ball')
            exclude_objects: Objects to exclude from comparison results
            target_unit: Base unit for target object data
            reference_unit: Base unit for reference object data
        
        Returns:
            List of tuples: (object_name, scaled_size_in_meters, description)
        """
        if exclude_objects is None:
            exclude_objects = []
        
        target_diameter = self.get_diameter_in_meters(target_object, target_unit)
        reference_diameter = self.get_diameter_in_meters(reference_object, reference_unit)
        
        # Calculate scale factor
        scale_factor = reference_diameter / target_diameter
        
        comparisons = []
        
        for obj_key, obj_data in self.objects.items():
            if obj_key in exclude_objects or obj_key == target_object:
                continue
            
            # Determine appropriate base unit for each object
            obj_unit = self.determine_base_unit_from_magnitude(obj_key)
            original_diameter = self.get_diameter_in_meters(obj_key, obj_unit)
            scaled_diameter = original_diameter * scale_factor
            
            comparisons.append((
                obj_data['name'],
                scaled_diameter,
                obj_data['description'],
                obj_key
            ))
        
        # Sort by scaled diameter for easier interpretation
        comparisons.sort(key=lambda x: x[1])
        
        return comparisons
    
    def format_size(self, size_in_meters: float, preferred_unit: str = None) -> str:
        """
        Format size in appropriate units for readability.
        
        Args:
            size_in_meters: Size value in meters
            preferred_unit: Optional preferred unit for display
        
        Returns:
            Formatted string with value and unit
        """
        value, unit = self.assign_unit_from_magnitude(size_in_meters, preferred_unit)
        
        # Format with appropriate precision
        if value >= 1000:
            return f"{value:.2e} {unit}"
        elif value >= 100:
            return f"{value:.1f} {unit}"
        elif value >= 10:
            return f"{value:.2f} {unit}"
        else:
            return f"{value:.3f} {unit}"
    
    def compare_objects(self, target_object: str, reference_object: str, 
                       num_comparisons: int = 10, target_unit: str = 'm', 
                       reference_unit: str = 'm') -> None:
        """
        Print a comparison showing what other objects would be like 
        if target_object was scaled to reference_object size.
        
        Args:
            target_object: Object to scale
            reference_object: Reference size object
            num_comparisons: Number of comparisons to show
            target_unit: Base unit for target object
            reference_unit: Base unit for reference object
        """
        target_name = self.objects[target_object]['name']
        reference_name = self.objects[reference_object]['name']
        
        print(f"\n🔍 If {target_name} were the size of a {reference_name}:")
        print("=" * 60)
        
        comparisons = self.find_best_comparison(
            target_object, 
            reference_object, 
            exclude_objects=[reference_object],
            target_unit=target_unit,
            reference_unit=reference_unit
        )
        
        # Show the reference size
        ref_size = self.get_diameter_in_meters(reference_object, reference_unit)
        print(f"📏 {reference_name}: {self.format_size(ref_size)}")
        print(f"📏 {target_name} (scaled): {self.format_size(ref_size)}")
        print()
        
        # Show comparisons
        count = 0
        for name, scaled_size, description, obj_key in comparisons:
            if count >= num_comparisons:
                break
            
            print(f"• {name}: {self.format_size(scaled_size)}")
            count += 1
    
    def create_scale_analogy(self, obj1: str, obj2: str, obj3: str,
                           obj1_unit: str = 'm', obj2_unit: str = 'm', 
                           obj3_unit: str = 'm') -> None:
        """
        Create an analogy: if obj1 is to obj2, then obj3 is to what?
        
        Args:
            obj1, obj2, obj3: Object keys for the analogy
            obj1_unit, obj2_unit, obj3_unit: Base units for each object
        """
        size1 = self.get_diameter_in_meters(obj1, obj1_unit)
        size2 = self.get_diameter_in_meters(obj2, obj2_unit)
        size3 = self.get_diameter_in_meters(obj3, obj3_unit)
        
        # Calculate the ratio
        ratio = size2 / size1
        result_size = size3 * ratio
        
        # Find the closest object to the result size
        best_match = None
        min_ratio_diff = float('inf')
        
        for obj_key, obj_data in self.objects.items():
            obj_unit = self.determine_base_unit_from_magnitude(obj_key)
            obj_size = self.get_diameter_in_meters(obj_key, obj_unit)
            ratio_diff = abs(obj_size - result_size) / result_size
            
            if ratio_diff < min_ratio_diff:
                min_ratio_diff = ratio_diff
                best_match = (obj_key, obj_data['name'], obj_size)
        
        name1 = self.objects[obj1]['name']
        name2 = self.objects[obj2]['name']
        name3 = self.objects[obj3]['name']
        
        print(f"\n🔗 Scale Analogy:")
        print(f"{name1} is to {name2}")
        print(f"as {name3} is to {best_match[1]}")
        print()
        print(f"Ratio: {ratio:.2e}")
        print(f"Expected size: {self.format_size(result_size)}")
        print(f"Closest match: {self.format_size(best_match[2])} (difference: {min_ratio_diff*100:.1f}%)")

def main():
    """Example usage of the ObjectSizeComparator with enhanced unit handling."""
    comparator = ObjectSizeComparator()
    
    # Example 1: If Earth was the size of a golf ball, what would other things be?
    print("🌍 EARTH AS A GOLF BALL")
    comparator.compare_objects('earth', 'golf_ball', num_comparisons=8)
    
    # Let's calculate some interesting specific examples
    earth_diameter = comparator.get_diameter_in_meters('earth')
    golf_ball_diameter = comparator.get_diameter_in_meters('golf_ball')
    scale_factor = golf_ball_diameter / earth_diameter
    
    # Calculate what Sun would be at this scale
    sun_diameter = comparator.get_diameter_in_meters('sun')
    sun_scaled = sun_diameter * scale_factor
    
    moon_diameter = comparator.get_diameter_in_meters('moon')
    moon_scaled = moon_diameter * scale_factor
    
    print(f"\n🌟 Specific Examples (Earth = golf ball scale):")
    print(f"• Sun would be: {comparator.format_size(sun_scaled)}")
    print(f"• Moon would be: {comparator.format_size(moon_scaled)}")
    
    # Example 2: More reasonable scale - Earth as basketball
    print("\n" + "="*60)
    print("🌍 EARTH AS A BASKETBALL")
    comparator.compare_objects('earth', 'basketball', num_comparisons=8)
    
    # Calculate specific examples for this scale
    basketball_diameter = comparator.get_diameter_in_meters('basketball')
    scale_factor2 = basketball_diameter / earth_diameter
    
    sun_scaled2 = sun_diameter * scale_factor2
    moon_scaled2 = moon_diameter * scale_factor2
    
    print(f"\n🌟 Specific Examples (Earth = basketball scale):")
    print(f"• Sun would be: {comparator.format_size(sun_scaled2)}")
    print(f"• Moon would be: {comparator.format_size(moon_scaled2)}")
    
    # Example 3: Show the actual analogy working
    print("\n" + "="*60)
    print("🔗 SCALE ANALOGIES")
    
    # If Earth is to golf ball, then Sun is to what?
    ratio = golf_ball_diameter / earth_diameter
    sun_scaled_size = sun_diameter * ratio
    print(f"\nIf Earth ({comparator.format_size(earth_diameter)}) = Golf Ball ({comparator.format_size(golf_ball_diameter)})")
    print(f"Then Sun ({comparator.format_size(sun_diameter)}) = {comparator.format_size(sun_scaled_size)}")
    
    # Find what object is closest to this size
    best_match = None
    min_diff = float('inf')
    for obj_key, obj_data in comparator.objects.items():
        obj_unit = comparator.determine_base_unit_from_magnitude(obj_key)
        obj_size = comparator.get_diameter_in_meters(obj_key, obj_unit)
        diff = abs(obj_size - sun_scaled_size)
        if diff < min_diff and obj_key != 'sun':
            min_diff = diff
            best_match = (obj_key, obj_data['name'], obj_size)
    
    if best_match:
        print(f"Closest object: {best_match[1]} ({comparator.format_size(best_match[2])})")
    
    # Example 4: Demonstrate unit flexibility
    print("\n" + "="*60)
    print("� UNIT FLEXIBILITY EXAMPLES")
    print("="*60)
    
    # Show different unit representations for the same object
    earth_size_m = comparator.get_diameter_in_meters('earth', 'm')
    print(f"\nEarth diameter representations:")
    print(f"• In meters: {comparator.format_size(earth_size_m, 'm')}")
    print(f"• In kilometers: {comparator.format_size(earth_size_m, 'km')}")
    print(f"• Auto-format: {comparator.format_size(earth_size_m)}")
    
    virus_size = comparator.get_diameter_in_meters('virus', 'm')
    print(f"\nVirus diameter representations:")
    print(f"• In meters: {comparator.format_size(virus_size, 'm')}")
    print(f"• In micrometers: {comparator.format_size(virus_size, 'μm')}")
    print(f"• In nanometers: {comparator.format_size(virus_size, 'nm')}")
    print(f"• Auto-format: {comparator.format_size(virus_size)}")
    
    print("\n" + "="*60)
    print(" AVAILABLE OBJECTS")
    print("="*60)
    
    # Sort objects by size for better organization
    sorted_objects = sorted(
        comparator.objects.items(), 
        key=lambda x: comparator.get_diameter_in_meters(x[0], 'm')
    )
    
    print(f"\nAll objects (sorted by size, smallest to largest):")
    for obj_key, obj_data in sorted_objects:
        obj_unit = comparator.determine_base_unit_from_magnitude(obj_key)
        size = comparator.get_diameter_in_meters(obj_key, obj_unit)
        print(f"  • {obj_data['name']}: {comparator.format_size(size)}")
    
    # Fun additional examples
    print("\n" + "="*60)
    print("🎯 MORE FUN COMPARISONS")
    print("="*60)
    
    # If Moon was a tennis ball
    print("\n🌙 MOON AS A TENNIS BALL")
    comparator.compare_objects('moon', 'tennis_ball', num_comparisons=6)

if __name__ == "__main__":
    main()