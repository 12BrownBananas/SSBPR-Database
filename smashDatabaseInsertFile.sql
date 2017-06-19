set SQL_SAFE_UPDATES = 0;

delete from tournament_set;
delete from tournament;
delete from venue;
delete from tournament_character;
delete from doubles_set;
delete from team;
delete from player;

insert into player values('00000', 'Dinner', 'Wilmington', '20', '6', '200');
insert into player values('00001', 'Skynerd', 'Wilmington', '22', '4', '240');
insert into player values('00002', 'Lazyboredom', 'Jacksonville', '24', '4', '250');
insert into player values('00003', 'Musk Ox', 'Wilmington', '16', '7', '140');
insert into player values('00004', 'YUM!', 'Wilmington', '12', '8', '130');
insert into player values('00005', 'Failcant', 'Wilmington', '6', '6', '90');
insert into player values('00006', 'Glist', 'Raleigh', '18', '6', '210');
insert into player values('00007', 'Antiyami', 'Charlotte', '16', '7', '140');
insert into player values('00008', 'The Cheese', 'Raleigh', '1', '20', '2');
insert into player values('00009', 'MattsOk', 'Wilmington', '14', '8', '130');
insert into player values('00010', 'Kam Steele', 'Raleigh', '20', '6', '200');
insert into player values('00011', 'Dietsoda', 'Jacksonville', '18', '5', '190');
insert into player values('00012', 'Dublio', 'Jacksonville', '10', '8', '100');


insert into venue values('Cape Fear Games', 'Wilmington');
insert into venue values('East Coast Gaming', 'Cary');
insert into venue values('High Tide Lounge', 'Carolina Beach');


insert into tournament values ('FNS15', 'Friday Night Smash 15', 'Cape Fear Games', '2017-03-10', '23');
insert into tournament values('SSF-12', 'Smash Sans Monthly 12', 'East Coast Gaming', '2016-02-28', '70');
insert into tournament values('PP-4', 'Pier Pressure 4', 'High Tide Lounge', '2016-12-04', '55');


insert into tournament_character values('Bayonetta', '1');
insert into tournament_character values('Diddy Kong', '2');
insert into tournament_character values('Cloud', '3');
insert into tournament_character values('Shiek', '4');
insert into tournament_character values('Sonic', '5');
insert into tournament_character values('Mario', '6');
insert into tournament_character values('Fox', '7');
insert into tournament_character values('Rosalina & Luma', '8');
insert into tournament_character values('Mewtwo', '9');
insert into tournament_character values('Marth', '10');
insert into tournament_character values('Zero Suit Samus', '11');
insert into tournament_character values('Ryu', '12');
insert into tournament_character values('Corrin', '13');
insert into tournament_character values('Meta Knight', '14');
insert into tournament_character values('Pikachu', '15');
insert into tournament_character values('Mega Man', '16');
insert into tournament_character values('Villager', '17');
insert into tournament_character values('Lucina', '18');
insert into tournament_character values('Lucario', '19');
insert into tournament_character values('Toon Link', '20');
insert into tournament_character values('Peach', '21');
insert into tournament_character values('Greninja', '22');
insert into tournament_character values('Captain Falcon', '23');
insert into tournament_character values('Ness', '24');
insert into tournament_character values('Bowser', '25');
insert into tournament_character values('Luigi', '26');
insert into tournament_character values('Olimar', '27');
insert into tournament_character values('Donkey Kong', '28');
insert into tournament_character values('Yoshi', '29');
insert into tournament_character values('Pit', '30');
insert into tournament_character values('Dark Pit', '31');
insert into tournament_character values('Lucas', '32');
insert into tournament_character values('ROB', '33');
insert into tournament_character values('Robin', '34');
insert into tournament_character values('Ike', '35');
insert into tournament_character values('Wario', '36');
insert into tournament_character values('Duck Hunt', '37');
insert into tournament_character values('Shulk', '38');
insert into tournament_character values('Link', '39');
insert into tournament_character values('Mr. Game & Watch', '40');
insert into tournament_character values('Samus', '41');
insert into tournament_character values('Palutena', '42');
insert into tournament_character values('Little Mac', '43');
insert into tournament_character values('Roy', '44');
insert into tournament_character values('Charizard', '45');
insert into tournament_character values('Pac Man', '46');
insert into tournament_character values('Kirby', '47');
insert into tournament_character values('Bowser Jr.', '48');
insert into tournament_character values('Wii Fit Trainer', '49');
insert into tournament_character values('Falco', '50');
insert into tournament_character values('Doctor Mario', '51');
insert into tournament_character values('King Dedede', '52');
insert into tournament_character values('Ganondorf', '53');
insert into tournament_character values('Mii Gunner', '54');
insert into tournament_character values('Zelda', '55');
insert into tournament_character values('Mii Brawler', '56');
insert into tournament_character values('Mii Swordfighter', '57');
insert into tournament_character values('Jigglypuff', '58');


