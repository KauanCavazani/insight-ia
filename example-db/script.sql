-- Criar o banco de dados
CREATE DATABASE loja;

-- Usar o banco de dados recém-criado
USE loja;

-- Criar a tabela de Usuários
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_registro DATE NOT NULL
);

-- Criar a tabela de Endereços
CREATE TABLE enderecos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    rua VARCHAR(150) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    cep VARCHAR(20) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Criar a tabela de Pedidos
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    produto VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    data_pedido DATE NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Inserir dados na tabela de Usuários
INSERT INTO usuarios (nome, idade, email, data_registro) VALUES
('Alice Souza', 28, 'alice.souza@email.com', '2023-01-15'),
('Bruno Lima', 35, 'bruno.lima@email.com', '2023-02-20'),
('Carla Pereira', 22, 'carla.pereira@email.com', '2023-03-10'),
('Diego Rocha', 42, 'diego.rocha@email.com', '2023-04-05'),
('Elaine Silva', 30, 'elaine.silva@email.com', '2023-05-12'),
('Fernando Alves', 45, 'fernando.alves@email.com', '2023-06-22'),
('Gisele Santos', 31, 'gisele.santos@email.com', '2023-07-14'),
('Hugo Mendes', 29, 'hugo.mendes@email.com', '2023-08-03'),
('Isabela Costa', 38, 'isabela.costa@email.com', '2023-09-11'),
('João Martins', 33, 'joao.martins@email.com', '2023-10-21'),
('Karina Duarte', 27, 'karina.duarte@email.com', '2023-11-02'),
('Lucas Ferreira', 40, 'lucas.ferreira@email.com', '2023-12-12'),
('Mariana Monteiro', 36, 'mariana.monteiro@email.com', '2023-01-30'),
('Nathalia Ramos', 24, 'nathalia.ramos@email.com', '2023-02-13'),
('Otavio Sousa', 32, 'otavio.sousa@email.com', '2023-03-18'),
('Patricia Andrade', 26, 'patricia.andrade@email.com', '2023-04-25'),
('Ricardo Teixeira', 34, 'ricardo.teixeira@email.com', '2023-05-29'),
('Sabrina Farias', 29, 'sabrina.farias@email.com', '2023-06-17'),
('Thiago Moura', 31, 'thiago.moura@email.com', '2023-07-07'),
('Ursula Brito', 41, 'ursula.brito@email.com', '2023-08-20');

-- Inserir dados na tabela de Endereços
INSERT INTO enderecos (usuario_id, rua, cidade, estado, cep) VALUES
(1, 'Rua A, 123', 'São Paulo', 'SP', '01000-000'),
(2, 'Rua B, 456', 'Rio de Janeiro', 'RJ', '20000-000'),
(3, 'Rua C, 789', 'Belo Horizonte', 'MG', '30000-000'),
(4, 'Rua D, 101', 'Curitiba', 'PR', '80000-000'),
(5, 'Rua E, 202', 'Porto Alegre', 'RS', '90000-000'),
(6, 'Rua F, 303', 'Recife', 'PE', '50000-000'),
(7, 'Rua G, 404', 'Salvador', 'BA', '40000-000'),
(8, 'Rua H, 505', 'Fortaleza', 'CE', '60000-000'),
(9, 'Rua I, 606', 'Florianópolis', 'SC', '88000-000'),
(10, 'Rua J, 707', 'Brasília', 'DF', '70000-000'),
(11, 'Rua K, 808', 'Goiânia', 'GO', '74000-000'),
(12, 'Rua L, 909', 'Belém', 'PA', '66000-000'),
(13, 'Rua M, 1010', 'Manaus', 'AM', '69000-000'),
(14, 'Rua N, 1111', 'Campo Grande', 'MS', '79000-000'),
(15, 'Rua O, 1212', 'João Pessoa', 'PB', '58000-000'),
(16, 'Rua P, 1313', 'Maceió', 'AL', '57000-000'),
(17, 'Rua Q, 1414', 'Natal', 'RN', '59000-000'),
(18, 'Rua R, 1515', 'Teresina', 'PI', '64000-000'),
(19, 'Rua S, 1616', 'Aracaju', 'SE', '49000-000'),
(20, 'Rua T, 1717', 'Cuiabá', 'MT', '78000-000');

-- Inserir dados na tabela de Pedidos
INSERT INTO pedidos (usuario_id, produto, quantidade, data_pedido, valor_total) VALUES
(1, 'Notebook', 1, '2023-06-01', 3500.00),
(2, 'Mouse', 2, '2023-06-15', 150.00),
(3, 'Teclado', 1, '2023-07-05', 200.00),
(4, 'Monitor', 1, '2023-08-10', 1200.00),
(5, 'Impressora', 1, '2023-09-01', 800.00),
(6, 'Cadeira Gamer', 1, '2023-06-18', 700.00),
(7, 'Webcam', 2, '2023-07-22', 400.00),
(8, 'Headset', 1, '2023-08-12', 300.00),
(9, 'HD Externo', 1, '2023-09-21', 500.00),
(10, 'SSD', 1, '2023-10-02', 350.00),
(11, 'Smartphone', 1, '2023-06-03', 2500.00),
(12, 'Tablet', 1, '2023-07-14', 1200.00),
(13, 'Notebook', 1, '2023-08-07', 4000.00),
(14, 'Smartwatch', 1, '2023-09-19', 800.00),
(15, 'Mouse', 3, '2023-10-11', 225.00),
(16, 'Teclado Mecânico', 1, '2023-11-05', 450.00),
(17, 'Monitor 4K', 1, '2023-12-01', 1500.00),
(18, 'Mousepad', 1, '2023-11-15', 50.00),
(19, 'Roteador', 1, '2023-12-10', 600.00),
(20, 'Notebook', 1, '2023-12-20', 3200.00);