--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-09-12 15:58:10 CEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE pweb2;
--
-- TOC entry 3433 (class 1262 OID 17290)
-- Name: pweb2; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE pweb2 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C.UTF-8';


\connect pweb2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- TOC entry 3434 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 17291)
-- Name: autostrada; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.autostrada (
    cod_naz character varying NOT NULL,
    cod_eu character varying NOT NULL,
    nome character varying NOT NULL,
    lunghezza character varying NOT NULL
);


--
-- TOC entry 216 (class 1259 OID 17296)
-- Name: casello; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.casello (
    codice character varying NOT NULL,
    cod_naz character varying NOT NULL,
    comune character varying NOT NULL,
    nome character varying NOT NULL,
    x character varying NOT NULL,
    y character varying NOT NULL,
    is_automatico smallint NOT NULL,
    data_automazione character varying
);


--
-- TOC entry 217 (class 1259 OID 17301)
-- Name: comune; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.comune (
    codice character varying NOT NULL,
    provincia character varying NOT NULL,
    nome character varying NOT NULL
);


--
-- TOC entry 218 (class 1259 OID 17306)
-- Name: provincia; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.provincia (
    sigla character varying NOT NULL,
    regione integer NOT NULL,
    nome character varying NOT NULL
);


--
-- TOC entry 219 (class 1259 OID 17311)
-- Name: regione; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.regione (
    codice integer NOT NULL,
    nome character varying NOT NULL
);


