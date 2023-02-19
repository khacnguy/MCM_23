import pandas as pd
import sqlite3


def load_csv():
    data1 = pd.read_csv('dataverse/data/Batbaatar_et_al_JEcol2021_RepData1.csv')
    data2 = pd.read_csv('dataverse/data/Batbaatar_et_al_JEcol2021_RepData2.csv')
    data3 = pd.read_csv('dataverse/data/Batbaatar_et_al_JEcol2021_RepData3.csv')
    data4 = pd.read_csv('dataverse/data/Batbaatar_et_al_JEcol2021_RepData4.csv')
    data5 = pd.read_csv('dataverse/data/Batbaatar_et_al_JEcol2021_RepData5.csv')
    data6 = pd.read_csv('dataverse/data/Batbaatar_et_al_JEcol2021_RepData6.csv')
    return [None , data1, data2, data3, data4, data5, data6]

def check_unique_drought(data):
    '''
        Description: confirm that each plot has 1 drought condition
        
        Input:
            data: dataframe want to check
            
        Results:
            1 if each plot has 1 drought condition
            0 otherwise
    '''
    data = data[['plot', 'drought', 'year']]
    print(type(data))
    plot_drought_dict = {}
    for _,row in data.iterrows():
        if row['plot'] not in plot_drought_dict.keys():
            plot_drought_dict[row['plot']] = row['drought']
        else:
            if row['drought'] != plot_drought_dict[row['plot']]: 
                print("inconsistent")
                return 0
    return 1

def create_connection(db_file):
    """ 
    Description: 
        create a database connection to the SQLite database
    
    Input:
        db_file: database file
    
    Return: 
        Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def plot_unique(row):
    cur.execute(
            '''
                SELECT * FROM plots WHERE plot_id = ?
            '''
            , (row['plot'],)
        )
    if cur.fetchone() != None:
        return False
    return True

def insert_new_plot(data):
    for _, row in data.iterrows():
        if plot_unique(row):
            cur.execute(
                '''
                INSERT INTO plots(plot_id, site_located, drought) 
                VALUES (?,?,?) 
                '''
                , (row['plot'], row['site'], row['drought'])
            )
            conn.commit()

def species_unique(row):
    cur.execute(
            '''
                SELECT * FROM species WHERE species_id = ?
            '''
            , (row['species'],)
        )
    if cur.fetchone() != None:
        return False
    return True

def insert_new_species(data):
    for _, row in data.iterrows():
        if species_unique(row):
            cur.execute(
                '''
                INSERT INTO species(species_id, func) 
                VALUES (?,?) 
                '''
                , (row['species'], row['func'])
            )
            conn.commit()

def find_bad_plot(data1, data4):
    plot_count = {}
    for _, row in data1[['plot', 'year']].iterrows():
        if row['plot'] not in plot_count:
            plot_count[row['plot']] = 1
        else:
            plot_count[row['plot']] += 1

    for _, row in data4[['plot', 'year']].iterrows():
        if row['plot'] not in plot_count:
            plot_count[row['plot']] = 1
        else:
            plot_count[row['plot']] += 1
    
    plot_not_good = []
    for plot in plot_count.keys():
        if plot_count[plot] != 6:
            print(plot)
            plot_not_good.append(plot)

    return plot_not_good

def insert_plots_year(data1, data4):
    merge_data = pd.merge(data1, data4, on = ['plot', 'year', 'site', 'drought'])
    for _, row in merge_data.iterrows():
        cur.execute(
            '''
            INSERT INTO plots_year(plot_id, year, anpp, grass, forb, roots, litter, richness, evenness, carbon, nitrogen) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?) 
            '''
            , (row[['plot', 'year', 'anpp', 'grass', 'forb', 'root', 'litter', 'richness', 'evenness', 'C', 'N']])
        )
        conn.commit()

def insert_plots_year_species(data2):
    for _, row in data2.iterrows():
        cur.execute(
            '''
            INSERT INTO plots_year_species(plot_id, year, species_id, rel_cover) 
            VALUES (?,?,?,?) 
            '''
            , (row[['plot', 'year', 'species', 'rel.cover']])
        )
        conn.commit()

def insert_plots_month_vwc_ssm(data3,data6):
    pass

def main():
    data = load_csv()
    global conn, cur
    conn = create_connection('dataverse/data.sql')
    cur = conn.cursor()

    #confirm a plot has a specific drought condition
    #print(check_unique_drought(data[1]))

    #insert plots
    #plot already inserted
    #insert_new_plot(data[1][['plot', 'site', 'drought']])

    #insert species
    #species already inserted
    #insert_new_species(data[2][['species', 'func']])

    #check in a naive way if there is missing data between two files
    #already checked
    #print(find_bad_plot(data[1], data[4]))

    #insert plots_year
    #already inserted
    #insert_plots_year(data[1],data[4])

    #insert plots_year_species
    #already inserted
    #insert_plots_year_species(data[2])


main()





    




