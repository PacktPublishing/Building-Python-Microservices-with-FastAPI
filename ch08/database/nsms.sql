--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: admin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admin (
    id integer NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    age integer NOT NULL,
    date_started date NOT NULL,
    status integer NOT NULL,
    login_id integer NOT NULL,
    birthday date NOT NULL
);


ALTER TABLE public.admin OWNER TO postgres;

--
-- Name: billing; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.billing (
    id integer NOT NULL,
    payable double precision NOT NULL,
    approved_by character varying(45) NOT NULL,
    date_approved date NOT NULL,
    date_billed date NOT NULL,
    total_issues integer NOT NULL,
    vendor_id integer NOT NULL,
    admin_id integer NOT NULL,
    received_by character varying(45) NOT NULL,
    date_received date NOT NULL
);


ALTER TABLE public.billing OWNER TO postgres;

--
-- Name: content; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.content (
    id integer NOT NULL,
    publication_id integer NOT NULL,
    headline character varying(100) NOT NULL,
    content text NOT NULL,
    content_type character varying(20) NOT NULL,
    date_published date NOT NULL
);


ALTER TABLE public.content OWNER TO postgres;

--
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    id integer NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    age integer NOT NULL,
    birthday date NOT NULL,
    date_subscribed date NOT NULL,
    status integer NOT NULL,
    subscription_type integer NOT NULL,
    login_id integer NOT NULL
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- Name: login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login (
    id integer NOT NULL,
    username character varying(45) NOT NULL,
    password character varying(45) NOT NULL,
    user_type integer NOT NULL
);


ALTER TABLE public.login OWNER TO postgres;

--
-- Name: messenger; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.messenger (
    id integer NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    salary double precision NOT NULL,
    date_employed date NOT NULL,
    status integer NOT NULL,
    vendor_id integer NOT NULL
);


ALTER TABLE public.messenger OWNER TO postgres;

--
-- Name: publication; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.publication (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    type character varying(45) NOT NULL,
    vendor_id integer NOT NULL,
    messenger_id integer NOT NULL
);


ALTER TABLE public.publication OWNER TO postgres;

--
-- Name: sales; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sales (
    id integer NOT NULL,
    publication_id integer NOT NULL,
    copies_issued integer NOT NULL,
    date_issued date NOT NULL,
    revenue double precision NOT NULL,
    profit double precision NOT NULL,
    copies_sold integer NOT NULL
);


ALTER TABLE public.sales OWNER TO postgres;

--
-- Name: subscription; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subscription (
    id integer NOT NULL,
    customer_id integer NOT NULL,
    branch character varying(100) NOT NULL,
    price double precision NOT NULL,
    qty integer NOT NULL,
    date_purchased date NOT NULL
);


ALTER TABLE public.subscription OWNER TO postgres;

--
-- Name: vendor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vendor (
    id integer NOT NULL,
    rep_firstname character varying(45) NOT NULL,
    rep_lastname character varying(45) NOT NULL,
    rep_id character varying(45) NOT NULL,
    rep_date_employed date NOT NULL,
    account_name character varying(45) NOT NULL,
    account_number character varying(45) NOT NULL,
    date_consigned date NOT NULL,
    login_id integer NOT NULL
);


ALTER TABLE public.vendor OWNER TO postgres;

--
-- Data for Name: admin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.admin (id, firstname, lastname, age, date_started, status, login_id, birthday) FROM stdin;
1	Sherwin John	Tragura	44	2022-03-16	1	1	1978-10-30
2	Jean	Grey	40	2022-03-16	1	5	2022-03-16
\.


--
-- Data for Name: billing; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.billing (id, payable, approved_by, date_approved, date_billed, total_issues, vendor_id, admin_id, received_by, date_received) FROM stdin;
101	800000	rujen	2022-03-16	2022-03-16	1000	2	1	anna	2022-03-16
\.


--
-- Data for Name: content; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.content (id, publication_id, headline, content, content_type, date_published) FROM stdin;
403	301	Kakampink sa Ortigas	sub-main2	news	2022-03-16
401	301	Communism is back!	main	news	2022-03-16
402	301	Philippine President Son of a Murderer	sub-main1	news	2022-03-16
\.


--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer (id, firstname, lastname, age, birthday, date_subscribed, status, subscription_type, login_id) FROM stdin;
3	Mathew Geofrey	Domino	35	1983-09-23	2022-03-16	1	1	3
\.


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (id, username, password, user_type) FROM stdin;
1	sjctrags	sjctrags	0
2	owen	owen	1
3	matet	matet	2
4	abby	abby	1
5	admin	admin	1
\.


