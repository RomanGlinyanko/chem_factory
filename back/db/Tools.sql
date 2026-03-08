-- 1. создаем пользователя с паролем
create User chem_fact 
with encrypted password 'RX777ngS';

-- 2. создаем базу данных и назначаем 
-- владельцем нашего пользователя
create Database chem_fact
owner chem_fact encoding = 'UTF8';

-- 3. подключаемся к новой базе данных (в psql: \c my_database)
-- после подключения создаем схему
--\c my_database

-- 4. создаем схему и назначаем владельца
create Schema if not exists chem_fact 
authorization chem_fact;

-- 5. (опционально) даем пользователю все права на схему, если он не владелец
grant all Privileges on schema 
chem_fact to chem_fact;

-- 6. (опционально) права на создание таблиц 
-- в будущем в этой схеме
alter default privileges in schema 
chem_fact grant all on tables to chem_fact;