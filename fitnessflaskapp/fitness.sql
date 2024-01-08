-- Creates the database
DROP DATABASE IF EXISTS fitness;
CREATE DATABASE fitness;

USE fitness;

-- Create the tables
CREATE TABLE users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    UserFirstName VARCHAR(25),
    UserLastName VARCHAR(50),
    ExperienceLevel VARCHAR(25),
    Goals TEXT
);

CREATE TABLE exercises (
    ExerciseID INT AUTO_INCREMENT PRIMARY KEY,
    ExerciseName VARCHAR(100),
    ExerciseType VARCHAR(50),
    Description TEXT
);

CREATE TABLE workouts (
    WorkoutID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    WorkoutName VARCHAR(100),
    WorkoutType VARCHAR(50),
    DateCreated DATETIME,
    LastUpdate DATETIME,
    FOREIGN KEY (UserID) REFERENCES users(UserID)
);

CREATE TABLE workoutdetails (
    WorkoutDetailID INT AUTO_INCREMENT PRIMARY KEY,
    WorkoutID INT,
    ExerciseID INT,
    Sets INT,
    Reps INT,
    Weight DECIMAL(5),
    FOREIGN KEY (WorkoutID) REFERENCES workouts(WorkoutID),
    FOREIGN KEY (ExerciseID) REFERENCES exercises(ExerciseID)
);

-- Sample data
INSERT INTO users (UserFirstName, UserLastName, ExperienceLevel, Goals) VALUES
('Ryan', 'Anderson', 'Advanced', 'Muscle Growth'),
('Steve', 'Jobs', 'Intermediate', 'Lose Weight');

INSERT INTO exercises (ExerciseName, ExerciseType, Description) VALUES
('Bench Press', 'Weight Training', 'A compound exercise that targets upper body muscles, mostly the chest. Press weight while lying flat on a bench.'),
('T-Bar Rows', 'Weight Training', 'A back exercise where you lift wait with your back on a T-bar machine.'),
('Chest Flys', 'Weight Training', 'A chest exercise where you move your arms together on a machine, dumbbells, or with cables.'),
('Dumbbell Bench Press', 'Weight Training', 'A chest exercise where you press dumbbells while laying flat on a bench.'),
('Dumbbell Rows', 'Weight Training', 'A back exercise that uses the lats. With your hand on a bench pull a dumbbell up to your body.'),
('Lat Pulldowns', 'Weight Training', 'A back exercise that isolates the lats. On a machine or cable machine use a bent bar to pull down to your chest.'),
('Squat', 'Weight Training', 'An exercise that involves a person lowering into a position where the knees are deeply bent and then rise to to a standing position.'),
('Smith Machine Calf Raises', 'Weight Training', 'An exercise that involves a smith machine. On a raised platform have your feet half on the platform and move lift with your toes.'),
('Hamstring Curls', 'Weight Training', 'An exercise that involves using a hamstring curl machine. Laying flat on the machine pull your legs to your body.'),
('Leg Extensions', 'Weight Training', 'An exercise that targets the quadriceps while using a leg extension machine. Extend your legs outwards and repeat.'),
('Leg Press', 'Weight Training', 'An exercies that involves using a leg press machine. Place your legs on the machine backplate and press your legs and then press them down to your chest.'),
('Seated Calf Raises', 'Weight Training', 'An exercise that involves using a seated calf raise machine. Sit on the machine and place your feet halfway off the platform. Press up with your feet.'),
('Barbell Curls', 'Weight Training', 'An exercise that targets the biceps. With a barbell keep your back straight and curl your arms to your chest.' ),
('Seated Tricep Extensions', 'Weight Training', 'An exercise that targets the triceps. Sitting down hold a barbell with both hands and press up keeping your elbows in.'),
('Shoulder Press', 'Weight Training', 'An exercise that targets shoulders. On a machine press the weight up. With dumbbells keep your arms at your side and press up.'),
('Seated Bicep Curls', 'Weight Training', 'An exercise that involves the biceps. While sitting down with dumbbells press them up towards the body.'),
('Tricep Pull downs', 'Weight Training', 'An exercise that isolates the triceps. This exercise can be done on a machine or with cables along with multiple grips such as a V-bar or flat-bar.'),
('Lateral Raises', 'Weight Training', 'An exercise that involves the shoulders. This exercise can be done with cables or dumbbells. Move the weight so that your arm is straight out.'),
('Cable Bicep Curls', 'Weight Training', 'An exercise that involves the biceps. With cables use your biceps to pull your arms up to your chest.'),
('Dumbbell Bicep Curls', 'Weight Training', 'An exercise that uses dumbbells to utilize your biceps. Multiple grips can be used to isolate a certain bicep head.'),
('Jog', 'Cardio', 'An exercise where you jog to gain endurance and cardio.');


INSERT INTO workouts (UserID, WorkoutName, WorkoutType, DateCreated, LastUpdate) VALUES
(1, 'Chest and Back Routine', 'Stength and Muscle Growth', NOW(), NOW()),
(1, 'Leg Routine', 'Strength and Muscle Growth', NOW(), NOW()),
(1, 'Arm Routine', 'Strength and Muscle Growth', NOW(), NOW()),
(1, 'Upper Chest and Back Routine', 'Strength and Muscle Growth', NOW(), NOW()),
(2, 'Cardio Routine', 'Weight Loss and Cardio', NOW(), NOW());

INSERT INTO workoutdetails (WorkoutID, ExerciseID, Sets, Reps, Weight) VALUES
(1, 1, 3, 12, 185),
(1, 2, 4, 10, 255),
(1, 3, 3, 10, 175),
(1, 4, 3, 10, 55),
(1, 5, 3, 10, 100),
(1, 6, 3, 10, 165);

-- Create User and Grant Access
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT, UPDATE, DELETE ON fitness.* TO 'admin'@'localhost';

