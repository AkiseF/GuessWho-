import json
import os
from threading import Lock
from typing import List, Optional, Dict
from characterFactory import CharacterFactory
from characterModels import Character

class CharacterManager:
    """Singleton class to manage character loading and access"""
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Only initialize once
        if not hasattr(self, '_initialized'):
            self._characters = []
            self._characters_by_id = {}
            self._characters_by_series = {}
            self._characters_by_name = {}
            self._load_all_characters()
            self._initialized = True
    
    def _load_all_characters(self):
        """Load all characters from JSON files"""
        json_files = ['onepiece.json', 'naruto.json', 'demonslayer.json', 'attackontitan.json']
        
        for file_path in json_files:
            full_path = os.path.join(os.path.dirname(__file__), "..", "data", file_path)
            try:
                print(f"Loading characters from {file_path}")
                with open(full_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    if data['status'] != 200:
                        continue
                        
                    # Extract series name from filename
                    series_name = file_path.split('.')[0]
                    
                    for char_data in data['body']:
                        if char_data is None:
                            continue
                            
                        try:
                            character = CharacterFactory.create_character(char_data, series_name)
                            self._characters.append(character)
                            
                            # Index by ID
                            self._characters_by_id[character.id] = character
                            
                            # Index by series
                            if character.series not in self._characters_by_series:
                                self._characters_by_series[character.series] = []
                            self._characters_by_series[character.series].append(character)
                            
                            # Index by name (case-insensitive)
                            self._characters_by_name[character.name.lower()] = character
                            
                        except Exception as e:
                            print(f"Error creating character {char_data.get('name', 'Unknown')}: {e}")
                            continue
                            
            except FileNotFoundError:
                print(f"Warning: {file_path} not found")
                continue
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
                continue
        
        print(f"Loaded {len(self._characters)} characters total")
    
    def get_all_characters(self) -> List[Character]:
        """Get all loaded characters"""
        return self._characters.copy()
    
    def get_character_by_id(self, char_id: int) -> Optional[Character]:
        """Get a character by ID"""
        return self._characters_by_id.get(char_id)
    
    def get_character_by_name(self, name: str) -> Optional[Character]:
        """Get a character by name (case-insensitive)"""
        return self._characters_by_name.get(name.lower())
    
    def get_characters_by_series(self, series: str) -> List[Character]:
        """Get characters by series name"""
        return self._characters_by_series.get(series.lower(), []).copy()
    
    def get_available_series(self) -> List[str]:
        """Get list of available series"""
        return list(self._characters_by_series.keys())
    
    def get_character_count(self) -> int:
        """Get total number of characters"""
        return len(self._characters)
    
    def get_character_count_by_series(self) -> Dict[str, int]:
        """Get character count by series"""
        return {series: len(chars) for series, chars in self._characters_by_series.items()}
    
    def search_characters(self, query: str) -> List[Character]:
        """Search characters by name (partial match, case-insensitive)"""
        query_lower = query.lower()
        return [char for char in self._characters if query_lower in char.name.lower()]
    
    def filter_characters(self, **filters) -> List[Character]:
        """Filter characters by various criteria"""
        result = self._characters.copy()
        
        for key, value in filters.items():
            if value is None:
                continue
                
            if key == 'series':
                result = [char for char in result if char.series.lower() == value.lower()]
            elif key == 'status':
                result = [char for char in result if char.status and char.status.lower() == value.lower()]
            elif key == 'name_contains':
                result = [char for char in result if value.lower() in char.name.lower()]
            # Add more filters as needed
        
        return result

