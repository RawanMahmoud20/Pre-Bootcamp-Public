-- 1. Forward Engineer / Create Schema
CREATE DATABASE IF NOT EXISTS friendships_schema;
USE friendships_schema;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE friendships (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    friend_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (friend_id) REFERENCES users(id)
);

-- 2. Create 6 new users
INSERT INTO users (first_name, last_name) 
VALUES ('Amy', 'Giver'), ('Eli', 'Byers'), ('Big', 'Bird'), ('Kermit', 'The Frog'), ('Marky', 'Mark'), ('John', 'Doe');

-- 3. Create Friendships
INSERT INTO friendships (user_id, friend_id) VALUES 
(1, 2), (1, 4), (1, 6), -- User 1 friends with 2, 4, 6
(2, 1), (2, 3), (2, 5), -- User 2 friends with 1, 3, 5
(3, 2), (3, 5),          -- User 3 friends with 2, 5
(4, 3),                 -- User 4 friends with 3
(5, 1), (5, 6),          -- User 5 friends with 1, 6
(6, 2), (6, 3);          -- User 6 friends with 2, 3

-- 4. Display relationships
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id;

-- 5. NINJA: Friends of the first user
SELECT user2.first_name, user2.last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id
WHERE users.id = 1;

-- 6. NINJA: Count of all friendships
SELECT COUNT(*) as total_friendships FROM friendships;

-- 7. NINJA: Who has most friends?
SELECT users.first_name, users.last_name, COUNT(friendships.id) as num_of_friends
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
GROUP BY users.id
ORDER BY num_of_friends DESC
LIMIT 1;

-- 8. NINJA: Friends of 3rd user in alphabetical order
SELECT user2.first_name, user2.last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id
WHERE users.id = 3
ORDER BY user2.first_name ASC;