insert into tournament_set values('WR1-1: FNS15', 'FNS15', 'YUM!', 'Failcant', '2', '1', 'Robin', 'Roy', 'YUM!');
insert into tournament_set values('LR1-5: FNS15', 'FNS15', 'Failcant', 'The Cheese', '2', '0', 'Roy', 'Little Mac', 'Failcant');
insert into tournament_set values('WR2-3: FNS15', 'FNS15', 'Dinner', 'Dietsoda', '2', '1', 'Fox', 'Cloud', 'Dinner');
insert into tournament_set values('WR2-4: FNS15', 'FNS15', 'Dublio', 'MattsOk', '0', '2', 'Cloud', 'Zero Suit Samus', 'MattsOk');
insert into tournament_set values('WF: FNS15', 'FNS15', 'Dinner', 'Lazyboredom', '1', '3', 'Fox', 'Little Mac', 'Lazyboredom');
insert into tournament_set values('GF-1: FNS15', 'FNS15', 'Skynerd', 'Lazyboredom', '2', '3', 'Bowser', 'Little Mac', 'Lazyboredom');
insert into tournament_set values('WR1-5: SSF-12', 'SSF-12', 'The Cheese', 'Kam Steele', '0', '2', 'Little Mac', 'Fox', 'Kam Steele');
insert into tournament_set values('WR2-4: SSF-12', 'SSF-12', 'Dietsoda', 'Glist', '0', '2', 'Cloud', 'Lucario', 'Glist');
insert into tournament_set values('WF: SSF-12', 'SSF-12', 'Glist', 'Lazyboredom', '1', '3', 'Lucario', 'Little Mac', 'Lazyboredom');
insert into tournament_set values('LR4-3: PP-4', 'PP-4', 'Antiyami', 'Musk Ox', '2', '1', 'Lucina', 'ROB', 'Antiyami');
insert into tournament_set values('WR4-1: PP-4', 'PP-4', 'Dinner', 'MattsOk', '2', '0', 'Fox', 'Zero Suit Samus', 'Dinner');
insert into tournament_set values('WR4-2: PP-4', 'PP-4', 'Dietsoda', 'YUM!', '2', '1', 'Cloud', 'Robin', 'Dietsoda');
insert into tournament_set values('GF-2: PP-4', 'PP-4', 'Skynerd', 'Lazyboredom', '3', '2', 'Bowser', 'Mewtwo', 'Skynerd');


insert into team values('Bad Grab Grab Bag', 'YUM!', 'MattsOk', '5', '4', '20');
insert into team values('Our Boy and His ROB', 'Failcant', 'Musk Ox', '6', '4', '25');
insert into team values('Skynerd+Lazyboredom','Skynerd','Lazyboredom', '10', '1', '55');
insert into team values('Diet Dubs', 'Dietsoda', 'Dublio', '4', '4', '15');


insert into doubles_set values('WR1-1: SSF-12', 'SSF-12', 'Bad Grab Grab Bag', 'Our Boy and His ROB', '1', '2', 'Our Boy and His ROB');
insert into doubles_set values('WF: SSF-12', 'SSF-12', 'Skynerd+Lazyboredom', 'Our Boy and His ROB', '3', '1', 'Skynerd+Lazyboredom');
insert into doubles_set values('GF-1: SSF-12', 'SSF-12', 'Skynerd+Lazyboredom', 'Our Boy and His ROB', '1', '3', 'Our Boy and His ROB');
insert into doubles_set values('GF-2: SSF-12', 'SSF-12', 'Skynerd+Lazyboredom', 'Our Boy and His ROB', '2', '3', 'Our Boy and His ROB');