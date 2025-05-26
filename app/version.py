def get_version():
    try:
        with open('version.txt', 'r') as file:
            version = file.read().strip()
            return version if version else '1.0.0'
    except (FileNotFoundError, IOError):
        return '1.0.0'