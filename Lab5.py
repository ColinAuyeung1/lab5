def load_movie_data():
    fileName = input("Enter the file name:")
    headers = []
    movie_list_of_list = []
    try:
        with open(fileName, 'r') as moviesData:
            movies = moviesData.readlines()
            headers = movies[0][:-1].split(",")
            count = 1;
            for movie in movies[1:]:
                count += 1
                movie_list = []
                movie_details = movie.split(",")
                try:
                    movie_list.append(movie_details[0])
                    movie_list.append(movie_details[1])
                    movie_list.append(int(movie_details[2]))
                    movie_list.append(int(movie_details[3]))
                    movie_list_of_list.append(movie_list)
                except:
                    print("unmatched data type on line number:", count)
    except:
        print('file not found')
    add_profit_column(headers, movie_list_of_list)


def add_profit_column(headers, movie_list_of_list):
    headers.append("profit")
    for movie in movie_list_of_list:
        movie.append(movie[-1] - movie[-2])
    print_min_and_max_profit(headers, movie_list_of_list)

def print_min_and_max_profit(headers, movie_list_of_list):
    min_profit = float("inf")
    max_profit = float("-inf")
    min_profit_index, max_profit_index, count = 0, 0, 0
    for movie in movie_list_of_list:
        if (movie[-1] > max_profit):
            max_profit = movie[-1]
            max_profit_index = count
        if (movie[-1] < min_profit):
            min_profit = movie[-1]
            min_profit_index = count
        count += 1
    index = 0
    Highest = ''
    lowest = ''
    for i in movie_list_of_list[max_profit_index]:
        Highest = Highest + " " + headers[index] + " " + str(i)
        index += 1
    index = 0
    for i in movie_list_of_list[min_profit_index]:
        lowest = lowest + " " + headers[index] + " " + str(i)
        index += 1
    print("Highest profit movie", Highest)
    print("lowest profit movie", lowest)
    save_movie_data(headers, movie_list_of_list)


def save_movie_data(headers, movie_list_of_list):
    output_filename = input("Enter the filename to save the movie data with .csv extension: ")
    with open(output_filename, "w") as wr:
        headers = ",".join(headers)
        wr.write(headers + "\n")
        for line in movie_list_of_list:
            temp = [str(i) for i in line]
            temp = ",".join(temp)
            wr.write(temp + "\n")


def main():
    load_movie_data()

if __name__ == '__main__':
    main()