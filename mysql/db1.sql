CREATE TABLE `shop`.`product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `price` INT UNSIGNED NULL,
  `description` VARCHAR(255) NULL,
  `category_id` INT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `shop`.`category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `image url` VARCHAR(255) NULL,
  `description` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

ALTER TABLE `shop`.`product`
ADD INDEX `fk_category_idx` (`category_id` ASC);
;
ALTER TABLE `shop`.`product`
ADD CONSTRAINT `fk_category`
  FOREIGN KEY (`category_id`)
  REFERENCES `shop`.`category` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

CREATE TABLE `shop`.`image` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `image_url` VARCHAR(255) NULL,
  `description` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));
ALTER TABLE `shop`.`image`
ADD COLUMN `product_id` INT NULL AFTER `description`;

ALTER TABLE `shop`.`image`
ADD INDEX `fk_product_idx` (`product_id` ASC);
;
ALTER TABLE `shop`.`image`
ADD CONSTRAINT `fk_product`
  FOREIGN KEY (`product_id`)
  REFERENCES `shop`.`image` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;