--
-- Data for Name: messenger; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.messenger (id, firstname, lastname, salary, date_employed, status, vendor_id) FROM stdin;
201	Glenn	James	10000	2022-03-16	1	2
202	Nora	Jean	15000	2022-03-16	1	2
203	Joanna	Lumley	60000	2022-04-03	1	2
204	Carlos	James	100000	2022-04-04	1	2
205	Onan	Bean	4000	2022-04-04	1	2
206	Renan	Cruz	4000	2022-04-04	1	2
207	Jimmy	Tan	2000	2022-04-04	1	2
\.


--
-- Data for Name: publication; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.publication (id, name, type, vendor_id, messenger_id) FROM stdin;
301	Bandera	tabloid	2	201
302	Philippine Tatler	magazine	2	201
303	The Liason	gazette	2	201
304	The Buzz	showbiz	2	202
\.


--
-- Data for Name: sales; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sales (id, publication_id, copies_issued, date_issued, revenue, profit, copies_sold) FROM stdin;
501	301	1000000	2022-03-16	700000	500000	500000
502	302	6000	2022-03-17	9000	8000	600
503	302	10000	2022-03-17	20000	18000	6000
504	302	600	2022-03-18	4000	3000	400
505	303	1600	2022-03-17	14000	13000	1400
506	303	11600	2022-03-18	24000	23000	11400
507	304	400	2022-03-16	3000	2000	350
508	304	800	2022-03-01	7000	6000	750
509	301	11800	2022-03-19	10000	9000	11750
\.


--
-- Data for Name: subscription; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.subscription (id, customer_id, branch, price, qty, date_purchased) FROM stdin;
601	3	Little Baguio	55	1	2022-03-16
602	3	Cubao	56	1	2022-03-16
603	3	Trinoma	55.4	1	2022-03-16
604	3	Mandaluyong	78	10	2022-03-22
605	3	Pasig	10	90	2022-03-23
606	3	Makati	15	900	2022-03-23
607	3	Cubao	13	1000	2022-03-23
\.


--
-- Data for Name: vendor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vendor (id, rep_firstname, rep_lastname, rep_id, rep_date_employed, account_name, account_number, date_consigned, login_id) FROM stdin;
2	Owen Salvador	Estabillo	123456	2022-03-16	Manila Bulletin	MB-13456	1989-10-11	2
\.


--
-- Name: admin admin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (id);


--
-- Name: billing billing_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.billing
    ADD CONSTRAINT billing_pkey PRIMARY KEY (id);


--
-- Name: content content_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.content
    ADD CONSTRAINT content_pkey PRIMARY KEY (id);


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (id);


--
-- Name: login login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_pkey PRIMARY KEY (id);


--
-- Name: login login_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_username_key UNIQUE (username);


--
-- Name: messenger messenger_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messenger
    ADD CONSTRAINT messenger_pkey PRIMARY KEY (id);


--
-- Name: publication publication_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT publication_pkey PRIMARY KEY (id);


--
-- Name: subscription subscription_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subscription
    ADD CONSTRAINT subscription_pkey PRIMARY KEY (id);


--
-- Name: vendor vendor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vendor
    ADD CONSTRAINT vendor_pkey PRIMARY KEY (id);


--
-- Name: admin fk_admin_login; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT fk_admin_login FOREIGN KEY (login_id) REFERENCES public.login(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: billing fk_billing_admin1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.billing
    ADD CONSTRAINT fk_billing_admin1 FOREIGN KEY (admin_id) REFERENCES public.admin(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: billing fk_billing_vendor1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.billing
    ADD CONSTRAINT fk_billing_vendor1 FOREIGN KEY (vendor_id) REFERENCES public.vendor(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: content fk_content_publication1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.content
    ADD CONSTRAINT fk_content_publication1 FOREIGN KEY (publication_id) REFERENCES public.publication(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: customer fk_customer_login1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT fk_customer_login1 FOREIGN KEY (login_id) REFERENCES public.login(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: sales fk_issues_publication1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sales
    ADD CONSTRAINT fk_issues_publication1 FOREIGN KEY (publication_id) REFERENCES public.publication(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: messenger fk_messenger_vendor1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.messenger
    ADD CONSTRAINT fk_messenger_vendor1 FOREIGN KEY (vendor_id) REFERENCES public.vendor(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: publication fk_publication_messenger1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT fk_publication_messenger1 FOREIGN KEY (messenger_id) REFERENCES public.messenger(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: publication fk_publication_vendor1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT fk_publication_vendor1 FOREIGN KEY (vendor_id) REFERENCES public.vendor(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: subscription fk_subscription_customer1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subscription
    ADD CONSTRAINT fk_subscription_customer1 FOREIGN KEY (customer_id) REFERENCES public.customer(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: vendor fk_vendor_login1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vendor
    ADD CONSTRAINT fk_vendor_login1 FOREIGN KEY (login_id) REFERENCES public.login(id) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- PostgreSQL database dump complete
--

