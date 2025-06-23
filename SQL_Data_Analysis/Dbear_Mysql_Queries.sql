
--select all the result set
select * from dataset_1 ;

--select weather, temperature from dataset
select weather, temperature  from dataset_1;

-- top 10 records
select * from dataset_1 LImit 10;

--unique or distinct data for passanger
select DISTINCT passanger  from dataset_1;

--Filter as per 'Home'
select * from dataset_1 where destination='Home';

--sort by coupon
select * from dataset_1 order by coupon; 

--applying alisas
select destination as 'Destination' from dataset_1;

--group by occupation and columnname 'occupation'
select occupation  from dataset_1 group by occupation ;

--group by occupation and columname as average of temperature. 
select avg(temperature) from dataset_1 group BY weather; 

--group by weather and columname as minimum of temperature. 
select min(temperature) from dataset_1 group BY weather; 

--sum of temperature
select sum(temperature)as 'sum_of_temperature' from dataset_1 group BY weather; 

--group by weather and columname as maximum of temperature. 
select max(temperature) from dataset_1 group BY weather; 

--filter by occupation ='Student'
select * from dataset_1 where occupation ='Student'