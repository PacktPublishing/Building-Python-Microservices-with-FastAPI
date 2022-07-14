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
-- Name: auctions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auctions (
    id integer NOT NULL,
    name character varying(45) NOT NULL,
    type_id integer NOT NULL,
    details text NOT NULL,
    max_price double precision NOT NULL,
    min_price double precision NOT NULL,
    buyout_price double precision NOT NULL,
    created_date date NOT NULL,
    updated_date date NOT NULL,
    condition character varying(45) NOT NULL,
    profile_id integer NOT NULL
);


ALTER TABLE public.auctions OWNER TO postgres;

--
-- Name: bids; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bids (
    id integer NOT NULL,
    auction_id integer NOT NULL,
    profile_id integer NOT NULL,
    created_date date NOT NULL,
    updated_date date NOT NULL,
    price double precision NOT NULL
);


ALTER TABLE public.bids OWNER TO postgres;

--
-- Name: login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login (
    id integer NOT NULL,
    username character varying(45) NOT NULL,
    password character varying(45) NOT NULL,
    passphrase character varying(100) NOT NULL,
    approved_date date NOT NULL
);


ALTER TABLE public.login OWNER TO postgres;

--
-- Name: product_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.product_type (
    id integer NOT NULL,
    name character varying(45) NOT NULL,
    description character varying(100) NOT NULL
);


ALTER TABLE public.product_type OWNER TO postgres;

--
-- Name: profile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.profile (
    id integer NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    age integer NOT NULL,
    membership_date date NOT NULL,
    member_type character varying(45) NOT NULL,
    login_id integer NOT NULL,
    status integer NOT NULL
);


ALTER TABLE public.profile OWNER TO postgres;

--
-- Name: signup; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.signup (
    id integer NOT NULL,
    username character varying(45) NOT NULL,
    password character varying(45) NOT NULL
);


ALTER TABLE public.signup OWNER TO postgres;

--
-- Name: sold; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sold (
    id integer NOT NULL,
    bid_id integer NOT NULL,
    sold_date date NOT NULL,
    buyer integer NOT NULL
);


ALTER TABLE public.sold OWNER TO postgres;

--
-- Data for Name: auctions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auctions (id, name, type_id, details, max_price, min_price, buyout_price, created_date, updated_date, condition, profile_id) FROM stdin;
1	Diamond XXX	5	Expensive	500000	1000	500000	2022-02-16	2022-02-16	perfect	1
\.


--
-- Data for Name: bids; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bids (id, auction_id, profile_id, created_date, updated_date, price) FROM stdin;
100	1	1	2022-02-16	2022-02-16	400000
\.


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (id, username, password, passphrase, approved_date) FROM stdin;
1	sjctrags	sjctrags	$5$rounds=535000$rDtiI8SD1zxOnpny$SfcE/fxQejdAAnngCY7XdkOW9QYzBGdU/54VM6JrES8	2022-02-10
\.


--
-- Data for Name: product_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.product_type (id, name, description) FROM stdin;
1	jewelry	necklace
2	jewelry	earing
3	vehicle	Suzuki
4	vehicle	Honda
5	gem	Diamond
\.


--
-- Data for Name: profile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.profile (id, firstname, lastname, age, membership_date, member_type, login_id, status) FROM stdin;
1	Sherwin John	Tragura	43	2022-02-16	auctioner	1	1
\.


--
-- Data for Name: signup; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.signup (id, username, password) FROM stdin;
1	sjctrags	sjctrags
\.


--
-- Data for Name: sold; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sold (id, bid_id, sold_date, buyer) FROM stdin;
\.


--
-- Name: auctions auctions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auctions
    ADD CONSTRAINT auctions_pkey PRIMARY KEY (id);


--
-- Name: bids bids_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bids
    ADD CONSTRAINT bids_pkey PRIMARY KEY (id);


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
-- Name: product_type product_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.product_type
    ADD CONSTRAINT product_type_pkey PRIMARY KEY (id);


--
-- Name: profile profile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile
    ADD CONSTRAINT profile_pkey PRIMARY KEY (id);


--
-- Name: signup signup_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.signup
    ADD CONSTRAINT signup_pkey PRIMARY KEY (id);


--
-- Name: signup signup_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.signup
    ADD CONSTRAINT signup_username_key UNIQUE (username);


--
-- Name: sold sold_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sold
    ADD CONSTRAINT sold_pkey PRIMARY KEY (id);


--
-- Name: auctions fk_auctions_product_type1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auctions
    ADD CONSTRAINT fk_auctions_product_type1 FOREIGN KEY (type_id) REFERENCES public.product_type(id);


--
-- Name: auctions fk_auctions_profile1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auctions
    ADD CONSTRAINT fk_auctions_profile1 FOREIGN KEY (profile_id) REFERENCES public.profile(id);


--
-- Name: bids fk_bids_auctions1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bids
    ADD CONSTRAINT fk_bids_auctions1 FOREIGN KEY (auction_id) REFERENCES public.auctions(id);


--
-- Name: bids fk_bids_profile1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bids
    ADD CONSTRAINT fk_bids_profile1 FOREIGN KEY (profile_id) REFERENCES public.profile(id);


--
-- Name: sold fk_sold_bids1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sold
    ADD CONSTRAINT fk_sold_bids1 FOREIGN KEY (bid_id) REFERENCES public.bids(id);


--
-- Name: sold fk_sold_profile1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sold
    ADD CONSTRAINT fk_sold_profile1 FOREIGN KEY (buyer) REFERENCES public.profile(id);


--
-- Name: profile login_profile_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile
    ADD CONSTRAINT login_profile_fk FOREIGN KEY (login_id) REFERENCES public.login(id);


--
-- PostgreSQL database dump complete
--

