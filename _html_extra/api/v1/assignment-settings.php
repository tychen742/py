<?php
declare(strict_types=1);

require_once __DIR__ . '/../lib/quiz-app.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

$assignmentId = trim((string) ($_GET['assignment_id'] ?? ''));
if ($assignmentId === '' || py_assignment_definition($assignmentId) === null) {
    http_response_code(404);
    echo json_encode([
        'ok' => false,
        'error' => 'unknown_assignment',
    ], JSON_UNESCAPED_SLASHES);
    exit;
}

try {
    $config = py_load_config();
    $pdo = py_database_ready($config);
    echo json_encode([
        'ok' => true,
        'assignment_id' => $assignmentId,
        'answers_unlocked' => py_assignment_answers_unlocked($pdo, $assignmentId),
    ], JSON_UNESCAPED_SLASHES);
} catch (Throwable $exception) {
    error_log('Python assignment settings API error: ' . $exception->getMessage());
    http_response_code(500);
    echo json_encode([
        'ok' => false,
        'error' => 'settings_unavailable',
    ], JSON_UNESCAPED_SLASHES);
}
