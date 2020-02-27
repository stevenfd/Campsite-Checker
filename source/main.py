import reader

SETTINGS_FILENAME = "settings.json"

def main():
    checks = reader.readFile(SETTINGS_FILENAME)

    for check in checks:
        #Build url
        #Example: https://www.recreation.gov/api/camps/availability/campground/232451/month?start_date=2020-06-01T00%3A00%3A00.000Z
        return

    return

    
if __name__ == '__main__':
    main()