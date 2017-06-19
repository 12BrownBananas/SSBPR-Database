CREATE DEFINER=`root`@`localhost` FUNCTION `getPlayerInfo`(pTag varchar(20)) RETURNS varchar(20) CHARSET utf8
BEGIN
	DECLARE tagMatch varchar(20);
	SELECT tag INTO tagMatch FROM player WHERE tag = pTag;
RETURN tagMatch;
END