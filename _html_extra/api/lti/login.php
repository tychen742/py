<?php
declare(strict_types=1);

require_once __DIR__ . '/../lib/quiz-app.php';

$config = py_load_config();
py_lti_login_redirect($config, $_REQUEST);
