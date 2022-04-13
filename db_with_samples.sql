--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2 (Debian 14.2-1.pgdg110+1)
-- Dumped by pg_dump version 14.2

-- Started on 2022-04-10 14:09:44

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
-- TOC entry 3374 (class 1262 OID 32769)
-- Name: tasklistwsb; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE tasklistwsb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE tasklistwsb OWNER TO postgres;

\connect tasklistwsb

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
-- TOC entry 5 (class 2615 OID 32770)
-- Name: tasks; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA tasks;


ALTER SCHEMA tasks OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 32790)
-- Name: assignee; Type: TABLE; Schema: tasks; Owner: postgres
--

CREATE TABLE tasks.assignee (
    id integer NOT NULL,
    email text NOT NULL,
    password text NOT NULL,
    isadmin boolean NOT NULL
);


ALTER TABLE tasks.assignee OWNER TO postgres;

--
-- TOC entry 3375 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN assignee.id; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.assignee.id IS 'ID of user';


--
-- TOC entry 3376 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN assignee.email; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.assignee.email IS 'Email of user';


--
-- TOC entry 3377 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN assignee.password; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.assignee.password IS 'Password of user';


--
-- TOC entry 3378 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN assignee.isadmin; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.assignee.isadmin IS 'Tells if user is administrator';


--
-- TOC entry 215 (class 1259 OID 32789)
-- Name: assignee_id_seq; Type: SEQUENCE; Schema: tasks; Owner: postgres
--

CREATE SEQUENCE tasks.assignee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tasks.assignee_id_seq OWNER TO postgres;

--
-- TOC entry 3379 (class 0 OID 0)
-- Dependencies: 215
-- Name: assignee_id_seq; Type: SEQUENCE OWNED BY; Schema: tasks; Owner: postgres
--

ALTER SEQUENCE tasks.assignee_id_seq OWNED BY tasks.assignee.id;


--
-- TOC entry 214 (class 1259 OID 32781)
-- Name: description; Type: TABLE; Schema: tasks; Owner: postgres
--

CREATE TABLE tasks.description (
    id integer NOT NULL,
    description text
);


ALTER TABLE tasks.description OWNER TO postgres;

--
-- TOC entry 3380 (class 0 OID 0)
-- Dependencies: 214
-- Name: COLUMN description.id; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.description.id IS 'ID of description';


--
-- TOC entry 3381 (class 0 OID 0)
-- Dependencies: 214
-- Name: COLUMN description.description; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.description.description IS 'Text of description';


--
-- TOC entry 213 (class 1259 OID 32780)
-- Name: description_id_seq; Type: SEQUENCE; Schema: tasks; Owner: postgres
--

CREATE SEQUENCE tasks.description_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tasks.description_id_seq OWNER TO postgres;

--
-- TOC entry 3382 (class 0 OID 0)
-- Dependencies: 213
-- Name: description_id_seq; Type: SEQUENCE OWNED BY; Schema: tasks; Owner: postgres
--

ALTER SEQUENCE tasks.description_id_seq OWNED BY tasks.description.id;


--
-- TOC entry 212 (class 1259 OID 32772)
-- Name: task; Type: TABLE; Schema: tasks; Owner: postgres
--

CREATE TABLE tasks.task (
    id integer NOT NULL,
    title text NOT NULL,
    priority integer NOT NULL,
    assigneid integer NOT NULL,
    descriptionid integer NOT NULL,
    status text NOT NULL
);


ALTER TABLE tasks.task OWNER TO postgres;

--
-- TOC entry 3383 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN task.id; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.task.id IS 'ID of task';


--
-- TOC entry 3384 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN task.title; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.task.title IS 'Title of task';


--
-- TOC entry 3385 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN task.priority; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.task.priority IS 'Priority of task';


--
-- TOC entry 3386 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN task.assigneid; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.task.assigneid IS 'ID of assignee responsible for task';


--
-- TOC entry 3387 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN task.descriptionid; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.task.descriptionid IS 'ID of description in task';


--
-- TOC entry 3388 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN task.status; Type: COMMENT; Schema: tasks; Owner: postgres
--

COMMENT ON COLUMN tasks.task.status IS 'status of task';


--
-- TOC entry 211 (class 1259 OID 32771)
-- Name: task_id_seq; Type: SEQUENCE; Schema: tasks; Owner: postgres
--

