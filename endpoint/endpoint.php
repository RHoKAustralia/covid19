<?php
include "mysql-config.php";

function get_question_aliases($pdo) {
  $q = "SELECT alias, question from questionadmin_question";
  $stmt = $pdo -> query($q);
  $stmt->execute();
  $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
  echo json_encode($results);
}

function get_nanswers($pdo) {
  # get count of unique answers:
  $q = "SELECT COUNT(*) as n_answer FROM (SELECT COUNT(*) FROM questionadmin_answer GROUP BY participant_id, dateto) as t";
  $stmt = $pdo -> query($q);
  $stmt->execute();
  $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
  echo json_encode($results);
}

function get_keysymptoms($pdo) {
  $key_symptoms = "Cough,Sore-throat,FeelingFeverish";
  get_symptoms($pdo, $key_symptoms);
}

function get_symptoms($pdo, $symptomslist) {
  $symptoms = explode(",", $symptomslist);
  $output = array();
  foreach ($symptoms as $symptom) {
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

if ($_POST["action"] == "stats") {
  get_nanswers($pdo);
} else if ($_POST["action"] == "keysymptoms") {
  get_keysymptoms($pdo);
} else if ($_POST["action"] == "symptoms") {
  get_symptoms($pdo, $_POST["symptomslist"]);
} else if ($_POST["action"] == "aliases") {
  get_question_aliases($pdo);
} else {
  echo json_encode("Unknown request received");
}

$pdo = null;
?>
