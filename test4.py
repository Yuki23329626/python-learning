
# weapon_cut = 2.64
# weapon_smash = 2

# weapon_level = 20
# agile = 70
# power = 90

# if weapon_cut > weapon_smash:
#     majar_damage = 20 + (0.4*weapon_cut*(agile+weapon_level))
#     minor_damage = 0 + (0.5*weapon_smash*(power+weapon_level))
# else:
#     majar_damage = 20 + (0.4*weapon_smash*(power+weapon_level))
#     minor_damage = 8 + (0.46*weapon_cut*(agile+weapon_level))

# total = majar_damage + minor_damage
# print('total:', total)
import winreg
import logging
import os
import subprocess
import sys

# Get the path of the current Python script
script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)
print('script_dir: ', script_dir)

FORMAT = '[%(levelname)-5s][%(asctime)s] %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(
    filename=os.path.join(script_dir, 'log_test4.log'), encoding='utf-8')],
    format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

def del_reg():
    # Specify the registry key path and name
    key_path = r"SOFTWARE\Google\Chrome\NativeMessagingHosts\com.example.nativeapp"

    # Open the registry key for deletion
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as registry_key:
            winreg.DeleteKey(registry_key, '')  # The second argument should be an empty string to delete the key
            logging.info(f"Registry key '{key_path}' has been removed.")

        var_name = "Path"
        # Specify the value you want to remove from the Path
        value_to_remove = "ffmpeg"  # Replace with the actual value you want to remove
        # Retrieve the current value of the environment variable
        current_value = os.environ.get(var_name, "")
        
        # Split the current value into a list of values using semicolon as the separator
        values_list = current_value.split(os.pathsep)
        # Use a list comprehension to find values containing 'ffmpeg'
        filtered_list = [item for item in values_list if value_to_remove in item]

        for item in filtered_list:
            values_list.remove(item)
        
        # Reconstruct the Path with the modified components
        new_path = os.pathsep.join(values_list)
        # Update the Path environment variable
        os.environ["Path"] = new_path
        subprocess.check_call(['setx', var_name, new_path])

        logging.info(f"Value '{value_to_remove}' removed from Path.")
        logging.info(f"new_path: '{new_path}'")

    except FileNotFoundError:
        logging.error(f"Registry key '{key_path}' not found.")
    except Exception as e:
        logging.error(e)

del_reg()