PGDMP                         {           db_lifecellbot #   14.8 (Ubuntu 14.8-0ubuntu0.22.04.1) #   14.8 (Ubuntu 14.8-0ubuntu0.22.04.1)                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    17031    db_lifecellbot    DATABASE     c   CREATE DATABASE db_lifecellbot WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'uk_UA.UTF-8';
    DROP DATABASE db_lifecellbot;
                postgres    false            �            1259    17032    data_tariffs    TABLE     �   CREATE TABLE public.data_tariffs (
    id uuid NOT NULL,
    username character varying NOT NULL,
    tariff_id integer NOT NULL
);
     DROP TABLE public.data_tariffs;
       public         heap    postgres    false                      0    17032    data_tariffs 
   TABLE DATA           ?   COPY public.data_tariffs (id, username, tariff_id) FROM stdin;
    public          postgres    false    209   t             x������ � �     