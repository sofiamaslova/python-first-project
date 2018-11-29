START TRANSACTION;

ALTER TABLE `shop`.`product`
ADD COLUMN `image_id` INT(11) NULL DEFAULT NULL AFTER `category_id`,
ADD INDEX `fk_image_idx` (`image_id` ASC);

ALTER TABLE `shop`.`product`
ADD CONSTRAINT `fk_image`
  FOREIGN KEY (`image_id`)
  REFERENCES `shop`.`image` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION

ENGINE = InnoDB;

COMMIT;