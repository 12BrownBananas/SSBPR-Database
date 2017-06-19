CREATE TRIGGER before_tournament_update
	BEFORE UPDATE ON tournament
    FOR EACH ROW
	SET New.entrants = New.entrants+1;