-- 코드를 입력하세요

select animal_id, animal_type, name
from animal_ins
where animal_id in (select animal_id from animal_ins where substring_index(sex_upon_intake, ' ', 1) = 'Intact') and animal_id in (select animal_id from animal_outs where substring_index(sex_upon_outcome, ' ', 1) != 'Intact')
order by animal_id asc