--
-- TOC entry 3423 (class 0 OID 17291)
-- Dependencies: 215
-- Data for Name: autostrada; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.autostrada VALUES ('A1', 'E1', 'A1-E1', '1038701106');
INSERT INTO public.autostrada VALUES ('A2', 'E2', 'A2-E2', '1669665582');
INSERT INTO public.autostrada VALUES ('A3', 'E3', 'A3-E3', '350884745');
INSERT INTO public.autostrada VALUES ('A4', 'E4', 'A4-E4', '2101348923');
INSERT INTO public.autostrada VALUES ('A5', 'E5', 'A5-E5', '634346473');
INSERT INTO public.autostrada VALUES ('A6', 'E6', 'A6-E6', '492449395');
INSERT INTO public.autostrada VALUES ('A7', 'E7', 'A7-E7', '349443528');
INSERT INTO public.autostrada VALUES ('A8', 'E8', 'A8-E8', '1230897494');
INSERT INTO public.autostrada VALUES ('A9', 'E9', 'A9-E9', '2044527743');
INSERT INTO public.autostrada VALUES ('A10', 'E10', 'A10-E10', '1659408084');
INSERT INTO public.autostrada VALUES ('A11', 'E11', 'A11-E11', '1234430793');
INSERT INTO public.autostrada VALUES ('A12', 'E12', 'A12-E12', '1200777122');
INSERT INTO public.autostrada VALUES ('A13', 'E13', 'A13-E13', '357261354');
INSERT INTO public.autostrada VALUES ('A14', 'E14', 'A14-E14', '2104896732');
INSERT INTO public.autostrada VALUES ('A15', 'E15', 'A15-E15', '760168406');
INSERT INTO public.autostrada VALUES ('A16', 'E16', 'A16-E16', '360397083');
INSERT INTO public.autostrada VALUES ('A17', 'E17', 'A17-E17', '1246423611');
INSERT INTO public.autostrada VALUES ('A18', 'E18', 'A18-E18', '1243628414');
INSERT INTO public.autostrada VALUES ('A19', 'E19', 'A19-E19', '1294269476');
INSERT INTO public.autostrada VALUES ('A20', 'E20', 'A20-E20', '1287719578');
INSERT INTO public.autostrada VALUES ('A21', 'E21', 'A21-E21', '1883149442');
INSERT INTO public.autostrada VALUES ('A22', 'E22', 'A22-E22', '1956250193');
INSERT INTO public.autostrada VALUES ('A23', 'E23', 'A23-E23', '1401833490');
INSERT INTO public.autostrada VALUES ('A24', 'E24', 'A24-E24', '1376237602');
INSERT INTO public.autostrada VALUES ('A25', 'E25', 'A25-E25', '1422532179');
INSERT INTO public.autostrada VALUES ('A26', 'E26', 'A26-E26', '100782504');
INSERT INTO public.autostrada VALUES ('A27', 'E27', 'A27-E27', '630114224');
INSERT INTO public.autostrada VALUES ('A28', 'E28', 'A28-E28', '799583531');
INSERT INTO public.autostrada VALUES ('A29', 'E29', 'A29-E29', '980738622');
INSERT INTO public.autostrada VALUES ('A30', 'E30', 'A30-E30', '1468179809');
INSERT INTO public.autostrada VALUES ('A31', 'E31', 'A31-E31', '319596873');
INSERT INTO public.autostrada VALUES ('A32', 'E32', 'A32-E32', '1413564504');
INSERT INTO public.autostrada VALUES ('A33', 'E33', 'A33-E33', '1488334758');
INSERT INTO public.autostrada VALUES ('A34', 'E34', 'A34-E34', '770135672');
INSERT INTO public.autostrada VALUES ('A35', 'E35', 'A35-E35', '788712468');
INSERT INTO public.autostrada VALUES ('A36', 'E36', 'A36-E36', '2141733631');
INSERT INTO public.autostrada VALUES ('A37', 'E37', 'A37-E37', '181743685');
INSERT INTO public.autostrada VALUES ('A38', 'E38', 'A38-E38', '45605229');
INSERT INTO public.autostrada VALUES ('A39', 'E39', 'A39-E39', '1633633151');
INSERT INTO public.autostrada VALUES ('A40', 'E40', 'A40-E40', '2137143857');
INSERT INTO public.autostrada VALUES ('A41', 'E41', 'A41-E41', '217721674');
INSERT INTO public.autostrada VALUES ('A42', 'E42', 'A42-E42', '987568458');
INSERT INTO public.autostrada VALUES ('A43', 'E43', 'A43-E43', '1208607046');
INSERT INTO public.autostrada VALUES ('A44', 'E44', 'A44-E44', '1662322210');
INSERT INTO public.autostrada VALUES ('A45', 'E45', 'A45-E45', '371062766');
INSERT INTO public.autostrada VALUES ('A46', 'E46', 'A46-E46', '496574920');
INSERT INTO public.autostrada VALUES ('A47', 'E47', 'A47-E47', '292330216');
INSERT INTO public.autostrada VALUES ('A48', 'E48', 'A48-E48', '887472630');
INSERT INTO public.autostrada VALUES ('A49', 'E49', 'A49-E49', '1321887614');
INSERT INTO public.autostrada VALUES ('A50', 'E50', 'A50-E50', '358377315');
INSERT INTO public.autostrada VALUES ('A51', 'E51', 'A51-E51', '1288152965');
INSERT INTO public.autostrada VALUES ('A52', 'E52', 'A52-E52', '666487335');
INSERT INTO public.autostrada VALUES ('A53', 'E53', 'A53-E53', '1272826309');
INSERT INTO public.autostrada VALUES ('A54', 'E54', 'A54-E54', '1595110367');
INSERT INTO public.autostrada VALUES ('A55', 'E55', 'A55-E55', '563173087');
INSERT INTO public.autostrada VALUES ('A56', 'E56', 'A56-E56', '1920543461');
INSERT INTO public.autostrada VALUES ('A57', 'E57', 'A57-E57', '1901273595');
INSERT INTO public.autostrada VALUES ('A58', 'E58', 'A58-E58', '381321034');
INSERT INTO public.autostrada VALUES ('A59', 'E59', 'A59-E59', '294317438');
INSERT INTO public.autostrada VALUES ('A60', 'E60', 'A60-E60', '2113800898');
INSERT INTO public.autostrada VALUES ('A61', 'E61', 'A61-E61', '1457939954');
INSERT INTO public.autostrada VALUES ('A62', 'E62', 'A62-E62', '2120337454');
INSERT INTO public.autostrada VALUES ('A63', 'E63', 'A63-E63', '1545742373');
INSERT INTO public.autostrada VALUES ('A64', 'E64', 'A64-E64', '537819144');
INSERT INTO public.autostrada VALUES ('A65', 'E65', 'A65-E65', '883940858');
INSERT INTO public.autostrada VALUES ('A66', 'E66', 'A66-E66', '2041174051');
INSERT INTO public.autostrada VALUES ('A67', 'E67', 'A67-E67', '659326900');
INSERT INTO public.autostrada VALUES ('A68', 'E68', 'A68-E68', '51984499');
INSERT INTO public.autostrada VALUES ('A69', 'E69', 'A69-E69', '1651913631');
INSERT INTO public.autostrada VALUES ('A70', 'E70', 'A70-E70', '194442358');
INSERT INTO public.autostrada VALUES ('A71', 'E71', 'A71-E71', '1083006046');
INSERT INTO public.autostrada VALUES ('A72', 'E72', 'A72-E72', '814504252');
INSERT INTO public.autostrada VALUES ('A73', 'E73', 'A73-E73', '1420627287');
INSERT INTO public.autostrada VALUES ('A74', 'E74', 'A74-E74', '1078759223');
INSERT INTO public.autostrada VALUES ('A75', 'E75', 'A75-E75', '1841307625');
INSERT INTO public.autostrada VALUES ('A76', 'E76', 'A76-E76', '1690111274');
INSERT INTO public.autostrada VALUES ('A77', 'E77', 'A77-E77', '705533396');
INSERT INTO public.autostrada VALUES ('A78', 'E78', 'A78-E78', '99601403');
INSERT INTO public.autostrada VALUES ('A79', 'E79', 'A79-E79', '611963876');
INSERT INTO public.autostrada VALUES ('A80', 'E80', 'A80-E80', '2122304494');
INSERT INTO public.autostrada VALUES ('A81', 'E81', 'A81-E81', '1388330296');
INSERT INTO public.autostrada VALUES ('A82', 'E82', 'A82-E82', '1800474680');
INSERT INTO public.autostrada VALUES ('A83', 'E83', 'A83-E83', '741298048');
INSERT INTO public.autostrada VALUES ('A84', 'E84', 'A84-E84', '1095121646');
INSERT INTO public.autostrada VALUES ('A85', 'E85', 'A85-E85', '959058985');
INSERT INTO public.autostrada VALUES ('A86', 'E86', 'A86-E86', '1254920266');
INSERT INTO public.autostrada VALUES ('A87', 'E87', 'A87-E87', '1392838182');
INSERT INTO public.autostrada VALUES ('A88', 'E88', 'A88-E88', '1326968596');
INSERT INTO public.autostrada VALUES ('A89', 'E89', 'A89-E89', '2045497182');
INSERT INTO public.autostrada VALUES ('A90', 'E90', 'A90-E90', '289024085');
INSERT INTO public.autostrada VALUES ('A91', 'E91', 'A91-E91', '1215726798');
INSERT INTO public.autostrada VALUES ('A92', 'E92', 'A92-E92', '1943537638');
INSERT INTO public.autostrada VALUES ('A93', 'E93', 'A93-E93', '1011327122');
INSERT INTO public.autostrada VALUES ('A94', 'E94', 'A94-E94', '1825669771');
INSERT INTO public.autostrada VALUES ('A95', 'E95', 'A95-E95', '730771842');
INSERT INTO public.autostrada VALUES ('A96', 'E96', 'A96-E96', '211934660');
INSERT INTO public.autostrada VALUES ('A97', 'E97', 'A97-E97', '1424862981');
INSERT INTO public.autostrada VALUES ('A98', 'E98', 'A98-E98', '1650763466');
INSERT INTO public.autostrada VALUES ('A99', 'E99', 'A99-E99', '1492790342');
INSERT INTO public.autostrada VALUES ('A100', 'E100', 'A100-E100', '640820344');


