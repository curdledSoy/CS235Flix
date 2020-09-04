from datafilereaders.movie_file_csv_reader import MovieFileCSVReader



def main():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
    print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
    print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
    print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')
    print(f'first row of actors: {movie_file_reader.dataset_of_movies[2].actors}')
if __name__ == "__main__":
    main()