CREATE SEQUENCE tasks.task_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tasks.task_id_seq OWNER TO postgres;

--
-- TOC entry 3389 (class 0 OID 0)
-- Dependencies: 211
-- Name: task_id_seq; Type: SEQUENCE OWNED BY; Schema: tasks; Owner: postgres
--

ALTER SEQUENCE tasks.task_id_seq OWNED BY tasks.task.id;


--
-- TOC entry 3217 (class 2604 OID 32793)
-- Name: assignee id; Type: DEFAULT; Schema: tasks; Owner: postgres
--

ALTER TABLE ONLY tasks.assignee ALTER COLUMN id SET DEFAULT nextval('tasks.assignee_id_seq'::regclass);


--
-- TOC entry 3216 (class 2604 OID 32784)
-- Name: description id; Type: DEFAULT; Schema: tasks; Owner: postgres
--

ALTER TABLE ONLY tasks.description ALTER COLUMN id SET DEFAULT nextval('tasks.description_id_seq'::regclass);


--
-- TOC entry 3215 (class 2604 OID 32775)
-- Name: task id; Type: DEFAULT; Schema: tasks; Owner: postgres
--

ALTER TABLE ONLY tasks.task ALTER COLUMN id SET DEFAULT nextval('tasks.task_id_seq'::regclass);


--
-- TOC entry 3368 (class 0 OID 32790)
-- Dependencies: 216
-- Data for Name: assignee; Type: TABLE DATA; Schema: tasks; Owner: postgres
--

COPY tasks.assignee (id, email, password, isadmin) FROM stdin;
2	admin@email.com	$2a$06$UFr5/wenwj3X9x8lOoCwtuBDOpy8tIYWZ1/4vQsPu2EFHbM5JEUmS	t
3	user@email.com	$2a$06$zHjHN8TtFLqQebTp8nU3HeQKeu0NHcXLfsk3iROI.T6bAOdZs./GW	t
\.


--
-- TOC entry 3366 (class 0 OID 32781)
-- Dependencies: 214
-- Data for Name: description; Type: TABLE DATA; Schema: tasks; Owner: postgres
--

COPY tasks.description (id, description) FROM stdin;
1	Some task description blablalblab
\.


--
-- TOC entry 3364 (class 0 OID 32772)
-- Dependencies: 212
-- Data for Name: task; Type: TABLE DATA; Schema: tasks; Owner: postgres
--

COPY tasks.task (id, title, priority, assigneid, descriptionid, status) FROM stdin;
1	Task title by user	1	3	1	In progress
2	Task title by admin	1	2	1	In progress
\.


--
-- TOC entry 3390 (class 0 OID 0)
-- Dependencies: 215
-- Name: assignee_id_seq; Type: SEQUENCE SET; Schema: tasks; Owner: postgres
--

SELECT pg_catalog.setval('tasks.assignee_id_seq', 3, true);


--
-- TOC entry 3391 (class 0 OID 0)
-- Dependencies: 213
-- Name: description_id_seq; Type: SEQUENCE SET; Schema: tasks; Owner: postgres
--

SELECT pg_catalog.setval('tasks.description_id_seq', 1, true);


--
-- TOC entry 3392 (class 0 OID 0)
-- Dependencies: 211
-- Name: task_id_seq; Type: SEQUENCE SET; Schema: tasks; Owner: postgres
--

SELECT pg_catalog.setval('tasks.task_id_seq', 2, true);


--
-- TOC entry 3223 (class 2606 OID 32797)
-- Name: assignee assignee_pkey; Type: CONSTRAINT; Schema: tasks; Owner: postgres
--

ALTER TABLE ONLY tasks.assignee
    ADD CONSTRAINT assignee_pkey PRIMARY KEY (id);


--
-- TOC entry 3221 (class 2606 OID 32788)
-- Name: description description_pkey; Type: CONSTRAINT; Schema: tasks; Owner: postgres
--

ALTER TABLE ONLY tasks.description
    ADD CONSTRAINT description_pkey PRIMARY KEY (id);


--
-- TOC entry 3219 (class 2606 OID 32779)
-- Name: task task_pkey; Type: CONSTRAINT; Schema: tasks; Owner: postgres
--

ALTER TABLE ONLY tasks.task
    ADD CONSTRAINT task_pkey PRIMARY KEY (id);


-- Completed on 2022-04-10 14:09:44

--
-- PostgreSQL database dump complete
--

