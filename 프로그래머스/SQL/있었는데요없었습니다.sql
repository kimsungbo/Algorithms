-- 코드를 입력하세요
select INS.ANIMAL_ID, INS.NAME
from animal_ins as INS
LEFT JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.DATETIME < INS.DATETIME
ORDER BY INS.DATETIME ASC