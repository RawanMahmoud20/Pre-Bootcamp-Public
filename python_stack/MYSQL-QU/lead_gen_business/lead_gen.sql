USE `lead_gen_business`;


-- 1. Total revenue for March 2012
SELECT SUM(amount) AS revenue FROM billing 
WHERE charged_datetime >= '2012/03/01' AND charged_datetime <= '2012/03/31';

-- 2. Total revenue from client with ID 2
SELECT SUM(amount) AS total_revenue FROM billing WHERE client_id = 2;

-- 3. All sites owned by client with ID 10
SELECT domain_name, client_id FROM sites WHERE client_id = 10;

-- 4. Monthly sites created per year for client 1 and 20
SELECT client_id, COUNT(site_id) AS number_of_sites, MONTHNAME(created_datetime) AS month, YEAR(created_datetime) AS year 
FROM sites WHERE client_id IN (1, 20)
GROUP BY year, month, client_id;

-- 5. Total leads for each site between Jan 1, 2011 and Feb 15, 2011
SELECT sites.domain_name, COUNT(leads.leads_id) AS total_leads, leads.registered_datetime 
FROM sites 
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011/01/01' AND '2011/02/15'
GROUP BY sites.site_id;

-- 6. Client names and total leads in 2011
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011/01/01' AND '2011/12/31'
GROUP BY clients.client_id;

-- 7. Client names and total leads per month (Months 1-6 of 2011)
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS total_leads, MONTHNAME(leads.registered_datetime) AS month
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011/01/01' AND '2011/06/30'
GROUP BY clients.client_id, month;

-- 8. Leads per client site in 2011 and total for all time
-- Part 1: 2011
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011/01/01' AND '2011/12/31'
GROUP BY sites.site_id ORDER BY clients.client_id;
-- Part 2: All time
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY sites.site_id;

-- 9. Monthly revenue per client
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, SUM(billing.amount) AS total_revenue, MONTHNAME(billing.charged_datetime) AS month, YEAR(billing.charged_datetime) AS year
FROM clients
JOIN billing ON clients.client_id = billing.client_id
GROUP BY clients.client_id, year, month
ORDER BY clients.client_id;

-- 10. Grouped sites for each client
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name SEPARATOR ' / ') AS sites
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;