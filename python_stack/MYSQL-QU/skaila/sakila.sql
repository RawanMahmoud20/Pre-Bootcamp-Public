USE sakila;
-- 1. Customers in city_id = 312
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE address.city_id = 312;

-- 2. All comedy films
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

-- 3. All films by actor_id = 5
SELECT actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

-- 4. Customers in store_id = 1 and city_ids (1, 42, 312, 459)
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE customer.store_id = 1 AND address.city_id IN (1, 42, 312, 459);

-- 5. Films rating "G", "behind the scenes", and actor_id = 15
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
WHERE film.rating = 'G' 
  AND film.special_features LIKE '%behind the scenes%' 
  AND film_actor.actor_id = 15;

-- 6. All actors in film_id = 369
SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE film.film_id = 369;

-- 7. All drama films with rental rate = 2.99
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Drama' AND film.rental_rate = 2.99;

-- 8. All action films by SANDRA KILMER
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' AND actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER';