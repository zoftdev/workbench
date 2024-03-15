
basion server:
--
ssh zoftdev@45.252.53.165

install
--
install psql client +pgbench

apt install postgresql postgresql-contrib

create db for bench
--
```
sudo -i -u postgres
psql

CREATE DATABASE my_benchmark_test_db;
 psql -h pgm-tw9ny436chxf1y16.pg.rds.asr-ops.clouds.trueidc.com -U hlex -p 3433

passwd: abcABC***

```
 
checking
--
psql -h pgm-tw9ny436chxf1y16.pg.rds.asr-ops.clouds.trueidc.com -U hlex -p 3433 -d my_benchmark_test_db

load
--
pgbench -c 10 -j 2 -t 1000 my_benchmark_test_db -h  pgm-tw9ny436chxf1y16.pg.rds.asr-ops.clouds.trueidc.com -U hlex -p 3433

automate
--
loop find tps : run_tps.sh 
* should export PGPASSWD=xx before run
  
cvs-> image: report.py



