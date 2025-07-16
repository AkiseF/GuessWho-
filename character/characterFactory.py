from characterModels import Character, OnePieceCharacter, NarutoCharacter, DemonSlayerCharacter, AttackOnTitanCharacter
from typing import Dict

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
