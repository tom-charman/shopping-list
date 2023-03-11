CREATE TABLE products
(
    pid               SERIAL       PRIMARY KEY,
    name              varchar(255) NOT NULL
);


CREATE TABLE recipes
(
    rec_id          SERIAL          PRIMARY KEY,
    name            varchar(120)    NOT NULL,
    description     text            NOT NULL,
    DishSize        integer         NOT NULL
);


CREATE TABLE productsToRecipes
(
    rec_id          integer         REFERENCES recipes (rec_id),
    pid             integer         REFERENCES products (pid),
    quantity        integer         NOT NULL,
    quantity_unit   varchar(100)    NOT NULL,
    PRIMARY KEY(rec_Id, pid)
);