--
-- TOC entry 3424 (class 0 OID 17296)
-- Dependencies: 216
-- Data for Name: casello; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.casello VALUES ('3', 'A69', 'E687', '3', '-4030.3193', '-711.42017', 1, '1424-10-20');
INSERT INTO public.casello VALUES ('6', 'A89', 'D532', '6', '28.34797', '-258.8421', 1, '1158-07-20');
INSERT INTO public.casello VALUES ('18', 'A17', 'F566', '18', '-3032.0745', '1370.5051', 0, 'NULL');
INSERT INTO public.casello VALUES ('19', 'A97', 'D757', '19', '-3308.785', '-116.028786', 0, 'NULL');
INSERT INTO public.casello VALUES ('28', 'A98', 'A313', '28', '3080.697', '-2647.5786', 1, '1738-01-04');
INSERT INTO public.casello VALUES ('30', 'A33', 'A313', '30', '-1246.8893', '-2258.0195', 1, '2934-01-15');
INSERT INTO public.casello VALUES ('40', 'A78', 'C449', '40', '-4569.518', '-924.9699', 1, '0086-10-13');
INSERT INTO public.casello VALUES ('43', 'A20', 'D757', '43', '3003.0007', '-409.3915', 1, '2157-12-23');
INSERT INTO public.casello VALUES ('54', 'A9', 'L439', '54', '-1731.9423', '-3141.4175', 0, 'NULL');
INSERT INTO public.casello VALUES ('56', 'A37', 'L166', '56', '-2265.5696', '3149.3425', 1, '0385-06-09');
INSERT INTO public.casello VALUES ('60', 'A41', 'A777', '60', '4643.9214', '3088.7688', 0, 'NULL');
INSERT INTO public.casello VALUES ('68', 'A7', 'D108', '68', '-516.30676', '1979.0262', 1, '0814-06-16');
INSERT INTO public.casello VALUES ('76', 'A49', 'A909', '76', '4053.391', '-2893.3262', 1, '1858-04-20');
INSERT INTO public.casello VALUES ('128', 'A50', 'I866', '128', '2963.4346', '3931.6118', 1, '1497-05-21');
INSERT INTO public.casello VALUES ('131', 'A23', 'M079', '131', '2106.3596', '-4859.3633', 0, 'NULL');
INSERT INTO public.casello VALUES ('140', 'A8', 'M323', '140', '3071.8457', '3399.2356', 1, '1424-04-03');
INSERT INTO public.casello VALUES ('154', 'A13', 'A392', '154', '1044.0981', '364.26306', 1, '2603-11-22');
INSERT INTO public.casello VALUES ('161', 'A25', 'A326', '161', '2622.17', '1892.0667', 0, 'NULL');
INSERT INTO public.casello VALUES ('187', 'A29', 'B409', '187', '-1662.2747', '-418.5277', 1, '2472-10-28');
INSERT INTO public.casello VALUES ('211', 'A60', 'B920', '211', '-4836.439', '178.3371', 0, 'NULL');
INSERT INTO public.casello VALUES ('212', 'A14', 'G924', '212', '4906.136', '-3291.005', 0, 'NULL');
INSERT INTO public.casello VALUES ('234', 'A93', 'E307', '234', '1855.7435', '1119.9778', 1, '2492-08-22');
INSERT INTO public.casello VALUES ('256', 'A26', 'G619', '256', '-4019.7407', '828.5761', 0, 'NULL');
INSERT INTO public.casello VALUES ('258', 'A99', 'G305', '258', '264.55463', '-2508.8936', 0, 'NULL');
INSERT INTO public.casello VALUES ('267', 'A3', 'F165', '267', '-3054.1282', '1219.0664', 1, '1404-10-16');
INSERT INTO public.casello VALUES ('268', 'A91', 'C006', '268', '-3766.7358', '2719.5334', 0, 'NULL');
INSERT INTO public.casello VALUES ('269', 'A89', 'E709', '269', '4726.614', '-4723.4604', 1, '2580-11-17');
INSERT INTO public.casello VALUES ('277', 'A33', 'F392', '277', '-606.58636', '4310.1646', 0, 'NULL');
INSERT INTO public.casello VALUES ('282', 'A25', 'E480', '282', '-1127.0964', '2976.1755', 1, '0872-04-08');
INSERT INTO public.casello VALUES ('286', 'A30', 'I408', '286', '372.1231', '678.46', 1, '1543-05-17');
INSERT INTO public.casello VALUES ('288', 'A16', 'G224', '288', '3739.7505', '4196.2676', 0, 'NULL');
INSERT INTO public.casello VALUES ('291', 'A49', 'A326', '291', '2099.4146', '1471.2303', 1, '2131-12-13');
INSERT INTO public.casello VALUES ('297', 'A63', 'E666', '297', '2233.6567', '80.62005', 0, 'NULL');
INSERT INTO public.casello VALUES ('302', 'A18', 'B920', '302', '3226.5293', '2285.542', 0, 'NULL');
INSERT INTO public.casello VALUES ('323', 'A20', 'G039', '323', '-4065.9673', '359.41064', 0, 'NULL');
INSERT INTO public.casello VALUES ('334', 'A81', 'G859', '334', '2870.4082', '76.23136', 1, '1581-05-01');
INSERT INTO public.casello VALUES ('345', 'A13', 'D607', '345', '1782.6008', '-3753.8784', 0, 'NULL');
INSERT INTO public.casello VALUES ('372', 'A66', 'G039', '372', '-3070.187', '3526.5244', 0, 'NULL');
INSERT INTO public.casello VALUES ('376', 'A44', 'D121', '376', '122.368935', '-2645.0437', 1, '1589-04-18');
INSERT INTO public.casello VALUES ('377', 'A15', 'F734', '377', '-3281.3018', '2690.9656', 0, 'NULL');
INSERT INTO public.casello VALUES ('383', 'A42', 'E929', '383', '-3696.0417', '-2164.225', 1, '2937-07-14');
INSERT INTO public.casello VALUES ('405', 'A56', 'M323', '405', '-1062.982', '-3244.0508', 1, '1994-10-25');
INSERT INTO public.casello VALUES ('406', 'A14', 'H672', '406', '4670.756', '-2332.2124', 0, 'NULL');
INSERT INTO public.casello VALUES ('422', 'A46', 'H880', '422', '1288.1249', '1391.9001', 0, 'NULL');
INSERT INTO public.casello VALUES ('431', 'A18', 'D607', '431', '-413.77545', '3190.4705', 0, 'NULL');
INSERT INTO public.casello VALUES ('432', 'A49', 'C006', '432', '-4275.4883', '-1911.7046', 1, '0034-06-19');
INSERT INTO public.casello VALUES ('439', 'A82', 'E687', '439', '2711.2168', '2558.7095', 0, 'NULL');
INSERT INTO public.casello VALUES ('446', 'A76', 'E307', '446', '3392.4253', '3615.5002', 1, '0838-05-08');
INSERT INTO public.casello VALUES ('447', 'A99', 'B312', '447', '-3745.2073', '1268.4613', 1, '1322-04-20');
INSERT INTO public.casello VALUES ('452', 'A4', 'A178', '452', '2039.243', '-3937.531', 0, 'NULL');
INSERT INTO public.casello VALUES ('453', 'A65', 'M177', '453', '-1803.978', '1700.7864', 0, 'NULL');
INSERT INTO public.casello VALUES ('454', 'A12', 'F734', '454', '-4161.028', '2242.7595', 1, '2940-06-05');
INSERT INTO public.casello VALUES ('473', 'A11', 'D532', '473', '2008.5883', '-87.889435', 1, '0971-03-15');
INSERT INTO public.casello VALUES ('479', 'A57', 'H030', '479', '-617.75684', '-2653.9648', 0, 'NULL');
INSERT INTO public.casello VALUES ('482', 'A9', 'L578', '482', '4377.5547', '-3559.6675', 0, 'NULL');
INSERT INTO public.casello VALUES ('488', 'A18', 'G966', '488', '1002.9006', '-2615.565', 1, '1782-06-10');
INSERT INTO public.casello VALUES ('489', 'A62', 'I866', '489', '-3216.6064', '3613.4517', 1, '0728-09-25');
INSERT INTO public.casello VALUES ('499', 'A74', 'D108', '499', '-429.59988', '3071.016', 0, 'NULL');
INSERT INTO public.casello VALUES ('500', 'A62', 'B829', '500', '244.81117', '705.3638', 0, 'NULL');
INSERT INTO public.casello VALUES ('511', 'A73', 'A909', '511', '3345.3518', '834.254', 1, '1577-12-17');
INSERT INTO public.casello VALUES ('513', 'A68', 'F566', '513', '4503.6484', '-1106.0774', 1, '0722-05-02');
INSERT INTO public.casello VALUES ('527', 'A51', 'A392', '527', '830.9978', '4464.1973', 0, 'NULL');
INSERT INTO public.casello VALUES ('530', 'A1', 'M177', '530', '1746.766', '-1002.68604', 0, 'NULL');
INSERT INTO public.casello VALUES ('540', 'A47', 'L578', '540', '3995.5986', '-2507.282', 0, 'NULL');
INSERT INTO public.casello VALUES ('545', 'A18', 'F841', '545', '-1039.9932', '2428.6199', 0, 'NULL');
INSERT INTO public.casello VALUES ('554', 'A100', 'F392', '554', '-4858.3867', '-3222.0752', 1, '1147-10-08');
INSERT INTO public.casello VALUES ('560', 'A10', 'I648', '560', '1366.1469', '-82.25977', 1, '1020-03-14');
INSERT INTO public.casello VALUES ('562', 'A4', 'G859', '562', '1011.1553', '3841.12', 0, 'NULL');
INSERT INTO public.casello VALUES ('567', 'A33', 'C449', '567', '-4984.6206', '-805.04535', 1, '0954-12-18');
INSERT INTO public.casello VALUES ('573', 'A66', 'E968', '573', '-1872.8309', '1584.0792', 0, 'NULL');
INSERT INTO public.casello VALUES ('603', 'A32', 'F841', '603', '3391.086', '-2282.8157', 0, 'NULL');
INSERT INTO public.casello VALUES ('607', 'A76', 'E810', '607', '37.14144', '3632.8357', 1, '0267-01-07');
INSERT INTO public.casello VALUES ('612', 'A31', 'E929', '612', '-4895.5254', '173.3166', 0, 'NULL');
INSERT INTO public.casello VALUES ('623', 'A88', 'F912', '623', '2754.6692', '4889.9097', 1, '0306-12-04');
INSERT INTO public.casello VALUES ('639', 'A8', 'G619', '639', '-3920.8608', '-3420.021', 0, 'NULL');
INSERT INTO public.casello VALUES ('642', 'A91', 'E060', '642', '4362.964', '-3617.2874', 0, 'NULL');
INSERT INTO public.casello VALUES ('659', 'A12', 'E666', '659', '-1017.2987', '-2390.0754', 0, 'NULL');
INSERT INTO public.casello VALUES ('666', 'A96', 'E055', '666', '-4945.1987', '-1080.119', 0, 'NULL');
INSERT INTO public.casello VALUES ('670', 'A62', 'F165', '670', '81.78473', '-3097.4346', 0, 'NULL');
INSERT INTO public.casello VALUES ('675', 'A28', 'I648', '675', '-4175.026', '-2287.3794', 1, '2805-12-17');
INSERT INTO public.casello VALUES ('685', 'A68', 'B828', '685', '-3851.4763', '-4189.404', 0, 'NULL');
INSERT INTO public.casello VALUES ('693', 'A6', 'E810', '693', '1897.1025', '4039.4353', 0, 'NULL');
INSERT INTO public.casello VALUES ('701', 'A19', 'H880', '701', '-2426.436', '4313.2793', 1, '0791-01-12');
INSERT INTO public.casello VALUES ('708', 'A89', 'G305', '708', '-3691.278', '-1788.8248', 0, 'NULL');
INSERT INTO public.casello VALUES ('733', 'A33', 'A178', '733', '2571.6514', '3463.4', 1, '0752-09-16');
INSERT INTO public.casello VALUES ('763', 'A13', 'L166', '763', '-1031.6188', '-3828.063', 0, 'NULL');
INSERT INTO public.casello VALUES ('769', 'A63', 'I812', '769', '2057.7036', '2572.5889', 1, '0320-12-03');
INSERT INTO public.casello VALUES ('776', 'A84', 'B828', '776', '-3568.644', '3857.0059', 0, 'NULL');
INSERT INTO public.casello VALUES ('778', 'A99', 'E307', '778', '-540.36975', '-2155.4941', 1, '1571-09-23');
INSERT INTO public.casello VALUES ('783', 'A15', 'B312', '783', '-896.94025', '4289.075', 0, 'NULL');
INSERT INTO public.casello VALUES ('788', 'A34', 'G924', '788', '-284.72067', '106.40085', 1, '2105-06-21');
INSERT INTO public.casello VALUES ('792', 'A73', 'L908', '792', '-1341.5951', '-2452.7388', 0, 'NULL');
INSERT INTO public.casello VALUES ('815', 'A55', 'I812', '815', '2554.614', '658.4585', 1, '0108-09-22');
INSERT INTO public.casello VALUES ('821', 'A26', 'D121', '821', '4173.6533', '-2263.0823', 1, '0101-11-06');
INSERT INTO public.casello VALUES ('823', 'A70', 'E060', '823', '-3496.5051', '-2914.002', 1, '0566-12-23');
INSERT INTO public.casello VALUES ('842', 'A82', 'H672', '842', '-416.3939', '-1160.8398', 1, '1432-12-15');
INSERT INTO public.casello VALUES ('865', 'A97', 'L439', '865', '-1194.4241', '-3427.9626', 0, 'NULL');
INSERT INTO public.casello VALUES ('868', 'A97', 'G224', '868', '249.20345', '-601.12775', 0, 'NULL');
INSERT INTO public.casello VALUES ('871', 'A26', 'B829', '871', '-4893.9253', '2613.2273', 0, 'NULL');
INSERT INTO public.casello VALUES ('897', 'A68', 'A777', '897', '2139.1052', '1578.1444', 0, 'NULL');
INSERT INTO public.casello VALUES ('903', 'A74', 'F912', '903', '681.4849', '4260.1885', 1, '1971-06-07');
INSERT INTO public.casello VALUES ('909', 'A27', 'H030', '909', '-4756.6094', '4800.6904', 0, 'NULL');
INSERT INTO public.casello VALUES ('913', 'A34', 'I408', '913', '-2504.9407', '796.4659', 0, 'NULL');
INSERT INTO public.casello VALUES ('916', 'A16', 'B409', '916', '-977.53406', '745.31195', 1, '1199-06-01');
INSERT INTO public.casello VALUES ('918', 'A8', 'E709', '918', '4965.2773', '-1570.7255', 1, '1838-02-21');
INSERT INTO public.casello VALUES ('941', 'A66', 'E480', '941', '4083.246', '3740.3596', 1, '0570-09-06');
INSERT INTO public.casello VALUES ('952', 'A42', 'G966', '952', '-2300.911', '2086.464', 0, 'NULL');
INSERT INTO public.casello VALUES ('974', 'A4', 'E968', '974', '-4378.6484', '-1620.3112', 1, '2613-06-11');
INSERT INTO public.casello VALUES ('989', 'A34', 'M079', '989', '-4264.367', '348.16742', 0, 'NULL');
INSERT INTO public.casello VALUES ('993', 'A47', 'E055', '993', '-3174.7837', '-2677.5564', 1, '1793-12-19');
INSERT INTO public.casello VALUES ('994', 'A71', 'L908', '994', '2912.3582', '-2554.2473', 1, '1417-03-31');


