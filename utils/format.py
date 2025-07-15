import json
import os
import sys

def format_json_file(input_file_path, output_file_path=None):
    """
    Format a JSON file to make it more human-readable.
    
    Args:
        input_file_path (str): Path to the input JSON file
        output_file_path (str): Path to the output file (optional, defaults to input file)
    """
    try:
        # Read the JSON file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # If no output path specified, overwrite the input file
        if output_file_path is None:
            output_file_path = input_file_path
        
        # Write the formatted JSON back to file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False, separators=(',', ': '))
        
        print(f"Successfully formatted JSON file: {output_file_path}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{input_file_path}': {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function to handle command line arguments or interactive input."""
    if len(sys.argv) > 1:
        # Command line usage
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        format_json_file(input_file, output_file)
    else:
        # Interactive usage
        print("JSON Formatter")
        print("=============")
        
        # Default to the Attack on Titan JSON file
        default_file = r"c:\Users\Axela\OneDrive\Escritorio\GuessWho-\CharacterJSONs\attackontitan.json"
        
        input_file = input(f"Enter JSON file path (default: {default_file}): ").strip()
        if not input_file:
            input_file = default_file
        
        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found.")
            return
        
        # Ask if user wants to overwrite or create new file
        choice = input("Overwrite original file? (y/n, default: y): ").strip().lower()
        if choice == 'n':
            output_file = input("Enter output file path: ").strip()
            if not output_file:
                print("Error: Output file path cannot be empty.")
                return
        else:
            output_file = None
        
        format_json_file(input_file, output_file)

if __name__ == "__main__":
    main()
