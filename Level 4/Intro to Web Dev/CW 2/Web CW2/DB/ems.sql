-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2022 at 01:09 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ems`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `searchmovie` (IN `movie` VARCHAR(1000))  NO SQL
SELECT * from movies where Movie_Name like CONCAT('%', movie, '%')$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('ramy', '123');

-- --------------------------------------------------------

--
-- Table structure for table `bookings`
--

CREATE TABLE `bookings` (
  `username` varchar(200) NOT NULL,
  `movie` varchar(200) NOT NULL,
  `theatre` varchar(200) NOT NULL,
  `seats` varchar(2000) NOT NULL,
  `date` varchar(100) NOT NULL,
  `movie_time` varchar(100) NOT NULL,
  `location` varchar(200) NOT NULL,
  `amount` int(200) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bookings`
--

INSERT INTO `bookings` (`username`, `movie`, `theatre`, `seats`, `date`, `movie_time`, `location`, `amount`, `id`) VALUES
('ramy', 'The Godfather', 'Cinema Galaxy', 'D4 D9', '15-05-2022', '10:00', 'Cairo Festival', 300, 20),
('ramy', 'Inception', 'Cinema Galaxy', 'C2 C3', '15-05-2022', '13:00', 'Cairo Festival', 400, 21),
('ramy', 'The Godfather', 'Cinema Galaxy', 'C2 C3', '16-05-2022', '10:00', 'Cairo Festival', 300, 22),
('ramy', 'The Godfather', 'Cinema Galaxy', 'C2 C3', '17-05-2022', '10:00', 'Cairo Festival', 300, 23);

-- --------------------------------------------------------

--
-- Table structure for table `movies`
--