--
-- TOC entry 3425 (class 0 OID 17301)
-- Dependencies: 217
-- Data for Name: comune; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.comune VALUES ('G619', 'AL', 'Pietra Marazzi');
INSERT INTO public.comune VALUES ('A326', 'AO', 'Aosta');
INSERT INTO public.comune VALUES ('H672', 'AO', 'Saint-Nicolas');
INSERT INTO public.comune VALUES ('E307', 'AQ', 'Introdacqua');
INSERT INTO public.comune VALUES ('F566', 'AV', 'Montemiletto');
INSERT INTO public.comune VALUES ('I812', 'BG', 'Solto Collina');
INSERT INTO public.comune VALUES ('E687', 'BL', 'Lorenzago di Cadore');
INSERT INTO public.comune VALUES ('I866', 'BL', 'Sospirolo');
INSERT INTO public.comune VALUES ('A392', 'BO', 'Argelato');
INSERT INTO public.comune VALUES ('G859', 'BS', 'Pontevico');
INSERT INTO public.comune VALUES ('F392', 'BZ', 'Montagna sulla Strada del Vino/Montan an der Weinstraße');
INSERT INTO public.comune VALUES ('D757', 'CH', 'Fraine');
INSERT INTO public.comune VALUES ('M323', 'FE', 'Fiscaglia');
INSERT INTO public.comune VALUES ('B829', 'FG', 'Carpino');
INSERT INTO public.comune VALUES ('H880', 'FR', 'San Giorgio a Liri');
INSERT INTO public.comune VALUES ('I408', 'FR', 'San Vittore del Lazio');
INSERT INTO public.comune VALUES ('E810', 'GR', 'Magliano in Toscana');
INSERT INTO public.comune VALUES ('L166', 'LE', 'Tiggiano');
INSERT INTO public.comune VALUES ('F165', 'MB', 'Mezzago');
INSERT INTO public.comune VALUES ('A313', 'ME', 'Antillo');
INSERT INTO public.comune VALUES ('D607', 'MO', 'Fiorano Modenese');
INSERT INTO public.comune VALUES ('B920', 'NO', 'Casalvolone');
INSERT INTO public.comune VALUES ('E055', 'PA', 'Giuliana');
INSERT INTO public.comune VALUES ('A909', 'PC', 'Bobbio');
INSERT INTO public.comune VALUES ('E709', 'PD', 'Lozzo Atestino');
INSERT INTO public.comune VALUES ('G224', 'PD', 'Padova');
INSERT INTO public.comune VALUES ('D108', 'PG', 'Costacciaro');
INSERT INTO public.comune VALUES ('M079', 'PV', 'Vistarino');
INSERT INTO public.comune VALUES ('L439', 'PZ', 'Trivigno');
INSERT INTO public.comune VALUES ('D121', 'RA', 'Cotignola');
INSERT INTO public.comune VALUES ('E968', 'RC', 'Maropati');
INSERT INTO public.comune VALUES ('B828', 'RM', 'Carpineto Romano');
INSERT INTO public.comune VALUES ('F734', 'RM', 'Morlupo');
INSERT INTO public.comune VALUES ('E060', 'SA', 'Giungano');
INSERT INTO public.comune VALUES ('E480', 'SA', 'Laureana Cilento');
INSERT INTO public.comune VALUES ('F912', 'SA', 'Nocera Inferiore');
INSERT INTO public.comune VALUES ('G039', 'SA', 'Oliveto Citra');
INSERT INTO public.comune VALUES ('I648', 'SA', 'Serramezzana');
INSERT INTO public.comune VALUES ('A777', 'SO', 'Bema');
INSERT INTO public.comune VALUES ('L908', 'SO', 'Villa di Tirano');
INSERT INTO public.comune VALUES ('M177', 'SP', 'Zignago');
INSERT INTO public.comune VALUES ('C006', 'SR', 'Cassaro');
INSERT INTO public.comune VALUES ('G924', 'SS', 'Porto Torres');
INSERT INTO public.comune VALUES ('F841', 'SU', 'Narcao');
INSERT INTO public.comune VALUES ('B409', 'SV', 'Calice Ligure');
INSERT INTO public.comune VALUES ('C449', 'TE', 'Cellino Attanasio');
INSERT INTO public.comune VALUES ('A178', 'TN', 'Aldeno');
INSERT INTO public.comune VALUES ('G305', 'TN', 'Panchià');
INSERT INTO public.comune VALUES ('D532', 'TO', 'Fenestrelle');
INSERT INTO public.comune VALUES ('L578', 'TO', 'Valgioie');
INSERT INTO public.comune VALUES ('G966', 'UD', 'Pozzuolo del Friuli');
INSERT INTO public.comune VALUES ('B312', 'VA', 'Castello Cabiaglio');
INSERT INTO public.comune VALUES ('E666', 'VA', 'Lonate Pozzolo');
INSERT INTO public.comune VALUES ('E929', 'VA', 'Marchirolo');
INSERT INTO public.comune VALUES ('H030', 'VB', 'Premeno');


