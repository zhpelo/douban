# 豆瓣读书 采集爬虫

使用了隧道代理，和mysql数据库

```
php install -r requirements.txt
```

所需的mysql数据表结构

```

--
-- 表的结构 `book`
--

CREATE TABLE `book` (
  `id` int(11) NOT NULL,
  `title` varchar(120) NOT NULL COMMENT '书名',
  `isbn` varchar(13) NOT NULL COMMENT '书号',
  `origin_title` varchar(255) DEFAULT NULL COMMENT '原作名',
  `subtitle` varchar(255) DEFAULT NULL COMMENT '副标题',
  `image` varchar(255) NOT NULL COMMENT '封面',
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `translator` varchar(255) DEFAULT NULL COMMENT '译者',
  `publisher` varchar(120) DEFAULT NULL COMMENT '出版社',
  `pubdate` varchar(60) DEFAULT NULL COMMENT '出版时间',
  `binding` varchar(20) DEFAULT NULL COMMENT '装帧',
  `price` decimal(10,2) DEFAULT NULL COMMENT '定价',
  `series` varchar(120) DEFAULT NULL COMMENT '所属丛书',
  `pages` int(11) DEFAULT NULL COMMENT '页数',
  `tags` varchar(255) DEFAULT NULL COMMENT '标签',
  `rating` int(11) DEFAULT NULL COMMENT '评分',
  `clc` varchar(50) DEFAULT NULL COMMENT '中图法分类号',
  `comments` int(11) NOT NULL DEFAULT '0' COMMENT '评论数',
  `createtime` int(11) NOT NULL COMMENT '创建时间',
  `updatetime` int(11) DEFAULT NULL COMMENT '更新时间',
  `status` enum('normal','hidden') NOT NULL DEFAULT 'normal' COMMENT '状态'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='图书信息表';

--
-- 转储表的索引
--

--
-- 表的索引 `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `book`
--
ALTER TABLE `book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;



-- --------------------------------------------------------

--
-- 表的结构 `book_data`
--

CREATE TABLE `book_data` (
  `book_id` int(11) NOT NULL COMMENT '图书ID',
  `author_intro` mediumtext COMMENT '作者简介',
  `catalog` mediumtext COMMENT '章节目录',
  `summary` mediumtext COMMENT '内容简介',
  `intro` mediumtext COMMENT '内容简介[短]',
  `spec` varchar(120) DEFAULT NULL COMMENT '装订规格'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转储表的索引
--

--
-- 表的索引 `book_data`
--
ALTER TABLE `book_data`
  ADD UNIQUE KEY `book_id` (`book_id`);
COMMIT;

```