# 豆瓣读书 采集爬虫

使用了隧道代理，和mysql数据库

```
php install -r requirements.txt
```

采集开始网址：
`https://book.douban.com/tag/?view=type&icn=index-sorttags-all`

所需的mysql数据表结构

```

CREATE TABLE `book` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(120) NOT NULL COMMENT '书名' COLLATE 'utf8mb4_general_ci',
	`isbn` VARCHAR(13) NOT NULL COMMENT '书号' COLLATE 'utf8mb4_general_ci',
	`origin_title` VARCHAR(255) NULL DEFAULT NULL COMMENT '原作名' COLLATE 'utf8mb4_general_ci',
	`subtitle` VARCHAR(255) NULL DEFAULT NULL COMMENT '副标题' COLLATE 'utf8mb4_general_ci',
	`image` VARCHAR(80) NOT NULL COMMENT '封面' COLLATE 'utf8mb4_general_ci',
	`author` VARCHAR(120) NULL DEFAULT NULL COMMENT '作者' COLLATE 'utf8mb4_general_ci',
	`translator` VARCHAR(120) NULL DEFAULT NULL COMMENT '译者' COLLATE 'utf8mb4_general_ci',
	`publisher` VARCHAR(120) NULL DEFAULT NULL COMMENT '出版社' COLLATE 'utf8mb4_general_ci',
	`pubdate` VARCHAR(60) NULL DEFAULT NULL COMMENT '出版时间' COLLATE 'utf8mb4_general_ci',
	`binding` VARCHAR(20) NULL DEFAULT NULL COMMENT '装帧' COLLATE 'utf8mb4_general_ci',
	`price` DECIMAL(5,2) UNSIGNED NULL DEFAULT NULL COMMENT '定价',
	`series` VARCHAR(120) NULL DEFAULT NULL COMMENT '所属丛书' COLLATE 'utf8mb4_general_ci',
	`pages` INT(6) UNSIGNED NULL DEFAULT NULL COMMENT '页数',
	`rating` INT(2) UNSIGNED NULL DEFAULT NULL COMMENT '评分',
	`catalog` TEXT NULL DEFAULT NULL COMMENT '章节目录' COLLATE 'utf8mb4_general_ci',
	`summary` TEXT NULL DEFAULT NULL COMMENT '内容简介' COLLATE 'utf8mb4_general_ci',
	`author_intro` TEXT NULL DEFAULT NULL COMMENT '作者简介' COLLATE 'utf8mb4_general_ci',
	`grab_url` VARCHAR(60) NULL DEFAULT NULL COMMENT '采集网址' COLLATE 'utf8mb4_general_ci',
	`updatetime` INT(11) UNSIGNED NULL DEFAULT NULL COMMENT '更新时间',
	`status` ENUM('normal','hidden') NOT NULL DEFAULT 'normal' COMMENT '状态' COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`id`) USING BTREE,
	UNIQUE INDEX `isbn` (`isbn`) USING BTREE,
	UNIQUE INDEX `grab_url` (`grab_url`) USING BTREE
)
COMMENT='图书信息表'
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;


```