--
-- TOC entry 3426 (class 0 OID 17306)
-- Dependencies: 218
-- Data for Name: provincia; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.provincia VALUES ('AG', 19, 'Agrigento');
INSERT INTO public.provincia VALUES ('AL', 1, 'Alessandria');
INSERT INTO public.provincia VALUES ('AN', 11, 'Ancona');
INSERT INTO public.provincia VALUES ('AO', 2, 'Valle d`Aosta/Vallée d`Aoste');
INSERT INTO public.provincia VALUES ('AP', 11, 'Ascoli Piceno');
INSERT INTO public.provincia VALUES ('AQ', 13, 'L`Aquila');
INSERT INTO public.provincia VALUES ('AR', 9, 'Arezzo');
INSERT INTO public.provincia VALUES ('AT', 1, 'Asti');
INSERT INTO public.provincia VALUES ('AV', 15, 'Avellino');
INSERT INTO public.provincia VALUES ('BA', 16, 'Bari');
INSERT INTO public.provincia VALUES ('BG', 3, 'Bergamo');
INSERT INTO public.provincia VALUES ('BI', 1, 'Biella');
INSERT INTO public.provincia VALUES ('BL', 5, 'Belluno');
INSERT INTO public.provincia VALUES ('BN', 15, 'Benevento');
INSERT INTO public.provincia VALUES ('BO', 8, 'Bologna');
INSERT INTO public.provincia VALUES ('BR', 16, 'Brindisi');
INSERT INTO public.provincia VALUES ('BS', 3, 'Brescia');
INSERT INTO public.provincia VALUES ('BT', 16, 'Barletta-Andria-Trani');
INSERT INTO public.provincia VALUES ('BZ', 4, 'Bolzano/Bozen');
INSERT INTO public.provincia VALUES ('CA', 20, 'Cagliari');
INSERT INTO public.provincia VALUES ('CB', 14, 'Campobasso');
INSERT INTO public.provincia VALUES ('CE', 15, 'Caserta');
INSERT INTO public.provincia VALUES ('CH', 13, 'Chieti');
INSERT INTO public.provincia VALUES ('CL', 19, 'Caltanissetta');
INSERT INTO public.provincia VALUES ('CN', 1, 'Cuneo');
INSERT INTO public.provincia VALUES ('CO', 3, 'Como');
INSERT INTO public.provincia VALUES ('CR', 3, 'Cremona');
INSERT INTO public.provincia VALUES ('CS', 18, 'Cosenza');
INSERT INTO public.provincia VALUES ('CT', 19, 'Catania');
INSERT INTO public.provincia VALUES ('CZ', 18, 'Catanzaro');
INSERT INTO public.provincia VALUES ('EN', 19, 'Enna');
INSERT INTO public.provincia VALUES ('FC', 8, 'Forlì-Cesena');
INSERT INTO public.provincia VALUES ('FE', 8, 'Ferrara');
INSERT INTO public.provincia VALUES ('FG', 16, 'Foggia');
INSERT INTO public.provincia VALUES ('FI', 9, 'Firenze');
INSERT INTO public.provincia VALUES ('FM', 11, 'Fermo');
INSERT INTO public.provincia VALUES ('FR', 12, 'Frosinone');
INSERT INTO public.provincia VALUES ('GE', 7, 'Genova');
INSERT INTO public.provincia VALUES ('GO', 6, 'Gorizia');
INSERT INTO public.provincia VALUES ('GR', 9, 'Grosseto');
INSERT INTO public.provincia VALUES ('IM', 7, 'Imperia');
INSERT INTO public.provincia VALUES ('IS', 14, 'Isernia');
INSERT INTO public.provincia VALUES ('KR', 18, 'Crotone');
INSERT INTO public.provincia VALUES ('LC', 3, 'Lecco');
INSERT INTO public.provincia VALUES ('LE', 16, 'Lecce');
INSERT INTO public.provincia VALUES ('LI', 9, 'Livorno');
INSERT INTO public.provincia VALUES ('LO', 3, 'Lodi');
INSERT INTO public.provincia VALUES ('LT', 12, 'Latina');
INSERT INTO public.provincia VALUES ('LU', 9, 'Lucca');
INSERT INTO public.provincia VALUES ('MB', 3, 'Monza e della Brianza');
INSERT INTO public.provincia VALUES ('MC', 11, 'Macerata');
INSERT INTO public.provincia VALUES ('ME', 19, 'Messina');
INSERT INTO public.provincia VALUES ('MI', 3, 'Milano');
INSERT INTO public.provincia VALUES ('MN', 3, 'Mantova');
INSERT INTO public.provincia VALUES ('MO', 8, 'Modena');
INSERT INTO public.provincia VALUES ('MS', 9, 'Massa-Carrara');
INSERT INTO public.provincia VALUES ('MT', 17, 'Matera');
INSERT INTO public.provincia VALUES ('NA', 15, 'Napoli');
INSERT INTO public.provincia VALUES ('NO', 1, 'Novara');
INSERT INTO public.provincia VALUES ('NU', 20, 'Nuoro');
INSERT INTO public.provincia VALUES ('OR', 20, 'Oristano');
INSERT INTO public.provincia VALUES ('PA', 19, 'Palermo');
INSERT INTO public.provincia VALUES ('PC', 8, 'Piacenza');
INSERT INTO public.provincia VALUES ('PD', 5, 'Padova');
INSERT INTO public.provincia VALUES ('PE', 13, 'Pescara');
INSERT INTO public.provincia VALUES ('PG', 10, 'Perugia');
INSERT INTO public.provincia VALUES ('PI', 9, 'Pisa');
INSERT INTO public.provincia VALUES ('PN', 6, 'Pordenone');
INSERT INTO public.provincia VALUES ('PO', 9, 'Prato');
INSERT INTO public.provincia VALUES ('PR', 8, 'Parma');
INSERT INTO public.provincia VALUES ('PT', 9, 'Pistoia');
INSERT INTO public.provincia VALUES ('PU', 11, 'Pesaro e Urbino');
INSERT INTO public.provincia VALUES ('PV', 3, 'Pavia');
INSERT INTO public.provincia VALUES ('PZ', 17, 'Potenza');
INSERT INTO public.provincia VALUES ('RA', 8, 'Ravenna');
INSERT INTO public.provincia VALUES ('RC', 18, 'Reggio Calabria');
INSERT INTO public.provincia VALUES ('RE', 8, 'Reggio nell`Emilia');
INSERT INTO public.provincia VALUES ('RG', 19, 'Ragusa');
INSERT INTO public.provincia VALUES ('RI', 12, 'Rieti');
INSERT INTO public.provincia VALUES ('RM', 12, 'Roma');
INSERT INTO public.provincia VALUES ('RN', 8, 'Rimini');
INSERT INTO public.provincia VALUES ('RO', 5, 'Rovigo');
INSERT INTO public.provincia VALUES ('SA', 15, 'Salerno');
INSERT INTO public.provincia VALUES ('SI', 9, 'Siena');
INSERT INTO public.provincia VALUES ('SO', 3, 'Sondrio');
INSERT INTO public.provincia VALUES ('SP', 7, 'La Spezia');
INSERT INTO public.provincia VALUES ('SR', 19, 'Siracusa');
INSERT INTO public.provincia VALUES ('SS', 20, 'Sassari');
INSERT INTO public.provincia VALUES ('SU', 20, 'Sud Sardegna');
INSERT INTO public.provincia VALUES ('SV', 7, 'Savona');
INSERT INTO public.provincia VALUES ('TA', 16, 'Taranto');
INSERT INTO public.provincia VALUES ('TE', 13, 'Teramo');
INSERT INTO public.provincia VALUES ('TN', 4, 'Trento');
INSERT INTO public.provincia VALUES ('TO', 1, 'Torino');
INSERT INTO public.provincia VALUES ('TP', 19, 'Trapani');
INSERT INTO public.provincia VALUES ('TR', 10, 'Terni');
INSERT INTO public.provincia VALUES ('TS', 6, 'Trieste');
INSERT INTO public.provincia VALUES ('TV', 5, 'Treviso');
INSERT INTO public.provincia VALUES ('UD', 6, 'Udine');
INSERT INTO public.provincia VALUES ('VA', 3, 'Varese');
INSERT INTO public.provincia VALUES ('VB', 1, 'Verbano-Cusio-Ossola');
INSERT INTO public.provincia VALUES ('VC', 1, 'Vercelli');
INSERT INTO public.provincia VALUES ('VE', 5, 'Venezia');
INSERT INTO public.provincia VALUES ('VI', 5, 'Vicenza');
INSERT INTO public.provincia VALUES ('VR', 5, 'Verona');
INSERT INTO public.provincia VALUES ('VT', 12, 'Viterbo');
INSERT INTO public.provincia VALUES ('VV', 18, 'Vibo Valentia');


