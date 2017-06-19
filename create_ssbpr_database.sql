drop table if exists tournament_set;
drop table if exists tournament;
drop table if exists venue;
drop table if exists tournament_character;
drop table if exists doubles_set;
drop table if exists team;
drop table if exists player;

create table player (
	player_id INTEGER,
	tag varchar(12), 
	city varchar(15), 
	wins SMALLINT, 
	losses SMALLINT,
	points INTEGER, 
	primary key (player_id),
    unique key(tag)
);
create table venue (
	vname varchar(30),
	city char(15),
	primary key (vname)
);
create table tournament (
	tournament_id varchar(6),
	tname varchar(30),
	vname varchar(30),
	tdate DATE,
	entrants SMALLINT,
	primary key(tournament_id),
	foreign key(vname) references venue(vname) on delete cascade on update cascade
);

create table tournament_character (
	cname varchar(16),
	ranking SMALLINT,
	primary key (cname)
);

create table tournament_set (
	set_id varchar(14),
	tournament_id varchar(6),
	p1_tag varchar(12),
	p2_tag varchar(12),
	p1_score SMALLINT,
	p2_score SMALLINT,
	p1_cname varchar(16),
	p2_cname varchar(16),
	winner varchar(12),
	primary key(set_id),
	foreign key(tournament_id) references tournament(tournament_id), 
	foreign key(p1_tag) references player(tag) on delete cascade on update cascade,
	foreign key(p2_tag) references player(tag) on delete cascade on update cascade,
	foreign key(p1_cname) references tournament_character(cname),
	foreign key(p2_cname) references tournament_character(cname)
);


create table team(
	tname varchar(22),
	p1_tag varchar(12),
	p2_tag varchar(12),
	wins smallint,
	losses smallint,
	points integer,
	primary key(tname),
	foreign key(p1_tag) references player(tag) on delete cascade on update cascade, 
	foreign key(p2_tag) references player(tag) on delete cascade on update cascade
);
create table doubles_set(
	dset_id varchar(14),
	tournament_id varchar(6),
	t1_name varchar(22),
	t2_name varchar(22),
	t1_score SMALLINT,
	t2_score SMALLINT,
	winner varchar(22),
	primary key(dset_id),
	foreign key (t1_name) references team(tname) on delete cascade on update cascade, 
	foreign key (t2_name) references team(tname) on delete cascade on update cascade,
    foreign key (tournament_id) references tournament(tournament_id)
);
