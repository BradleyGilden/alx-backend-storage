-- a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score;
    -- calculate project mark average of given user_id
    SELECT AVG(score) INTO avg_score FROM corrections
    WHERE corrections.user_id = user_id;
    -- update user table with average score
    UPDATE users SET average_score = avg_score
    WHERE id = user_id;
END $$
DELIMITER ;
