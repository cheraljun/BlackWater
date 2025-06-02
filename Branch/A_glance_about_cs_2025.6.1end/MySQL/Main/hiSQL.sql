SHOW DATABASES;
DROP DATABASE `hiSQL`;
CREATE DATABASE `hiSQL`;
USE `hiSQL`;

CREATE TABLE `employee`(
`employee_id` INT,
`employee_name` VARCHAR(20),
`birth_date` DATE,
`sex` VARCHAR(20),
`salary` INT,
`branch_id` INT,
`sup_id` int,
PRIMARY KEY(`employee_id`)
);
DESCRIBE `employee`;

CREATE TABLE `branch`(
`branch_id` INT,
`branch_name` VARCHAR(20),
`manager_id` INT,
PRIMARY KEY(`branch_id`),
FOREIGN KEY (`manager_id`) REFERENCES `employee`(`employee_id`) ON DELETE SET NULL -- 对应不到设定成NULL
);

ALTER TABLE `employee`
ADD FOREIGN KEY(`branch_id`)
REFERENCES `branch`(`branch_id`)
ON DELETE SET NULL;

ALTER TABLE `employee`
ADD FOREIGN KEY(sup_id)
REFERENCES `employee`(`employee_id`)
ON DELETE SET NULL;

CREATE TABLE `client`(
`client_id` INT,
`client_name` VARCHAR(20),
`phone` VARCHAR(20),
PRIMARY KEY(`client_id`)
);

CREATE TABLE `works_with`(
`employee_id` INT,
`client_id` INT,
`total_sales` INT,
PRIMARY KEY(`employee_id`,`client_id`),
FOREIGN KEY (`employee_id`) REFERENCES `employee`(`employee_id`) ON DELETE CASCADE, -- 对应不到就删掉
FOREIGN KEY (`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE
);
-- 部门资料
INSERT INTO `branch` VALUES(1,'研发',NULL);
INSERT INTO `branch` VALUES(2,'行政',NULL);
INSERT INTO `branch` VALUES(3,'咨询',NULL);

-- 员工资料
INSERT INTO `employee` VALUES(206,'小黄','1998-10-08','F',50000,1,NULL);
INSERT INTO `employee` VALUES(207,'小绿','1985-09-16','M',29000,2,206);
INSERT INTO `employee` VALUES(208,'小黑','2000-12-19','M',35000,3,206);
INSERT INTO `employee` VALUES(209,'小白','1997-01-22','F',39000,3,207);
INSERT INTO `employee` VALUES(210,'小蓝','1925-11-10','F',84000,1,207);

UPDATE `branch`
SET `manager_id` = 206
WHERE `branch_id` = 1;

UPDATE `branch`
SET `manager_id` = 207
WHERE `branch_id` = 2;

UPDATE `branch`
SET `manager_id` = 208
WHERE `branch_id` = 3;

INSERT INTO `client` VALUES(400,'阿狗','254354335');
INSERT INTO `client` VALUES(401,'阿猫','25633899');
INSERT INTO `client` VALUES(402,'旺财','45354345');
INSERT INTO `client` VALUES(403,'露西','54354365');
INSERT INTO `client` VALUES(404,'艾瑞克','18783783');

INSERT INTO `works_with` VALUES(206,400,'70000');
INSERT INTO `works_with` VALUES(207,401,'24000');
INSERT INTO `works_with` VALUES(208,402,'9800');
INSERT INTO `works_with` VALUES(208,403,'24000');
INSERT INTO `works_with` VALUES(210,404,'87940');

-- 取得所有员工资料
SELECT * FROM `employee`;
-- 取得所有客户资料
SELECT * FROM `client`;
-- 按照薪水低到高取得员工资料
SELECT * FROM `employee`
ORDER BY `salary`;
-- 取得薪水前3高的员工资料
SELECT * FROM `employee`
ORDER BY `salary` DESC
LIMIT 3;
-- 取得所有员工的名字
SELECT `employee_name` FROM `employee`;
-- 取得员工的非重复性别
SELECT `sex` FROM `employee`; -- 有重复的
SELECT DISTINCT `sex` FROM `employee`; -- 去重

-- 聚合函数 aggregate function
-- 取得员工人数
SELECT COUNT(*) FROM `employee`;
-- 取得出生于1970-01-01之后的女性员工人数alter
SELECT COUNt(*) FROM `employee`
WHERE `birth_date` > '1970-01-01' AND `sex` = 'F';
-- 取得平均薪水
SELECT AVG(`salary`) FROM `employee`;
-- 取得薪水总和
SELECT SUM(`salary`) FROM `employee`;
-- 取得薪水最高的员工
SELECT MAX(`salary`) FROM `employee`;
-- 取得薪水最低的员工
SELECT MIN(`salary`) FROM `employee`;

-- wildcards万用字元,%代表多个字元,_代表一个字元
-- 取得电话号码尾数是335的客户
SELECT * FROM `client`
WHERE `phone` LIKE '%335'; -- 只要符合有335的就返回, 前面的%代表多个字元
-- 取得姓艾的客户
SELECT * FROM `client`
WHERE `client_name` LIKE '艾%';
-- 取得生日在12月的员工
SELECT * FROM `employee`
WHERE `birth_date` LIKE '_____12%'; -- 5个_代表5个单一字元,然后是12,然后是12之后的多个字元

-- UNION 联集
-- 员工名字 UNION 客户名字
SELECT `employee_name` FROM `employee`
UNION
SELECT `client_name` FROM `client`;
-- 员工id+员工名字 UNION 客户id+客户名字
SELECT `employee_id`,`employee_name` FROM `employee`
UNION
SELECT `client_id`,`client_name` FROM `client`;
-- 员工薪水+销售金额
SELECT `salary` FROM `employee`
UNION
SELECT `total_sales` FROM `works_with`;

-- join 连接
INSERT INTO `branch` VALUES(4,'偷懒',NULL);
SELECT * FROM `branch`;
-- 取得所有部门经理的名字
SELECT * FROM `employee`
JOIN `branch`
ON `employee_id` = `manager_id`;
-- 选择并输出
SELECT `employee`.`employee_id`,`employee`.`employee_name`,`branch`.`branch_name`
FROM `employee` JOIN `branch`
ON `employee`.`employee_id` = `branch`.`manager_id`;

SELECT `employee`.`employee_id`,`employee`.`employee_name`,`branch`.`branch_name`
FROM `employee` LEFT JOIN `branch` -- 无论条件是否成立都会回传LEFT边的全部内容
ON `employee`.`employee_id` = `branch`.`manager_id`;

SELECT `employee`.`employee_id`,`employee`.`employee_name`,`branch`.`branch_name`
FROM `employee` RIGHT JOIN `branch` -- 无论条件是否成立都会回传RIGHT边的全部内容
ON `employee`.`employee_id` = `branch`.`manager_id`;

-- SUBQUERY 子查询
-- 找出研发部门的经理名字
SELECT `employee_name` FROM `employee`
WHERE `employee_id` = (
SELECT `manager_id` FROM `branch`
WHERE `branch_name` = '研发'
);
-- 找出对一位客户销售金额超过50000的员工名字
SELECT `employee_name` FROM `employee`
WHERE `employee_id` IN (
SELECT `employee_id` FROM `works_with`
WHERE `total_sales` > 50000
); -- 不止1笔资料用IN