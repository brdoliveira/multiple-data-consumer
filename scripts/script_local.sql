-- Criação da tabela 'users'
CREATE TABLE users (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    name_user VARCHAR(255),
    email_user VARCHAR(255),
    pass_user VARCHAR(255),
    created_at DATETIME
);

-- Criação da tabela 'trucks'
CREATE TABLE trucks (
    id_truck AUTO_INCREMENT INT PRIMARY KEY,
    created_at DATETIME,
    fk_user INT,
    FOREIGN KEY (fk_user) REFERENCES users(id_user)
);

-- Criação da tabela 'reads'
CREATE TABLE reads (
    id_read INT PRIMARY KEY AUTO_INCREMENT,
    temperature FLOAT,
    umidity FLOAT,
    vibration FLOAT,
    noise FLOAT,
    proximity FLOAT,
    weight FLOAT,
    latitude FLOAT,
    created_at DATETIME,
    fk_truck INT,
    fk_route INT,
    FOREIGN KEY (fk_route) REFERENCES routes(id_route)
);

-- Criação da tabela 'routes'
CREATE TABLE routes (
    id_route INT AUTO_INCREMENT PRIMARY KEY,
    name_route VARCHAR(255),
    lat_inicial DECIMAL(10, 8),
    long_inicial DECIMAL(11, 8),
    lat_final DECIMAL(10, 8),
    long_final DECIMAL(11, 8),
    fk_truck INT,
    FOREIGN KEY (fk_truck) REFERENCES trucks(id_truck)
);