SELECT COUNT(*) FROM ( 
	SELECT TERM FROM FREQUENCY WHERE DOCID="10398_txt_earn" AND COUNT=1
	UNION
	SELECT TERM FROM FREQUENCY WHERE DOCID="925_txt_trade" AND COUNT=1 );
