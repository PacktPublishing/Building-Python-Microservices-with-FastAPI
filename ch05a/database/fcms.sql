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

--
-- Name: attendance_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.attendance_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.attendance_seq OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: attendance_member; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attendance_member (
    id integer DEFAULT nextval('public.attendance_seq'::regclass) NOT NULL,
    member_id integer NOT NULL,
    timeout time without time zone NOT NULL,
    timein time without time zone NOT NULL,
    date_log date NOT NULL
);


ALTER TABLE public.attendance_member OWNER TO postgres;

--
-- Name: gym_class; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gym_class (
    id integer NOT NULL,
    name character varying(45) NOT NULL,
    trainer_id integer NOT NULL,
    member_id integer NOT NULL,
    approved integer NOT NULL
);


ALTER TABLE public.gym_class OWNER TO postgres;

--
-- Name: login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login (
    id integer NOT NULL,
    username character varying(45) NOT NULL,
    password character varying(45) NOT NULL,
    date_approved date NOT NULL,
    user_type integer NOT NULL
);


ALTER TABLE public.login OWNER TO postgres;

--
-- Name: profile_members; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.profile_members (
    id integer NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    age character varying(45) NOT NULL,
    height double precision NOT NULL,
    weight double precision NOT NULL,
    membership_type character varying(45) NOT NULL,
    trainer_id integer NOT NULL
);


ALTER TABLE public.profile_members OWNER TO postgres;

--
-- Name: profile_trainers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.profile_trainers (
    id integer NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    age integer NOT NULL,
    "position" character varying(45) NOT NULL,
    tenure double precision NOT NULL,
    shift integer NOT NULL
);


ALTER TABLE public.profile_trainers OWNER TO postgres;

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
-- Data for Name: attendance_member; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attendance_member (id, member_id, timeout, timein, date_log) FROM stdin;
\.


--
-- Data for Name: gym_class; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.gym_class (id, name, trainer_id, member_id, approved) FROM stdin;
\.


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (id, username, password, date_approved, user_type) FROM stdin;
\.


--
-- Data for Name: profile_members; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.profile_members (id, firstname, lastname, age, height, weight, membership_type, trainer_id) FROM stdin;
\.


--
-- Data for Name: profile_trainers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.profile_trainers (id, firstname, lastname, age, "position", tenure, shift) FROM stdin;
\.


--
-- Data for Name: signup; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.signup (id, username, password) FROM stdin;
\.


--
-- Name: attendance_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attendance_seq', 1, false);


--
-- Name: attendance_member attendance_member_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attendance_member
    ADD CONSTRAINT attendance_member_pkey PRIMARY KEY (id);


--
-- Name: gym_class gym_class_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gym_class
    ADD CONSTRAINT gym_class_pkey PRIMARY KEY (id);


--
-- Name: login login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_pkey PRIMARY KEY (id);


--
-- Name: profile_members profile_members_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile_members
    ADD CONSTRAINT profile_members_pkey PRIMARY KEY (id);


--
-- Name: profile_trainers profile_trainers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile_trainers
    ADD CONSTRAINT profile_trainers_pkey PRIMARY KEY (id);


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
-- Name: profile_members fk_login_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile_members
    ADD CONSTRAINT fk_login_id FOREIGN KEY (id) REFERENCES public.login(id);


--
-- Name: attendance_member fk_members_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attendance_member
    ADD CONSTRAINT fk_members_id FOREIGN KEY (member_id) REFERENCES public.profile_members(id);


--
-- Name: gym_class fk_members_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gym_class
    ADD CONSTRAINT fk_members_id FOREIGN KEY (member_id) REFERENCES public.profile_members(id);


--
-- Name: profile_trainers fk_trainers_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile_trainers
    ADD CONSTRAINT fk_trainers_id FOREIGN KEY (id) REFERENCES public.login(id);


--
-- Name: profile_members fk_trainers_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile_members
    ADD CONSTRAINT fk_trainers_id FOREIGN KEY (trainer_id) REFERENCES public.profile_trainers(id);


--
-- Name: gym_class fk_trainers_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.gym_class
    ADD CONSTRAINT fk_trainers_id FOREIGN KEY (trainer_id) REFERENCES public.profile_trainers(id);


--
-- PostgreSQL database dump complete
--

