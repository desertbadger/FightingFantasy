drop table if exists entries;
create table enemies (
  id integer primary key autoincrement,
  name int not null,
  skill int not null,
  stamina int not null
);