CREATE TABLE plots (
    plot_id TEXT,
    site_located TEXT

    PRIMARY KEY (plot_id)
);

CREATE TABLE year (
    year INTEGER,
    PRIMARY KEY (year)
)

CREATE TABLE plots_year
    plot_id TEXT PRIMARY KEY
    REFERENCES plots(plot_id)
    ON DELET CASCADE,
    drought TEXT,
    anpp REAL,
    forb REAL,
    roots REAL,
    litter REAL,
    richness INTEGER,
    evenness REAL,
)
