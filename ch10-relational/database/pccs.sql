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
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: answers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.answers (
    id integer NOT NULL,
    respondent_id integer,
    question_id integer,
    answer_choice integer DEFAULT 0 NOT NULL,
    answer_text text DEFAULT ''::text NOT NULL
);


ALTER TABLE public.answers OWNER TO postgres;

--
-- Name: answers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.answers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.answers_id_seq OWNER TO postgres;

--
-- Name: answers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.answers_id_seq OWNED BY public.answers.id;


--
-- Name: choices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.choices (
    id integer NOT NULL,
    question_id integer,
    choice character varying(255) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.choices OWNER TO postgres;

--
-- Name: choices_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.choices_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.choices_id_seq OWNER TO postgres;

--
-- Name: choices_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.choices_id_seq OWNED BY public.choices.id;


--
-- Name: education; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.education (
    id integer NOT NULL,
    name character varying(255) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.education OWNER TO postgres;

--
-- Name: education_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.education_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.education_id_seq OWNER TO postgres;

--
-- Name: education_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.education_id_seq OWNED BY public.education.id;


--
-- Name: location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.location (
    id integer NOT NULL,
    city character varying(255) DEFAULT ''::character varying NOT NULL,
    state character varying(255) DEFAULT ''::character varying NOT NULL,
    country character varying(255) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.location OWNER TO postgres;

--
-- Name: location_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.location_id_seq OWNER TO postgres;

--
-- Name: location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.location_id_seq OWNED BY public.location.id;


--
-- Name: login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login (
    id integer NOT NULL,
    username character varying(255) DEFAULT ''::character varying NOT NULL,
    password character varying(255) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.login OWNER TO postgres;

--
-- Name: login_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.login_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.login_id_seq OWNER TO postgres;

--
-- Name: login_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.login_id_seq OWNED BY public.login.id;


--
-- Name: migration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.migration (
    id integer NOT NULL,
    name character varying(200) DEFAULT ''::character varying NOT NULL,
    app_name character varying(200) DEFAULT ''::character varying NOT NULL,
    ran_on timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.migration OWNER TO postgres;

--
-- Name: migration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.migration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.migration_id_seq OWNER TO postgres;

--
-- Name: migration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.migration_id_seq OWNED BY public.migration.id;


--
-- Name: occupation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.occupation (
    id integer NOT NULL,
    name character varying(255) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.occupation OWNER TO postgres;

--
-- Name: occupation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.occupation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.occupation_id_seq OWNER TO postgres;

--
-- Name: occupation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.occupation_id_seq OWNED BY public.occupation.id;


--
-- Name: profile; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.profile (
    id integer NOT NULL,
    fname character varying(255) DEFAULT ''::character varying NOT NULL,
    lname character varying(255) DEFAULT ''::character varying NOT NULL,
    age integer DEFAULT 0 NOT NULL,
    "position" character varying(255) DEFAULT ''::character varying NOT NULL,
    login_id integer,
    official_id integer DEFAULT 0 NOT NULL,
    date_employed date DEFAULT CURRENT_DATE NOT NULL
);


ALTER TABLE public.profile OWNER TO postgres;

--
-- Name: profile_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.profile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.profile_id_seq OWNER TO postgres;

--
-- Name: profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.profile_id_seq OWNED BY public.profile.id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.question (
    id integer NOT NULL,
    statement text DEFAULT ''::text NOT NULL,
    type integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.question OWNER TO postgres;

--
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_id_seq OWNER TO postgres;

--
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.question_id_seq OWNED BY public.question.id;


--
-- Name: respondent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.respondent (
    id integer NOT NULL,
    fname character varying(255) DEFAULT ''::character varying NOT NULL,
    lname character varying(255) DEFAULT ''::character varying NOT NULL,
    age integer DEFAULT 0 NOT NULL,
    birthday date DEFAULT CURRENT_DATE NOT NULL,
    occupation_id integer,
    occupation_years integer DEFAULT 0 NOT NULL,
    salary_estimate double precision DEFAULT 0.0 NOT NULL,
    company character varying(255) DEFAULT ''::character varying NOT NULL,
    address character varying(255) DEFAULT ''::character varying NOT NULL,
    location_id integer,
    education_id integer,
    school character varying(255) DEFAULT ''::character varying NOT NULL,
    marital boolean DEFAULT false NOT NULL,
    count_kids integer DEFAULT 0 NOT NULL,
    gender character varying(1) DEFAULT ''::character varying NOT NULL
);


ALTER TABLE public.respondent OWNER TO postgres;

--
-- Name: respondent_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.respondent_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.respondent_id_seq OWNER TO postgres;

--
-- Name: respondent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.respondent_id_seq OWNED BY public.respondent.id;


--
-- Name: answers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.answers ALTER COLUMN id SET DEFAULT nextval('public.answers_id_seq'::regclass);


--
-- Name: choices id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choices ALTER COLUMN id SET DEFAULT nextval('public.choices_id_seq'::regclass);


--
-- Name: education id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.education ALTER COLUMN id SET DEFAULT nextval('public.education_id_seq'::regclass);


--
-- Name: location id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.location ALTER COLUMN id SET DEFAULT nextval('public.location_id_seq'::regclass);


--
-- Name: login id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login ALTER COLUMN id SET DEFAULT nextval('public.login_id_seq'::regclass);


--
-- Name: migration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.migration ALTER COLUMN id SET DEFAULT nextval('public.migration_id_seq'::regclass);


--
-- Name: occupation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.occupation ALTER COLUMN id SET DEFAULT nextval('public.occupation_id_seq'::regclass);


--
-- Name: profile id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile ALTER COLUMN id SET DEFAULT nextval('public.profile_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_id_seq'::regclass);


--
-- Name: respondent id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.respondent ALTER COLUMN id SET DEFAULT nextval('public.respondent_id_seq'::regclass);


--
-- Data for Name: answers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.answers (id, respondent_id, question_id, answer_choice, answer_text) FROM stdin;
1	3	1	5	NA
2	3	2	6	NA
4	3	4	14	NA
5	3	5	17	NA
7	3	6	19	NA
8	3	7	21	NA
9	3	8	22	NA
10	3	9	25	NA
11	3	10	29	NA
12	3	11	31	NA
13	3	12	34	NA
14	3	13	38	NA
24	4	9	26	NA
25	4	10	28	NA
26	4	11	31	NA
27	4	12	35	NA
28	4	13	37	NA
29	4	14	0	2
30	4	15	0	3
31	5	1	3	NA
32	5	2	8	NA
33	5	3	11	NA
34	5	4	14	NA
35	5	5	16	NA
36	5	6	19	NA
37	5	7	20	NA
38	5	8	22	NA
39	5	9	26	NA
43	5	10	28	NA
44	5	11	32	NA
45	5	12	36	NA
46	5	13	37	NA
47	5	14	0	3
48	5	15	0	1
49	6	1	4	NA
50	6	2	8	NA
51	6	3	11	NA
53	6	5	16	NA
54	6	6	19	NA
55	6	7	20	NA
56	6	8	22	NA
57	6	9	26	NA
59	6	11	32	NA
60	6	12	35	NA
61	6	13	37	NA
63	6	15	0	1
64	7	1	1	string
65	7	2	8	string
66	7	3	10	string
67	7	4	13	string
68	7	5	17	string
69	7	6	19	string
70	7	7	21	string
71	7	9	25	string
72	7	10	29	string
73	7	11	30	string
74	7	12	34	string
75	7	13	38	string
76	7	14	0	4
77	7	15	0	3
90	8	14	0	1
91	8	15	0	3
78	8	1	2	NA
79	8	2	7	NA
80	8	3	11	NA
81	8	4	14	NA
82	8	5	17	NA
83	8	6	19	NA
84	8	7	21	NA
85	8	8	22	NA
86	8	9	25	NA
87	8	10	28	NA
88	8	11	32	NA
89	8	13	38	NA
124	11	2	8	NA
125	11	3	11	NA
17	4	1	1	NA
3	3	3	11	NA
19	4	3	11	NA
20	4	4	14	NA
58	6	10	28	NA
22	4	6	19	NA
23	4	8	22	NA
126	11	4	14	NA
92	9	1	1	NA
93	9	2	8	NA
94	9	3	11	NA
95	9	4	14	NA
96	9	5	16	NA
97	9	6	19	NA
98	9	7	20	NA
99	9	8	22	NA
101	9	9	27	NA
102	9	10	28	NA
103	9	11	33	NA
104	9	12	36	NA
105	9	13	37	NA
106	9	14	37	0
107	9	15	37	3
62	6	14	0	0
15	3	14	0	0
16	3	15	0	0
108	10	1	3	NA
109	10	2	8	NA
110	10	3	9	NA
111	10	4	12	NA
112	10	5	17	NA
113	10	6	18	NA
114	10	7	21	NA
115	10	8	23	NA
116	10	9	25	NA
117	10	10	29	NA
118	10	11	30	NA
119	10	12	34	NA
120	10	13	38	NA
121	10	14	0	3
122	10	15	0	3
123	11	1	3	NA
127	11	5	16	NA
128	11	6	19	NA
129	11	7	20	NA
130	11	8	22	NA
131	11	9	27	NA
132	11	10	28	NA
133	11	11	31	NA
134	11	12	35	NA
135	11	13	37	NA
136	11	14	0	2
137	11	15	0	0
138	12	1	2	NA
139	12	2	8	NA
140	12	3	11	NA
141	12	4	15	NA
142	12	5	16	NA
143	12	6	19	NA
144	12	7	20	NA
145	12	8	22	NA
146	12	9	27	NA
147	12	10	28	NA
148	12	11	31	NA
149	12	12	35	NA
150	12	13	37	NA
151	12	14	0	1
152	12	15	0	2
18	4	2	7	NA
52	6	4	13	NA
21	4	4	15	NA
\.


--
-- Data for Name: choices; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.choices (id, question_id, choice) FROM stdin;
1	1	Four or more
2	1	Three
3	1	Two
4	1	One
5	1	None
6	2	No
7	2	No one in the age range
8	2	Yes
9	3	Tile, palm leaves, straw, or leaves
10	3	Tin, asbestos (Eternit), or others
11	3	Reinforced concrete/flagstone/concrete
12	4	None, latrine, flush toilet, and pit. Flush toilet and septic tank not inside the residence.
13	4	Flush toilet to the sewer system. Not inside the residence.
14	4	Flush toilet and septic tank. Inside the residence.
15	4	Flush toilet to the sewer system. Inside the residence.
16	5	Yes
17	5	No
18	6	Firewood/charcoal or others
19	6	Gas, electricity, or one cooks
20	7	Yes
21	7	No
22	8	Yes
23	8	No
24	9	None
25	9	One
26	9	Two
27	9	Three or more
28	10	Yes
29	10	No
30	11	One
31	11	Two
32	11	Three
33	11	Four or more
34	12	One
35	12	Two
36	12	Three or more
37	13	Yes
38	13	No
\.


--
-- Data for Name: education; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.education (id, name) FROM stdin;
1	None
2	Elementary
3	Secondary
4	Senior High
5	Diploma
6	Bachellor (College)
7	Masters
8	Doctorate
\.


--
-- Data for Name: location; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.location (id, city, state, country) FROM stdin;
1	Pasig	Manila	PH
2	Cebu	Cebu	PH
3	Batangas	Batangas	PH
4	Cavite	Cavite	PH
5	Bacolod	Negros Occidental	PH
6	Dumaguete	Negros Oriental	PH
7	Iloilo	Iloilo	PH
8	Kalibo	Aklan	PH
9	Quezon	Manila	PH
10	Ormoc	Leyte	PH
11	Puerto Princesa	Palawan	PH
12	Manila	Manila	PH
13	Tacloban	Leyte	PH
14	Mandaue	Cebu	PH
15	Makati	Manila	PH
16	Calamba	Laguna	PH
\.


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (id, username, password) FROM stdin;
1	admin	admin
2	sjctrags	sjctrags
3	roldan	roldan
4	rhonalyn	rhonalyn
\.


--
-- Data for Name: migration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.migration (id, name, app_name, ran_on) FROM stdin;
1	2022-06-09T18:08:51:592478	survey	2022-06-09 18:09:03.451473
2	2022-06-09T19:26:00:511909	survey	2022-06-09 19:26:07.463951
\.


--
-- Data for Name: occupation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.occupation (id, name) FROM stdin;
1	unemployed
2	janitor
3	clerk
4	information officer
5	janitorial jobs
6	manager
7	engineer
8	teacher
9	professor
10	scientist
11	business-related
12	business owner
\.


--
-- Data for Name: profile; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.profile (id, fname, lname, age, "position", login_id, official_id, date_employed) FROM stdin;
1	Joanna	Cruz	40	administrator	1	897654	2020-06-09
2	Sherwin John	Tragura	42	survey manager	2	111567	2019-04-11
3	Roldan	Egot	31	survey leader	3	54623	2019-05-10
4	Rhonalyn	Estrelles	35	survey leader	4	12322	2019-11-09
\.


--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.question (id, statement, type) FROM stdin;
1	How many household members are 16-years-old or lower?	1
2	Do all household members ages 5 to 16 attend school?	1
3	What is the main material of the roof of the residence?	1
4	What type of toilet arrangement does the household have?	1
5	Does the household has a shower?	2
6	What fuel does the household use for cooking?	1
7	Does the household have a car?	2
8	Does the household have a refrigerator?	2
9	How many color televisions does the household have?	1
10	Does the household have a blender?	2
11	How many rooms do the household use? (Excluding kitchen, bathroom, hallway, garage, or business-use	1
12	How many irons does the household owns?	1
13	Does the household owns lounge or sofa?	2
14	How many boys are not in school	0
15	How many girls are not in school	0
\.


--
-- Data for Name: respondent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.respondent (id, fname, lname, age, birthday, occupation_id, occupation_years, salary_estimate, company, address, location_id, education_id, school, marital, count_kids, gender) FROM stdin;
3	Juan	Luna	32	1990-11-10	3	10	10000	Anzons Plaza	Tondo	12	4	PUP	f	0	M
4	Zeta	Ngo	30	1992-09-01	6	20	40000	LNHS	113 Real St.	13	6	Eastern Visayas State College	t	5	F
5	Jim	Chu	40	1982-05-11	6	13	60000	HSBC	Bangkal St.	15	6	UP Diliman	t	4	M
6	Larry	Santos	33	1991-03-22	8	16	55000	Makati Science High School	6754 Poblacion	15	7	TIP	f	1	M
7	Gene	Chua	23	1999-06-20	5	7	9600	Makati Science High School	Sampaloc	12	3	Soro-Soro High School	t	7	F
8	Larson	Alcala	55	1969-02-10	4	30	22600	NAPOLCOM	Pandacan	12	4	Pandacan Colleges	t	4	M
9	Stella	Marquez	45	1977-07-05	9	32	82600	DOST	123 Pioneer St	1	7	Up Diliman	t	3	F
10	John	Cruz	39	1983-10-15	5	23	8600	Zeus Merchandize	Soro Soro Ilaya	3	3	Mababang Paaralan ng Tibag	f	6	M
11	Liza	Muring	38	1984-08-28	11	26	33000	Alipay Bistro	178 Vietnam Village	11	6	Palawan College	t	2	F
12	Samuel	Relli	34	1988-04-27	10	11	89000	The Survey Inc	Little Baguio	9	8	UPLB	t	3	M
\.


--
-- Name: answers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.answers_id_seq', 152, true);


--
-- Name: choices_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.choices_id_seq', 38, true);


--
-- Name: education_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.education_id_seq', 8, true);


--
-- Name: location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.location_id_seq', 16, true);


--
-- Name: login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.login_id_seq', 4, true);


--
-- Name: migration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.migration_id_seq', 2, true);


--
-- Name: occupation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.occupation_id_seq', 12, true);


--
-- Name: profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.profile_id_seq', 4, true);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.question_id_seq', 15, true);


--
-- Name: respondent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.respondent_id_seq', 12, true);


--
-- Name: answers answers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.answers
    ADD CONSTRAINT answers_pkey PRIMARY KEY (id);


--
-- Name: choices choices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choices
    ADD CONSTRAINT choices_pkey PRIMARY KEY (id);


--
-- Name: education education_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.education
    ADD CONSTRAINT education_pkey PRIMARY KEY (id);


--
-- Name: location location_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (id);


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
-- Name: migration migration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.migration
    ADD CONSTRAINT migration_pkey PRIMARY KEY (id);


--
-- Name: occupation occupation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.occupation
    ADD CONSTRAINT occupation_pkey PRIMARY KEY (id);


--
-- Name: profile profile_login_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile
    ADD CONSTRAINT profile_login_id_key UNIQUE (login_id);


--
-- Name: profile profile_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile
    ADD CONSTRAINT profile_pkey PRIMARY KEY (id);


--
-- Name: question question_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_pkey PRIMARY KEY (id);


--
-- Name: respondent respondent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.respondent
    ADD CONSTRAINT respondent_pkey PRIMARY KEY (id);


--
-- Name: answers answers_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.answers
    ADD CONSTRAINT answers_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.question(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: answers answers_respondent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.answers
    ADD CONSTRAINT answers_respondent_id_fkey FOREIGN KEY (respondent_id) REFERENCES public.respondent(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: choices choices_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.choices
    ADD CONSTRAINT choices_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.question(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: profile profile_login_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profile
    ADD CONSTRAINT profile_login_id_fkey FOREIGN KEY (login_id) REFERENCES public.login(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: respondent respondent_education_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.respondent
    ADD CONSTRAINT respondent_education_id_fkey FOREIGN KEY (education_id) REFERENCES public.education(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: respondent respondent_location_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.respondent
    ADD CONSTRAINT respondent_location_id_fkey FOREIGN KEY (location_id) REFERENCES public.location(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: respondent respondent_occupation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.respondent
    ADD CONSTRAINT respondent_occupation_id_fkey FOREIGN KEY (occupation_id) REFERENCES public.occupation(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

