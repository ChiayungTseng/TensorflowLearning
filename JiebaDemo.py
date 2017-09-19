import jieba as jb
str="纪录，职业生涯季后赛总得分超过了迈克尔-乔丹（5987分），居历史第一。他全场打了三节，拿下了35分、8个篮板和8次助攻。凯里-欧文24分7次助攻， 凯文-勒夫15分。替补出场持";

heho=jb.cut(str,cut_all=False);
print("/".join(heho));