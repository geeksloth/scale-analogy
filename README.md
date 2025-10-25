# Relative Sizes - Scale Analogies Explorer

A comprehensive tool for comparing sizes of objects across the universe, from quantum particles to cosmic structures. This project helps understand the relative sizes of objects through proportional relationships and scale analogies.

## Overview

This project provides an intuitive way to understand the vast range of sizes in our universe by creating scale analogies between familiar and unfamiliar objects. The database spans **61 orders of magnitude**, from the Planck length (10^-35 m) to the observable universe (10^26 m).

## Latest Version: v2.1

The current implementation (v2.1) features:

- **33 objects** spanning quantum to cosmic scales
- **Efficient JSON format** with compressed field names and metadata
- **Advanced scale analogy generation** and analysis
- **Comprehensive metric prefix support** (21 prefixes: yoctometer to yottameter)
- **Professional scientific formatting** and presentation
- **Cross-scale relationship discovery**

## Key Features

### 🔬 Scale Analogies
Create compelling analogies like:
- "If an atom were the size of a golf ball, Earth would be..."
- "If Earth were the size of a tennis ball, Jupiter would be..."

### 📏 Comprehensive Size Range
The database includes objects from:
- **Quantum Scale**: Planck length, protons, atomic nuclei
- **Atomic Scale**: Hydrogen atoms, carbon atoms, electrons
- **Molecular Scale**: DNA double helix, viruses
- **Cellular Scale**: Red blood cells, human hair
- **Everyday Objects**: Sports balls, landmarks, structures
- **Geographic Scale**: Mountains, ocean depths, atmosphere
- **Planetary Scale**: Planets, moons, orbital distances
- **Stellar Scale**: The Sun, solar system diameter
- **Galactic Scale**: Light years, galaxy diameter
- **Cosmic Scale**: Observable universe

### 🎯 Smart Unit Selection
Automatically selects the most appropriate metric unit for display:
- Supports all 21 metric prefixes (ym to Ym)
- Handles extreme ranges with scientific notation
- Provides human-readable formatting

## Database Structure (v2.1)

The `objects.json` file uses an efficient format:

```json
{
  "_metadata": {
    "version": "2.0",
    "created": "2025-10-25",
    "description": "Efficient object size database with metric prefix support",
    "units": "meters",
    "total_objects": 33,
    "scale_range": "10^-35 to 10^26 meters"
  },
  "objects": {
    "object_key": {
      "n": "Object Name",
      "d": 1.23e-10,
      "r": [1.0e-10, 1.5e-10],
      "desc": "Object description",
      "tags": ["category", "type"]
    }
  }
}
```

**Field Abbreviations:**
- `n`: Name
- `d`: Diameter (in meters)
- `r`: Range (optional, [min, max] values)
- `desc`: Description
- `tags`: Classification tags

### Computational Complexity

The tool implements several algorithms with different complexity characteristics:

**Object Comparison**: $O(1)$ - Direct diameter lookup and ratio calculation

**Best Match Finding**: $O(n)$ - Linear search through all objects to find the closest match

$$\text{bestmatch} = \arg\min_{i} |d_i - d_{target}|$$

**Range Queries**: $O(n)$ - Filter objects within specified size bounds

$$\{o_i : d_{min} \leq d_i \leq d_{max}\}$$

**Analogy Generation**: $O(n)$ - Calculate scaled sizes for all objects and find optimal matches

### Scale Distribution Analysis

The database spans 61 orders of magnitude with logarithmic distribution:

$$\log_{10}(d_{max}) - \log_{10}(d_{min}) = 26 - (-35) = 61$$

Objects are distributed across scale domains:
- **Quantum Domain**: $d < 10^{-15}$ m
- **Atomic Domain**: $10^{-15} \leq d < 10^{-9}$ m  
- **Molecular Domain**: $10^{-9} \leq d < 10^{-6}$ m
- **Cellular Domain**: $10^{-6} \leq d < 10^{-3}$ m
- **Everyday Domain**: $10^{-3} \leq d < 10^{3}$ m
- **Geographic Domain**: $10^{3} \leq d < 10^{7}$ m
- **Planetary Domain**: $10^{7} \leq d < 10^{9}$ m
- **Stellar Domain**: $10^{9} \leq d < 10^{12}$ m
- **Galactic Domain**: $d \geq 10^{12}$ m

### Error Propagation

For objects with ranges, the uncertainty in scale analogies is calculated using error propagation:

$$\sigma_{ratio} = \sqrt{\left(\frac{\partial R}{\partial d_1}\sigma_{d_1}\right)^2 + \left(\frac{\partial R}{\partial d_2}\sigma_{d_2}\right)^2}$$

Where $\sigma_{d_i}$ represents the uncertainty in diameter measurements.

## Usage Examples

### Basic Object Comparison
```python
from main import ObjectSizeComparator

comparator = ObjectSizeComparator()

# Compare two objects
comparison = comparator.compare_objects('earth', 'golf_ball')
print(comparison['comparison_text'])
# Output: "Earth is 2.99e8 times larger than Golf Ball"

# Format object size
size = comparator.format_size('virus')
print(size)  # Output: "100 nm"
```

### Scale Analogies
```python
# Create scale analogy: if atom is to golf ball, then earth is to what?
analogy = comparator.create_scale_analogy('hydrogen_atom', 'golf_ball', 'earth')
comparator.display_scale_analogy('hydrogen_atom', 'golf_ball', 'earth')
```

