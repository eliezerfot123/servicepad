--
-- PostgreSQL database dump
--

-- Dumped from database version 13.7 (Ubuntu 13.7-0ubuntu0.21.10.1)
-- Dumped by pg_dump version 13.7 (Ubuntu 13.7-0ubuntu0.21.10.1)

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
-- Name: publication; Type: TABLE; Schema: public; Owner: eliox
--

CREATE TABLE public.publication (
    id integer NOT NULL,
    title character varying(50) NOT NULL,
    description text,
    priority character varying(50),
    status boolean,
    user_id integer,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.publication OWNER TO eliox;

--
-- Name: publication_id_seq; Type: SEQUENCE; Schema: public; Owner: eliox
--

CREATE SEQUENCE public.publication_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publication_id_seq OWNER TO eliox;

--
-- Name: publication_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: eliox
--

ALTER SEQUENCE public.publication_id_seq OWNED BY public.publication.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: eliox
--

CREATE TABLE public.users (
    id integer NOT NULL,
    public_id character varying(50),
    fullname character varying(50),
    email character varying(50),
    password character varying(200),
    images character varying(100)
);


ALTER TABLE public.users OWNER TO eliox;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: eliox
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO eliox;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: eliox
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: publication id; Type: DEFAULT; Schema: public; Owner: eliox
--

ALTER TABLE ONLY public.publication ALTER COLUMN id SET DEFAULT nextval('public.publication_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: eliox
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: publication; Type: TABLE DATA; Schema: public; Owner: eliox
--

COPY public.publication (id, title, description, priority, status, user_id, created_at, updated_at) FROM stdin;
1	La cima mas alta del mundo	Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum	High	t	1	2022-06-27 05:54:16.459781	\N
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: eliox
--

COPY public.users (id, public_id, fullname, email, password, images) FROM stdin;
1	c6c6614f-90d6-4ff2-bac5-abe8cb2140cf	Eliezer Romero	eliezerfot123@gmail.com	sha256$sP8e7vNPDBzLl0eF$3c05c6ddfa716ebffe1453e542be0eb0f5414bcb0b4cdaa796f005783694391d	
\.


--
-- Name: publication_id_seq; Type: SEQUENCE SET; Schema: public; Owner: eliox
--

SELECT pg_catalog.setval('public.publication_id_seq', 1, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: eliox
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: publication publication_pkey; Type: CONSTRAINT; Schema: public; Owner: eliox
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT publication_pkey PRIMARY KEY (id);


--
-- Name: publication publication_title_key; Type: CONSTRAINT; Schema: public; Owner: eliox
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT publication_title_key UNIQUE (title);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: eliox
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: eliox
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_public_id_key; Type: CONSTRAINT; Schema: public; Owner: eliox
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_public_id_key UNIQUE (public_id);


--
-- PostgreSQL database dump complete
--

