CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `tournament_history` AS
    SELECT DISTINCT
        `tournament_set`.`tournament_id` AS `set_tournament_id`,
        `tournament`.`tournament_id` AS `tournament_tournament_id`,
        `tournament`.`tname` AS `tname`,
        `tournament`.`tdate` AS `tdate`,
        `tournament_set`.`p1_tag` AS `p1_tag`,
        `tournament_set`.`p2_tag` AS `p2_tag`
    FROM
        (`tournament_set`
        JOIN `tournament`)