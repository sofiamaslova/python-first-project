START TRANSACTION;

CREATE TABLE IF NOT EXISTS `blog` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ,
  `body` TEXT CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ,
  `product_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_blog_product_idx` (`product_id` ASC),
  CONSTRAINT `fk_blog_product`
    FOREIGN KEY (`product_id`)
    REFERENCES `shop`.`product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

ALTER TABLE `image`
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `product`
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `category`
CHANGE COLUMN `title` `title` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ,
CHANGE COLUMN `image url` `image url` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ,
CHANGE COLUMN `description` `description` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ;

ALTER TABLE `image`
CHANGE COLUMN `image_url` `image_url` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ,
CHANGE COLUMN `description` `description` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ;

ALTER TABLE `product`
CHANGE COLUMN `title` `title` VARCHAR(45) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ,
CHANGE COLUMN `description` `description` VARCHAR(255) CHARACTER SET 'utf8' COLLATE 'utf8_general_ci' NULL DEFAULT NULL ;

ALTER TABLE `shop`.`product`
ADD COLUMN `image_id` INT NULL AFTER `category_id`,
ADD INDEX `fk_images_idx` (`image_id` ASC);
;
ALTER TABLE `shop`.`product`
ADD CONSTRAINT `fk_images`
  FOREIGN KEY (`image_id`)
  REFERENCES `shop`.`image` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

COMMIT;

