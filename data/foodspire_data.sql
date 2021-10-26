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
-- Name: categories; Type: TABLE; Schema: public; Owner: asahipritchard
--

CREATE TABLE public.categories (
    category_id integer NOT NULL,
    category_name character varying(15) NOT NULL
);


ALTER TABLE public.categories OWNER TO asahipritchard;

--
-- Name: categories_category_id_seq; Type: SEQUENCE; Schema: public; Owner: asahipritchard
--

CREATE SEQUENCE public.categories_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_category_id_seq OWNER TO asahipritchard;

--
-- Name: categories_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asahipritchard
--

ALTER SEQUENCE public.categories_category_id_seq OWNED BY public.categories.category_id;


--
-- Name: fav_recipes; Type: TABLE; Schema: public; Owner: asahipritchard
--

CREATE TABLE public.fav_recipes (
    fav_id integer NOT NULL,
    user_id integer,
    recipe_id integer
);


ALTER TABLE public.fav_recipes OWNER TO asahipritchard;

--
-- Name: fav_recipes_fav_id_seq; Type: SEQUENCE; Schema: public; Owner: asahipritchard
--

CREATE SEQUENCE public.fav_recipes_fav_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fav_recipes_fav_id_seq OWNER TO asahipritchard;

--
-- Name: fav_recipes_fav_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asahipritchard
--

ALTER SEQUENCE public.fav_recipes_fav_id_seq OWNED BY public.fav_recipes.fav_id;


--
-- Name: recipe_categories; Type: TABLE; Schema: public; Owner: asahipritchard
--

CREATE TABLE public.recipe_categories (
    recipe_category_id integer NOT NULL,
    recipe_id integer,
    category_id integer
);


ALTER TABLE public.recipe_categories OWNER TO asahipritchard;

--
-- Name: recipe_categories_recipe_category_id_seq; Type: SEQUENCE; Schema: public; Owner: asahipritchard
--

CREATE SEQUENCE public.recipe_categories_recipe_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipe_categories_recipe_category_id_seq OWNER TO asahipritchard;

--
-- Name: recipe_categories_recipe_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asahipritchard
--

ALTER SEQUENCE public.recipe_categories_recipe_category_id_seq OWNED BY public.recipe_categories.recipe_category_id;


--
-- Name: recipes; Type: TABLE; Schema: public; Owner: asahipritchard
--

CREATE TABLE public.recipes (
    recipe_id integer NOT NULL,
    directions character varying NOT NULL,
    fat integer,
    calories integer,
    description character varying,
    protein integer,
    rating double precision,
    recipe_title character varying NOT NULL,
    ingredients_list character varying NOT NULL,
    sodium integer
);


ALTER TABLE public.recipes OWNER TO asahipritchard;

--
-- Name: recipes_recipe_id_seq; Type: SEQUENCE; Schema: public; Owner: asahipritchard
--

CREATE SEQUENCE public.recipes_recipe_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipes_recipe_id_seq OWNER TO asahipritchard;

--
-- Name: recipes_recipe_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asahipritchard
--

ALTER SEQUENCE public.recipes_recipe_id_seq OWNED BY public.recipes.recipe_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: asahipritchard
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    fname character varying(20) NOT NULL,
    lname character varying(20) NOT NULL,
    username character varying(15) NOT NULL,
    email character varying(30) NOT NULL,
    passwordd character varying(20) NOT NULL
);


ALTER TABLE public.users OWNER TO asahipritchard;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: asahipritchard
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO asahipritchard;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: asahipritchard
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: categories category_id; Type: DEFAULT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.categories ALTER COLUMN category_id SET DEFAULT nextval('public.categories_category_id_seq'::regclass);


--
-- Name: fav_recipes fav_id; Type: DEFAULT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.fav_recipes ALTER COLUMN fav_id SET DEFAULT nextval('public.fav_recipes_fav_id_seq'::regclass);


--
-- Name: recipe_categories recipe_category_id; Type: DEFAULT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.recipe_categories ALTER COLUMN recipe_category_id SET DEFAULT nextval('public.recipe_categories_recipe_category_id_seq'::regclass);


--
-- Name: recipes recipe_id; Type: DEFAULT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.recipes ALTER COLUMN recipe_id SET DEFAULT nextval('public.recipes_recipe_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: asahipritchard
--

COPY public.categories (category_id, category_name) FROM stdin;
\.


--
-- Data for Name: fav_recipes; Type: TABLE DATA; Schema: public; Owner: asahipritchard
--

COPY public.fav_recipes (fav_id, user_id, recipe_id) FROM stdin;
\.


--
-- Data for Name: recipe_categories; Type: TABLE DATA; Schema: public; Owner: asahipritchard
--

COPY public.recipe_categories (recipe_category_id, recipe_id, category_id) FROM stdin;
\.


--
-- Data for Name: recipes; Type: TABLE DATA; Schema: public; Owner: asahipritchard
--

COPY public.recipes (recipe_id, directions, fat, calories, description, protein, rating, recipe_title, ingredients_list, sodium) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: asahipritchard
--

COPY public.users (user_id, fname, lname, username, email, passwordd) FROM stdin;
1	Bob	Smith	BobtheBanshee	bob.s@yahoo.com	eatpizza99
2	Terry	Cruz	TakeaCruz	Cruzing@aol.com	flowerssmellnice
3	Ami	Kinjo	Okinawa<3	kinjo.a@hotmail.com	kikiDoggy
5	Mona	Bones	ballqueen	ball4lyfe@gmail.com	givemetreats223
6	Mimi	Kat	iamacat	Meow@yahoo.com	mewomewomewo
7	Michael	Henderson	ElectricBuzzz	henderson@aol.com	ilivehere1212
8	Bunt	Cake	CAAAKE	iamsweet@gmail.com	sugarforme123
9	Asahi	Pants	Pants!	asahip@aol.com	iamme230
\.


--
-- Name: categories_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asahipritchard
--

SELECT pg_catalog.setval('public.categories_category_id_seq', 1, false);


--
-- Name: fav_recipes_fav_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asahipritchard
--

SELECT pg_catalog.setval('public.fav_recipes_fav_id_seq', 1, false);


--
-- Name: recipe_categories_recipe_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asahipritchard
--

SELECT pg_catalog.setval('public.recipe_categories_recipe_category_id_seq', 1, false);


--
-- Name: recipes_recipe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asahipritchard
--

SELECT pg_catalog.setval('public.recipes_recipe_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: asahipritchard
--

SELECT pg_catalog.setval('public.users_user_id_seq', 9, true);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);


--
-- Name: fav_recipes fav_recipes_pkey; Type: CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.fav_recipes
    ADD CONSTRAINT fav_recipes_pkey PRIMARY KEY (fav_id);


--
-- Name: recipe_categories recipe_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.recipe_categories
    ADD CONSTRAINT recipe_categories_pkey PRIMARY KEY (recipe_category_id);


--
-- Name: recipes recipes_pkey; Type: CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_pkey PRIMARY KEY (recipe_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: fav_recipes fav_recipes_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.fav_recipes
    ADD CONSTRAINT fav_recipes_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(recipe_id);


--
-- Name: fav_recipes fav_recipes_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.fav_recipes
    ADD CONSTRAINT fav_recipes_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: recipe_categories recipe_categories_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.recipe_categories
    ADD CONSTRAINT recipe_categories_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(category_id);


--
-- Name: recipe_categories recipe_categories_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: asahipritchard
--

ALTER TABLE ONLY public.recipe_categories
    ADD CONSTRAINT recipe_categories_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(recipe_id);


--
-- PostgreSQL database dump complete
--