CREATE TABLE `movies` (
  `Movie_Name` varchar(50) NOT NULL,
  `Actor` varchar(25) NOT NULL,
  `Actress` varchar(25) NOT NULL,
  `Release_date` varchar(50) NOT NULL,
  `Director` varchar(50) NOT NULL,
  `Movie_id` int(100) NOT NULL,
  `poster` varchar(300) NOT NULL,
  `RunTime` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `ActorImg` varchar(300) NOT NULL,
  `ActressImg` varchar(400) NOT NULL,
  `DirectorImg` varchar(300) NOT NULL,
  `Description` varchar(4000) DEFAULT NULL,
  `trailer` varchar(400) NOT NULL,
  `wiki` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `movies`
--

INSERT INTO `movies` (`Movie_Name`, `Actor`, `Actress`, `Release_date`, `Director`, `Movie_id`, `poster`, `RunTime`, `type`, `ActorImg`, `ActressImg`, `DirectorImg`, `Description`, `trailer`, `wiki`) VALUES
('The Shawshank Redemption', ' Tim Robbins, Morgan Free', '.', '1994-01-01', 'Frank Darabont', 29, 'd.jpg', '2 h 25 min', 'Drama', 'tom robinbins.jpg', 'MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_FMjpg_UX1000_.jpg', 'Frank.jpeg', 'Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse of Shawshank after being found guilty of a crime he did not commit.                     ', 'NmzuHjWmXOc', 'https://en.wikipedia.org/wiki/The_Shawshank_Redemption'),
('The Godfather', ' Marlon Brando, Al Pacino', 'Simonetta Stefanelli', '1972-01-01', 'Francis Ford Coppola', 30, 'Godfather.jpg', '2h 55m', 'Action', 'actorgodfather.jpg', 'Simonetta Stefanelli.png', 'godfather director.png', 'Ethan Hunt and his IMF team, along with some familiar allies, race against time after a mission gone wrong.                ', 'UaVTIH8mujA', 'https://en.wikipedia.org/wiki/The_Godfather'),
(' The Dark Knight', 'Christian Bale,   Heath L', 'Marion Cotillard', '2008-01-01', 'Christopher Nolan', 35, 'dark night poster.jpg', '2h 32m', 'Action', 'dark knight christian bale.jpg', 'dark knight actress.jpg', 'dark knight director.png', 'Set within a year after the events of Batman Begins (2005), Batman, Lieutenant James Gordon, and new District Attorney Harvey Dent successfully begin to round up the criminals that plague Gotham City, until a mysterious and sadistic criminal mastermind known only as \"The Joker\" appears in Gotham, creating a new wave of chaos.    ', 'EXeTwQWrcwY', 'https://en.wikipedia.org/wiki/The_Dark_Knight_(film)'),
('The Lord of the Rings: The Return of the King', ' Elijah Wood', 'Miranda Otto', '2003-01-01', ' Peter Jackson', 39, 'ringposter.jpg', '3h 21m', 'Action', 'MCDLOOF_EC265.png', 'MV5BMTQyMzM1ODgwMF5BMl5BanBnXkFtZTcwMzk2MTk2Mw@@._V1_.jpg', 'MV5BYjFjOThjMjgtYzM5ZS00Yjc0LTk5OTAtYWE4Y2IzMDYyZTI5XkEyXkFqcGdeQXVyMTMxMTIwMTE0._V1_.jpg', 'The final confrontation between the forces of good and evil fighting for control of the future of Middle-earth. Frodo and Sam reach Mordor in their quest to destroy the One Ring,      ', 'r5X-hFf6Bwo', 'https://en.wikipedia.org/wiki/The_Lord_of_the_Rings:_The_Return_of_the_King'),
('Forrest Gump', ' Tom Hanks', 'Robin Wright', '1994-01-01', ' Robert Zemeckis', 46, 'movieposter_en.jpg', '2h 22m', 'Drama', 'Forest_Gump_Character.jpg', 'MV5BMTU0NTc4MzEyOV5BMl5BanBnXkFtZTcwODY0ODkzMQ@@._V1_UY1200_CR105,0,630,1200_AL_.jpg', 'download.png', 'Forrest Gump is a simple man with a low I.Q. but good intentions. He is running through childhood with his best and only friend Jenny.    ', 'bLvqoHBptjg', 'https://en.wikipedia.org/wiki/Forrest_Gump'),
('Inception', ' Leonardo DiCaprio', 'Ellen Page', '2010-01-01', 'Christopher Nolan', 47, '14592148_max.jpg', '2h 28m', 'Drama', 'fb7d723063b32908cc7b27c5659e18b7.jpg', 'TELEMMGLPICT000026540914_trans_NvBQzQNjv4BqZTGkdds8SWJRzcZ4ZecXrYq2Y4EMYdWetKddigfEn-g.jpeg', 'Christopher-Nolan.jpg', 'Dom Cobb is a skilled thief, the absolute best in the dangerous art of extraction, stealing valuable secrets from deep within the subconscious during the dream state       ', 'YoHD9XEInc0', 'https://en.wikipedia.org/wiki/Inception'),
('Goodfellas', ' Robert De Niro', 'Lorraine Bracco', '1990-01-01', 'Martin Scorsese', 48, 'Goodfellas.png', '2h 55m', 'Drama', '8d291bb7fb47acc9c3c484a8583cecdd.jpg', '9f3f97e6dbcdc74a7cfb3469aba3e36c.jpg', 'director.png', 'Thugs of Hindostan is an upcoming 2018 Indian Hindi-language epic action-adventure film written and directed by Vijay Krishna Acharya. It is produced by Aditya Chopra under his banner Yash Raj Films. The film features Amitabh Bachchan, Aamir Khan, Katrina Kaif, Fatima Sana Shaikh and Lloyd Owen in lead roles. It follows a band of thugs led by Azaad (Bachchan), which functions during company rule in India and aspires to free the country from the British. Alarmed, John Clive (Owen), a British commander, sends Firangi Mallah (Khan), a small-time thug from Awadh, to counter the threat.[5] The soundtrack was composed by Ajay-Atul with lyrics written by Amitabh Bhattacharya.        ', '2ilzidi_J8Q', 'https://en.wikipedia.org/wiki/Thugs_of_Hindostan'),
('Back to the Future', 'Robert Zemeckis', 'Lea Thompson', '1985-01-01', 'Robert Zemeckis', 49, 'back-to-the-future-2-i114156.jpg', '1h 56m', 'Comedy', 'da88f0f4a8db3b64f16950db10f5ecbc.jpg', '5f05d34e5af6cc081b198588.png', 'bio_robert-zemeckis.jpg', 'Marty McFly, a typical American teenager of the Eighties, is accidentally sent back to 1955 in a plutonium-powered DeLorean  ', 'qvsgGtivCgs', 'https://en.wikipedia.org/wiki/Back_to_the_Future'),
('Venom', 'Tom Hardy', 'Michelle Williams', '2018-10-05', 'Ruben Fleischer', 50, 'venom_hardy_style_teaser_EB05938_B-893199_1024x1024@2x.png', '2 hr 10 min', 'Horror/Thriller', 'tomhardy.png', 'Michelle Williams.png', 'l-intro-1633133143.jpg', 'Venom is a 2018 American superhero film based on the Marvel Comics character of the same name, produced by Columbia Pictures in association with Marvel. Distributed by Sony Pictures Releasing, it is the first film in Sony Marvel Universe, adjunct to the Marvel Cinematic Universe .The film is directed by Ruben Fleischer from a screenplay by Scott Rosenberg, Jeff Pinkner, and Kelly Marcel, and stars Tom Hardy as Eddie Brock  Venom, alongside Michelle Williams, Riz Ahmed, Scott Haze, and Reid Scott. In Venom, journalist Brock gains superpowers after being bound to an alien symbiote whose species plans to invade Earth.     ', 'u9Mv98Gr5pY', 'https://en.wikipedia.org/wiki/Venom_(2018_film)'),
('Star Wars: Episode VI - Return of the Jedi', 'Mark Hamill', 'Carrie Fisher', '1983-01-01', ' Richard Marquand', 51, 'star-wars-episode-vi-return-of-the-jedi-i90220.jpg', '2h 11m', 'Action', 'DHUrjqcoUUQtVZAX4sjcnS.jpg', 'downloa2d.png', 'MV5BMjgwY2ZkYjEtNzgxZi00ZDIyLWJhZWItZjg1NGQ4OWE5ZTZhXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg', 'Luke Skywalker battles Jabba the Hutt and Darth Vader to save his comrades in the Rebel Alliance and triumph over the Galactic Empire  ', '5UfA_aKBGMc', 'https://en.wikipedia.org/wiki/Return_of_the_Jedi'),
(' Fight Club', ' Brad Pitt', 'Maria Singer', '1999-01-01', 'David Fincher', 52, '14290080_max.jpg', '2h 19m', 'Action', '5da0df57045a3101c27ebff4.png', 'Marla_01.png', 'downlo22ad.png', 'A nameless first person narrator (Edward Norton) attends support groups in attempt to subdue his emotional state and relieve his insomniac state  ', 'qtRKdVHc-cE', 'https://en.wikipedia.org/wiki/Fight_Club'),
('Interstellar', ' Matthew McConaughey', 'Anne Hathaway', '2014-01-01', ' Christopher Nolan', 53, 'downloaddddd.png', '2h 49m', 'Thriller', 'Matthew_McConaughey.png', 'bfae9a7854462afa925d7b8c6abb7613.jpg', 'directorr.png', '.    ', 'Lm8p5rlrSkY', 'https://en.wikipedia.org/wiki/Interstellar_(film)');

-- --------------------------------------------------------

--
-- Table structure for table `theatres`
--

CREATE TABLE `theatres` (
  `Theatre_id` int(200) NOT NULL,
  `Theatre_Name` varchar(200) NOT NULL,
  `Location` varchar(300) NOT NULL,
  `Movie_Name` varchar(200) NOT NULL,
  `time1` varchar(200) NOT NULL,
  `time2` varchar(200) NOT NULL,
  `time3` varchar(200) NOT NULL,
  `time4` varchar(200) NOT NULL,
  `time5` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `theatres`
--

INSERT INTO `theatres` (`Theatre_id`, `Theatre_Name`, `Location`, `Movie_Name`, `time1`, `time2`, `time3`, `time4`, `time5`) VALUES
(3, 'Cinema Multiplex', 'P90', 'The Shawshank Redemption', '22:00', '15:00', '', '', ''),
(4, 'Cinema Galaxy', 'Cairo Festival', 'The Godfather', '13:00', '10:00', '', '', ''),
(5, 'Cinema Multiplex', 'P90', ' The Dark Knight', '22:00', '', '', '', ''),
(6, 'Cinema Galaxy', 'Cairo Festival', 'The Lord of the Rings: The Return of the King', '17:00', '20:00', '', '', ''),
(7, 'Vox Cinema', 'Mall of Egypt', 'Forrest Gump', '20:00', '17:00', '', '', ''),
(8, 'Cinema Galaxy', 'Cairo Festival', 'Inception', '13:00', '', '', '', ''),
(10, 'Cinema Multiplex', 'Mall of Egypt', 'Goodfellas', '13:00', '10:00', '', '', ''),
(11, 'Cinema Galaxy', 'Cairo Festival', 'Back to the Future', '17:00', '23:00', '', '', ''),
(12, 'Vox Cinema', 'Mall of Egypt', 'Venom', '20:00', '', '', '', ''),
(13, 'Cinema Multiplex', 'P90', 'Star Wars: Episode VI - Return of the Jedi', '23:00', '', '', '', ''),
(14, 'Vox Cinema', 'Mall of Egypt', ' Fight Club', '16:00', '', '', '', ''),
(15, 'Cinema Multiplex', 'P90', 'Interstellar', '18:00', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `timings`
--

CREATE TABLE `timings` (
  `id` int(200) NOT NULL,
  `showtime` varchar(200) NOT NULL,
  `Theatre_Name` varchar(200) NOT NULL,
  `ticket_rate_Gold` int(50) NOT NULL,
  `ticket_rate_Silver` int(50) NOT NULL,
  `seats` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timings`
--

INSERT INTO `timings` (`id`, `showtime`, `Theatre_Name`, `ticket_rate_Gold`, `ticket_rate_Silver`, `seats`) VALUES
(5, '13:00', 'Cinema Galaxy', 200, 180, 108),
(6, '10:00', 'Cinema Galaxy', 150, 120, 114),
(7, '09:00', 'Vox Cinema', 150, 100, 120),
(8, '13:00', 'Vox Cinema', 200, 180, 130),
(9, '17:00', 'Vox Cinema', 200, 150, 120),
(10, '20:00', 'Vox Cinema', 250, 200, 120),
(11, '10:00', 'P90', 150, 100, 120),
(12, '22:00', 'P90', 250, 220, 113),
(13, '22:00', 'Vox Cinema', 200, 180, 120),
(14, '13:00', 'P90', 200, 180, 150),
(15, '17:00', 'P90', 250, 220, 120),
(16, '20:00', 'P90', 300, 280, 120),
(17, '20:00', 'Cinema Galaxy', 250, 220, 120),
(18, '17:00', 'Cinema Galaxy', 250, 200, 120),
(19, '23:00', 'Cinema Galaxy', 250, 210, 120),
(20, '23:00', 'P90', 250, 220, 120),
(21, '16:00', 'Vox Cinema', 250, 180, 120);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `email`, `password`) VALUES
('ramy', 'test@gmail.com', '$2y$10$4Wthy9P6iEjKG8Qc4IUNpuMRpGc9BSFDJMFYVFJqbGEuQ/BiR/54K');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `bookings`
--
ALTER TABLE `bookings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`Movie_id`);

--
-- Indexes for table `theatres`
--
ALTER TABLE `theatres`
  ADD PRIMARY KEY (`Theatre_id`);

--
-- Indexes for table `timings`
--
ALTER TABLE `timings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookings`
--
ALTER TABLE `bookings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `movies`
--
ALTER TABLE `movies`
  MODIFY `Movie_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `theatres`
--
ALTER TABLE `theatres`
  MODIFY `Theatre_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `timings`
--
ALTER TABLE `timings`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
