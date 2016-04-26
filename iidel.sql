/*
Navicat MySQL Data Transfer

Source Server         : Local
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : iidel

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2016-04-26 12:03:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add tipo movimiento', '7', 'add_tipomovimiento');
INSERT INTO `auth_permission` VALUES ('20', 'Can change tipo movimiento', '7', 'change_tipomovimiento');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete tipo movimiento', '7', 'delete_tipomovimiento');
INSERT INTO `auth_permission` VALUES ('22', 'Can add moneda', '8', 'add_moneda');
INSERT INTO `auth_permission` VALUES ('23', 'Can change moneda', '8', 'change_moneda');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete moneda', '8', 'delete_moneda');
INSERT INTO `auth_permission` VALUES ('25', 'Can add impuestos', '9', 'add_impuestos');
INSERT INTO `auth_permission` VALUES ('26', 'Can change impuestos', '9', 'change_impuestos');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete impuestos', '9', 'delete_impuestos');
INSERT INTO `auth_permission` VALUES ('28', 'Can add producto', '10', 'add_producto');
INSERT INTO `auth_permission` VALUES ('29', 'Can change producto', '10', 'change_producto');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete producto', '10', 'delete_producto');
INSERT INTO `auth_permission` VALUES ('31', 'Can add producto impuesto', '11', 'add_productoimpuesto');
INSERT INTO `auth_permission` VALUES ('32', 'Can change producto impuesto', '11', 'change_productoimpuesto');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete producto impuesto', '11', 'delete_productoimpuesto');
INSERT INTO `auth_permission` VALUES ('34', 'Can add cupon descuento', '12', 'add_cupondescuento');
INSERT INTO `auth_permission` VALUES ('35', 'Can change cupon descuento', '12', 'change_cupondescuento');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete cupon descuento', '12', 'delete_cupondescuento');
INSERT INTO `auth_permission` VALUES ('37', 'Can add concepto', '13', 'add_concepto');
INSERT INTO `auth_permission` VALUES ('38', 'Can change concepto', '13', 'change_concepto');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete concepto', '13', 'delete_concepto');
INSERT INTO `auth_permission` VALUES ('40', 'Can add estados ecommerce', '14', 'add_estadosecommerce');
INSERT INTO `auth_permission` VALUES ('41', 'Can change estados ecommerce', '14', 'change_estadosecommerce');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete estados ecommerce', '14', 'delete_estadosecommerce');
INSERT INTO `auth_permission` VALUES ('43', 'Can add cargo', '15', 'add_cargo');
INSERT INTO `auth_permission` VALUES ('44', 'Can change cargo', '15', 'change_cargo');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete cargo', '15', 'delete_cargo');
INSERT INTO `auth_permission` VALUES ('46', 'Can add orden compra', '16', 'add_ordencompra');
INSERT INTO `auth_permission` VALUES ('47', 'Can change orden compra', '16', 'change_ordencompra');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete orden compra', '16', 'delete_ordencompra');
INSERT INTO `auth_permission` VALUES ('49', 'Can add cargo orden', '17', 'add_cargoorden');
INSERT INTO `auth_permission` VALUES ('50', 'Can change cargo orden', '17', 'change_cargoorden');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete cargo orden', '17', 'delete_cargoorden');
INSERT INTO `auth_permission` VALUES ('52', 'Can add forma pago', '18', 'add_formapago');
INSERT INTO `auth_permission` VALUES ('53', 'Can change forma pago', '18', 'change_formapago');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete forma pago', '18', 'delete_formapago');
INSERT INTO `auth_permission` VALUES ('55', 'Can add deposito', '19', 'add_deposito');
INSERT INTO `auth_permission` VALUES ('56', 'Can change deposito', '19', 'change_deposito');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete deposito', '19', 'delete_deposito');
INSERT INTO `auth_permission` VALUES ('58', 'Can add pago', '20', 'add_pago');
INSERT INTO `auth_permission` VALUES ('59', 'Can change pago', '20', 'change_pago');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete pago', '20', 'delete_pago');
INSERT INTO `auth_permission` VALUES ('61', 'Can add cat tipo entorno', '21', 'add_cattipoentorno');
INSERT INTO `auth_permission` VALUES ('62', 'Can change cat tipo entorno', '21', 'change_cattipoentorno');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete cat tipo entorno', '21', 'delete_cattipoentorno');
INSERT INTO `auth_permission` VALUES ('64', 'Can add cat operaciones api paypal', '22', 'add_catoperacionesapipaypal');
INSERT INTO `auth_permission` VALUES ('65', 'Can change cat operaciones api paypal', '22', 'change_catoperacionesapipaypal');
INSERT INTO `auth_permission` VALUES ('66', 'Can delete cat operaciones api paypal', '22', 'delete_catoperacionesapipaypal');
INSERT INTO `auth_permission` VALUES ('67', 'Can add cat api paypal', '23', 'add_catapipaypal');
INSERT INTO `auth_permission` VALUES ('68', 'Can change cat api paypal', '23', 'change_catapipaypal');
INSERT INTO `auth_permission` VALUES ('69', 'Can delete cat api paypal', '23', 'delete_catapipaypal');
INSERT INTO `auth_permission` VALUES ('70', 'Can add opciones api paypal operaciones', '24', 'add_opcionesapipaypaloperaciones');
INSERT INTO `auth_permission` VALUES ('71', 'Can change opciones api paypal operaciones', '24', 'change_opcionesapipaypaloperaciones');
INSERT INTO `auth_permission` VALUES ('72', 'Can delete opciones api paypal operaciones', '24', 'delete_opcionesapipaypaloperaciones');
INSERT INTO `auth_permission` VALUES ('73', 'Can add cuenta paypal', '25', 'add_cuentapaypal');
INSERT INTO `auth_permission` VALUES ('74', 'Can change cuenta paypal', '25', 'change_cuentapaypal');
INSERT INTO `auth_permission` VALUES ('75', 'Can delete cuenta paypal', '25', 'delete_cuentapaypal');
INSERT INTO `auth_permission` VALUES ('76', 'Can add estados pay pal', '26', 'add_estadospaypal');
INSERT INTO `auth_permission` VALUES ('77', 'Can change estados pay pal', '26', 'change_estadospaypal');
INSERT INTO `auth_permission` VALUES ('78', 'Can delete estados pay pal', '26', 'delete_estadospaypal');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$24000$zw1MXtLGWxeB$QOpZVhgN/XSrhrcZKgMIW2wfF58mrSf+9qy12qePDVU=', '2016-04-19 15:57:48', '1', 'victor', '', '', 'victor.castillo@prospectomedia.com', '1', '1', '2016-04-19 15:47:54');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2016-04-19 16:01:25', '1', 'MXN', '1', 'Added.', '8', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2016-04-19 16:53:55', '2', 'USD', '1', 'Added.', '8', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2016-04-19 16:54:02', '3', 'EUR', '1', 'Added.', '8', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2016-04-19 16:54:28', '1', 'Cargo', '1', 'Added.', '7', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2016-04-19 16:54:35', '2', 'Abono', '1', 'Added.', '7', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2016-04-19 17:04:18', '1', 'Impuesto al valor agregado - IVA', '1', 'Added.', '9', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2016-04-19 17:06:02', '1', 'Inscripción Curso - AAAAA00001', '1', 'Added.', '10', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2016-04-19 18:07:14', '1', 'Inscripción Curso - AAAAA00001', '2', 'Changed precio and precio_final.', '10', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2016-04-19 18:07:25', '1', 'ProductoImpuesto object', '1', 'Added.', '11', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2016-04-19 18:08:25', '1', 'Cupon Habilitado', '1', 'Added.', '14', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2016-04-19 18:08:27', '1', 'A0001', '1', 'Added.', '12', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('15', 'ecommerce', 'cargo');
INSERT INTO `django_content_type` VALUES ('17', 'ecommerce', 'cargoorden');
INSERT INTO `django_content_type` VALUES ('23', 'ecommerce', 'catapipaypal');
INSERT INTO `django_content_type` VALUES ('22', 'ecommerce', 'catoperacionesapipaypal');
INSERT INTO `django_content_type` VALUES ('21', 'ecommerce', 'cattipoentorno');
INSERT INTO `django_content_type` VALUES ('13', 'ecommerce', 'concepto');
INSERT INTO `django_content_type` VALUES ('25', 'ecommerce', 'cuentapaypal');
INSERT INTO `django_content_type` VALUES ('12', 'ecommerce', 'cupondescuento');
INSERT INTO `django_content_type` VALUES ('19', 'ecommerce', 'deposito');
INSERT INTO `django_content_type` VALUES ('14', 'ecommerce', 'estadosecommerce');
INSERT INTO `django_content_type` VALUES ('26', 'ecommerce', 'estadospaypal');
INSERT INTO `django_content_type` VALUES ('18', 'ecommerce', 'formapago');
INSERT INTO `django_content_type` VALUES ('9', 'ecommerce', 'impuestos');
INSERT INTO `django_content_type` VALUES ('8', 'ecommerce', 'moneda');
INSERT INTO `django_content_type` VALUES ('24', 'ecommerce', 'opcionesapipaypaloperaciones');
INSERT INTO `django_content_type` VALUES ('16', 'ecommerce', 'ordencompra');
INSERT INTO `django_content_type` VALUES ('20', 'ecommerce', 'pago');
INSERT INTO `django_content_type` VALUES ('10', 'ecommerce', 'producto');
INSERT INTO `django_content_type` VALUES ('11', 'ecommerce', 'productoimpuesto');
INSERT INTO `django_content_type` VALUES ('7', 'ecommerce', 'tipomovimiento');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2016-04-19 15:43:52');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2016-04-19 15:43:53');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2016-04-19 15:43:53');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2016-04-19 15:43:53');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2016-04-19 15:43:53');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2016-04-19 15:43:53');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2016-04-19 15:43:53');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2016-04-19 15:43:53');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2016-04-19 15:43:53');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2016-04-19 15:43:53');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2016-04-19 15:43:53');
INSERT INTO `django_migrations` VALUES ('12', 'ecommerce', '0001_initial', '2016-04-19 15:43:54');
INSERT INTO `django_migrations` VALUES ('13', 'sessions', '0001_initial', '2016-04-19 15:43:54');
INSERT INTO `django_migrations` VALUES ('14', 'ecommerce', '0002_auto_20160419_1703', '2016-04-19 17:03:19');
INSERT INTO `django_migrations` VALUES ('15', 'ecommerce', '0003_auto_20160419_1704', '2016-04-19 17:04:13');
INSERT INTO `django_migrations` VALUES ('16', 'ecommerce', '0004_auto_20160422_1547', '2016-04-22 15:47:37');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('h583mxtimn2vclyr3ge90utfqai5w66w', 'NWI4NGFjM2NmMDM3YmQ0YjliNzFlNzk5NTdiOWZmNzRkNWEzZWI1MTp7Il9hdXRoX3VzZXJfaGFzaCI6ImQ4NzU1OGY2N2QwNWUyMDQwOTFmYmIzNmRhYjdmOGJkMDUwOWNlZjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-05-03 15:57:48');

-- ----------------------------
-- Table structure for ecommerce_cargo
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_cargo`;
CREATE TABLE `ecommerce_cargo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_creacion` datetime NOT NULL,
  `fecha_vencimiento` datetime NOT NULL,
  `estado_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  `tipo_movimiento_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_cargo_2c189993` (`estado_id`),
  KEY `ecommerce_cargo_bb91903a` (`producto_id`),
  KEY `ecommerce_cargo_88e82677` (`tipo_movimiento_id`),
  CONSTRAINT `ecommerce_cargo_producto_id_b05d8555_fk_ecommerce_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `ecommerce_producto` (`id`),
  CONSTRAINT `ecommerce_ca_estado_id_2510a95f_fk_ecommerce_estadosecommerce_id` FOREIGN KEY (`estado_id`) REFERENCES `ecommerce_estadosecommerce` (`id`),
  CONSTRAINT `ecomm_tipo_movimiento_id_b437e88d_fk_ecommerce_tipomovimiento_id` FOREIGN KEY (`tipo_movimiento_id`) REFERENCES `ecommerce_tipomovimiento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_cargo
-- ----------------------------

-- ----------------------------
-- Table structure for ecommerce_cargoorden
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_cargoorden`;
CREATE TABLE `ecommerce_cargoorden` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cargo_id` int(11) NOT NULL,
  `orden_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_cargoorden_cargo_id_a4661b73_fk_ecommerce_cargo_id` (`cargo_id`),
  KEY `ecommerce_cargoorden_c33caba2` (`orden_id`),
  CONSTRAINT `ecommerce_cargoorden_cargo_id_a4661b73_fk_ecommerce_cargo_id` FOREIGN KEY (`cargo_id`) REFERENCES `ecommerce_cargo` (`id`),
  CONSTRAINT `ecommerce_cargoord_orden_id_e71a833e_fk_ecommerce_ordencompra_id` FOREIGN KEY (`orden_id`) REFERENCES `ecommerce_ordencompra` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_cargoorden
-- ----------------------------

-- ----------------------------
-- Table structure for ecommerce_catapipaypal
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_catapipaypal`;
CREATE TABLE `ecommerce_catapipaypal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) NOT NULL,
  `url_paypal` varchar(200) NOT NULL,
  `version` double NOT NULL,
  `cat_tipoentorno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_catapipaypal_70314866` (`cat_tipoentorno_id`),
  CONSTRAINT `ecomm_cat_tipoentorno_id_fcbccb82_fk_ecommerce_cattipoentorno_id` FOREIGN KEY (`cat_tipoentorno_id`) REFERENCES `ecommerce_cattipoentorno` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_catapipaypal
-- ----------------------------
INSERT INTO `ecommerce_catapipaypal` VALUES ('1', 'https://api-3t.sandbox.paypal.com/nvp', 'https://www.sandbox.paypal.com/webscr', '124', '1');
INSERT INTO `ecommerce_catapipaypal` VALUES ('2', 'https://api-3t.paypal.com/nvp', 'https://www.paypal.com', '124', '2');

-- ----------------------------
-- Table structure for ecommerce_catoperacionesapipaypal
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_catoperacionesapipaypal`;
CREATE TABLE `ecommerce_catoperacionesapipaypal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `metodo` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `metodo` (`metodo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_catoperacionesapipaypal
-- ----------------------------
INSERT INTO `ecommerce_catoperacionesapipaypal` VALUES ('2', 'DoExpressCheckoutPayment');
INSERT INTO `ecommerce_catoperacionesapipaypal` VALUES ('1', 'SetExpressCheckout');
INSERT INTO `ecommerce_catoperacionesapipaypal` VALUES ('3', 'Subscribe');

-- ----------------------------
-- Table structure for ecommerce_cattipoentorno
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_cattipoentorno`;
CREATE TABLE `ecommerce_cattipoentorno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_cattipoentorno
-- ----------------------------
INSERT INTO `ecommerce_cattipoentorno` VALUES ('1', 'sandbox');
INSERT INTO `ecommerce_cattipoentorno` VALUES ('2', 'live');

-- ----------------------------
-- Table structure for ecommerce_concepto
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_concepto`;
CREATE TABLE `ecommerce_concepto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_concepto
-- ----------------------------

-- ----------------------------
-- Table structure for ecommerce_cuentapaypal
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_cuentapaypal`;
CREATE TABLE `ecommerce_cuentapaypal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apiusername` varchar(254) NOT NULL,
  `apipassword` longtext NOT NULL,
  `apisignature` longtext NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  `receiver_email` varchar(254) NOT NULL,
  `cat_apipaypal_id` int(11) NOT NULL,
  `cat_tipoentorno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `receiver_email` (`receiver_email`),
  KEY `ecommerce_cat_apipaypal_id_e2e23f4c_fk_ecommerce_catapipaypal_id` (`cat_apipaypal_id`),
  KEY `ecomm_cat_tipoentorno_id_34cbd72c_fk_ecommerce_cattipoentorno_id` (`cat_tipoentorno_id`),
  CONSTRAINT `ecomm_cat_tipoentorno_id_34cbd72c_fk_ecommerce_cattipoentorno_id` FOREIGN KEY (`cat_tipoentorno_id`) REFERENCES `ecommerce_cattipoentorno` (`id`),
  CONSTRAINT `ecommerce_cat_apipaypal_id_e2e23f4c_fk_ecommerce_catapipaypal_id` FOREIGN KEY (`cat_apipaypal_id`) REFERENCES `ecommerce_catapipaypal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_cuentapaypal
-- ----------------------------
INSERT INTO `ecommerce_cuentapaypal` VALUES ('1', 'PayPal sandbox', 'castillotorresvictormanuel3.h_api1.gmail.com', '', '', '1', 'castillotorresvictormanuel3.h-facilitator@gmail.com', '1', '1');

-- ----------------------------
-- Table structure for ecommerce_cupondescuento
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_cupondescuento`;
CREATE TABLE `ecommerce_cupondescuento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clave_cupon` varchar(10) NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  `numero_cupones` int(11) NOT NULL,
  `descuento` decimal(10,2) NOT NULL,
  `porcentaje` tinyint(1) NOT NULL,
  `estado_id` int(11) NOT NULL,
  `moneda_id` int(11),
  `tipo_movimiento_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_cupondescuento_2c189993` (`estado_id`),
  KEY `ecommerce_cupondescuento_fabc26c3` (`moneda_id`),
  KEY `ecommerce_cupondescuento_88e82677` (`tipo_movimiento_id`),
  CONSTRAINT `ecommerce_cupondescuen_moneda_id_bd49d59e_fk_ecommerce_moneda_id` FOREIGN KEY (`moneda_id`) REFERENCES `ecommerce_moneda` (`id`),
  CONSTRAINT `ecommerce_cu_estado_id_31a928bd_fk_ecommerce_estadosecommerce_id` FOREIGN KEY (`estado_id`) REFERENCES `ecommerce_estadosecommerce` (`id`),
  CONSTRAINT `ecomm_tipo_movimiento_id_69ba3d73_fk_ecommerce_tipomovimiento_id` FOREIGN KEY (`tipo_movimiento_id`) REFERENCES `ecommerce_tipomovimiento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_cupondescuento
-- ----------------------------
INSERT INTO `ecommerce_cupondescuento` VALUES ('1', 'A0001', '1', '10', '50.00', '0', '1', '2', '2');

-- ----------------------------
-- Table structure for ecommerce_deposito
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_deposito`;
CREATE TABLE `ecommerce_deposito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `monto` decimal(14,2) NOT NULL,
  `estado_id` int(11) NOT NULL,
  `forma_pago_id` int(11) NOT NULL,
  `tipo_movimiento_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_deposito_2c189993` (`estado_id`),
  KEY `ecommerce_deposito_b81ac747` (`forma_pago_id`),
  KEY `ecommerce_deposito_88e82677` (`tipo_movimiento_id`),
  KEY `ecommerce_deposito_abfe0f96` (`usuario_id`),
  CONSTRAINT `ecommerce_deposito_usuario_id_c703557b_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `ecommerce_depos_forma_pago_id_1d89f43e_fk_ecommerce_formapago_id` FOREIGN KEY (`forma_pago_id`) REFERENCES `ecommerce_formapago` (`id`),
  CONSTRAINT `ecommerce_de_estado_id_fa622c52_fk_ecommerce_estadosecommerce_id` FOREIGN KEY (`estado_id`) REFERENCES `ecommerce_estadosecommerce` (`id`),
  CONSTRAINT `ecomm_tipo_movimiento_id_42ed52bb_fk_ecommerce_tipomovimiento_id` FOREIGN KEY (`tipo_movimiento_id`) REFERENCES `ecommerce_tipomovimiento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_deposito
-- ----------------------------

-- ----------------------------
-- Table structure for ecommerce_estadosecommerce
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_estadosecommerce`;
CREATE TABLE `ecommerce_estadosecommerce` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(100) NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  `contexto` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_estadosecommerce
-- ----------------------------
INSERT INTO `ecommerce_estadosecommerce` VALUES ('1', 'Cupon Habilitado', '1', 'cupones');

-- ----------------------------
-- Table structure for ecommerce_estadospaypal
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_estadospaypal`;
CREATE TABLE `ecommerce_estadospaypal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_estadospaypal
-- ----------------------------
INSERT INTO `ecommerce_estadospaypal` VALUES ('1', 'Transaccion PayPal pendiente');
INSERT INTO `ecommerce_estadospaypal` VALUES ('2', 'Transaccion PayPal procesada');
INSERT INTO `ecommerce_estadospaypal` VALUES ('3', 'IPN recibida');
INSERT INTO `ecommerce_estadospaypal` VALUES ('4', 'IPN verificada');
INSERT INTO `ecommerce_estadospaypal` VALUES ('5', 'IPN invalido');
INSERT INTO `ecommerce_estadospaypal` VALUES ('6', 'Transaccion PayPal fallida');

-- ----------------------------
-- Table structure for ecommerce_formapago
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_formapago`;
CREATE TABLE `ecommerce_formapago` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `forma_pago` varchar(100) NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_formapago
-- ----------------------------

-- ----------------------------
-- Table structure for ecommerce_impuestos
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_impuestos`;
CREATE TABLE `ecommerce_impuestos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_impuesto` varchar(100) NOT NULL,
  `abreviacion` varchar(10) NOT NULL,
  `valor` decimal(14,2) NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  `tipo_movimiento_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_impuestos_88e82677` (`tipo_movimiento_id`),
  CONSTRAINT `ecomm_tipo_movimiento_id_f0586cca_fk_ecommerce_tipomovimiento_id` FOREIGN KEY (`tipo_movimiento_id`) REFERENCES `ecommerce_tipomovimiento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_impuestos
-- ----------------------------
INSERT INTO `ecommerce_impuestos` VALUES ('1', 'Impuesto al valor agregado', 'IVA', '16.00', '1', '1');

-- ----------------------------
-- Table structure for ecommerce_moneda
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_moneda`;
CREATE TABLE `ecommerce_moneda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `divisa` varchar(5) NOT NULL,
  `moneda` varchar(100) NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_moneda
-- ----------------------------
INSERT INTO `ecommerce_moneda` VALUES ('1', 'MXN', 'Mexicana', '1');
INSERT INTO `ecommerce_moneda` VALUES ('2', 'USD', 'Dolar americano', '1');
INSERT INTO `ecommerce_moneda` VALUES ('3', 'EUR', 'Euro', '1');

-- ----------------------------
-- Table structure for ecommerce_opcionesapipaypaloperaciones
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_opcionesapipaypaloperaciones`;
CREATE TABLE `ecommerce_opcionesapipaypaloperaciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `request_field` varchar(80) NOT NULL,
  `value` varchar(2048) NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  `catapipaypal_id` int(11) NOT NULL,
  `catoperacionesapipaypal_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ecommerce_opcionesapipaypaloperaci_catapipaypal_id_2a3bd059_uniq` (`catapipaypal_id`,`catoperacionesapipaypal_id`,`request_field`),
  KEY `D29aa8e513a3c3b64dd8de4ec202eeeb` (`catoperacionesapipaypal_id`),
  CONSTRAINT `D29aa8e513a3c3b64dd8de4ec202eeeb` FOREIGN KEY (`catoperacionesapipaypal_id`) REFERENCES `ecommerce_catoperacionesapipaypal` (`id`),
  CONSTRAINT `ecommerce__catapipaypal_id_180d0446_fk_ecommerce_catapipaypal_id` FOREIGN KEY (`catapipaypal_id`) REFERENCES `ecommerce_catapipaypal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_opcionesapipaypaloperaciones
-- ----------------------------
INSERT INTO `ecommerce_opcionesapipaypaloperaciones` VALUES ('1', 'CARTBORDERCOLOR', '7ab800', '1', '1', '1');
INSERT INTO `ecommerce_opcionesapipaypaloperaciones` VALUES ('2', 'CARTBORDERCOLOR', '7ab800', '1', '2', '1');
INSERT INTO `ecommerce_opcionesapipaypaloperaciones` VALUES ('3', 'image_url', 'header_mail.jpg', '1', '1', '3');
INSERT INTO `ecommerce_opcionesapipaypaloperaciones` VALUES ('4', 'image_url', 'header_mail.jpg', '1', '2', '3');

-- ----------------------------
-- Table structure for ecommerce_ordencompra
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_ordencompra`;
CREATE TABLE `ecommerce_ordencompra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `habilitado` tinyint(1) NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `fecha_vencimiento` datetime NOT NULL,
  `concepto_id` int(11) NOT NULL,
  `cupon_id` int(11) DEFAULT NULL,
  `estado_id` int(11) NOT NULL,
  `tipo_movimiento_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_ordencom_concepto_id_42e150c0_fk_ecommerce_concepto_id` (`concepto_id`),
  KEY `ecommerce_orden_cupon_id_3aef708c_fk_ecommerce_cupondescuento_id` (`cupon_id`),
  KEY `ecommerce_or_estado_id_6bcd6f5b_fk_ecommerce_estadosecommerce_id` (`estado_id`),
  KEY `ecommerce_ordencompra_88e82677` (`tipo_movimiento_id`),
  KEY `ecommerce_ordencompra_abfe0f96` (`usuario_id`),
  CONSTRAINT `ecommerce_ordencompra_usuario_id_cbebb1ec_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `ecommerce_ordencom_concepto_id_42e150c0_fk_ecommerce_concepto_id` FOREIGN KEY (`concepto_id`) REFERENCES `ecommerce_concepto` (`id`),
  CONSTRAINT `ecommerce_orden_cupon_id_3aef708c_fk_ecommerce_cupondescuento_id` FOREIGN KEY (`cupon_id`) REFERENCES `ecommerce_cupondescuento` (`id`),
  CONSTRAINT `ecommerce_or_estado_id_6bcd6f5b_fk_ecommerce_estadosecommerce_id` FOREIGN KEY (`estado_id`) REFERENCES `ecommerce_estadosecommerce` (`id`),
  CONSTRAINT `ecomm_tipo_movimiento_id_3d73e120_fk_ecommerce_tipomovimiento_id` FOREIGN KEY (`tipo_movimiento_id`) REFERENCES `ecommerce_tipomovimiento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_ordencompra
-- ----------------------------

-- ----------------------------
-- Table structure for ecommerce_pago
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_pago`;
CREATE TABLE `ecommerce_pago` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `monto` decimal(14,2) NOT NULL,
  `cargo_id` int(11) NOT NULL,
  `deposito_id` int(11) NOT NULL,
  `estado_id` int(11) NOT NULL,
  `forma_pago_id` int(11) NOT NULL,
  `tipo_movimiento_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_pago_cargo_id_de386a07_fk_ecommerce_cargo_id` (`cargo_id`),
  KEY `ecommerce_pago_deposito_id_a75b0d66_fk_ecommerce_deposito_id` (`deposito_id`),
  KEY `ecommerce_pa_estado_id_9b0c7a94_fk_ecommerce_estadosecommerce_id` (`estado_id`),
  KEY `ecommerce_pago_forma_pago_id_b9186e29_fk_ecommerce_formapago_id` (`forma_pago_id`),
  KEY `ecommerce_pago_88e82677` (`tipo_movimiento_id`),
  CONSTRAINT `ecommerce_pago_cargo_id_de386a07_fk_ecommerce_cargo_id` FOREIGN KEY (`cargo_id`) REFERENCES `ecommerce_cargo` (`id`),
  CONSTRAINT `ecommerce_pago_deposito_id_a75b0d66_fk_ecommerce_deposito_id` FOREIGN KEY (`deposito_id`) REFERENCES `ecommerce_deposito` (`id`),
  CONSTRAINT `ecommerce_pago_forma_pago_id_b9186e29_fk_ecommerce_formapago_id` FOREIGN KEY (`forma_pago_id`) REFERENCES `ecommerce_formapago` (`id`),
  CONSTRAINT `ecommerce_pa_estado_id_9b0c7a94_fk_ecommerce_estadosecommerce_id` FOREIGN KEY (`estado_id`) REFERENCES `ecommerce_estadosecommerce` (`id`),
  CONSTRAINT `ecomm_tipo_movimiento_id_0f121ca0_fk_ecommerce_tipomovimiento_id` FOREIGN KEY (`tipo_movimiento_id`) REFERENCES `ecommerce_tipomovimiento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_pago
-- ----------------------------

-- ----------------------------
-- Table structure for ecommerce_producto
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_producto`;
CREATE TABLE `ecommerce_producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `clave` varchar(10) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `precio_final` decimal(10,2) NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  `valido_hasta` datetime DEFAULT NULL,
  `moneda_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_producto_moneda_id_ff685f30_fk_ecommerce_moneda_id` (`moneda_id`),
  CONSTRAINT `ecommerce_producto_moneda_id_ff685f30_fk_ecommerce_moneda_id` FOREIGN KEY (`moneda_id`) REFERENCES `ecommerce_moneda` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_producto
-- ----------------------------
INSERT INTO `ecommerce_producto` VALUES ('1', 'Inscripción Curso', 'AAAAA00001', '100.00', '160.00', '1', null, '2');

-- ----------------------------
-- Table structure for ecommerce_productoimpuesto
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_productoimpuesto`;
CREATE TABLE `ecommerce_productoimpuesto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `impuesto_id` int(11) NOT NULL,
  `producto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ecommerce_product_impuesto_id_8c365933_fk_ecommerce_impuestos_id` (`impuesto_id`),
  KEY `ecommerce_producto_producto_id_8c205af8_fk_ecommerce_producto_id` (`producto_id`),
  CONSTRAINT `ecommerce_producto_producto_id_8c205af8_fk_ecommerce_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `ecommerce_producto` (`id`),
  CONSTRAINT `ecommerce_product_impuesto_id_8c365933_fk_ecommerce_impuestos_id` FOREIGN KEY (`impuesto_id`) REFERENCES `ecommerce_impuestos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_productoimpuesto
-- ----------------------------
INSERT INTO `ecommerce_productoimpuesto` VALUES ('1', '1', '1');

-- ----------------------------
-- Table structure for ecommerce_tipomovimiento
-- ----------------------------
DROP TABLE IF EXISTS `ecommerce_tipomovimiento`;
CREATE TABLE `ecommerce_tipomovimiento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(30) NOT NULL,
  `clave` varchar(3) NOT NULL,
  `signo` varchar(1) NOT NULL,
  `habilitado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ecommerce_tipomovimiento
-- ----------------------------
INSERT INTO `ecommerce_tipomovimiento` VALUES ('1', 'Cargo', 'C', '+', '1');
INSERT INTO `ecommerce_tipomovimiento` VALUES ('2', 'Abono', 'A', '-', '1');
