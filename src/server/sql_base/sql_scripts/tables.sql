CREATE TABLE IF NOT EXISTS car_repair_shop(
    id INTEGER PRIMARY KEY,
    City VARCHAR(100) NOT NULL,
    Number VARCHAR(10) NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Address INTEGER NOT NULL,
    Service_id INTEGER NOT NULL,
    Spare_parts_id INTEGER NOT NULL,
    Staff_id INTEGER NOT NULL,
    FOREIGN KEY (Service_id) REFERENCES Service(id),
    FOREIGN KEY (Spare_parts_id) REFERENCES Spare_parts(id),
    FOREIGN KEY (Staff_id) REFERENCES Staff(id)
);


CREATE TABLE IF NOT EXISTS Car(
    id INTEGER PRIMARY KEY,
    Brand VARCHAR(100)  NOT NULL,
    Car_model VARCHAR(100)  NOT NULL,
    Year VARCHAR(100)  NOT NULL,
    Polomka_id INTEGER NOT NULL,
    Service_id INTEGER NOT NULL,
    Spare_parts_id INTEGER NOT NULL
    FOREIGN KEY (Polomka_id) REFERENCES Polomka(id),
    FOREIGN KEY (Service_id) REFERENCES Service(id),
    FOREIGN KEY (Spare_parts_id) REFERENCES Spare_parts(id)

);

CREATE TABLE IF NOT EXISTS Service(
    id INTEGER PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Price VARCHAR(50) NOT NULL,
    Time VARCHAR(100) NOT NULL,
    Spare_parts_id INTEGER NOT NULL,
    FOREIGN KEY (Spare_parts_id) REFERENCES Spare_parts(id)

);

CREATE TABLE IF NOT EXISTS Staff(
    id INTEGER PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Surname VARCHAR(100) NOT NULL,
    Patronymic VARCHAR(100) NOT NULL,
    Date VARCHAR(100) NOT NULL,
    Car_repair_shop VARCHAR(100) NOT NULL,
    Post_id INTEGER NOT NULL,
    FOREIGN KEY (Post_id) REFERENCES Post(id)
);

CREATE TABLE IF NOT EXISTS post(
    id INTEGER PRIMARY KEY,
    name_post VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS Order(
    id INTEGER PRIMARY KEY,
    Name_order VARCHAR(100) NOT NULL,
    Name_of_service INTEGER NOT NULL,
    Car_repair_shop_id INTEGER NOT NULL,
    FOREIGN KEY(Car_repair_shop_id) REFERENCES Car_repair_shop(id)
);

CREATE TABLE IF NOT EXISTS polomka(
    id INTEGER PRIMARY KEY,
    Name_of_polomka VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS Spare_parts(
    id INTEGER PRIMARY KEY,
    Name VARCHAR(150),
    Price VARCHAR(100),
    Delivery_time VARCHAR(100),
    The_brand_of_the_car VARCHAR(100),
    Car_model VARCHAR(100)
);
