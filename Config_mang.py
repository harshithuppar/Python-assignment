import configparser
import json

def config_Parse():
    try:
        config = configparser.ConfigParser
        config.read()

        Data ={}
        for section in config.sections():
            Data[section] = dict(config.items(section))
     
        return Data
    
    except FileNotFoundError:
        print("Error: Configuration file not found.")
    except Exception as e:
        print(f"Error: {e}")


  
if __name__ == "__main__":
    
    File_path = "C:\Users\harsh\OneDrive\Documents\Devops\Assignments\New Text Document.ini"
    Result = config_Parse(File_path)

    if Result:
        print("Configuration File Parser Results:")
        for section, values in Result.items():
            print(f"\n{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")

    json_output = json.dumps(Result, indent=2)
    with open("result_output.json", "w") as json_file:
        json_file.write(json_output)

    print("\nJSON data saved to 'result_output.json'")