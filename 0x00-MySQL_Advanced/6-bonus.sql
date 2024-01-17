-- a SQL script that creates a stored procedure AddBonus that
-- adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE p_occurrences INT;
    DECLARE p_id INT;
    DECLARE s_occurrences INT;

    -- Check if the project_name already exists in the projects table
    SELECT COUNT(*) INTO p_occurrences FROM projects WHERE name = project_name;

    -- If project_name doesn't exist, insert it into the projects table
    IF p_occurrences = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    -- Get the project_id for the given project_name
    SELECT id INTO p_id FROM projects WHERE name = project_name LIMIT 1;

    -- Check if there is an existing record for the user and project in the corrections table
    SELECT COUNT(*) INTO s_occurrences FROM corrections WHERE user_id = VALUES(user_id) AND project_id = p_id;

    -- If no existing record, insert a new one; otherwise, update the existing record
    IF s_occurrences = 0 THEN
        INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, p_id, score);
    ELSE
        UPDATE corrections SET score = VALUES(score) WHERE user_id = VALUES(user_id) AND project_id = p_id;
    END IF;
END $$

DELIMITER ;
