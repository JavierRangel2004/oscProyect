-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 24-11-2024 a las 06:58:09
-- Versión del servidor: 8.0.29
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `osc_web`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `organizacion`
--

CREATE TABLE `organizacion` (
  `ID_Organizacion` int NOT NULL,
  `Nombre_Organizacion` char(100) NOT NULL,
  `ID_Sector` int NOT NULL,
  `Ubicacion` char(200) NOT NULL,
  `Redes_Sociales_1` char(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Redes_Sociales_2` char(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Pagina_Web` char(250) DEFAULT NULL,
  `Teléfono` bigint DEFAULT NULL,
  `correo` char(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `organizacion`
--

INSERT INTO `organizacion` (`ID_Organizacion`, `Nombre_Organizacion`, `ID_Sector`, `Ubicacion`, `Redes_Sociales_1`, `Redes_Sociales_2`, `Pagina_Web`, `Teléfono`, `correo`) VALUES
(1, 'Estancia Infantil Vasco de Quiroga I.A.P', 2, 'Ramón López Velarde # 7 colonia Lomas de Nuevo México', 'https://www.facebook.com/p/estancia-infantil-vasco-de-quiroga-iap-100064701769756/', NULL, '', 5552572088, NULL),
(2, 'Fundacion Semilla Durango', 2, 'Avenida General Lázaro Cárdenas esquina con Mascareñas 507 sur, Durango, Mexico', 'https://www.facebook.com/fundacionsemilla.dgo', '\r\nfundacionsemilla.dgo', NULL, 6188175359, 'fundacionsemilla.dgo@gmail.com'),
(3, 'Asilo Primavera, I.A.P.', 2, 'Choapan No. 29 Col. Hipódromo, Alcaldía Cuauhtémoc. C.P. 06100  Ciudad de México', NULL, NULL, 'https://www.asiloprimavera.org/', 5555150269, 'info@asiloprimavera.org'),
(4, 'Casa Hogar de las Niñas de Tláhuac, IAP', 2, 'Piraña #5 , Col. Del Mar , Alcaldía Tláhuac , Mexico City, Mexico', 'https://www.facebook.com/casahogartlahuac', NULL, NULL, 5558459323, 'contacto@casahogarninas-iap.org.mx'),
(5, ' Centro de Atención Integral de Labio y Paladar Hendido, A.C.', 1, 'Viaducto Miguel Alemán #121, Col. Escandón, I sección. Alcaldía Miguel Hidalgo casi esquina con Avenida Patriotismo. CDMX, México. CP. 03100', 'https://www.facebook.com/centrosumaorg/', 'https://instagram.com/lph.centrosuma?igshid=YmMyMTA2M2Y=', 'https://www.centrosuma.org/', 5552572088, 'info@centrosuma.org'),
(6, ' Damas Voluntarias del Instituto Nacional de Perinatología', 1, 'Montes Urales No, 800 Col. Virreyes, Alcaldía Miguel Hidalgo. CDMX 11000', 'https://es-la.facebook.com/pages/category/Community-Service/Damas-Voluntarias-INPER-155545378453704/', 'https://instagram.com/damasvoluntarias.inper?igshid=YzA2ZDJiZGQ=', 'https://www.damasvoluntariasinper.com/', 55209900, 'contacto@damasvoluntariasinper.com'),
(7, ' Escuela para Entrenamiento de Perros Guía Para Ciegos I.A.P.', 3, 'Avenida Canal Nacional número 1075, colonia Villa Quietud, Coyoacán, Ciudad de México, Código Postal 04960', 'https://www.facebook.com/perrosguiaiap', 'https://www.instagram.com/perrosguiaiap/', 'https://www.perrosguia.org.mx/', 5556731587, 'donativos@perrosguia.org.mx'),
(8, '  Asociación de Damas Voluntarias del Instituto Nacional de Pediatría, I.A.P.', 3, 'Calle Montes Urales, Blvd. de los Virreyes No, 800, Miguel Hidalgo, 11000 Ciudad de México, CDMX', 'https://www.facebook.com/damasvoluntariasINP/?ref=bookmarks', NULL, 'https://damasvoluntariasin.wixsite.com/misitio', NULL, 'damasvoluntariasinp@yahoo.com.mx'),
(9, 'Instituto Pedagógico para Problemas de Lenguaje, IAP (IPPPLIAP)', 3, 'Poussin 63, colonia San Juan, alcaldía Benito Juárez, C. P. 03730, Ciudad de México.', 'https://www.facebook.com/ippliap.educacion/', 'https://twitter.com/ippliapoficial?lang=es', 'https://ippliap.edu.mx/', 525555981120, 'ippliap@ippliap.edu.mx'),
(10, 'Fundación para la Asistencia Educativa FAE, I.A.P.', 2, 'Calle 27 #180 Col. El Sol, Nezahualcóyotl, Edo. de Méx. CP.57200', 'https://www.facebook.com/Fundaci%C3%B3n-FAE-250583648301397/', 'https://twitter.com/fundacionfae', 'https://fae.org.mx/', 5565856640, 'contacto@fae.org.mx');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programa`
--

CREATE TABLE `programa` (
  `ID_Programa` int NOT NULL,
  `Nombre_programa` char(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ID_Organizacion` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `programa`
--

INSERT INTO `programa` (`ID_Programa`, `Nombre_programa`, `ID_Organizacion`) VALUES
(1, 'Estancia Infantil', 1),
(2, 'Apoyo a niños indígenas', 2),
(3, 'Hogar Primavera', 3),
(4, 'Educación Formal', 3),
(5, 'Preparación Ética-Espiritual', 3),
(6, 'Salud Emocional', 3),
(7, 'Casa Hogar', 4),
(8, 'Cirugía Segura', 5),
(9, 'Atención Dental', 5),
(10, 'Nutrición y Lactancia', 5),
(11, 'Lenguaje y Estimulación temprana', 5),
(12, 'Apoyo emocional y vinculación familiar', 5),
(13, 'Programa Vida', 6),
(14, 'Diabetes Gestacional', 6),
(15, 'Programa Rafa', 6),
(16, 'Cardio', 6),
(17, 'Creando Sonrisas', 6),
(18, 'Ayudante Emergente', 6),
(19, 'Ayuda Prolongada', 6),
(20, 'Adopta', 7),
(21, 'Adopción temporal de cachorros', 7),
(22, 'Adopción definitiva', 7),
(23, 'H.V Consentidos', 7),
(24, 'Hospital Veterinario', 7),
(25, 'Obediencia básica', 7),
(26, 'Pensión canina', 7),
(27, 'Apadrinamiento', 8),
(28, 'Tanatología', 8),
(29, 'Ludoteca', 8),
(30, 'Acompañamiento', 8),
(31, 'Bazar de Maru', 8),
(32, 'Realiza tu sueño', 8),
(33, 'Escuela para sordos', 9),
(34, 'Programa de Atención a niños con problemas de Lenguaje y Aprendizaje', 9),
(35, 'Programa de jóvenes sordos', 9),
(36, 'Seminario Señalees', 9),
(37, 'Señalees para todos', 9),
(38, 'Capacitación en los estados', 9),
(39, 'Programa de prácticas educativas universitarias', 9),
(40, 'Educación Integral', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sector`
--

CREATE TABLE `sector` (
  `ID_Sector` int NOT NULL,
  `Sector_Nombre` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `sector`
--

INSERT INTO `sector` (`ID_Sector`, `Sector_Nombre`) VALUES
(1, 'Salud'),
(2, 'Infancia'),
(3, 'Apoyo Social');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `organizacion`
--
ALTER TABLE `organizacion`
  ADD PRIMARY KEY (`ID_Organizacion`);

--
-- Indices de la tabla `programa`
--
ALTER TABLE `programa`
  ADD PRIMARY KEY (`ID_Programa`);

--
-- Indices de la tabla `sector`
--
ALTER TABLE `sector`
  ADD PRIMARY KEY (`ID_Sector`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `organizacion`
--
ALTER TABLE `organizacion`
  MODIFY `ID_Organizacion` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `programa`
--
ALTER TABLE `programa`
  MODIFY `ID_Programa` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `sector`
--
ALTER TABLE `sector`
  MODIFY `ID_Sector` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
