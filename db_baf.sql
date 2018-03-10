-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 18, 2017 at 07:25 PM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_baf`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `ID` int(11) NOT NULL,
  `IDUser` int(11) NOT NULL,
  `IDJadwal` int(11) NOT NULL,
  `NoKursi` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `film`
--

CREATE TABLE `film` (
  `ID` int(11) NOT NULL,
  `Judul` varchar(50) NOT NULL,
  `Sinopsis` varchar(500) NOT NULL,
  `urlposter` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `film`
--

INSERT INTO `film` (`ID`, `Judul`, `Sinopsis`, `urlposter`) VALUES
(1, 'COCO', 'Miguel (Anthony Gonzalez) bermimpi untuk menjadi seorang musisi profesional seperti idolanya yang telah lama meninggal, Ernesto de la Cruz. Ia lalu menemukan dirinya secara ajaib masuk ke dalam alam kematian. \r\n\r\nMiguel berpetualang bersama Hector (Gael García Bernal) dan bertemu dengan nenek moyangnya yang melarang kehadiran musik di tengah keluarga mereka.', 'http://www.joblo.com/posters/images/full/coco-teaser-poster-gallery.jpg'),
(2, 'Star Wars: The Last Jedi', 'Rey (Daisy Ridley) akhirnya berhasil menemukan ksatria legendaris Jedi, Luke Skywalker (Mark Hamill) di sebuah pulau dengan aura magis. Para pahlawan dari The Force Awakens diantaranya Leia, Finn dan Poe bergabung dengan sang legenda dalam sebuah petualangan epik, yang membuka misteri kuno The Force dimasa lalu yang mengejutkan.', 'http://starwarsblog.starwars.com/wp-content/uploads/2017/10/the-last-jedi-theatrical-blog.jpg'),
(3, 'JUMANJI', 'Empat anak sekolah menemukan sebuah konsol permainan video game tua dengan permainan yang belum pernah mereka dengar bernama “Jumanji”. Mereka secara tidak sengaja “masuk” ke dalam permainan dan menjadi avatar yang mereka pilih.\r\n\r\nUntuk mengalahkan permainan dan kembali ke dunia nyata, mereka harus menjalani petualangan paling berbahaya dalam hidup mereka dan menemukan apa yang Alan Parrish tinggalkan 20 tahun yang lalu.', 'http://www.joblo.com/posters/images/full/jumanji-main-2.jpg'),
(4, 'FERDINAND', 'Seekor banteng besar bernama Ferdinand (John Cena) memiliki hati yang baik dan secara tidak disengaja dijual menjadi hewan buas untuk aduan. \r\n\r\nAkhirnya Ferdinand pun bertekad untuk kembali ke keluarganya dengan menempuh berbagai perjalanan. Ia ingin membuktikan bahwa siapapun tidak dapat menilai seekor banteng hanya dari wujudnya saja.', 'http://www.joblo.com/posters/images/full/FerdinandPoster-large1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `jadwal`
--

CREATE TABLE `jadwal` (
  `ID` int(11) NOT NULL,
  `IDFilm` int(11) NOT NULL,
  `Quota` int(2) NOT NULL,
  `Studio` int(1) NOT NULL,
  `JamTayang` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `jadwal`
--

INSERT INTO `jadwal` (`ID`, `IDFilm`, `Quota`, `Studio`, `JamTayang`) VALUES
(1, 1, 20, 1, '2017-12-17 12:00:00'),
(2, 1, 20, 1, '2017-12-17 14:00:00'),
(3, 2, 20, 2, '2017-12-18 12:00:00'),
(4, 2, 20, 2, '2017-12-18 14:00:00'),
(5, 3, 20, 3, '2017-12-17 12:00:00'),
(6, 3, 20, 3, '2017-12-17 14:00:00'),
(7, 4, 5, 4, '2017-12-17 12:00:00'),
(8, 4, 5, 3, '2017-12-17 14:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `ID` int(11) NOT NULL,
  `Nama` varchar(20) NOT NULL,
  `Username` varchar(10) NOT NULL,
  `Password` varchar(15) NOT NULL,
  `NoHP` varchar(15) NOT NULL,
  `Token` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`ID`, `Nama`, `Username`, `Password`, `NoHP`, `Token`) VALUES
(1, 'admin', 'admin', 'admin', '12345678', 500),
(2, 'dimas', 'edo', 'dimasraynal23', '71717', 100);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `IDUser` (`IDUser`,`IDJadwal`),
  ADD KEY `IDJadwal` (`IDJadwal`);

--
-- Indexes for table `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `jadwal`
--
ALTER TABLE `jadwal`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `IDFilm` (`IDFilm`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `film`
--
ALTER TABLE `film`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `jadwal`
--
ALTER TABLE `jadwal`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`IDJadwal`) REFERENCES `jadwal` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`IDUser`) REFERENCES `user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `jadwal`
--
ALTER TABLE `jadwal`
  ADD CONSTRAINT `jadwal_ibfk_1` FOREIGN KEY (`IDFilm`) REFERENCES `film` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
