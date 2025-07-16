# Character Manager - Singleton Class Usage Guide

The `CharacterManager` is a singleton class that provides centralized access to all character data from multiple anime series. It automatically loads and indexes characters from JSON files for efficient retrieval.

## Basic Usage

```python
from character.characterManager import CharacterManager

# Get the singleton instance (automatically loads all characters)
manager = CharacterManager()
```

## Available Methods

### 1. Get All Characters
```python
# Get all characters from all series
all_characters = manager.get_all_characters()
print(f"Total characters: {len(all_characters)}")
```

### 2. Get Character by ID
```python
# Get a specific character by their unique ID
character = manager.get_character_by_id(1)
if character:
    character.display_details()
```

### 3. Get Character by Name
```python
# Get a character by name (case-insensitive)
luffy = manager.get_character_by_name("Monkey D. Luffy")
naruto = manager.get_character_by_name("naruto uzumaki")  # Case doesn't matter
```

### 4. Get Characters by Series
```python
# Get all characters from a specific series
onepiece_chars = manager.get_characters_by_series("onepiece")
naruto_chars = manager.get_characters_by_series("naruto")
demonslayer_chars = manager.get_characters_by_series("demonslayer")
aot_chars = manager.get_characters_by_series("attackontitan")

print(f"One Piece characters: {len(onepiece_chars)}")
```

### 5. Search Characters
```python
# Search for characters by partial name match
results = manager.search_characters("Uchiha")  # Find all Uchiha clan members
monkey_chars = manager.search_characters("Monkey")  # Find characters with "Monkey" in name
```

### 6. Filter Characters
```python
# Filter characters by various criteria
alive_chars = manager.filter_characters(status="Alive")
onepiece_alive = manager.filter_characters(series="onepiece", status="Alive")
chars_with_luffy = manager.filter_characters(name_contains="Luffy")
```

### 7. Get Available Series
```python
# Get list of all available series
series_list = manager.get_available_series()
print(f"Available series: {series_list}")
```

### 8. Get Character Statistics
```python
# Get total character count
total_count = manager.get_character_count()

# Get character count by series
series_counts = manager.get_character_count_by_series()
for series, count in series_counts.items():
    print(f"{series}: {count} characters")
```

## Complete Example

```python
from character.characterManager import CharacterManager

# Initialize the manager (singleton pattern)
manager = CharacterManager()

# Display statistics
print(f"Total characters loaded: {manager.get_character_count()}")
print(f"Available series: {manager.get_available_series()}")

# Get characters by series
onepiece_chars = manager.get_characters_by_series("onepiece")
print(f"\nOne Piece characters: {len(onepiece_chars)}")

# Find a specific character
luffy = manager.get_character_by_name("Monkey D. Luffy")
if luffy:
    luffy.display_details()

# Search for characters
uchiha_members = manager.search_characters("Uchiha")
print(f"\nFound {len(uchiha_members)} Uchiha clan members")

# Filter characters
alive_characters = manager.filter_characters(status="Alive")
print(f"\nAlive characters: {len(alive_characters)}")

# Get character by ID
character_1 = manager.get_character_by_id(1)
if character_1:
    print(f"\nCharacter with ID 1: {character_1.name}")
```

## Available Series
- `onepiece` - One Piece characters
- `naruto` - Naruto characters  
- `demonslayer` - Demon Slayer characters
- `attackontitan` - Attack on Titan characters

## Notes
- The CharacterManager uses the singleton pattern - only one instance exists
- Characters are automatically loaded from JSON files on first initialization
- All search and filter operations are case-insensitive
- The manager indexes characters by ID, name, and series for efficient retrieval
- Each character type has series-specific attributes accessible through `get_specific_info()`