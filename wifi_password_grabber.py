import subprocess

def get_saved_wifi_profiles():
    profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='backslashreplace').split('\n')
    profiles = [line.split(':')[1].strip() for line in profiles_data if "All User Profile" in line]
    return profiles

def get_wifi_password(profile):
    profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors='backslashreplace').split('\n')
    password_lines = [line for line in profile_info if "Key Content" in line]
    if password_lines:
        password = password_lines[0].split(':')[1].strip()
        return password
    else:
        return None

def main():
    profiles = get_saved_wifi_profiles()
    for profile in profiles:
        password = get_wifi_password(profile)
        if password:
            print(f"Profile: {profile}\nPassword: {password}\n")
        else:
            print(f"Profile: {profile}\nPassword: No password set or cannot be retrieved\n")

if __name__ == "__main__":
    main()
