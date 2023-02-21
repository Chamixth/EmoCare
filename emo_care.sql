-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 21, 2023 at 09:36 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `emo_care`
--

-- --------------------------------------------------------

--
-- Table structure for table `album`
--

CREATE TABLE `album` (
  `albumNo` int(10) NOT NULL,
  `albumType` varchar(20) NOT NULL,
  `albumTitle` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `consultation`
--

CREATE TABLE `consultation` (
  `consultationRefId` int(10) NOT NULL,
  `patientId` int(10) NOT NULL,
  `therapistId` int(10) NOT NULL,
  `consultDate` varchar(10) NOT NULL,
  `consultTime` varchar(10) NOT NULL,
  `consultCost` varchar(10) NOT NULL,
  `consultDuration` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `live_session`
--

CREATE TABLE `live_session` (
  `liveMeetingId` int(10) NOT NULL,
  `meetingTime` varchar(10) NOT NULL,
  `meetingDate` varchar(10) NOT NULL,
  `meetingTitle` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `locationCode` varchar(10) NOT NULL,
  `registeredTherapistNo` varchar(10) NOT NULL,
  `registeredPatientNo` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `patientId` int(10) NOT NULL,
  `registeredPatientNo` varchar(10) NOT NULL,
  `firstName` varchar(100) NOT NULL,
  `lastName` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `photo`
--

CREATE TABLE `photo` (
  `photoId` int(10) NOT NULL,
  `liveMeetingId` int(10) NOT NULL,
  `recordedMeetingId` int(10) NOT NULL,
  `albumNo` int(10) NOT NULL,
  `photoType` varchar(30) NOT NULL,
  `photoDescription` varchar(1000) NOT NULL,
  `photoUploadDate` varchar(10) NOT NULL,
  `photoViewCount` varchar(10) NOT NULL,
  `photoTitle` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `recorded_session`
--

CREATE TABLE `recorded_session` (
  `recordedMeetingId` int(10) NOT NULL,
  `meetingTime` varchar(10) NOT NULL,
  `meetingDate` varchar(10) NOT NULL,
  `meetingTitle` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `reportId` int(10) NOT NULL,
  `therapistId` int(10) NOT NULL,
  `reportType` varchar(30) NOT NULL,
  `reportTitle` varchar(30) NOT NULL,
  `reportDescription` varchar(1000) NOT NULL,
  `recordedMeetingId` int(10) NOT NULL,
  `liveMeetingId` int(10) NOT NULL,
  `issueDate` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `therapist`
--

CREATE TABLE `therapist` (
  `therapistId` int(10) NOT NULL,
  `registeredTherapistNo` varchar(10) NOT NULL,
  `firstName` varchar(100) NOT NULL,
  `lastName` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `unregistered_user`
--

CREATE TABLE `unregistered_user` (
  `unregisteredUserNo` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `album`
--
ALTER TABLE `album`
  ADD PRIMARY KEY (`albumNo`);

--
-- Indexes for table `consultation`
--
ALTER TABLE `consultation`
  ADD PRIMARY KEY (`consultationRefId`),
  ADD KEY `therapistId` (`therapistId`),
  ADD KEY `patientId` (`patientId`);

--
-- Indexes for table `live_session`
--
ALTER TABLE `live_session`
  ADD PRIMARY KEY (`liveMeetingId`);

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`locationCode`),
  ADD KEY `registeredPatientNo` (`registeredPatientNo`),
  ADD KEY `registeredTherapistNo` (`registeredTherapistNo`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`patientId`);

--
-- Indexes for table `photo`
--
ALTER TABLE `photo`
  ADD PRIMARY KEY (`photoId`),
  ADD KEY `liveMeetingId` (`liveMeetingId`),
  ADD KEY `recordedMeetingId` (`recordedMeetingId`),
  ADD KEY `albumNo` (`albumNo`);

--
-- Indexes for table `recorded_session`
--
ALTER TABLE `recorded_session`
  ADD PRIMARY KEY (`recordedMeetingId`);

--
-- Indexes for table `report`
--
ALTER TABLE `report`
  ADD PRIMARY KEY (`reportId`),
  ADD KEY `liveMeetingId` (`liveMeetingId`),
  ADD KEY `recordedMeetingId` (`recordedMeetingId`),
  ADD KEY `therapistId` (`therapistId`);

--
-- Indexes for table `therapist`
--
ALTER TABLE `therapist`
  ADD PRIMARY KEY (`therapistId`);

--
-- Indexes for table `unregistered_user`
--
ALTER TABLE `unregistered_user`
  ADD PRIMARY KEY (`unregisteredUserNo`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `consultation`
--
ALTER TABLE `consultation`
  ADD CONSTRAINT `consultation_ibfk_1` FOREIGN KEY (`therapistId`) REFERENCES `consultation` (`consultationRefId`),
  ADD CONSTRAINT `consultation_ibfk_2` FOREIGN KEY (`patientId`) REFERENCES `consultation` (`consultationRefId`);

--
-- Constraints for table `location`
--
ALTER TABLE `location`
  ADD CONSTRAINT `location_ibfk_1` FOREIGN KEY (`registeredPatientNo`) REFERENCES `location` (`locationCode`),
  ADD CONSTRAINT `location_ibfk_2` FOREIGN KEY (`registeredTherapistNo`) REFERENCES `location` (`locationCode`);

--
-- Constraints for table `photo`
--
ALTER TABLE `photo`
  ADD CONSTRAINT `photo_ibfk_1` FOREIGN KEY (`liveMeetingId`) REFERENCES `photo` (`photoId`),
  ADD CONSTRAINT `photo_ibfk_2` FOREIGN KEY (`recordedMeetingId`) REFERENCES `photo` (`photoId`),
  ADD CONSTRAINT `photo_ibfk_3` FOREIGN KEY (`albumNo`) REFERENCES `photo` (`photoId`);

--
-- Constraints for table `report`
--
ALTER TABLE `report`
  ADD CONSTRAINT `report_ibfk_1` FOREIGN KEY (`liveMeetingId`) REFERENCES `report` (`reportId`),
  ADD CONSTRAINT `report_ibfk_2` FOREIGN KEY (`recordedMeetingId`) REFERENCES `report` (`reportId`),
  ADD CONSTRAINT `report_ibfk_3` FOREIGN KEY (`therapistId`) REFERENCES `report` (`reportId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
