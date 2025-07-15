import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Optional, Union

@dataclass
class Character(ABC):
    """Abstract base class for all character types"""
    id: int
    name: str
    status: Optional[str] = None
    appearance: Optional[str] = None
    personality: Optional[str] = None
    background: Optional[str] = None
    allies: Optional[List[str]] = None
    enemies: Optional[List[str]] = None
    voice_actors: Optional[Dict[str, str]] = None
    quotes: Optional[List[str]] = None
    first_appearance: Optional[str] = None
    series: Optional[str] = None
    @abstractmethod
    def get_specific_info(self) -> Dict:
        """Get anime-specific information"""
        pass

    @abstractmethod
    def display_details(self):
        """Display detailed character information"""
        pass

@dataclass
class OnePieceCharacter(Character):
    """One Piece specific character"""
    epithet: Optional[str] = None
    crew: Optional[str] = None
    position: Optional[str] = None
    origin: Optional[str] = None
    hometown: Optional[str] = None
    devil_fruit: Optional[Dict] = None
    bounty: Optional[str] = None
    age: Optional[Union[int, str]] = None
    birthday: Optional[str] = None
    height: Optional[str] = None
    blood_type: Optional[str] = None
    fighting_style: Optional[List[str]] = None
    haki: Optional[List[str]] = None
    techniques: Optional[List[str]] = None
    family: Optional[List[str]] = None
    dream: Optional[str] = None
    weapons: Optional[List[str]] = None
    achievements: Optional[List[str]] = None
    hobbies: Optional[str] = None
    weaknesses: Optional[List[str]] = None
    laugh: Optional[str] = None

    def get_specific_info(self) -> Dict:
        return {
            "epithet": self.epithet,
            "crew": self.crew,
            "position": self.position,
            "devil_fruit": self.devil_fruit,
            "bounty": self.bounty,
            "haki": self.haki,
            "techniques": self.techniques,
            "dream": self.dream
        }

    def display_details(self):
        print(f"\n=== {self.name} ===")
        print(f"Series: One Piece")
        if self.epithet:
            print(f"Epithet: {self.epithet}")
        if self.crew:
            print(f"Crew: {self.crew}")
        if self.position:
            print(f"Position: {self.position}")
        print(f"Status: {self.status}")
        print(f"Age: {self.age}")
        if self.bounty:
            print(f"Bounty: {self.bounty}")
        if self.devil_fruit:
            print(f"Devil Fruit: {self.devil_fruit.get('englishName')} ({self.devil_fruit.get('type')})")
        if self.haki:
            print(f"Haki: {', '.join(self.haki)}")
        if self.dream:
            print(f"Dream: {self.dream}")

@dataclass
class NarutoCharacter(Character):
    """Naruto specific character"""
    village: Optional[str] = None
    rank: Optional[str] = None
    clan: Optional[str] = None
    jutsu: Optional[List[str]] = None
    affiliation: Optional[List[str]] = None
    kekkei_genkai: Optional[str] = None
    nature_type: Optional[List[str]] = None
    family: Optional[List[str]] = None
    missions_completed: Optional[Dict] = None
    mentor: Optional[str] = None
    students: Optional[List[str]] = None
    weapons: Optional[List[str]] = None
    summonings: Optional[List[str]] = None
    achievements: Optional[List[str]] = None
    hobbies: Optional[str] = None
    transformations: Optional[List[str]] = None
    goals: Optional[List[str]] = None
    theme_song: Optional[str] = None

    def get_specific_info(self) -> Dict:
        return {
            "village": self.village,
            "rank": self.rank,
            "clan": self.clan,
            "jutsu": self.jutsu,
            "kekkei_genkai": self.kekkei_genkai,
            "nature_type": self.nature_type,
            "mentor": self.mentor
        }

    def display_details(self):
        print(f"\n=== {self.name} ===")
        print(f"Series: Naruto")
        if self.village:
            print(f"Village: {self.village}")
        if self.rank:
            print(f"Rank: {self.rank}")
        if self.clan:
            print(f"Clan: {self.clan}")
        print(f"Status: {self.status}")
        if self.kekkei_genkai:
            print(f"Kekkei Genkai: {self.kekkei_genkai}")
        if self.jutsu:
            print(f"Jutsu: {', '.join(self.jutsu[:3])}{'...' if len(self.jutsu) > 3 else ''}")
        if self.mentor:
            print(f"Mentor: {self.mentor}")

