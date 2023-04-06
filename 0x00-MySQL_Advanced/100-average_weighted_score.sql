-- Creates a stored procedure ComputeAverageWeightedScoreForUser that computes and stores the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(score * weight) / SUM(weight)
        FROM corrections AS C
        JOIN projects AS P ON C.project_id = P.id
        WHERE C.user_id = user_id
    )
    WHERE id = user_id;
END
$$
DELIMITER ;

