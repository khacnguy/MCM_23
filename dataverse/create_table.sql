CREATE TABLE plots (
    plot_id TEXT,
    site_located TEXT
    drought TEXT,
    PRIMARY KEY (plot_id)
);

CREATE TABLE plots_year (
    plot_id TEXT,
    year INTEGER,
    anpp REAL,
    grass REAL,
    forb REAL,
    roots REAL,
    litter REAL,
    richness INTEGER,
    evenness REAL,
    carbon REAL,
    nitrogen REAL,

    PRIMARY KEY (plot_id, year),
    FOREIGN KEY (plot_id) REFERENCES plots(plot_id)
);

CREATE TABLE species (
    species TEXT,
    func TEXT,

    PRIMARY KEY (species)
);

CREATE TABLE plots_year_species(
    plot_id TEXT,
    year INTEGER,
    species TEXT,
    rel_cover REAL,

    PRIMARY KEY (plot_id, year, species),
    FOREIGN KEY (plot_id, year) REFERENCES plots_year(plot_id, year)
);

CREATE TABLE plots_month_vwc_ssm (
    plot_id TEXT,
    vwc REAL,
    ssm REAL,
    year INTEGER,
    month INTEGER,
    ppt INTEGER,
    Tmax REAL,
    Tmin REAL,
    Tave REAL,
    rs_ppt REAL,

    PRIMARY KEY (plot_id, year, month),
    FOREIGN KEY (plot_id, year) REFERENCES plots(plot_id, year)

);

