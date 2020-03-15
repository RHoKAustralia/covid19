<?php
include "mysql-config.php";

function get_nanswers($pdo) {
  # get count of unique answers:
  $q = "SELECT COUNT(*) as n_answer FROM (SELECT COUNT(*) FROM questionadmin_answer GROUP BY participant_id, dateto) as t";
  $stmt = $pdo -> query($q);
  $stmt->execute();
  $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
  echo json_encode($results);
}

function get_keysymptomps($pdo, $country, $agebracket) {
  $key_symptomps = array("Cough", "Sore-throat", "FeelingFeverish");
  $output = array();
  foreach ($key_symptomps as $symptom) {
    $q = "SELECT scale_answer as scale, COUNT(*) as count FROM questionadmin_answer as a JOIN questionadmin_question as q ON q.id = a.question_id  WHERE question = '".$symptom."' GROUP BY scale_Answer";
    $stmt = $pdo -> query($q);
    $stmt->execute();
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
    $output[$symptom] = $result;
  }
  echo json_encode($output);
}

$pdo = new PDO ('mysql:dbname='.MYSQL_DB.';host='.MYSQL_HOST, MYSQL_USER, MYSQL_PWD);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

if ($_GET["action"] == "stats") {
  get_nanswers($pdo);
} else if ($_GET["action"] == "keysymptomps") {
  get_keysymptomps($pdo, $_GET["country"], $_GET["agebracket"]);
} else {
  echo json_encode("Unknown request received");
}

$pdo = null;
?>
