CREATE TABLE `Shop_Electronic`.`Category` (
  `idCategory` INT NOT NULL AUTO_INCREMENT,
  `categoryName` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL,
  `parent_idCategory` INT NULL,
  PRIMARY KEY (`idCategory`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE `Shop_Electronic`.`Product` (
  `idProduct` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL,
  `categoryID` INT NOT NULL,
  `Description` VARCHAR(256) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL,
  `imageId` INT NOT NULL,
  `price` INT(11) NULL,
  PRIMARY KEY (`idProduct`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE `Shop_Electronic`.`image` (
  `idimage` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL,
  `url` VARCHAR(256) CHARACTER SET 'utf8' NULL,
  PRIMARY KEY (`idimage`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

ALTER TABLE `Shop_Electronic`.`image`
CHANGE COLUMN `name` `name` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ,
CHANGE COLUMN `url` `url` VARCHAR(256) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ;

CREATE TABLE `Shop_Electronic`.`brand` (
  `idbrand` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL,
  `image_id` INT NULL,
  PRIMARY KEY (`idbrand`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE `Shop_Electronic`.`feature` (
  `id_feature` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL,
  PRIMARY KEY (`id_feature`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