### Search and Filter
```python
# Search objects
viruses = comparator.search_objects('virus')

# Filter by tags
biological = comparator.filter_by_tags(['biological'])

# Find objects in size range
small_objects = comparator.find_objects_by_size_range(1e-9, 1e-6, 'm')
```

## Sample Output

![Scale Analogies Explorer Screenshot](v2.1/static/screenshot.png)

```
SCALE ANALOGIES EXPLORER
============================================================
Understanding size through proportional relationships
From quantum particles to cosmic structures

If an atom were a golf ball, Earth would be...

Scale Analogy:
   Hydrogen Atom is to Golf Ball
   as Earth is to Solar System (Kuiper Belt)

Object Sizes:
   - Hydrogen Atom: 106 pm
   - Golf Ball: 42.7 mm
   - Earth: 12.7 Mm
   - Solar System (Kuiper Belt): 9.00 Tm

Scale Factor: 4.03e11
Expected Size: 5.14 Tm
Match Accuracy: 42.9%
```

## File Structure

```
v2.1/
├── main.py           # Core ObjectSizeComparator class and demonstration
├── objects.json      # Efficient object database with metadata
├── test_v2.py       # Unit tests
└── static/
    └── screenshot.png # Visual example of the tool
```

## Mathematical Foundations

### Scale Ratio Calculations

The core mathematical concept behind scale analogies is proportional scaling. For any scale analogy of the form "if A is to B, then C is to D", the relationship is defined by:

$$\frac{D}{C} = \frac{B}{A}$$

Where:
- $A$, $B$, $C$, $D$ are the diameters of objects in meters
- The scale factor $k = \frac{B}{A}$ is applied to object $C$ to find the expected size of $D$

**Example Calculation:**
If a hydrogen atom (diameter = $1.06 \times 10^{-10}$ m) were scaled to the size of a golf ball (diameter = $4.267 \times 10^{-2}$ m), what would Earth (diameter = $1.2749 \times 10^7$ m) become?

$$k = \frac{4.267 \times 10^{-2}}{1.06 \times 10^{-10}} = 4.025 \times 10^{11}$$

$$D_{expected} = k \times C = 4.025 \times 10^{11} \times 1.2749 \times 10^7 = 5.133 \times 10^{18} \text{ m}$$

### Size Comparison Metrics

For direct object comparisons, the ratio between two objects is calculated as:

$$R = \frac{d_1}{d_2}$$

Where $d_1$ and $d_2$ are the diameters of the objects being compared.

### Range Handling

For objects with size ranges, the effective diameter is calculated using the geometric mean:

$$d_{effective} = \sqrt{d_{min} \times d_{max}}$$

However, the current implementation uses the arithmetic mean for simplicity:

$$d_{effective} = \frac{d_{min} + d_{max}}{2}$$

### Unit Conversion

The tool supports conversion between metric prefixes using powers of 10:

$$d_{meters} = d_{input} \times 10^{n}$$

Where $n$ is the power corresponding to the metric prefix:
- Yoctometer (ym): $n = -24$
- Zeptometer (zm): $n = -21$
- ...
- Meter (m): $n = 0$
- ...
- Yottameter (Ym): $n = 24$

### Optimal Unit Selection

The algorithm selects the largest unit where the numerical value remains ≥ 1:

$$\text{unit} = \max\{u : \frac{d_{meters}}{10^{n_u}} \geq 1\}$$

Where $n_u$ is the power of 10 for unit $u$.

### Accuracy Measurement

For scale analogies, the accuracy of the best match is calculated as:

$$\text{Accuracy} = \left(1 - \frac{|d_{actual} - d_{expected}|}{d_{expected}}\right) \times 100\%$$

Where:
- $d_{actual}$ is the diameter of the closest matching object
- $d_{expected}$ is the calculated expected diameter from the scale analogy

## Technical Highlights

### Advanced Features
- **Range Support**: Objects can have size ranges (min/max values)
- **Metadata Tracking**: Version control and database statistics
- **Professional Formatting**: Scientific notation for extreme values
- **Cross-Domain Analysis**: Relationships between different scale domains
- **Interactive Discovery**: Automatic generation of interesting analogies

### Metric Prefix Support
Full support for SI metric prefixes:
- **Small**: yocto (10^-24) through nano (10^-9)
- **Medium**: micro (10^-6) through kilo (10^3)
- **Large**: mega (10^6) through yotta (10^24)

### Error Handling
- Graceful handling of missing objects
- Validation of units and ranges
- Comprehensive error messages

## Getting Started

1. Clone the repository
2. Navigate to the `v2.1` directory
3. Run the main demonstration:
   ```bash
   python main.py
   ```

This will display various scale analogies and demonstrate the tool's capabilities across different size domains.

## Educational Value

This tool is particularly valuable for:
- **Science Education**: Understanding scale relationships in physics, astronomy, and biology
- **Data Visualization**: Creating compelling size comparisons for presentations
- **Scientific Communication**: Making abstract concepts more relatable
- **Research**: Exploring cross-scale phenomena and relationships

## Contributing

The database can be extended by adding new objects to `objects.json` following the established format. Each object should include appropriate tags and descriptions to maximize the tool's educational value.
