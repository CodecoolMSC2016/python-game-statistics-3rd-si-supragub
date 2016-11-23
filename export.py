import reports
from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title
from reports import sort_abc
from reports import get_genres
from reports import when_was_top_sold_fps


def export_file(question, value):
    file = open("reports.txt", "a")
    file.write(question + "\n" + str(value) + '\n')
    file.close()

export_file("How many games are in the file?", count_games("game_stat.txt"))
export_file("Is there a game from a given year?",
            decide("game_stat.txt", 2004))
export_file("Which was the latest game?", get_latest("game_stat.txt"))
export_file("How many games do we have by genre?",
            count_by_genre("game_stat.txt", "First-person shooter"))
export_file("What is the line number of the given game (by title)?",
            get_line_number_by_title("game_stat.txt", "Diablo III"))
export_file(
    "What is the alphabetical ordered list of the titles?", sort_abc("game_stat.txt"))
export_file("What are the genres?", get_genres("game_stat.txt"))
export_file(
    "What is the release date of the top sold First-person shooter game?",
               when_was_top_sold_fps("game_stat.txt"))
