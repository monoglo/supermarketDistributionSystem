-- --------------------------------------------------------
-- 主机:                           localhost
-- 服务器版本:                        10.3.14-MariaDB - mariadb.org binary distribution
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 supermarket 的数据库结构
CREATE DATABASE IF NOT EXISTS `supermarket` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `supermarket`;

-- 导出  表 supermarket.administrators 结构
CREATE TABLE IF NOT EXISTS `administrators` (
  `aid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '管理员ID',
  `name` varchar(32) NOT NULL COMMENT '管理员用户名',
  `screenName` varchar(32) DEFAULT NULL COMMENT '管理员昵称',
  `email` varchar(32) NOT NULL COMMENT '管理员邮箱',
  `phone` varchar(16) DEFAULT NULL COMMENT '管理员手机号码',
  `adress` varchar(50) DEFAULT NULL COMMENT '管理员住址',
  `password` varchar(32) NOT NULL COMMENT '管理员密码',
  `group` varchar(16) NOT NULL DEFAULT 'Administrator' COMMENT '用户组',
  `status` varchar(16) NOT NULL DEFAULT 'normal' COMMENT '状态',
  `all` int(1) unsigned DEFAULT 1,
  PRIMARY KEY (`aid`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 COMMENT='管理员表';

-- 数据导出被取消选择。
-- 导出  表 supermarket.couriers 结构
CREATE TABLE IF NOT EXISTS `couriers` (
  `coid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '配送员ID',
  `name` varchar(32) NOT NULL COMMENT '配送员用户名',
  `screenName` varchar(32) DEFAULT NULL COMMENT '配送员昵称',
  `email` varchar(32) NOT NULL COMMENT '配送员邮箱',
  `phone` varchar(16) DEFAULT NULL COMMENT '配送员手机号码',
  `adress` varchar(50) DEFAULT NULL COMMENT '配送员住址',
  `password` varchar(32) NOT NULL COMMENT '配送员密码',
  `group` varchar(16) NOT NULL DEFAULT 'Courier' COMMENT '用户组',
  `deliveryTimes` int(10) unsigned NOT NULL DEFAULT 0,
  `salary` float unsigned NOT NULL DEFAULT 0,
  `status` varchar(16) NOT NULL DEFAULT 'normal' COMMENT '状态',
  `all` int(1) unsigned NOT NULL DEFAULT 1,
  PRIMARY KEY (`coid`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='配送员表';

-- 数据导出被取消选择。
-- 导出  表 supermarket.customers 结构
CREATE TABLE IF NOT EXISTS `customers` (
  `cuid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '配送员ID',
  `name` varchar(32) NOT NULL COMMENT '配送员用户名',
  `screenName` varchar(32) DEFAULT NULL COMMENT '配送员昵称',
  `email` varchar(32) NOT NULL COMMENT '配送员邮箱',
  `phone` varchar(16) DEFAULT NULL COMMENT '配送员手机号码',
  `adress` varchar(50) DEFAULT NULL COMMENT '配送员住址',
  `password` varchar(32) NOT NULL COMMENT '配送员密码',
  `group` varchar(16) NOT NULL DEFAULT 'Customer' COMMENT '用户组',
  `balance` float unsigned NOT NULL DEFAULT 0,
  `status` varchar(16) NOT NULL DEFAULT 'normal' COMMENT '状态',
  `all` int(1) unsigned NOT NULL DEFAULT 1,
  PRIMARY KEY (`cuid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='顾客表';

-- 数据导出被取消选择。
-- 导出  表 supermarket.goods 结构
CREATE TABLE IF NOT EXISTS `goods` (
  `gid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '批次ID',
  `productNumber` int(10) unsigned NOT NULL COMMENT '商品编号',
  `name` varchar(32) NOT NULL COMMENT '商品名称',
  `type` varchar(32) DEFAULT NULL COMMENT '商品类别',
  `expireDate` date NOT NULL COMMENT '过期时间',
  `createTime` datetime DEFAULT current_timestamp() COMMENT '到货时间',
  `unit` varchar(5) NOT NULL COMMENT '商品单位',
  `quantity` int(10) unsigned DEFAULT NULL COMMENT '剩余数量',
  `price` float unsigned NOT NULL COMMENT '销售价格',
  `cost` float unsigned DEFAULT NULL COMMENT '成本价格',
  `all` int(1) unsigned NOT NULL DEFAULT 1,
  PRIMARY KEY (`gid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='库存商品表';

-- 数据导出被取消选择。
-- 导出  表 supermarket.order 结构
CREATE TABLE IF NOT EXISTS `order` (
  `oid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `cuid` int(10) unsigned NOT NULL,
  `amount` float unsigned NOT NULL,
  `status` varchar(32) NOT NULL,
  `coid` int(10) unsigned DEFAULT NULL,
  `all` int(1) unsigned NOT NULL DEFAULT 1,
  PRIMARY KEY (`oid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单表';

-- 数据导出被取消选择。
-- 导出  表 supermarket.orderitems 结构
CREATE TABLE IF NOT EXISTS `orderitems` (
  `oid` int(10) unsigned NOT NULL COMMENT '订单ID',
  `gid` int(10) unsigned NOT NULL COMMENT '批次ID',
  `productNumbers` int(10) unsigned DEFAULT NULL COMMENT '商品名称',
  `unit` varchar(5) NOT NULL COMMENT '商品单位',
  `quantity` int(10) unsigned NOT NULL COMMENT '购买数量',
  `price` float unsigned NOT NULL COMMENT '单价',
  `amount` float unsigned NOT NULL COMMENT '总价',
  `all` int(1) unsigned NOT NULL DEFAULT 1,
  PRIMARY KEY (`oid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订单内容表';

-- 数据导出被取消选择。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
