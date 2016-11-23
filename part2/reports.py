def read_file(filename="game_stat.txt"):
    array = []
    with open(filename, "r") as ins:
        for line in ins:
            array.append(line)
    return array


def get_most_played(file_name):
    game_list = read_file(file_name)
    current_max = 0
    current_max_title = ""
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        if float(copies) > current_max:
            current_max = float(copies)
            current_max_title = title
    return current_max_title


def sum_sold(file_name):
    game_list = read_file(file_name)
    sum = 0
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        sum = sum + float(copies)
    return sum


def get_selling_avg(file_name):
    game_list = read_file(file_name)
    sum = 0
    count = 0
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        count = count + 1
        sum = sum + float(copies)
    return sum / count


def count_longest_title(file_name):
    game_list = read_file(file_name)
    longest = 0
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        if len(title) > longest:
            longest = int(len(title))
    return longest


def get_date_avg(file_name):
    with open(file_name, encoding="utf-8") as database:
        release_dates = [int(row.strip().split('\t')[2])
                         for row in database.readlines()]
        return round(sum(release_dates) / len(release_dates) + 0.5)


def get_game(file_name, title):
    with open(file_name, encoding="utf-8") as database:
        game = [row.strip().split('\t')
                for row in database.readlines() if row.strip().split('\t')[0] == title]
        g = game[0]
        return [g[0], float(g[1]), int(g[2]), g[3], g[4]]


def count_grouped_by_genre(file_name):
    with open(file_name, encoding="utf-8") as database:
        game_genres = {}
        while True:
            row = database.readline().split("\t")
            if row == ['']:
                return game_genres
            elif not row[3] in game_genres:
                game_genres[row[3]] = 1
            else:
                game_genres[row[3]] += 1