import sqlite3
import matplotlib.pyplot as plt



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

def get_data1(year, drought):
    cur.execute(
        '''
            with averageVWC (plot_id, avwc) as (
                SELECT plot_id, SUM (vwc)
                FROM plots_month_vwc pmv
                WHERE year = ?
                GROUP BY plot_id
            )
            SELECT py.plot_id, evenness, drought, avwc
            FROM plots_year py, plots p, averageVWC
            WHERE py.year = ?
            AND averageVWC.plot_id = p.plot_id
            AND p.plot_id = py.plot_id
            AND p.drought = ?;
        '''
        , (year, year, drought)
    )
    return cur.fetchall()

def year_drought_avwc_evenness():
    data_ambient = {}
    data_reduced = {}
    for year in [2017,2018,2019]:    
        data_ambient[year] = get_data1(year, 'ambient')
        data_reduced[year] = get_data1(year, 'reduced')
    fig, axs = plt.subplots(3,2)
    for year_idx in range (3):
        for drought_idx in range (2):
            if drought_idx == 0:
                x = [x[3] for x in data_ambient[year_idx + 2017]]
                y = [x[1] for x in data_ambient[year_idx + 2017]]
            else:
                x = [x[3] for x in data_reduced[year_idx + 2017]]
                y = [x[1] for x in data_reduced[year_idx + 2017]]
            axs[year_idx, drought_idx].scatter(x,y)
            axs[year_idx, drought_idx].set(xlim = (0,2.5), ylim = (0, 1))
    for ax in axs.flat:
        ax.set(xlabel = 'vwc', ylabel = 'evenness')
    plt.show() 

def year_evenness_drought():
    data_ambient = {}
    data_reduced = {}
    for year in [2017,2018,2019]:    
        data_ambient[year] = get_data2(year, 'ambient')
        data_reduced[year] = get_data2(year, 'reduced')
    fig, axs = plt.subplots(3,2)
    for year_idx in range (3):
        for drought_idx in range (2):
            if drought_idx == 0:
                y = [x[1] for x in data_ambient[year_idx + 2017]]
            else:
                y = [x[1] for x in data_reduced[year_idx + 2017]]
            axs[year_idx, drought_idx].boxplot(y)
            axs[year_idx, drought_idx].set(ylim = (0, 1))

    for ax in axs.flat:
        ax.set(xlabel = 'number of species', ylabel = 'evenness')
    plt.show() 

def get_data2(year, drought):
    cur.execute(
        '''
            with numberOfSpecies (plot_id, cnt) as (
                SELECT plot_id, COUNT(species_id)
                FROM plots_year_species
                WHERE year = ?
                GROUP BY plot_id
            )
            SELECT py.plot_id, evenness, drought, cnt
            FROM plots_year py, plots p, numberOfSpecies nos
            WHERE py.year = ?
            AND nos.plot_id = p.plot_id
            AND p.plot_id = py.plot_id
            AND p.drought = ?;
        '''
        , (year, year, drought)
    )
    return cur.fetchall()

def year_evenness_drought_noSpecies():
    data_ambient = {}
    data_reduced = {}
    for year in [2017,2018,2019]:    
        data_ambient[year] = get_data2(year, 'ambient')
        data_reduced[year] = get_data2(year, 'reduced')
    fig, axs = plt.subplots(3,2)
    for year_idx in range (3):
        for drought_idx in range (2):
            if drought_idx == 0:
                x = [x[3] for x in data_ambient[year_idx + 2017]]
                y = [x[1] for x in data_ambient[year_idx + 2017]]
            else:
                x = [x[3] for x in data_reduced[year_idx + 2017]]
                y = [x[1] for x in data_reduced[year_idx + 2017]]
            axs[year_idx, drought_idx].scatter(x,y)
            axs[year_idx, drought_idx].set(xlim = (0,30), ylim = (0, 1))
    for ax in axs.flat:
        ax.set(xlabel = 'number of species ', ylabel = 'evenness')
    plt.show() 


def main():
    global conn, cur
    conn = create_connection('dataverse/data.sql')
    cur = conn.cursor()
     
    #year_drought_avwc_evenness()
    
    #year_evenness_drought()

    #year_evenness_drought_noSpecies()

    #year_
    
main()
