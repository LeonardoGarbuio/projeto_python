-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 06/12/2025 às 20:20
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `telas_python`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `hamburguer`
--

CREATE TABLE `hamburguer` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `molho` varchar(255) NOT NULL,
  `carne` varchar(255) NOT NULL,
  `queijo` varchar(255) NOT NULL,
  `pao` varchar(255) NOT NULL,
  `bacon` int(11) NOT NULL,
  `ovo` int(11) NOT NULL,
  `picles` int(11) NOT NULL,
  `tomate` int(11) NOT NULL,
  `cebola` int(11) NOT NULL,
  `alface` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `hamburguer`
--

INSERT INTO `hamburguer` (`id`, `nome`, `molho`, `carne`, `queijo`, `pao`, `bacon`, `ovo`, `picles`, `tomate`, `cebola`, `alface`) VALUES
(1, 'Frango Cremoso', 'Maionese', 'Frango', 'Cheddar', '3 Queijos', 0, 0, 0, 0, 0, 1),
(2, 'Clássico Cheddar', 'Ketchup', 'Bovina', 'Cheddar', '3 Queijos', 1, 0, 0, 1, 1, 1),
(3, 'Veggie Delícia', 'Maionese', 'Vegana', 'Mussarela', 'Gergelim', 0, 0, 1, 1, 1, 1),
(4, 'Australiana', 'Barbecue', 'Frango', 'Prato', 'Australiano', 1, 1, 0, 1, 0, 1),
(5, 'Bacon Lovers', 'Mostarda', 'Suína', 'Suíço', 'Francês', 1, 1, 0, 0, 0, 0),
(6, 'Ovo & Bacon Clássico', 'Ketchup', 'Bovina', 'Cheddar', 'Francês', 1, 1, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `usuario` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `login`
--

INSERT INTO `login` (`id`, `usuario`, `senha`) VALUES
(1, 'gerente', '123'),
(2, 'cozinheiro', '123'),
(3, 'yas', '123');

-- --------------------------------------------------------

--
-- Estrutura para tabela `pedidos`
--

CREATE TABLE `pedidos` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_hamburguer` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `hamburguer`
--
ALTER TABLE `hamburguer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nome` (`nome`);

--
-- Índices de tabela `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`usuario`);

--
-- Índices de tabela `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_pedido_usuario` (`id_usuario`),
  ADD KEY `fk_pedido_hamburguer` (`id_hamburguer`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `hamburguer`
--
ALTER TABLE `hamburguer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `fk_pedido_hamburguer` FOREIGN KEY (`id_hamburguer`) REFERENCES `hamburguer` (`id`),
  ADD CONSTRAINT `fk_pedido_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `login` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
