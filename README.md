# PersonalityTest
This is a simple program that Determines your personality based on three categories.

# Database
CREATE TABLE questions (
q_num INTEGER PRIMARY KEY,
description TEXT NOT NULL,
option_a TEXT NOT NULL,
option_b TEXT NOT NULL,
option_c TEXT NOT NULL
);

INSERT INTO questions (q_num, description, option_a, option_b, option_c)
VALUES
(1,"You went to a party last night and when you arrived to school the next day, everybody is talking about something you didn’t do. What will you do?","Avoid everything and go with your friends","Go and talk with the person that started the rumors","Go and talk with the teacher"),
(2,"What quality do you excel the most?","Empathy","Curiosity","Perseverance"),
(3,"You are walking down the street when you see an old lady trying to cross, what will you do?","Go and help her","Go for a policeman and ask him to help","Keep walking ahead"),
(4,"You had a very difficult day at school, you will
maintain a ____ attitude","Depends on the situation","Positive","Negative"),
(5,"You are at a party and a friend of yours comes
over and offers you a drink, what do you do?","Say no thanks","Drink it until it is finished","Ignore him and get angry at him"),
(6,"You just started in a new school, you will...","Go and talk with the person next to you","Wait until someone comes over you","Not talk to anyone"),
(7,"Go out with your close friends to eat","Go out with your close friends to eat","Go to a social club and meet more people","Invite one of your friends to your house"),
(8,"Your relationship with your parents is..","I like both equally","I like both equally","I like my Mom the most");


CREATE TABLE results (
category TEXT PRIMARY KEY,
description TEXT NOT NULL
);

INSERT INTO results(category, description)
VALUES
("Self-Management", "You manage yourself well; You take responsibility for your own behavior and well-being."),
("Empathy", "You are emphatic. You see yourself in someone else’s situation before doing decisions. You tend to listen to other’s voices."),
("Self-Awareness", "You are conscious of your own character, feelings, motives, and desires. The process can be painful but it leads to greater self-awareness.");


# Install all Dependencies:

$ pip install -r requirements.txt

