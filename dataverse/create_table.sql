DROP TABLE IF EXISTS plots;
DROP TABLE IF EXISTS plots_year;
DROP TABLE IF EXISTS species;
DROP TABLE IF EXISTS plots_year_species;
DROP TABLE IF EXISTS plots_month_vwc_ssm;

CREATE TABLE plots (
    plot_id TEXT,
    site_located TEXT,
    drought TEXT,

    PRIMARY KEY (plot_id)
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
    ON DELETE CASCADE
    FOREIGN KEY (species_id) REFERENCES species(species_id)
    ON DELETE CASCADE
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
    ON DELETE CASCADE

);