@dataclass
class DemonSlayerCharacter(Character):
    """Demon Slayer specific character"""
    role: Optional[str] = None
    affiliation: Optional[List[str]] = None
    breath_style: Optional[str] = None
    techniques: Optional[List[str]] = None
    family: Optional[List[str]] = None
    achievements: Optional[List[str]] = None
    goals: Optional[List[str]] = None
    mentor: Optional[str] = None

    def get_specific_info(self) -> Dict:
        return {
            "role": self.role,
            "affiliation": self.affiliation,
            "breath_style": self.breath_style,
            "techniques": self.techniques,
            "mentor": self.mentor
        }

    def display_details(self):
        print(f"\n=== {self.name} ===")
        print(f"Series: Demon Slayer")
        if self.role:
            print(f"Role: {self.role}")
        if self.affiliation:
            print(f"Affiliation: {', '.join(self.affiliation)}")
        if self.breath_style:
            print(f"Breath Style: {self.breath_style}")
        print(f"Status: {self.status}")
        if self.techniques:
            print(f"Techniques: {', '.join(self.techniques[:3])}{'...' if len(self.techniques) > 3 else ''}")
        if self.mentor:
            print(f"Mentor: {self.mentor}")

@dataclass
class AttackOnTitanCharacter(Character):
    """Attack on Titan specific character"""
    age: Optional[Union[int, str]] = None
    height: Optional[str] = None
    weight: Optional[str] = None
    hair_color: Optional[str] = None
    eye_color: Optional[str] = None
    birthplace: Optional[str] = None
    skills: Optional[List[str]] = None
    titan_form: Optional[str] = None
    notable_battles: Optional[List[str]] = None
    love_interests: Optional[str] = None
    fears: Optional[str] = None
    hobbies: Optional[str] = None
    dislikes: Optional[str] = None
    education: Optional[str] = None
    affiliations: Optional[List[str]] = None
    trivia: Optional[List[str]] = None
    injuries_and_scars: Optional[List[str]] = None
    titan_kill_count: Optional[int] = None
    human_kill_count: Optional[int] = None
    character_arc: Optional[str] = None

    def get_specific_info(self) -> Dict:
        return {
            "titan_form": self.titan_form,
            "skills": self.skills,
            "notable_battles": self.notable_battles,
            "affiliations": self.affiliations,
            "titan_kill_count": self.titan_kill_count,
            "human_kill_count": self.human_kill_count
        }

    def display_details(self):
        print(f"\n=== {self.name} ===")
        print(f"Series: Attack on Titan")
        print(f"Age: {self.age}")
        print(f"Status: {self.status}")
        if self.height:
            print(f"Height: {self.height}")
        if self.birthplace:
            print(f"Birthplace: {self.birthplace}")
        if self.titan_form:
            print(f"Titan Form: {self.titan_form}")
        if self.skills:
            print(f"Skills: {', '.join(self.skills[:3])}{'...' if len(self.skills) > 3 else ''}")
        if self.affiliations:
            print(f"Affiliations: {', '.join(self.affiliations)}")