--
-- TOC entry 3427 (class 0 OID 17311)
-- Dependencies: 219
-- Data for Name: regione; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.regione VALUES (1, 'Piemonte');
INSERT INTO public.regione VALUES (2, 'Valle d`Aosta');
INSERT INTO public.regione VALUES (3, 'Lombardia');
INSERT INTO public.regione VALUES (4, 'Trentino-Alto Adige');
INSERT INTO public.regione VALUES (5, 'Veneto');
INSERT INTO public.regione VALUES (6, 'Friuli-Venezia Giulia');
INSERT INTO public.regione VALUES (7, 'Liguria');
INSERT INTO public.regione VALUES (8, 'Emilia-Romagna');
INSERT INTO public.regione VALUES (9, 'Toscana');
INSERT INTO public.regione VALUES (10, 'Umbria');
INSERT INTO public.regione VALUES (11, 'Marche');
INSERT INTO public.regione VALUES (12, 'Lazio');
INSERT INTO public.regione VALUES (13, 'Abruzzo');
INSERT INTO public.regione VALUES (14, 'Molise');
INSERT INTO public.regione VALUES (15, 'Campania');
INSERT INTO public.regione VALUES (16, 'Puglia');
INSERT INTO public.regione VALUES (17, 'Basilicata');
INSERT INTO public.regione VALUES (18, 'Calabria');
INSERT INTO public.regione VALUES (19, 'Sicilia');
INSERT INTO public.regione VALUES (20, 'Sardegna');


