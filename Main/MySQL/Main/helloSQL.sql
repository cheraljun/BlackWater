SET SQL_SAFE_UPDATES = 0;

SHOW DATABASES;

DROP DATABASE `helloSQL`;
CREATE DATABASE `helloSQL`;

USE `helloSQL`;
CREATE TABLE `student`(
`student_id` INT,
`name` VARCHAR(20),
`major` VARCHAR(20),
PRIMARY KEY(`student_id`)
);
DESCRIBE `student`;
ALTER TABLE `student` ADD `gpa` DECIMAL(3,2);
DESCRIBE `student`;
ALTER TABLE `student` DROP COLUMN `gpa`; 
DESCRIBE `student`;

INSERT INTO `student` VALUES(1,'小白','历史');
INSERT INTO `student` VALUES(2,'小黑','生物');
INSERT INTO `student` VALUES(3,'小绿','英语');
INSERT INTO `student` VALUES(4,'小蓝',NULL);

INSERT INTO `student`(`name`,`major`,`student_id`) VALUES('小蓝','英语',5);
SELECT * FROM `student`;

-- constraints
DROP TABLE `student`;
CREATE TABLE `student`(
`student_id` INT,
`name` VARCHAR(20) NOT NULL, -- 不能为空
`major` VARCHAR(20) UNIQUE, -- 唯一
PRIMARY KEY(`student_id`)
);
INSERT INTO `student` VALUES(1,'小白','历史');
INSERT INTO `student` VALUES(2,'小黑','英语');
SELECT * FROM `student`;

DROP TABLE `student`;
CREATE TABLE `student`(
`student_id` INT,
`name` VARCHAR(20) NOT NULL,
`major` VARCHAR(20) DEFAULT '历史', -- 预设值
PRIMARY KEY(`student_id`)
);
INSERT INTO `student`(`name`,`student_id`) VALUES('小白',1);
SELECT * FROM `student`;

DROP TABLE `student`;
CREATE TABLE `student`(
`student_id` INT AUTO_INCREMENT,
`name` VARCHAR(20),
`major` VARCHAR(20),
PRIMARY KEY(`student_id`)
);
INSERT INTO `student`(`name`,`major`) VALUES('小白','英语');
INSERT INTO `student`(`name`,`major`) VALUES('小黑','英语');
INSERT INTO `student`(`name`,`major`) VALUES('小绿','英语');
SELECT * FROM `student`;

DROP TABLE `student`;
CREATE TABLE `student`(
`student_id` INT AUTO_INCREMENT,
`name` VARCHAR(20),
`major` VARCHAR(20) DEFAULT '英语',
`score` INT DEFAULT 80,
PRIMARY KEY(`student_id`)
);
INSERT INTO `student`(`name`,`major`) VALUES('小绿', '语文');
INSERT INTO `student`(`name`,`major`) VALUES('小白', '数学');
INSERT INTO `student`(`name`,`major`) VALUES('小黄','卫生与健康');
INSERT INTO `student`(`name`,`score`) VALUES('小黑',30);
INSERT INTO `student`(`name`) VALUES('小红');
SELECT * FROM `student`;

UPDATE `student`
SET `major` = '英语文学英语艺术英语单词'
WHERE `major` = '英语';
SELECT * FROM `student`;

UPDATE `student`
SET `major` = '历史'
WHERE `student_id` = '1';
SELECT * FROM `student`;

UPDATE `student`
SET `major` = '计算机信息技术'
WHERE `major` = '数学' OR `major` = '历史';
SELECT * FROM `student`;

UPDATE `student`
SET `name` = '陈睿康',`major` = '哲学'
WHERE `major` = '英语文学英语艺术英语单词';
SELECT * FROM `student`;

DELETE FROM `student`
WHERE `student_id` = 5;
SELECT * FROM `student`;

DELETE FROM `student`
WHERE `name` = '小白' AND `major` = '计算机信息技术';
SELECT * FROM `student`;

DELETE FROM `student`
WHERE `score` >= 80;
SELECT * FROM `student`;

UPDATE `student`
SET `name` = '陈欢',`major` = '英语',`score` = 100;
SELECT * FROM `student`;

INSERT INTO `student` VALUES(1,'陈睿康','哲学',100);
SELECT * FROM `student`;
-- DELETE FROM `student`;
-- SELECT * FROM `student`;
-- DROP DATABASE `helloSQL`;alter

SELECT `name`,`major` FROM `student`;

UPDATE `student`
SET `score` = 80
WHERE `name` = '陈睿康';
SELECT * FROM `student` ORDER BY `score`;
SELECT * FROM `student` ORDER BY `score` DESC;
SELECT * FROM `student` LIMIT 1;

DROP TABLE `student`;
CREATE TABLE `student`(
`student_id` INT AUTO_INCREMENT,
`name` VARCHAR(20),
`major` VARCHAR(20) DEFAULT '英语',
`score` INT DEFAULT 80,
PRIMARY KEY(`student_id`)
);
INSERT INTO `student`(`name`,`major`) VALUES('小绿', '语文');
INSERT INTO `student`(`name`,`major`) VALUES('小白', '数学');
INSERT INTO `student`(`name`,`major`) VALUES('小黄','卫生与健康');
INSERT INTO `student`(`name`,`score`) VALUES('小黑',30);
INSERT INTO `student`(`name`) VALUES('小红');
SELECT * FROM `student`;
SELECT * FROM `student` WHERE `major` = '英语' or `major` = '卫生与健康'; -- 相当于IN
SELECT * FROM `student` WHERE `score` <> 80;
SELECT * FROM `student` WHERE `score` >= 30 LIMIT 2;
SELECT * FROM `student` WHERE `major` IN('英语', '卫生与健康'); -- 相当于OR
