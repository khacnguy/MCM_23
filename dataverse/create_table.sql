CREATE TABLE sites(
    site_id TEXT,
    PRIMARY KEY (site_id)
);

CREATE TABLE plots (
    plot_id TEXT,
    site_id TEXT,
    drought TEXT,

    PRIMARY KEY (plot_id),
    FOREIGN KEY (site_id) REFERENCES sites (site_id)
);

CREATE TABLE species (
    species_id TEXT,
    func TEXT,

    PRIMARY KEY (species_id)
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
    ON DELETE CASCADE
);

CREATE TABLE plots_year_species(
    plot_id TEXT,
    year INTEGER,
    species_id TEXT,
    rel_cover REAL,

    PRIMARY KEY (plot_id, year, species_id),
    FOREIGN KEY (plot_id, year) REFERENCES plots_year(plot_id, year)
    ON DELETE CASCADE,
    FOREIGN KEY (species_id) REFERENCES species(species_id)
    ON DELETE CASCADE
);

CREATE TABLE plots_month_vwc (
    plot_id TEXT,
    vwc REAL,
    month INTEGER,
    year INTEGER,

    PRIMARY KEY (plot_id, month, year),
    FOREIGN KEY (plot_id) REFERENCES plots (plot_id)
    ON DELETE CASCADE
);

CREATE TABLE sites_month (
    site_id TEXT,
    year INTEGER,
    month INTEGER, 
    ppt INTEGER,
    Tmax REAL,
    Tmin REAL,
    Tave REAL,
    rs_ppt REAL,

    PRIMARY KEY (site_id, year, month),
    FOREIGN KEY (site_id) REFERENCES sites(site_id)
    ON DELETE CASCADE
);