--
-- TOC entry 3267 (class 2606 OID 17317)
-- Name: autostrada cod_naz_autostrada_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.autostrada
    ADD CONSTRAINT cod_naz_autostrada_pk PRIMARY KEY (cod_naz);


--
-- TOC entry 3269 (class 2606 OID 17319)
-- Name: casello codice_casello_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.casello
    ADD CONSTRAINT codice_casello_pk PRIMARY KEY (codice);


--
-- TOC entry 3271 (class 2606 OID 17321)
-- Name: comune codice_comune_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.comune
    ADD CONSTRAINT codice_comune_pk PRIMARY KEY (codice);


--
-- TOC entry 3275 (class 2606 OID 17323)
-- Name: regione codice_regione_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.regione
    ADD CONSTRAINT codice_regione_pk PRIMARY KEY (codice);


--
-- TOC entry 3273 (class 2606 OID 17325)
-- Name: provincia sigla_provincia_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.provincia
    ADD CONSTRAINT sigla_provincia_pk PRIMARY KEY (sigla);


--
-- TOC entry 3276 (class 2606 OID 17326)
-- Name: casello cod_naz_casello_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.casello
    ADD CONSTRAINT cod_naz_casello_fk FOREIGN KEY (cod_naz) REFERENCES public.autostrada(cod_naz) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3277 (class 2606 OID 17331)
-- Name: casello comune_casello_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.casello
    ADD CONSTRAINT comune_casello_fk FOREIGN KEY (comune) REFERENCES public.comune(codice) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3278 (class 2606 OID 17336)
-- Name: comune comune_provincia_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.comune
    ADD CONSTRAINT comune_provincia_fk FOREIGN KEY (provincia) REFERENCES public.provincia(sigla) ON UPDATE CASCADE;


--
-- TOC entry 3279 (class 2606 OID 17341)
-- Name: provincia regione_provincia_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.provincia
    ADD CONSTRAINT regione_provincia_fk FOREIGN KEY (regione) REFERENCES public.regione(codice) ON UPDATE CASCADE;


-- Completed on 2024-09-12 15:58:10 CEST

--
-- PostgreSQL database dump complete
--

