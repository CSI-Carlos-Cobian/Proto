-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema protoapi_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema protoapi_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `protoapi_db` DEFAULT CHARACTER SET utf8 ;
USE `protoapi_db` ;

-- -----------------------------------------------------
-- Table `protoapi_db`.`type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `protoapi_db`.`type` (
  `idtype` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtype`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `protoapi_db`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `protoapi_db`.`user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`iduser`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `protoapi_db`.`record`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `protoapi_db`.`record` (
  `idrecord` INT NOT NULL AUTO_INCREMENT,
  `type_idtype` INT NOT NULL,
  `timestamp` INT NOT NULL,
  `user_iduser` INT NOT NULL,
  `ammount` DOUBLE NULL,
  PRIMARY KEY (`idrecord`),
  INDEX `fk_record_type_idx` (`type_idtype` ASC),
  INDEX `fk_record_user1_idx` (`user_iduser` ASC),
  CONSTRAINT `fk_record_type`
    FOREIGN KEY (`type_idtype`)
    REFERENCES `protoapi_db`.`type` (`idtype`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_record_user1`
    FOREIGN KEY (`user_iduser`)
    REFERENCES `protoapi_db`.`user` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Manual inclusion of proto user
-- -----------------------------------------------------
CREATE USER 'protoapi'@'%' IDENTIFIED BY '4dHocHomeworkPr0t0' ; 
GRANT ALL PRIVILEGES ON *.* TO 'protoapi'@'%';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'protoapi'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;