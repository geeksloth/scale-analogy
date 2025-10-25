#!/usr/bin/env python3
"""
Enhanced Object Size Comparator - v2 Efficient Format
A tool for comparing sizes of objects across many orders of magnitude.

This version uses the efficient JSON format with shortened field names and metadata.
Focuses on scale analogies to help understand relative sizes through proportional
relationships between familiar and unfamiliar objects.

Features:
- Comprehensive metric prefix support (21 prefixes, 61 orders of magnitude)
- Efficient JSON format with metadata tracking
- Advanced scale analogy generation and analysis
- Professional scientific formatting and presentation
- Cross-scale relationship discovery
"""

import json
import os
from typing import Optional, List, Tuple

class ObjectSizeComparator:
    """
    A comprehensive tool for comparing sizes of objects across the universe.
    
    This class provides methods for scale analysis, proportional relationships,
    and size comparisons spanning from quantum particles to cosmic structures.
    
    Features:
    - Support for 21 metric prefixes (yoctometer to yottameter)
    - Efficient JSON data format with metadata
    - Advanced scale analogy generation
    - Professional scientific formatting
    - Cross-domain size relationship analysis
    
    The database covers 61 orders of magnitude, from Planck length (10^-35 m)
    to the observable universe (10^26 m).
    """
    
    def __init__(self, json_file: str = 'objects.json'):
        """
        Initialize the comparator with object data from JSON file.
        
        Args:
            json_file: Path to the JSON file containing object data
        """
        # If json_file is just a filename (no path), look for it in the script's directory
        if not os.path.dirname(json_file):
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.json_file = os.path.join(script_dir, json_file)
        else:
            self.json_file = json_file
            
        self.metadata = {}
        self.objects = {}
        self.load_data()
    
    def load_data(self):
        """Load object data from JSON file."""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Load metadata
            self.metadata = data.get('_metadata', {})
            
            # Load objects - handle both flat structure and nested under "objects" key
            if 'objects' in data:
                self.objects = data['objects']
            else:
                # Flat structure (exclude metadata)
                self.objects = {k: v for k, v in data.items() if not k.startswith('_')}
            
            print(f"Loaded {len(self.objects)} objects from {self.json_file}")
            if self.metadata:
                print(f"Database version: {self.metadata.get('version', 'unknown')}")
                
        except FileNotFoundError:
            print(f"Error: Could not find {self.json_file}")
            self.objects = {}
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {self.json_file}: {e}")
            self.objects = {}
    
    def get_object_diameter(self, obj_key: str) -> float:
        """Get the diameter of an object, handling range values."""
        if obj_key not in self.objects:
            raise ValueError(f"Object '{obj_key}' not found in database")
        
        obj = self.objects[obj_key]
        diameter = obj['d']  # 'd' is the new field name for diameter
        
        # Handle range values
        if 'r' in obj:  # 'r' is the new field name for range
            range_vals = obj['r']
            # Use average of min and max
            diameter = (range_vals[0] + range_vals[1]) / 2
            
        return diameter
    
    def get_object_range(self, obj_key: str) -> tuple[float, float]:
        """Get the diameter range of an object."""
        if obj_key not in self.objects:
            raise ValueError(f"Object '{obj_key}' not found in database")
        
        obj = self.objects[obj_key]
        diameter = obj['d']
        
        if 'r' in obj:
            range_vals = obj['r']
            return (range_vals[0], range_vals[1])
        else:
            # No range specified, return the diameter as both min and max
            return (diameter, diameter)
    
    def search_objects(self, query: str) -> list[str]:
        """Search for objects by name or description."""
        query = query.lower()
        matching_objects = []
        
        for obj_key, obj_data in self.objects.items():
            # Search in name
            if query in obj_data['n'].lower():  # 'n' is the new field name for name
                matching_objects.append(obj_key)
                continue
            
            # Search in description if it exists
            if 'desc' in obj_data and query in obj_data['desc'].lower():
                matching_objects.append(obj_key)
                continue
        
        return matching_objects
    
    def filter_by_tags(self, tags: list[str]) -> list[str]:
        """Filter objects by tags."""
        if not tags:
            return list(self.objects.keys())
        
        matching_objects = []
        for obj_key, obj_data in self.objects.items():
            obj_tags = obj_data.get('tags', [])
            if any(tag in obj_tags for tag in tags):
                matching_objects.append(obj_key)
        
        return matching_objects
    
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
        diameter = self.get_object_diameter(obj_key)
        
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
            return diameter * unit_to_meters[base_unit]
        else:
            raise ValueError(f"Unknown base unit: {base_unit}. Supported units: {', '.join(unit_to_meters.keys())}")
    
    def assign_unit_from_magnitude(self, diameter_meters: float) -> tuple[float, str]:
        """
        Assign the most appropriate unit based on the magnitude of the diameter in meters.
        Returns a tuple of (value, unit) where the value is adjusted to the chosen unit.
        
        Args:
            diameter_meters: Diameter value in meters
            
        Returns:
            Tuple of (adjusted_value, unit_symbol)
        """
        # Map units from smallest to largest with their conversion factors from meters
        units = [
            (1e-24, 'ym'),   # yoctometer
            (1e-21, 'zm'),   # zeptometer
            (1e-18, 'am'),   # attometer
            (1e-15, 'fm'),   # femtometer
            (1e-12, 'pm'),   # picometer
            (1e-9,  'nm'),   # nanometer
            (1e-6,  'μm'),   # micrometer
            (1e-3,  'mm'),   # millimeter
            (1e-2,  'cm'),   # centimeter
            (1e-1,  'dm'),   # decimeter
            (1.0,   'm'),    # meter
            (1e1,   'dam'),  # decameter
            (1e2,   'hm'),   # hectometer
            (1e3,   'km'),   # kilometer
            (1e6,   'Mm'),   # megameter
            (1e9,   'Gm'),   # gigameter
            (1e12,  'Tm'),   # terameter
            (1e15,  'Pm'),   # petameter
            (1e18,  'Em'),   # exameter
            (1e21,  'Zm'),   # zettameter
            (1e24,  'Ym'),   # yottameter
        ]
        
        # Find the best unit (largest unit where the value would be >= 1)
        best_unit = units[0]  # Default to smallest unit
        for factor, unit in units:
            value_in_unit = diameter_meters / factor
            if value_in_unit >= 1.0:
                best_unit = (factor, unit)
            else:
                break
        
        factor, unit = best_unit
        adjusted_value = diameter_meters / factor
        
        return adjusted_value, unit
    
    def format_size(self, obj_key: str, precision: int = 3, base_unit: str = None) -> str:
        """
        Format the size of an object with appropriate units and precision.
        
        Args:
            obj_key: Key of the object in the database
            precision: Number of significant figures
            base_unit: Optional base unit override (if None, uses optimal unit)
            
        Returns:
            Formatted string like "1.23 km"
        """
        # Get diameter in meters
        diameter_meters = self.get_diameter_in_meters(obj_key, 'm')
        
        if base_unit:
            # Use specified unit
            unit_factors = {
                'ym': 1e-24, 'zm': 1e-21, 'am': 1e-18, 'fm': 1e-15, 'pm': 1e-12,
                'nm': 1e-9, 'μm': 1e-6, 'um': 1e-6, 'mm': 1e-3, 'cm': 1e-2,
                'dm': 1e-1, 'm': 1.0, 'dam': 1e1, 'hm': 1e2, 'km': 1e3,
                'Mm': 1e6, 'Gm': 1e9, 'Tm': 1e12, 'Pm': 1e15, 'Em': 1e18,
                'Zm': 1e21, 'Ym': 1e24
            }
            
            if base_unit not in unit_factors:
                raise ValueError(f"Unknown unit: {base_unit}")
            
            value = diameter_meters / unit_factors[base_unit]
            unit = base_unit
        else:
            # Auto-select best unit
            value, unit = self.assign_unit_from_magnitude(diameter_meters)
        
        # Format with specified precision
        if precision <= 0:
            formatted_value = f"{value:.0f}"
        else:
            # Use scientific notation for very small or very large numbers
            if abs(value) < 0.01 or abs(value) >= 10000:
                formatted_value = f"{value:.{precision-1}e}"
            else:
                formatted_value = f"{value:.{precision-1}f}".rstrip('0').rstrip('.')
        
        return f"{formatted_value} {unit}"
    
    def format_size_value(self, size_in_meters: float, preferred_unit: str = None) -> str:
        """
        Format a size value in meters with appropriate units for readability.
        
        Args:
            size_in_meters: Size value in meters
            preferred_unit: Optional preferred unit for display
        
        Returns:
            Formatted string with value and unit
        """
        if preferred_unit:
            unit_factors = {
                'ym': 1e-24, 'zm': 1e-21, 'am': 1e-18, 'fm': 1e-15, 'pm': 1e-12,
                'nm': 1e-9, 'μm': 1e-6, 'um': 1e-6, 'mm': 1e-3, 'cm': 1e-2,
                'dm': 1e-1, 'm': 1.0, 'dam': 1e1, 'hm': 1e2, 'km': 1e3,
                'Mm': 1e6, 'Gm': 1e9, 'Tm': 1e12, 'Pm': 1e15, 'Em': 1e18,
                'Zm': 1e21, 'Ym': 1e24
            }
            
            if preferred_unit in unit_factors:
                value = size_in_meters / unit_factors[preferred_unit]
                unit = preferred_unit
            else:
                value, unit = self.assign_unit_from_magnitude(size_in_meters)
        else:
            value, unit = self.assign_unit_from_magnitude(size_in_meters)
        
        # Format with appropriate precision
        if value >= 1000:
            return f"{value:.2e} {unit}"
        elif value >= 100:
            return f"{value:.1f} {unit}"
        elif value >= 10:
            return f"{value:.2f} {unit}"
        else:
            return f"{value:.3f} {unit}"
    
    def compare_objects(self, obj_key1: str, obj_key2: str) -> dict:
        """
        Compare two objects and return detailed comparison information.
        
        Args:
            obj_key1: Key of the first object
            obj_key2: Key of the second object
            
        Returns:
            Dictionary with comparison details
        """
        # Get diameters in meters
        diameter1 = self.get_diameter_in_meters(obj_key1)
        diameter2 = self.get_diameter_in_meters(obj_key2)
        
        # Calculate ratio
        if diameter2 != 0:
            ratio = diameter1 / diameter2
        else:
            ratio = float('inf')
        
        # Determine which is larger
        if diameter1 > diameter2:
            larger_obj = obj_key1
            smaller_obj = obj_key2
            size_ratio = ratio
        elif diameter2 > diameter1:
            larger_obj = obj_key2
            smaller_obj = obj_key1
            size_ratio = 1 / ratio
        else:
            larger_obj = smaller_obj = None
            size_ratio = 1.0
        
        return {
            'object1': {
                'key': obj_key1,
                'name': self.objects[obj_key1]['n'],
                'diameter_meters': diameter1,
                'formatted_size': self.format_size(obj_key1)
            },
            'object2': {
                'key': obj_key2,
                'name': self.objects[obj_key2]['n'],
                'diameter_meters': diameter2,
                'formatted_size': self.format_size(obj_key2)
            },
            'ratio': ratio,
            'larger_object': larger_obj,
            'smaller_object': smaller_obj,
            'size_ratio': size_ratio,
            'comparison_text': self._generate_comparison_text(obj_key1, obj_key2, ratio)
        }
    
    def _generate_comparison_text(self, obj_key1: str, obj_key2: str, ratio: float) -> str:
        """Generate human-readable comparison text."""
        name1 = self.objects[obj_key1]['n']
        name2 = self.objects[obj_key2]['n']
        
        if ratio > 1:
            if ratio < 2:
                return f"{name1} is {ratio:.2f} times larger than {name2}"
            elif ratio < 1000:
                return f"{name1} is {ratio:.1f} times larger than {name2}"
            else:
                return f"{name1} is {ratio:.2e} times larger than {name2}"
        elif ratio < 1:
            inverse_ratio = 1 / ratio
            if inverse_ratio < 2:
                return f"{name2} is {inverse_ratio:.2f} times larger than {name1}"
            elif inverse_ratio < 1000:
                return f"{name2} is {inverse_ratio:.1f} times larger than {name1}"
            else:
                return f"{name2} is {inverse_ratio:.2e} times larger than {name1}"
        else:
            return f"{name1} and {name2} are the same size"
    
    def find_objects_by_size_range(self, min_meters: float, max_meters: float, 
                                   base_unit: str = 'm') -> list[str]:
        """
        Find all objects within a given size range.
        
        Args:
            min_meters: Minimum diameter in meters
            max_meters: Maximum diameter in meters
            base_unit: Unit for the min/max values (converted to meters)
            
        Returns:
            List of object keys within the range
        """
        # Convert min/max to meters if needed
        unit_factors = {
            'ym': 1e-24, 'zm': 1e-21, 'am': 1e-18, 'fm': 1e-15, 'pm': 1e-12,
            'nm': 1e-9, 'μm': 1e-6, 'um': 1e-6, 'mm': 1e-3, 'cm': 1e-2,
            'dm': 1e-1, 'm': 1.0, 'dam': 1e1, 'hm': 1e2, 'km': 1e3,
            'Mm': 1e6, 'Gm': 1e9, 'Tm': 1e12, 'Pm': 1e15, 'Em': 1e18,
            'Zm': 1e21, 'Ym': 1e24
        }
        
        if base_unit in unit_factors:
            min_meters_actual = min_meters * unit_factors[base_unit]
            max_meters_actual = max_meters * unit_factors[base_unit]
        else:
            raise ValueError(f"Unknown unit: {base_unit}")
        
        matching_objects = []
        for obj_key in self.objects:
            diameter = self.get_diameter_in_meters(obj_key)
            if min_meters_actual <= diameter <= max_meters_actual:
                matching_objects.append(obj_key)
        
        return matching_objects
    
    def list_all_objects(self) -> list[dict]:
        """
        Get a list of all objects with their basic information.
        
        Returns:
            List of dictionaries with object information
        """
        object_list = []
        for obj_key, obj_data in self.objects.items():
            object_list.append({
                'key': obj_key,
                'name': obj_data['n'],
                'diameter_meters': self.get_diameter_in_meters(obj_key),
                'formatted_size': self.format_size(obj_key),
                'description': obj_data.get('desc', ''),
                'tags': obj_data.get('tags', [])
            })
        
        return object_list
    
    def find_best_comparison(self, target_object: str, reference_object: str, 
                           exclude_objects: Optional[List[str]] = None) -> List[Tuple[str, float, str]]:
        """
        Find objects that would be good size comparisons when scaling target to reference size.
        
        Args:
            target_object: The object to scale (e.g., 'earth')
            reference_object: What to scale it to (e.g., 'golf_ball')
            exclude_objects: Objects to exclude from comparison results
        
        Returns:
            List of tuples: (object_name, scaled_size_in_meters, description)
        """
        if exclude_objects is None:
            exclude_objects = []
        
        target_diameter = self.get_diameter_in_meters(target_object)
        reference_diameter = self.get_diameter_in_meters(reference_object)
        
        # Calculate scale factor
        scale_factor = reference_diameter / target_diameter
        
        comparisons = []
        
        for obj_key, obj_data in self.objects.items():
            if obj_key in exclude_objects or obj_key == target_object:
                continue
            
            original_diameter = self.get_diameter_in_meters(obj_key)
            scaled_diameter = original_diameter * scale_factor
            
            comparisons.append((
                obj_data['n'],
                scaled_diameter,
                obj_data.get('desc', ''),
                obj_key
            ))
        
        # Sort by scaled diameter for easier interpretation
        comparisons.sort(key=lambda x: x[1])
        
        return comparisons
    
    def display_comparison(self, target_object: str, reference_object: str, 
                          num_comparisons: int = 10) -> None:
        """
        Print a comparison showing what other objects would be like 
        if target_object was scaled to reference_object size.
        
        Args:
            target_object: Object to scale
            reference_object: Reference size object
            num_comparisons: Number of comparisons to show
        """
        target_name = self.objects[target_object]['n']
        reference_name = self.objects[reference_object]['n']
        
        print(f"\nIf {target_name} were the size of a {reference_name}:")
        print("=" * 60)
        
        comparisons = self.find_best_comparison(
            target_object, 
            reference_object, 
            exclude_objects=[reference_object]
        )
        
        # Show the reference size
        ref_size = self.get_diameter_in_meters(reference_object)
        print(f"Reference: {reference_name}: {self.format_size_value(ref_size)}")
        print(f"Scaled: {target_name} (scaled): {self.format_size_value(ref_size)}")
        print()
        
        # Show comparisons
        count = 0
        for name, scaled_size, description, obj_key in comparisons:
            if count >= num_comparisons:
                break
            
            print(f"- {name}: {self.format_size_value(scaled_size)}")
            count += 1
    
    def create_scale_analogy(self, obj1: str, obj2: str, obj3: str) -> dict:
        """
        Create an analogy: if obj1 is to obj2, then obj3 is to what?
        
        Args:
            obj1, obj2, obj3: Object keys for the analogy
            
        Returns:
            Dictionary with analogy information
        """
        size1 = self.get_diameter_in_meters(obj1)
        size2 = self.get_diameter_in_meters(obj2)
        size3 = self.get_diameter_in_meters(obj3)
        
        # Calculate the ratio
        ratio = size2 / size1
        result_size = size3 * ratio
        
        # Find the closest object to the result size
        best_match = None
        min_ratio_diff = float('inf')
        
        for obj_key, obj_data in self.objects.items():
            if obj_key == obj3:  # Skip the reference object
                continue
            obj_size = self.get_diameter_in_meters(obj_key)
            ratio_diff = abs(obj_size - result_size) / result_size
            
            if ratio_diff < min_ratio_diff:
                min_ratio_diff = ratio_diff
                best_match = (obj_key, obj_data['n'], obj_size)
        
        name1 = self.objects[obj1]['n']
        name2 = self.objects[obj2]['n']
        name3 = self.objects[obj3]['n']
        
        return {
            'obj1': {'key': obj1, 'name': name1, 'size': size1},
            'obj2': {'key': obj2, 'name': name2, 'size': size2},
            'obj3': {'key': obj3, 'name': name3, 'size': size3},
            'ratio': ratio,
            'expected_size': result_size,
            'best_match': {
                'key': best_match[0] if best_match else None,
                'name': best_match[1] if best_match else 'No match found',
                'size': best_match[2] if best_match else 0,
                'accuracy': min_ratio_diff
            }
        }
    
    def display_scale_analogy(self, obj1: str, obj2: str, obj3: str) -> None:
        """
        Display a scale analogy in a formatted way.
        
        Args:
            obj1, obj2, obj3: Object keys for the analogy
        """
        analogy = self.create_scale_analogy(obj1, obj2, obj3)
        
        print(f"\nScale Analogy:")
        print(f"   {analogy['obj1']['name']} is to {analogy['obj2']['name']}")
        print(f"   as {analogy['obj3']['name']} is to {analogy['best_match']['name']}")
        print()
        print(f"Object Sizes:")
        print(f"   - {analogy['obj1']['name']}: {self.format_size_value(analogy['obj1']['size'])}")
        print(f"   - {analogy['obj2']['name']}: {self.format_size_value(analogy['obj2']['size'])}")
        print(f"   - {analogy['obj3']['name']}: {self.format_size_value(analogy['obj3']['size'])}")
        print(f"   - {analogy['best_match']['name']}: {self.format_size_value(analogy['best_match']['size'])}")
        print()
        print(f"Scale Factor: {analogy['ratio']:.2e}")
        print(f"Expected Size: {self.format_size_value(analogy['expected_size'])}")
        print(f"Match Accuracy: {100-analogy['best_match']['accuracy']*100:.1f}%")
    
    def find_interesting_analogies(self) -> List[Tuple[str, str, str, str]]:
        """
        Find a collection of interesting scale analogies automatically.
        
        Returns:
            List of tuples: (obj1, obj2, obj3, description)
        """
        analogies = [
            # Quantum to everyday
            ('planck_length', 'atom_hydrogen', 'virus', "Quantum scale to atomic to biological"),
            ('atom_hydrogen', 'virus', 'human_hair', "Atomic to biological to visible"),
            ('virus', 'red_blood_cell', 'golf_ball', "Microscopic to everyday objects"),
            
            # Everyday to astronomical
            ('golf_ball', 'earth', 'sun', "Sports equipment to planetary to stellar"),
            ('tennis_ball', 'moon', 'jupiter', "Ball to moon to gas giant"),
            ('basketball', 'earth', 'solar_system', "Court to planet to solar system"),
            
            # Biological scales
            ('red_blood_cell', 'human_hair', 'blue_whale', "Cellular to hair to largest animal"),
            ('dna_helix', 'virus', 'mount_everest', "Molecular to microscopic to geographic"),
            
            # Geographic to cosmic
            ('mount_everest', 'earth', 'milky_way_galaxy', "Mountain to planet to galaxy"),
            ('earth', 'solar_system', 'observable_universe', "Planet to solar system to cosmos"),
            
            # Cross-scale relationships
            ('proton', 'soccer_ball', 'light_year', "Subatomic to sports to interstellar"),
            ('atom_carbon', 'basketball', 'sun', "Atomic to sports to stellar"),
        ]
        
        # Filter to only include analogies where all objects exist
        valid_analogies = []
        for obj1, obj2, obj3, desc in analogies:
            if all(obj in self.objects for obj in [obj1, obj2, obj3]):
                valid_analogies.append((obj1, obj2, obj3, desc))
        
        return valid_analogies

