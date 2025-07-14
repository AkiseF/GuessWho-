import json
from dataclasses import dataclass
from typing import List, Dict, Optional, Union

@dataclass
class Character:
    id: int
    name: str
    age: Optional[Union[int, str]] = None
    status: Optional[str] = None
    height: Optional[str] = None
    weight: Optional[str] = None
    origin: Optional[str] = None
    affiliations: Optional[List[str]] = None
    skills: Optional[List[str]] = None
    notable_quotes: Optional[List[str]] = None
    series: Optional[str] = None
    bounty: Optional[str] = None
    devil_fruit: Optional[Dict] = None
    jutsu: Optional[List[str]] = None
    titan_form: Optional[str] = None
    epithet: Optional[str] = None
    crew: Optional[str] = None
    village: Optional[str] = None

def load_characters(json_files: List[str]) -> List[Character]:
    characters = []
    
    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            if data['status'] != 200:
                continue
                
            series_name = file_path.split('.')[0].capitalize()
            
            for char_data in data['body']:
                if char_data is None:
                    continue
                    
                # Common fields
                fields = {
                    'id': char_data.get('id'),
                    'name': char_data.get('name'),
                    'series': series_name
                }
                
                # Series-specific fields
                if series_name == 'Onepiece':
                    fields.update({
                        'age': char_data.get('age'),
                        'status': char_data.get('status'),
                        'height': char_data.get('height'),
                        'origin': char_data.get('origin'),
                        'affiliations': [char_data.get('crew')] if char_data.get('crew') else None,
                        'skills': char_data.get('fighting_style', []) + char_data.get('techniques', []),
                        'notable_quotes': char_data.get('quotes'),
                        'bounty': char_data.get('bounty'),
                        'devil_fruit': char_data.get('devilFruit'),
                        'epithet': char_data.get('epithet'),
                        'crew': char_data.get('crew')
                    })
                elif series_name == 'Naruto':
                    fields.update({
                        'age': char_data.get('age'),
                        'status': char_data.get('status'),
                        'height': f"{char_data.get('height')} cm" if char_data.get('height') else None,
                        'origin': char_data.get('village'),
                        'affiliations': char_data.get('affiliation'),
                        'skills': char_data.get('jutsu'),
                        'notable_quotes': char_data.get('notableQuotes'),
                        'village': char_data.get('village')
                    })
                elif series_name == 'Attackontitan':
                    fields.update({
                        'age': char_data.get('age'),
                        'status': char_data.get('status'),
                        'height': char_data.get('height'),
                        'weight': char_data.get('weight'),
                        'origin': char_data.get('birthplace'),
                        'affiliations': char_data.get('affiliations'),
                        'skills': char_data.get('skills'),
                        'notable_quotes': char_data.get('notableQuotes'),
                        'titan_form': char_data.get('titanForm')
                    })
                
                # Create character object
                characters.append(Character(**fields))
    
    return characters

def display_character_list(characters: List[Character], max_chars: int = 10):
    """Display a summary list of characters"""
    print(f"\n{'ID':<5}{'Name':<25}{'Series':<15}{'Status':<10}{'Age':<5}{'Origin':<20}")
    print("-" * 80)
    
    for i, char in enumerate(characters[:max_chars]):
        print(f"{char.id:<5}{char.name[:24]:<25}{char.series[:14]:<15}{str(char.status)[:9]:<10}{str(char.age)[:4]:<5}{str(char.origin)[:19]:<20}")
        
        if i == max_chars - 1 and len(characters) > max_chars:
            print(f"... and {len(characters) - max_chars} more characters")

def get_character_details(character: Character):
    """Display detailed information about a character"""
    print(f"\n=== {character.name} ===")
    print(f"Series: {character.series}")
    if character.epithet:
        print(f"Epithet: {character.epithet}")
    print(f"Status: {character.status}")
    print(f"Age: {character.age}")
    
    if character.height:
        print(f"Height: {character.height}")
    if character.weight:
        print(f"Weight: {character.weight}")
    if character.origin:
        print(f"Origin: {character.origin}")
    if character.crew:
        print(f"Crew: {character.crew}")
    if character.village:
        print(f"Village: {character.village}")
    if character.bounty:
        print(f"Bounty: {character.bounty}")
    if character.devil_fruit:
        print(f"Devil Fruit: {character.devil_fruit.get('englishName')} ({character.devil_fruit.get('type')})")
    if character.titan_form:
        print(f"Titan Form: {character.titan_form}")
    
    if character.affiliations:
        print("\nAffiliations:")
        for aff in character.affiliations:
            print(f"- {aff}")
    
    if character.skills:
        print("\nSkills/Abilities:")
        for skill in character.skills[:5]:  # Show first 5 skills
            print(f"- {skill}")
        if len(character.skills) > 5:
            print(f"... and {len(character.skills) - 5} more")
    
    if character.notable_quotes:
        print("\nNotable Quotes:")
        for quote in character.notable_quotes[:2]:  # Show first 2 quotes
            print(f"- '{quote}'")
        if len(character.notable_quotes) > 2:
            print(f"... and {len(character.notable_quotes) - 2} more")

# Main program
if __name__ == "__main__":
    # Load the JSON files
    json_files = ['onepiece.json', 'naruto.json', 'attackontitan.json']
    
    try:
        # Deserialize the data into character objects
        all_characters = load_characters(json_files)
        
        # Display a summary of loaded characters
        print(f"Successfully loaded {len(all_characters)} characters from 3 series")
        display_character_list(all_characters)
        
        # Example: Get details for specific characters
        print("\n=== Example Character Details ===")
        get_character_details(all_characters[0])  # First character
        get_character_details(all_characters[10])  # 11th character
        get_character_details(all_characters[20])  # 21st character
        
    except FileNotFoundError as e:
        print(f"Error: {e}. Please make sure the JSON files are in the same directory.")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")