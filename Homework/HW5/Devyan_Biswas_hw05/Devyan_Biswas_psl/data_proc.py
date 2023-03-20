import csv
import itertools
import jaro

if __name__ == "__main__":
    print("HELLO")
    
    data_imdb = dict()
    data_rt = dict()

    # #RN I AM INCLUDING THE NULL ENTRIES FOR THESE ONES
    file = open("movies3/csv_files/imdb.csv", "r")
    data = list(csv.reader(file, delimiter=","))

    # DICT FOR SIM FUNCS
    for idx, row in enumerate(data):
        if idx == 0:
            continue
        data_imdb[row[0]] = {"Title" : row[1], "Director": row[4]}

    # IMDB WRITE SECTION
    imdb_ids = list()
    for idx,row in enumerate(data):
        if idx == 0:
            continue
        imdb_ids.append(row[0])

    with open('data/imdb_title.txt', 'w') as fp:
        for idx, row in enumerate(data):
            if idx == 0:
                continue
            to_write = row[0] + "\t" + row[1] + "\n"
            fp.write(to_write)
    with open('data/imdb_director.txt', 'w') as fp:
        for idx, row in enumerate(data):
            if idx == 0:
                continue
            to_write = row[0] + "\t" + row[4] + "\n"
            fp.write(to_write)
    with open('data/imdb_date.txt', 'w') as fp:
        for idx, row in enumerate(data):
            if idx == 0:
                continue
            to_write = row[0] + "\t" + row[2] + "\n"
            fp.write(to_write)

    file = open("movies3/csv_files/rotten_tomatoes.csv", "r")
    data = list(csv.reader(file, delimiter=","))
    
    # DICT FOR SIM FUNCS
    for idx, row in enumerate(data):
        if idx == 0:
            continue
        data_rt[row[0]] = {"Title" : row[1], "Director": row[4]}

    rt_ids = list()
    for idx,row in enumerate(data):
        if idx == 0:
            continue
        rt_ids.append(row[0])

    with open('data/rotten_tomatoes_title.txt', 'w') as fp:
        for idx, row in enumerate(data):
            if idx == 0:
                continue
            to_write = row[0] + "\t" + row[1] + "\n"
            fp.write(to_write)
    with open('data/rotten_tomatoes_director.txt', 'w') as fp:
        for idx, row in enumerate(data):
            if idx == 0:
                continue
            to_write = row[0] + "\t" + row[4] + "\n"
            fp.write(to_write)
    with open('data/rotten_tomatoes_date.txt', 'w') as fp:
        for idx, row in enumerate(data):
            if idx == 0:
                continue
            time = row[2].replace("/", "-")
            to_write = row[0] + "\t" + time + "\n"
            fp.write(to_write)
    
    # THIS IS THE GENERATION OF THE FULL TARGET SPACE/LIST
    # THIS SUBSETTING IS DONE CAUSE MY COMPUTER IS SLOW
    combos = list(itertools.product(imdb_ids, rt_ids))#[0:100000]

    with open('data/director_obs.txt', 'w') as fp:
        for idx,item in enumerate(combos):
            imdb_entry = data_imdb[item[0]]
            rt_entry = data_rt[item[1]]
            director_sim = jaro.jaro_winkler_metric(imdb_entry['Director'], rt_entry['Director'])
            to_write = item[0] + "\t" + item[1] + "\t" + str(director_sim) + "\n"
            fp.write(to_write)
    
    with open('data/title_obs.txt', 'w') as fp:
        for idx,item in enumerate(combos):
            imdb_entry = data_imdb[item[0]]
            rt_entry = data_rt[item[1]]
            title_sim = jaro.jaro_winkler_metric(imdb_entry['Title'], rt_entry['Title'])
            to_write = item[0] + "\t" + item[1] + "\t" + str(title_sim) + "\n"
            fp.write(to_write)
    

    with open('data/same_movie_target.txt', 'w') as fp:
        for idx, row in enumerate(combos):
            to_write = row[0] + "\t" + row[1] + "\n"
            fp.write(to_write)

    # VALUES WITH TRUTH LABELS HERE
    file = open("movies3/csv_files/labeled_data.csv", "r")
    data = list(csv.reader(file, delimiter=","))


    with open('data/same_movie_truth.txt', 'w') as fp:
        for idx,row in enumerate(data):
            if(idx <= 5):
                continue
            if row[9] == "":
                continue
            to_write = "a-" + row[1] + "\t" + "b-" + row[2] + "\t" + str(float(row[9])) + "\n"
            fp.write(to_write)