

if __name__ == "__main__":
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
    for language, creator in languages.items():
        print("{} was created by {}".format(language, creator))
