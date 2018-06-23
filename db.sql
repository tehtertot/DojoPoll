-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema dojoPolls
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojoPolls` ;

-- -----------------------------------------------------
-- Schema dojoPolls
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojoPolls` DEFAULT CHARACTER SET utf8 ;
USE `dojoPolls` ;

-- -----------------------------------------------------
-- Table `dojoPolls`.`polls`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojoPolls`.`polls` ;

CREATE TABLE IF NOT EXISTS `dojoPolls`.`polls` (
  `room_id` VARCHAR(5) NOT NULL,
  `title` VARCHAR(45) NULL,
  `admin` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` TIMESTAMP NULL DEFAULT NOW(),
  `updated_at` TIMESTAMP NULL DEFAULT NOW() on update NOW(),
  PRIMARY KEY (`room_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojoPolls`.`responses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dojoPolls`.`responses` ;

CREATE TABLE IF NOT EXISTS `dojoPolls`.`responses` (
  `response_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `response` TEXT NULL,
  `created_at` TIMESTAMP NULL DEFAULT NOW(),
  `updated_at` TIMESTAMP NULL DEFAULT NOW() on update NOW(),
  `poll_id` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`response_id`),
  INDEX `fk_responses_polls_idx` (`poll_id` ASC),
  CONSTRAINT `fk_responses_polls`
    FOREIGN KEY (`poll_id`)
    REFERENCES `dojoPolls`.`polls` (`room_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
