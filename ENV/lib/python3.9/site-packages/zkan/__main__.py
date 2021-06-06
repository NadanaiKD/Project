import pprint


def main():
    card = {
        "Name": "Kan Ouivirach",
        "Work": "Data Craftsman, ODDS",
        "GitHub": "https://github.com/zkan",
        "Linkedin": "https://linkedin.com/in/kanouivirach",
        "Twitter": "https://twitter.com/zkancs",
    }
    for each in card:
        print(f'{each}: {card[each]}')


if __name__ == "__main__":
    main()
