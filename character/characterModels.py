from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List, Dict, Union

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