def main():
    """
    Scale Analogies Explorer - Understanding Size Through Relationships
    
    This script focuses on scale analogies to help understand the relative sizes
    of objects across the universe, from quantum to cosmic scales.
    """
    print("SCALE ANALOGIES EXPLORER")
    print("=" * 60)
    print("Understanding size through proportional relationships")
    print("From quantum particles to cosmic structures")
    print("=" * 60)
    
    comparator = ObjectSizeComparator()
    
    # Introduction to scale analogies
    print(f"\nWhat are Scale Analogies?")
    print("Scale analogies help us understand size relationships by comparing")
    print("familiar objects with unfamiliar ones using proportional scaling.")
    print(f"Database contains {len(comparator.objects)} objects spanning 61 orders of magnitude.")
    
    # Section 1: Classic analogies
    print("\n" + "CLASSIC SCALE ANALOGIES")
    print("=" * 60)
    
    classic_analogies = [
        ('atom_hydrogen', 'golf_ball', 'earth', "If an atom were a golf ball, Earth would be..."),
        ('earth', 'golf_ball', 'sun', "If Earth were a golf ball, the Sun would be..."),
        ('virus', 'basketball', 'earth', "If a virus were a basketball, Earth would be..."),
        ('moon', 'tennis_ball', 'jupiter', "If the Moon were a tennis ball, Jupiter would be...")
    ]
    
    for obj1, obj2, obj3, description in classic_analogies:
        if all(obj in comparator.objects for obj in [obj1, obj2, obj3]):
            print(f"\n{description}")
            comparator.display_scale_analogy(obj1, obj2, obj3)
    
    # Section 2: Cross-scale journeys
    print("\n" + "CROSS-SCALE JOURNEYS")
    print("=" * 60)
    print("Following proportional relationships across different domains of size")
    
    journey_analogies = [
        ('planck_length', 'proton', 'atom_hydrogen', "Quantum foundations"),
        ('virus', 'red_blood_cell', 'human_hair', "Biological scales"),
        ('golf_ball', 'earth', 'solar_system', "Planetary to cosmic"),
        ('mount_everest', 'earth', 'milky_way_galaxy', "Geographic to galactic")
    ]
    
    for obj1, obj2, obj3, description in journey_analogies:
        if all(obj in comparator.objects for obj in [obj1, obj2, obj3]):
            print(f"\n{description}:")
            comparator.display_scale_analogy(obj1, obj2, obj3)
    
    # Section 3: Interactive analogies
    print("\n" + "DISCOVER MORE ANALOGIES")
    print("=" * 60)
    
    # Find interesting analogies automatically
    auto_analogies = comparator.find_interesting_analogies()
    interesting_ones = auto_analogies[4:7]  # Pick a few more interesting ones
    
    for obj1, obj2, obj3, description in interesting_ones:
        print(f"\n{description}:")
        comparator.display_scale_analogy(obj1, obj2, obj3)
    
    # Section 4: Scale perspective
    print("\n" + "SCALE PERSPECTIVE")
    print("=" * 60)
    
    # Show the extreme range
    smallest = min(comparator.objects.items(), key=lambda x: comparator.get_diameter_in_meters(x[0]))
    largest = max(comparator.objects.items(), key=lambda x: comparator.get_diameter_in_meters(x[0]))
    
    smallest_size = comparator.get_diameter_in_meters(smallest[0])
    largest_size = comparator.get_diameter_in_meters(largest[0])
    total_ratio = largest_size / smallest_size
    
    print(f"\nDatabase Coverage:")
    print(f"   Smallest: {smallest[1]['n']} ({comparator.format_size_value(smallest_size)})")
    print(f"   Largest:  {largest[1]['n']} ({comparator.format_size_value(largest_size)})")
    print(f"   Total ratio: {total_ratio:.2e} (61 orders of magnitude)")
    
    # Final demonstration with extreme analogy
    print(f"\nExtreme Scale Analogy:")
    comparator.display_scale_analogy(smallest[0], 'earth', largest[0])
    
    # Available objects summary
    print("\n" + "AVAILABLE OBJECTS FOR ANALOGIES")
    print("=" * 60)
    
    # Group objects by scale for easier browsing
    scale_groups = {
        'Quantum (< 1 fm)': [],
        'Atomic (1 fm - 1 nm)': [],
        'Molecular (1 nm - 1 μm)': [],
        'Cellular (1 μm - 1 mm)': [],
        'Everyday (1 mm - 1 km)': [],
        'Geographic (1 km - 10,000 km)': [],
        'Planetary (10,000 km - 1 Mm)': [],
        'Stellar (1 Mm - 1 Tm)': [],
        'Galactic (> 1 Tm)': []
    }
    
    for obj_key, obj_data in comparator.objects.items():
        size = comparator.get_diameter_in_meters(obj_key)
        name = obj_data['n']
        
        if size < 1e-15:
            scale_groups['Quantum (< 1 fm)'].append(f"{name}: {comparator.format_size_value(size)}")
        elif size < 1e-9:
            scale_groups['Atomic (1 fm - 1 nm)'].append(f"{name}: {comparator.format_size_value(size)}")
        elif size < 1e-6:
            scale_groups['Molecular (1 nm - 1 μm)'].append(f"{name}: {comparator.format_size_value(size)}")
        elif size < 1e-3:
            scale_groups['Cellular (1 μm - 1 mm)'].append(f"{name}: {comparator.format_size_value(size)}")
        elif size < 1e3:
            scale_groups['Everyday (1 mm - 1 km)'].append(f"{name}: {comparator.format_size_value(size)}")
        elif size < 1e7:
            scale_groups['Geographic (1 km - 10,000 km)'].append(f"{name}: {comparator.format_size_value(size)}")
        elif size < 1e9:
            scale_groups['Planetary (10,000 km - 1 Mm)'].append(f"{name}: {comparator.format_size_value(size)}")
        elif size < 1e12:
            scale_groups['Stellar (1 Mm - 1 Tm)'].append(f"{name}: {comparator.format_size_value(size)}")
        else:
            scale_groups['Galactic (> 1 Tm)'].append(f"{name}: {comparator.format_size_value(size)}")
    
    for group_name, objects in scale_groups.items():
        if objects:
            print(f"\n{group_name}:")
            for obj in objects[:5]:  # Show first 5 in each category
                print(f"  - {obj}")
            if len(objects) > 5:
                print(f"  ... and {len(objects) - 5} more")
    
    print("\n" + "CREATE YOUR OWN ANALOGIES")
    print("=" * 60)
    print("Guidelines for creating effective analogies:")
    print("- If a [small object] were a [familiar object], then [large object] would be...")
    print("- Use objects from different scale groups for the most striking analogies")
    print("- The bigger the scale jump, the more compelling the result")
    print("- Choose familiar objects as reference points for better understanding")

if __name__ == "__main__":
    main()