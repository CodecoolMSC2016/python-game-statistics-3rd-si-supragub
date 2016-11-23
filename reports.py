def read_file(filename="game_stat.txt"):
    array = []
    with open(filename, "r") as ins:
        for line in ins:
            array.append(line)
    return array


def count_games(file_name="game_stat.txt"):
    game_list = read_file(file_name)
    return len(game_list)


def decide(file_name, year):
    game_list = read_file(file_name)
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        if str(release) == str(year):
            return True
    return False


def get_latest(file_name):
    game_list = read_file(file_name)
    max = 0
    maxTitle = "N/A"
    for i in range(0, len(game_list)):
        title, copies, release, genre, publisher = game_list[i].split("\t")
        if int(release) > int(max):
            max = release
            maxTitle = title
    return maxTitle


def count_by_genre(file_name, genre):
    game_list = read_file(file_name)
    count = 0
    for i in game_list:
        title, copies, release, genre_file, publisher = i.split("\t")
        if str(genre) == str(genre_file):
            count += 1
    return count


def get_line_number_by_title(file_name, title):
    game_list = read_file(file_name)
    line = 0
    for i in game_list:
        line += 1
        title_file, copies, release, genre_file, publisher = i.split("\t")
        if str(title_file) == str(title):
            return line


def sort_abc(file_name):
    game_list = read_file(file_name)
    game_titles = []
    for i in game_list:
        title, copies, release, genre_file, publisher = i.split("\t")
        game_titles.append(title)
    game_titles.sort()
    return game_titles


def check_item_in_list(list, item):
    for i in list:
        if str(i) == str(item):
            return True
    return False


def get_genres(file_name):
    game_list = read_file(file_name)
    genres = []
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        if check_item_in_list(genres, genre) == False:
            genres.append(genre)
    genres.sort(key=str.lower)
    return genres


def when_was_top_sold_fps(file_name):
    game_list = read_file(file_name)
    topCopies = 0
    topRelease = 0
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        if str(genre) == "First-person shooter":
            if float(copies) > float(topCopies):
                topCopies = copies
                topRelease = release
    return int(topRelease)
