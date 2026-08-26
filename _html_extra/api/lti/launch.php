<?php
declare(strict_types=1);

require_once __DIR__ . '/../lib/quiz-app.php';

try {
    $config = py_load_config();
    $pdo = py_database_ready($config);
    $target = py_lti_handle_launch($pdo, $config, $_POST);
    header('Location: ' . $target);
} catch (Throwable $exception) {
    error_log('Python LTI launch error: ' . $exception->getMessage());
    http_response_code(400);
    echo '<!doctype html><meta charset="utf-8"><title>LTI Launch Failed</title>';
    echo '<h1>LTI Launch Failed</h1>';
    echo '<p>The Canvas launch could not be verified.</p>';
    echo '<pre>' . py_h($exception->getMessage()) . '</pre>';
}