class CharacterFactory:
    """Factory class to create appropriate character types"""
    
    @staticmethod
    def create_character(char_data: Dict, series: str) -> Character:
        """Create a character object based on the series"""
        
        # Common fields mapping
        common_fields = {
            'id': char_data.get('id'),
            'name': char_data.get('name'),
            'status': char_data.get('status'),
            'appearance': char_data.get('appearance'),
            'personality': char_data.get('personality'),
            'background': char_data.get('background'),
            'allies': char_data.get('allies'),
            'enemies': char_data.get('enemies'),
            'voice_actors': char_data.get('voiceActors') or char_data.get('voice_actor'),
            'quotes': char_data.get('quotes') or char_data.get('notableQuotes'),
            'first_appearance': char_data.get('first_appearance') or char_data.get('firstAppearance'),
            'series': series
        }
        
        if series.lower() == 'onepiece':
            return OnePieceCharacter(
                **common_fields,
                epithet=char_data.get('epithet'),
                crew=char_data.get('crew'),
                position=char_data.get('position'),
                origin=char_data.get('origin'),
                hometown=char_data.get('hometown'),
                devil_fruit=char_data.get('devilFruit'),
                bounty=char_data.get('bounty'),
                age=char_data.get('age'),
                birthday=char_data.get('birthday'),
                height=char_data.get('height'),
                blood_type=char_data.get('bloodType'),
                fighting_style=char_data.get('fighting_style'),
                haki=char_data.get('haki'),
                techniques=char_data.get('techniques'),
                family=char_data.get('family'),
                dream=char_data.get('dream'),
                weapons=char_data.get('weapons'),
                achievements=char_data.get('achievements'),
                hobbies=char_data.get('hobbies'),
                weaknesses=char_data.get('weaknesses'),
                laugh=char_data.get('laugh')
            )
        
        elif series.lower() == 'naruto':
            return NarutoCharacter(
                **common_fields,
                village=char_data.get('village'),
                rank=char_data.get('rank'),
                clan=char_data.get('clan'),
                jutsu=char_data.get('jutsu'),
                affiliation=char_data.get('affiliation'),
                kekkei_genkai=char_data.get('kekkeiGenkai'),
                nature_type=char_data.get('natureType'),
                family=char_data.get('family'),
                missions_completed=char_data.get('missions_completed'),
                mentor=char_data.get('mentor'),
                students=char_data.get('students'),
                weapons=char_data.get('weapons'),
                summonings=char_data.get('summonings'),
                achievements=char_data.get('achievements'),
                hobbies=char_data.get('hobbies'),
                transformations=char_data.get('transformations'),
                goals=char_data.get('goals'),
                theme_song=char_data.get('theme_song')
            )
        
        elif series.lower() == 'demonslayer':
            return DemonSlayerCharacter(
                **common_fields,
                role=char_data.get('role'),
                affiliation=char_data.get('affiliation'),
                breath_style=char_data.get('breathStyle'),
                techniques=char_data.get('techniques'),
                family=char_data.get('family'),
                achievements=char_data.get('achievements'),
                goals=char_data.get('goals'),
                mentor=char_data.get('mentor')
            )
        
        elif series.lower() == 'attackontitan':
            return AttackOnTitanCharacter(
                **common_fields,
                age=char_data.get('age'),
                height=char_data.get('height'),
                weight=char_data.get('weight'),
                hair_color=char_data.get('hairColor'),
                eye_color=char_data.get('eyeColor'),
                birthplace=char_data.get('birthplace'),
                skills=char_data.get('skills'),
                titan_form=char_data.get('titanForm'),
                notable_battles=char_data.get('notableBattles'),
                love_interests=char_data.get('loveInterests'),
                fears=char_data.get('fears'),
                hobbies=char_data.get('hobbies'),
                dislikes=char_data.get('dislikes'),
                education=char_data.get('education'),
                affiliations=char_data.get('affiliations'),
                trivia=char_data.get('trivia'),
                injuries_and_scars=char_data.get('injuriesAndScars'),
                titan_kill_count=char_data.get('titanKillCount'),
                human_kill_count=char_data.get('humanKillCount'),
                character_arc=char_data.get('characterArc')
            )
        
        else:
            raise ValueError(f"Unknown series: {series}")

def load_characters(json_files: List[str]) -> List[Character]:
    characters = []
    
    for file_path in json_files:
        file_path = r"CharacterJSONs\\" + file_path
        print(f"Loading characters from {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            if data['status'] != 200:
                continue
                
            # Extract series name from filename
            series_name = file_path.split('\\')[-1].split('.')[0]
            
            for char_data in data['body']:
                if char_data is None:
                    continue
                    
                try:
                    character = CharacterFactory.create_character(char_data, series_name)
                    characters.append(character)
                except Exception as e:
                    print(f"Error creating character {char_data.get('name', 'Unknown')}: {e}")
                    continue
    
    return characters

def display_character_list(characters: List[Character], max_chars: int = 10):
    """Display a summary list of characters"""
    print(f"\n{'ID':<5}{'Name':<25}{'Series':<15}{'Status':<10}{'Type':<20}")
    print("-" * 75)
    
    for i, char in enumerate(characters[:max_chars]):
        char_type = type(char).__name__.replace('Character', '')
        print(f"{char.id:<5}{char.name[:24]:<25}{char.series[:14]:<15}{str(char.status)[:9]:<10}{char_type:<20}")
        
        if i == max_chars - 1 and len(characters) > max_chars:
            print(f"... and {len(characters) - max_chars} more characters")

def get_character_by_id(characters: List[Character], char_id: int) -> Optional[Character]:
    """Get a character by ID"""
    for char in characters:
        if char.id == char_id:
            return char
    return None

def filter_characters_by_series(characters: List[Character], series: str) -> List[Character]:
    """Filter characters by series"""
    return [char for char in characters if char.series.lower() == series.lower()]

# Main program
if __name__ == "__main__":
    # Load the JSON files
    json_files = ['onepiece.json', 'naruto.json', 'demonslayer.json', 'attackontitan.json']
    
    try:
        # Deserialize the data into character objects
        all_characters = load_characters(json_files)
        
        # Display a summary of loaded characters
        print(f"Successfully loaded {len(all_characters)} characters from multiple series")
        display_character_list(all_characters)
        
        # Display details for all loaded characters using the parent Character class
        print("\n=== All Character Details ===")
        
        # Show details for all characters using polymorphism
        for char in all_characters:
            char.display_details()  # Calls the appropriate display_details() method for each character type
        
        # Example: Filter characters by series
        print("\n=== Attack on Titan Characters ===")
        aot_characters = filter_characters_by_series(all_characters, 'attackontitan')
        display_character_list(aot_characters, 5)
        
    except FileNotFoundError as e:
        print(f"Error: {e}. Please make sure the JSON files are in the same directory.")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")