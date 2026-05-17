-- 1. All countries where the primary language is Slovene, ordered by percentage descending
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

-- 2. Total number of cities for each country, ordered by number of cities descending
SELECT countries.name, COUNT(cities.id) AS total_cities
FROM countries
LEFT JOIN cities ON countries.code = cities.country_code
GROUP BY countries.code
ORDER BY total_cities DESC;

-- 3. All cities in Mexico with population > 500,000, ordered by population descending
SELECT cities.name, cities.population, cities.country_code
FROM cities
WHERE cities.country_code = 'MEX' AND cities.population > 500000
ORDER BY cities.population DESC;

-- 4. All languages in each country with percentage > 89%, ordered by percentage descending
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE languages.percentage > 89.0
ORDER BY languages.percentage DESC;

-- 5. Countries with surface area < 501 and population > 100,000
SELECT name, surface_area, population 
FROM countries 
WHERE surface_area < 501 AND population > 100000;

-- 6. Countries with Constitutional Monarchy, life expectancy > 75, and capital ID > 200
SELECT name, government_form, life_expectancy, capital 
FROM countries 
WHERE government_form = 'Constitutional Monarchy' 
  AND life_expectancy > 75.0 
  AND capital > 200;

-- 7. All cities of Argentina within Buenos Aires district and population > 500,000
SELECT countries.name AS country_name, cities.name AS city_name, cities.district, cities.population
FROM countries
JOIN cities ON countries.code = cities.country_code
WHERE countries.code = 'ARG' 
  AND cities.district = 'Buenos Aires' 
  AND cities.population > 500000;

-- 8. Summarize the number of countries in each region, ordered by country count descending
SELECT region, COUNT(code) AS number_of_countries
FROM countries
GROUP BY region
ORDER BY number_of_countries DESC;