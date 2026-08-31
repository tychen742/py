<?php
declare(strict_types=1);

require_once __DIR__ . '/../lib/quiz-app.php';

$config = py_load_config();
$pdo = py_database_ready($config);
py_start_admin_session($config);

$admin = py_current_admin($pdo);
if ($admin === null) {
    header('Location: /api/admin/');
    exit;
}

$assignmentTypes = ['preview' => 'Preview', 'lab' => 'Lab', 'homework' => 'Homework'];
$selectedAssignmentType = strtolower(trim((string) ($_GET['assignment_type'] ?? '')));
if (!isset($assignmentTypes[$selectedAssignmentType])) {
    $selectedAssignmentType = '';
}

$assignmentNumbers = py_list_admin_report_assignment_numbers($pdo);
$selectedAssignmentNumber = strtolower(trim((string) ($_GET['assignment_number'] ?? '')));
if (!in_array($selectedAssignmentNumber, $assignmentNumbers, true)) {
    $selectedAssignmentNumber = '';
}

$scoreModes = ['best' => 'Best', 'all' => 'All'];
$selectedScoreMode = strtolower(trim((string) ($_GET['score_mode'] ?? 'best')));
if (!isset($scoreModes[$selectedScoreMode])) {
    $selectedScoreMode = 'best';
}

$selectedStudent = py_normalize_student_identifier((string) ($_GET['student_identifier'] ?? ''));

$studentOptions = py_list_admin_report_students($pdo);
$rows = py_list_admin_score_report(
    $pdo,
    $selectedAssignmentType !== '' ? $selectedAssignmentType : null,
    $selectedAssignmentNumber !== '' ? $selectedAssignmentNumber : null,
    $selectedStudent !== '' ? $selectedStudent : null,
    $selectedScoreMode
);
$scoreHeader = $selectedScoreMode === 'all' ? 'Score' : 'Best Score';
$attemptHeader = $selectedScoreMode === 'all' ? 'Attempt' : 'Attempts';
$submittedHeader = $selectedScoreMode === 'all' ? 'Submitted' : 'Last Submitted';
?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Score Report</title>
  <style><?php echo report_css(); ?></style>
</head>
<body>
  <?php echo py_admin_nav('report'); ?>
  <main class="shell">
    <header class="topbar">
      <div>
        <h1>Score Report</h1>
        <p>Scores and attempt counts by student and assignment.</p>
      </div>
    </header>

    <form class="filters" method="get" action="/api/admin/report.php">
      <label>
        <span>Assignment Name</span>
        <select name="assignment_type">
          <option value="">All names</option>
          <?php foreach ($assignmentTypes as $assignmentType => $assignmentTypeLabel): ?>
            <option value="<?php echo py_h($assignmentType); ?>" <?php echo $selectedAssignmentType === $assignmentType ? 'selected' : ''; ?>>
              <?php echo py_h($assignmentTypeLabel); ?>
            </option>
          <?php endforeach; ?>
        </select>
      </label>
      <label>
        <span>Assignment Number</span>
        <select name="assignment_number">
          <option value="">All numbers</option>
          <?php foreach ($assignmentNumbers as $assignmentNumber): ?>
            <option value="<?php echo py_h($assignmentNumber); ?>" <?php echo $selectedAssignmentNumber === $assignmentNumber ? 'selected' : ''; ?>>
              <?php echo py_h($assignmentNumber); ?>
            </option>
          <?php endforeach; ?>
        </select>
      </label>
      <label>
        <span>Student</span>
        <select name="student_identifier">
          <option value="">All students</option>
          <?php foreach ($studentOptions as $student): ?>
            <?php $studentIdentifier = (string) $student['student_identifier']; ?>
            <option value="<?php echo py_h($studentIdentifier); ?>" <?php echo $selectedStudent === $studentIdentifier ? 'selected' : ''; ?>>
              <?php echo py_h($student['label']); ?>
            </option>
          <?php endforeach; ?>
        </select>
      </label>
      <label>
        <span>Score</span>
        <select name="score_mode">
          <?php foreach ($scoreModes as $scoreMode => $scoreModeLabel): ?>
            <option value="<?php echo py_h($scoreMode); ?>" <?php echo $selectedScoreMode === $scoreMode ? 'selected' : ''; ?>>
              <?php echo py_h($scoreModeLabel); ?>
            </option>
          <?php endforeach; ?>
        </select>
      </label>
      <button class="button" type="submit">Apply</button>
      <a class="button secondary" href="/api/admin/report.php">Clear</a>
    </form>

    <p class="filter-summary"><?php echo count($rows); ?> row<?php echo count($rows) === 1 ? '' : 's'; ?> shown.</p>

    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Student ID</th>
            <th>Name</th>
            <th>Assignment</th>
            <th><?php echo py_h($scoreHeader); ?></th>
            <th><?php echo py_h($attemptHeader); ?></th>
            <th><?php echo py_h($submittedHeader); ?></th>
          </tr>
        </thead>
        <tbody>
        <?php if (count($rows) === 0): ?>
          <tr>
            <td class="empty" colspan="6">No scores match the selected filters.</td>
          </tr>
        <?php endif; ?>
        <?php foreach ($rows as $row): ?>
          <tr>
            <td><?php echo py_h($row['student_identifier']); ?></td>
            <td><?php echo py_h($row['display_name']); ?></td>
            <td><?php echo py_h($row['quiz_id']); ?></td>
            <td><?php echo py_h($row['best_score']); ?> / <?php echo py_h($row['max_score']); ?></td>
            <td><?php echo py_h($row['attempt_count']); ?></td>
            <td><?php echo py_h($row['last_submitted_at']); ?></td>
          </tr>
        <?php endforeach; ?>
        </tbody>
      </table>
    </div>
  </main>
</body>
</html>
<?php

function report_css(): string
{
    return py_admin_nav_css() . '
body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: #24292f; background: #f6f8fa; }
.shell { max-width: 1180px; margin: 0 auto; padding: 32px; }
h1 { margin: 0 0 8px; font-size: 28px; }
.topbar { display: flex; justify-content: space-between; gap: 16px; align-items: center; margin-bottom: 20px; }
.topbar p { margin: 0; color: #57606a; }
.filters { display: flex; flex-wrap: wrap; gap: 12px; align-items: flex-end; margin: 0 0 12px; }
.filters label { display: grid; gap: 6px; min-width: 240px; font-size: 13px; font-weight: 700; color: #57606a; }
.filters select { min-height: 40px; padding: 8px 34px 8px 10px; border: 1px solid #d0d7de; border-radius: 6px; background: white; color: #24292f; font: inherit; font-weight: 500; }
.button { display: inline-block; min-height: 40px; padding: 9px 14px; border: 1px solid #0969da; border-radius: 6px; background: #0969da; color: white; font: inherit; font-weight: 700; line-height: 20px; text-decoration: none; cursor: pointer; }
.button.secondary { background: white; color: #0969da; }
.filter-summary { margin: 0 0 12px; color: #57606a; font-size: 14px; }
.table-wrap { overflow-x: auto; border: 1px solid #d8dee4; border-radius: 8px; background: white; }
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th, td { padding: 10px 12px; border-bottom: 1px solid #d8dee4; text-align: left; }
th { background: #f6f8fa; font-weight: 700; }
.empty { padding: 18px 12px; color: #57606a; text-align: center; }
';
}
