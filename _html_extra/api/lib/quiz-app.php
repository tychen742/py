<?php
declare(strict_types=1);

function py_load_config(): array
{
    $default = [
        'database' => [
            'driver' => 'sqlite',
            'dsn' => 'sqlite:/tmp/py_quiz_attempts.sqlite',
            'username' => null,
            'password' => null,
        ],
        'canvas' => [
            'enabled' => false,
            'base_url' => null,
            'access_token' => null,
        ],
        'file_store' => [
            'path' => '/var/www/py_private/py_quiz_attempts.jsonl',
            'sqlite_backup_path' => '/home/tychen/py_private/backups/py_quiz_attempts_backup.sqlite',
            'sqlite_backup_enabled' => true,
        ],
        'course' => [
            'allowed_student_identifiers' => [],
        ],
        'auth' => [
            'session_name' => 'py_quiz_admin',
            'bootstrap_admins' => [],
        ],
        'student_auth' => [
            'session_name' => 'py_student',
            'require_authenticated_submissions' => false,
            'require_university_email_verification' => false,
            'allowed_email_domains' => ['umsystem.edu', 'mst.edu'],
            'verification_code_minutes' => 20,
            'email_from' => 'no-reply@thinkpy.org',
            'smtp' => [
                'host' => null,
                'port' => 587,
                'username' => null,
                'password' => null,
                'secure' => 'tls',
            ],
        ],
        'lti' => [
            'enabled' => false,
            'session_name' => 'py_lti',
            'issuer' => 'https://canvas.instructure.com',
            'client_id' => null,
            'deployment_ids' => [],
            'auth_login_url' => 'https://sso.canvaslms.com/api/lti/authorize_redirect',
            'jwks_url' => 'https://sso.canvaslms.com/api/lti/security/jwks',
            'redirect_uri' => 'https://thinkpy.org/api/lti/launch.php',
            'default_target_link_uri' => 'https://thinkpy.org/chapters/01-intro/assignments/preview.html',
        ],
    ];

    $paths = [];
    $envPath = getenv('PY_QUIZ_CONFIG');
    if (is_string($envPath) && $envPath !== '') {
        $paths[] = $envPath;
    }
    $paths[] = '/home/tychen/py_private/quiz_config.php';
    $paths[] = '/var/www/py_private/quiz_config.php';

    $allowDsmFallback = strtolower((string) getenv('PY_ALLOW_DSM_CONFIG_FALLBACK'));
    if (in_array($allowDsmFallback, ['1', 'true', 'yes'], true)) {
        $paths[] = '/var/www/dsm_private/quiz_config.php';
    }

    foreach ($paths as $path) {
        if (is_readable($path)) {
            $loaded = require $path;
            if (is_array($loaded)) {
                return array_replace_recursive($default, $loaded);
            }
        }
    }

    return $default;
}

function py_connect_database(array $database): PDO
{
    return new PDO(
        (string) $database['dsn'],
        $database['username'] ?? null,
        $database['password'] ?? null,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]
    );
}

function py_normalize_student_identifier(?string $identifier): string
{
    $identifier = strtolower(trim((string) $identifier));
    return preg_replace('/@.*$/', '', $identifier) ?? $identifier;
}

function py_student_identifier_allowed(array $config, ?string $identifier): bool
{
    $allowed = $config['course']['allowed_student_identifiers'] ?? [];
    if (!is_array($allowed) || count($allowed) === 0) {
        return true;
    }

    $normalizedIdentifier = py_normalize_student_identifier($identifier);
    if ($normalizedIdentifier === '') {
        return false;
    }

    $normalizedAllowed = array_map(
        static fn (mixed $value): string => py_normalize_student_identifier((string) $value),
        $allowed
    );

    return in_array($normalizedIdentifier, $normalizedAllowed, true);
}

function py_initialize_schema(PDO $pdo): void
{
    $driver = (string) $pdo->getAttribute(PDO::ATTR_DRIVER_NAME);
    $idColumn = $driver === 'sqlite'
        ? 'id INTEGER PRIMARY KEY AUTOINCREMENT'
        : 'id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY';

    $pdo->exec(
        'CREATE TABLE IF NOT EXISTS py_quiz_users (
            ' . $idColumn . ',
            email VARCHAR(255) NOT NULL UNIQUE,
            display_name VARCHAR(255) NULL,
            role VARCHAR(32) NOT NULL DEFAULT \'student\',
            password_hash VARCHAR(255) NULL,
            status VARCHAR(32) NOT NULL DEFAULT \'active\',
            canvas_user_id VARCHAR(64) NULL,
            student_identifier VARCHAR(255) NULL,
            email_verified_at DATETIME NULL,
            verification_code_hash VARCHAR(255) NULL,
            verification_code_expires_at DATETIME NULL,
            last_login_at DATETIME NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        )'
    );
    py_add_column_if_missing($pdo, 'py_quiz_users', 'student_identifier', 'VARCHAR(255) NULL');
    py_add_column_if_missing($pdo, 'py_quiz_users', 'email_verified_at', 'DATETIME NULL');
    py_add_column_if_missing($pdo, 'py_quiz_users', 'verification_code_hash', 'VARCHAR(255) NULL');
    py_add_column_if_missing($pdo, 'py_quiz_users', 'verification_code_expires_at', 'DATETIME NULL');
    py_add_column_if_missing($pdo, 'py_quiz_users', 'last_login_at', 'DATETIME NULL');

    $pdo->exec(
        'CREATE TABLE IF NOT EXISTS py_quiz_attempts (
            ' . $idColumn . ',
            quiz_id VARCHAR(100) NOT NULL,
            chapter VARCHAR(100) NOT NULL,
            assignment_slug VARCHAR(100) NOT NULL,
            student_user_id INT NULL,
            canvas_course_id VARCHAR(64) NULL,
            canvas_assignment_id VARCHAR(64) NULL,
            canvas_user_id VARCHAR(64) NULL,
            lti_deployment_id VARCHAR(255) NULL,
            lti_context_id VARCHAR(255) NULL,
            lti_resource_link_id VARCHAR(255) NULL,
            lti_lineitem_url TEXT NULL,
            student_identifier VARCHAR(255) NULL,
            score DECIMAL(6,2) NOT NULL,
            max_score DECIMAL(6,2) NOT NULL,
            answers_json TEXT NOT NULL,
            feedback_json TEXT NOT NULL,
            canvas_sync_status VARCHAR(32) NOT NULL DEFAULT \'pending\',
            canvas_sync_error TEXT NULL,
            synced_to_canvas_at DATETIME NULL,
            ip_address VARCHAR(64) NULL,
            user_agent TEXT NULL,
            submitted_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        )'
    );

    py_add_column_if_missing($pdo, 'py_quiz_attempts', 'student_user_id', 'INT NULL');
    py_add_column_if_missing($pdo, 'py_quiz_attempts', 'lti_deployment_id', 'VARCHAR(255) NULL');
    py_add_column_if_missing($pdo, 'py_quiz_attempts', 'lti_context_id', 'VARCHAR(255) NULL');
    py_add_column_if_missing($pdo, 'py_quiz_attempts', 'lti_resource_link_id', 'VARCHAR(255) NULL');
    py_add_column_if_missing($pdo, 'py_quiz_attempts', 'lti_lineitem_url', 'TEXT NULL');
    py_ensure_decimal_score_columns($pdo);
}

function py_add_column_if_missing(PDO $pdo, string $table, string $column, string $definition): void
{
    $driver = (string) $pdo->getAttribute(PDO::ATTR_DRIVER_NAME);
    if ($driver === 'sqlite') {
        $stmt = $pdo->query('PRAGMA table_info(' . $table . ')');
        foreach ($stmt->fetchAll() as $row) {
            if (($row['name'] ?? '') === $column) {
                return;
            }
        }
    } else {
        $stmt = $pdo->prepare('SHOW COLUMNS FROM ' . $table . ' LIKE :column');
        $stmt->execute(['column' => $column]);
        if ($stmt->fetch()) {
            return;
        }
    }

    $pdo->exec('ALTER TABLE ' . $table . ' ADD COLUMN ' . $column . ' ' . $definition);
}

function py_ensure_decimal_score_columns(PDO $pdo): void
{
    $driver = (string) $pdo->getAttribute(PDO::ATTR_DRIVER_NAME);
    if ($driver === 'sqlite') {
        return;
    }

    foreach (['score', 'max_score'] as $column) {
        $stmt = $pdo->prepare('SHOW COLUMNS FROM py_quiz_attempts LIKE :column');
        $stmt->execute(['column' => $column]);
        $info = $stmt->fetch();
        $type = strtolower((string) ($info['Type'] ?? ''));
        if (strpos($type, 'decimal') === 0) {
            continue;
        }

        $pdo->exec('ALTER TABLE py_quiz_attempts MODIFY ' . $column . ' DECIMAL(6,2) NOT NULL');
    }
}

function py_seed_admins(PDO $pdo, array $config): void
{
    foreach (($config['auth']['bootstrap_admins'] ?? []) as $admin) {
        $email = trim((string) ($admin['email'] ?? ''));
        $passwordHash = (string) ($admin['password_hash'] ?? '');
        if ($email === '' || $passwordHash === '') {
            continue;
        }

        $stmt = $pdo->prepare('SELECT id FROM py_quiz_users WHERE LOWER(email) = LOWER(:email) LIMIT 1');
        $stmt->execute(['email' => $email]);
        if ($stmt->fetch()) {
            continue;
        }

        $insert = $pdo->prepare(
            'INSERT INTO py_quiz_users (email, display_name, role, password_hash, status, canvas_user_id)
             VALUES (:email, :display_name, \'admin\', :password_hash, \'active\', :canvas_user_id)'
        );
        $insert->execute([
            'email' => $email,
            'display_name' => $admin['display_name'] ?? $email,
            'password_hash' => $passwordHash,
            'canvas_user_id' => $admin['canvas_user_id'] ?? null,
        ]);
    }
}

function py_seed_course_students(PDO $pdo, array $config): void
{
    $students = [];
    foreach (($config['course']['students'] ?? []) as $student) {
        if (is_array($student)) {
            $students[] = $student;
        }
    }

    foreach (($config['course']['allowed_student_identifiers'] ?? []) as $identifier) {
        $students[] = ['student_identifier' => (string) $identifier];
    }

    foreach ($students as $student) {
        $identifier = py_normalize_student_identifier((string) ($student['student_identifier'] ?? $student['sis_login_id'] ?? ''));
        if ($identifier === '') {
            continue;
        }

        $email = trim((string) ($student['email'] ?? ''));
        $displayName = trim((string) ($student['display_name'] ?? $student['name'] ?? $identifier));
        $passwordHash = (string) ($student['password_hash'] ?? '');

        $stmt = $pdo->prepare(
            'SELECT id FROM py_quiz_users
             WHERE LOWER(student_identifier) = LOWER(:student_identifier)
                OR LOWER(email) = LOWER(:email)
             LIMIT 1'
        );
        $stmt->execute([
            'student_identifier' => $identifier,
            'email' => $email !== '' ? $email : $identifier . '@student.local',
        ]);
        $existing = $stmt->fetch();

        if (is_array($existing)) {
            $sql = 'UPDATE py_quiz_users
                    SET student_identifier = :student_identifier,
                        display_name = :display_name,
                        role = \'student\',
                        status = \'active\'';
            $params = [
                'student_identifier' => $identifier,
                'display_name' => $displayName,
                'id' => (int) $existing['id'],
            ];
            if ($email !== '') {
                $sql .= ', email = :email';
                $params['email'] = $email;
            }
            if ($passwordHash !== '') {
                $sql .= ', password_hash = :password_hash';
                $params['password_hash'] = $passwordHash;
            }
            $sql .= ' WHERE id = :id';
            $pdo->prepare($sql)->execute($params);
            continue;
        }

        $insert = $pdo->prepare(
            'INSERT INTO py_quiz_users (email, display_name, role, password_hash, status, canvas_user_id, student_identifier)
             VALUES (:email, :display_name, \'student\', :password_hash, \'active\', NULL, :student_identifier)'
        );
        $insert->execute([
            'email' => $email !== '' ? $email : $identifier . '@student.local',
            'display_name' => $displayName,
            'password_hash' => $passwordHash !== '' ? $passwordHash : null,
            'student_identifier' => $identifier,
        ]);
    }
}

function py_database_ready(array $config): PDO
{
    $pdo = py_connect_database($config['database']);
    py_initialize_schema($pdo);
    py_seed_admins($pdo, $config);
    py_seed_course_students($pdo, $config);
    return $pdo;
}

function py_quiz_definition(string $quizId): ?array
{
    $quizzes = [
        'ch01-preview' => [
            'chapter' => '01-intro',
            'assignment_slug' => 'preview',
            'max_score' => 10,
            'canvas_assignment_column' => 'preview_ch01',
            'questions' => [
                'q1' => 'A',
                'q2' => 'B',
                'q3' => 'A',
                'q4' => 'B',
                'q5' => 'C',
                'q6' => 'A',
                'q7' => 'B',
                'q8' => 'A',
                'q9' => 'A',
                'q10' => 'C',
                'q11' => 'A',
                'q12' => 'B',
            ],
        ],
    ];

    return $quizzes[$quizId] ?? null;
}

function py_lab_definition(string $labId): ?array
{
    $labs = [
        'ch01-lab' => [
            'chapter' => '01-intro',
            'assignment_slug' => 'lab',
            'max_score' => 10,
            'canvas_assignment_column' => 'lab_ch01',
        ],
    ];

    return $labs[$labId] ?? null;
}

function py_assignment_definition(string $assignmentId): ?array
{
    return py_quiz_definition($assignmentId) ?? py_lab_definition($assignmentId);
}

function py_grade_attempt(array $quiz, array $answers): array
{
    $feedback = [];
    $normalizedAnswers = [];
    $correctCount = 0;

    foreach ($quiz['questions'] as $questionKey => $correctAnswer) {
        $submitted = strtoupper(trim((string) ($answers[$questionKey] ?? '')));
        $isCorrect = $submitted === $correctAnswer;
        if ($isCorrect) {
            $correctCount++;
        }

        $normalizedAnswers[$questionKey] = $submitted !== '' ? $submitted : null;
        $feedback[$questionKey] = [
            'correct' => $isCorrect,
            'submitted' => $submitted !== '' ? $submitted : null,
            'message' => $submitted === ''
                ? 'No answer submitted.'
                : ($isCorrect ? 'Correct.' : 'Try again.'),
        ];
    }

    $questionCount = count($quiz['questions']);
    $maxScore = (float) ($quiz['max_score'] ?? $questionCount);
    $score = $questionCount > 0 ? round(($correctCount / $questionCount) * $maxScore, 2) : 0.0;

    return [
        'score' => $score,
        'max_score' => $maxScore,
        'answers' => $normalizedAnswers,
        'feedback' => $feedback,
    ];
}

function py_grade_lab_attempt(array $lab, array $answers): array
{
    $normalizedAnswers = [
        'phase_1' => py_normalize_lab_string($answers['phase_1'] ?? ''),
        'phase_6' => py_normalize_lab_string($answers['phase_6'] ?? ''),
        'data_visualization_tool' => py_normalize_lab_string($answers['data_visualization_tool'] ?? ''),
        'manual_binary' => py_normalize_lab_binary($answers['manual_binary'] ?? ''),
        'subtotal' => py_normalize_lab_string($answers['subtotal'] ?? ''),
        'tax' => py_normalize_lab_string($answers['tax'] ?? ''),
        'total' => py_normalize_lab_string($answers['total'] ?? ''),
        'c_decimal' => py_normalize_lab_string($answers['c_decimal'] ?? ''),
        'c_binary' => py_normalize_lab_binary($answers['c_binary'] ?? ''),
        'item_hex' => py_normalize_lab_hex($answers['item_hex'] ?? ''),
    ];

    $feedback = [];
    $score = 0.0;

    $q1Score = 0.0;
    $q1Score += py_normalize_lab_phrase($normalizedAnswers['phase_1']) === 'business understanding' ? 1.0 : 0.0;
    $q1Score += py_normalize_lab_phrase($normalizedAnswers['phase_6']) === 'deployment' ? 1.0 : 0.0;
    $score += $q1Score;
    $feedback['q1'] = py_lab_feedback($q1Score, 2.0);

    $visualizationTools = ['matplotlib', 'seaborn', 'plotly'];
    $q2Score = in_array(py_normalize_lab_phrase($normalizedAnswers['data_visualization_tool']), $visualizationTools, true) ? 2.0 : 0.0;
    $score += $q2Score;
    $feedback['q2'] = py_lab_feedback($q2Score, 2.0);

    $q3Score = in_array($normalizedAnswers['manual_binary'], ['0b1101', '1101'], true) ? 2.0 : 0.0;
    $score += $q3Score;
    $feedback['q3'] = py_lab_feedback($q3Score, 2.0);

    $q4Score = 0.0;
    $q4Score += py_lab_number_equals($normalizedAnswers['subtotal'], 75.0) ? (2.0 / 3.0) : 0.0;
    $q4Score += py_lab_number_equals($normalizedAnswers['tax'], 6.19) ? (2.0 / 3.0) : 0.0;
    $q4Score += py_lab_number_equals($normalizedAnswers['total'], 81.19) ? (2.0 / 3.0) : 0.0;
    $score += $q4Score;
    $feedback['q4'] = py_lab_feedback($q4Score, 2.0);

    $q5Score = 0.0;
    $q5Score += py_lab_number_equals($normalizedAnswers['c_decimal'], 67.0) ? (2.0 / 3.0) : 0.0;
    $q5Score += $normalizedAnswers['c_binary'] === '0b1000011' ? (2.0 / 3.0) : 0.0;
    $q5Score += $normalizedAnswers['item_hex'] === '0x40' ? (2.0 / 3.0) : 0.0;
    $score += $q5Score;
    $feedback['q5'] = py_lab_feedback($q5Score, 2.0);

    return [
        'score' => round($score, 2),
        'max_score' => (float) ($lab['max_score'] ?? 10),
        'answers' => $normalizedAnswers,
        'feedback' => $feedback,
    ];
}

function py_lab_feedback(float $score, float $maxScore): array
{
    if ($score >= $maxScore - 0.001) {
        return [
            'correct' => true,
            'score' => round($score, 2),
            'max_score' => $maxScore,
            'message' => 'Accepted.',
        ];
    }

    return [
        'correct' => false,
        'score' => round($score, 2),
        'max_score' => $maxScore,
        'message' => $score > 0 ? 'Some entries need review.' : 'Try again.',
    ];
}

function py_normalize_lab_string(mixed $value): string
{
    return trim((string) $value);
}

function py_normalize_lab_phrase(string $value): string
{
    $value = strtolower(trim($value));
    $value = preg_replace('/[^a-z0-9]+/', ' ', $value) ?? $value;
    return trim(preg_replace('/\s+/', ' ', $value) ?? $value);
}

function py_normalize_lab_binary(mixed $value): string
{
    return strtolower(str_replace(' ', '', trim((string) $value)));
}

function py_normalize_lab_hex(mixed $value): string
{
    return strtolower(str_replace(' ', '', trim((string) $value)));
}

function py_lab_number_equals(string $submitted, float $expected): bool
{
    if (!is_numeric($submitted)) {
        return false;
    }
    return abs((float) $submitted - $expected) <= 0.01;
}

function py_save_attempt_record(array $config, array $attempt): int|string
{
    try {
        $pdo = py_database_ready($config);
        $attemptId = py_save_attempt($pdo, $attempt);
        py_save_attempt_sqlite_backup($config['file_store'], $attempt);
        return $attemptId;
    } catch (Throwable $exception) {
        error_log('Python quiz database save failed, using file fallback: ' . $exception->getMessage());
        $attemptId = py_save_attempt_file($config['file_store'], $attempt, $exception->getMessage());
        py_save_attempt_sqlite_backup($config['file_store'], $attempt);
        return $attemptId;
    }
}

function py_save_attempt(PDO $pdo, array $attempt): int
{
    $sql = 'INSERT INTO py_quiz_attempts (
        quiz_id, chapter, assignment_slug, student_user_id, canvas_course_id, canvas_assignment_id,
        canvas_user_id, lti_deployment_id, lti_context_id, lti_resource_link_id, lti_lineitem_url,
        student_identifier, score, max_score, answers_json, feedback_json,
        canvas_sync_status, canvas_sync_error, synced_to_canvas_at, ip_address, user_agent
    ) VALUES (
        :quiz_id, :chapter, :assignment_slug, :student_user_id, :canvas_course_id, :canvas_assignment_id,
        :canvas_user_id, :lti_deployment_id, :lti_context_id, :lti_resource_link_id, :lti_lineitem_url,
        :student_identifier, :score, :max_score, :answers_json, :feedback_json,
        :canvas_sync_status, :canvas_sync_error, :synced_to_canvas_at, :ip_address, :user_agent
    )';

    $stmt = $pdo->prepare($sql);
    $stmt->execute($attempt);
    return (int) $pdo->lastInsertId();
}

function py_save_attempt_file(array $fileStore, array $attempt, string $storageWarning): string
{
    $path = (string) ($fileStore['path'] ?? (sys_get_temp_dir() . '/py_quiz_attempts.jsonl'));
    $directory = dirname($path);
    if (!is_dir($directory) && !@mkdir($directory, 0770, true) && !is_dir($directory)) {
        $path = sys_get_temp_dir() . '/py_quiz_attempts.jsonl';
    }

    $attemptId = gmdate('YmdHis') . '-' . bin2hex(random_bytes(4));
    $record = $attempt + [
        'id' => $attemptId,
        'submitted_at' => gmdate('Y-m-d H:i:s'),
        'storage_warning' => $storageWarning,
    ];

    $json = json_encode($record, JSON_UNESCAPED_SLASHES);
    if ($json === false || file_put_contents($path, $json . PHP_EOL, FILE_APPEND | LOCK_EX) === false) {
        throw new RuntimeException('Could not write quiz attempt file.');
    }

    return $attemptId;
}

function py_save_attempt_sqlite_backup(array $fileStore, array $attempt): void
{
    if (($fileStore['sqlite_backup_enabled'] ?? true) === false) {
        return;
    }

    try {
        $path = (string) ($fileStore['sqlite_backup_path'] ?? (sys_get_temp_dir() . '/py_quiz_attempts_backup.sqlite'));
        $directory = dirname($path);
        if (!is_dir($directory) && !@mkdir($directory, 0770, true) && !is_dir($directory)) {
            $path = sys_get_temp_dir() . '/py_quiz_attempts_backup.sqlite';
        }

        $pdo = py_connect_database([
            'dsn' => 'sqlite:' . $path,
            'username' => null,
            'password' => null,
        ]);
        py_initialize_schema($pdo);
        py_save_attempt($pdo, $attempt);
    } catch (Throwable $exception) {
        error_log('Python quiz SQLite backup failed: ' . $exception->getMessage());
    }
}

function py_canvas_ready(array $config, array $identity): bool
{
    return !empty($config['canvas']['enabled'])
        && !empty($config['canvas']['base_url'])
        && !empty($config['canvas']['access_token'])
        && !empty($identity['canvas_course_id'])
        && !empty($identity['canvas_assignment_id'])
        && !empty($identity['canvas_user_id']);
}

function py_find_existing_best_score(PDO $pdo, string $quizId, array $identity): ?float
{
    if (
        !empty($identity['canvas_course_id'])
        && !empty($identity['canvas_assignment_id'])
        && !empty($identity['canvas_user_id'])
    ) {
        $stmt = $pdo->prepare(
            'SELECT MAX(score) AS best_score
             FROM py_quiz_attempts
             WHERE quiz_id = :quiz_id
               AND canvas_course_id = :canvas_course_id
               AND canvas_assignment_id = :canvas_assignment_id
               AND canvas_user_id = :canvas_user_id'
        );
        $stmt->execute([
            'quiz_id' => $quizId,
            'canvas_course_id' => $identity['canvas_course_id'],
            'canvas_assignment_id' => $identity['canvas_assignment_id'],
            'canvas_user_id' => $identity['canvas_user_id'],
        ]);
    } elseif (!empty($identity['student_identifier'])) {
        $stmt = $pdo->prepare(
            'SELECT MAX(score) AS best_score
             FROM py_quiz_attempts
             WHERE quiz_id = :quiz_id
               AND student_identifier = :student_identifier'
        );
        $stmt->execute([
            'quiz_id' => $quizId,
            'student_identifier' => $identity['student_identifier'],
        ]);
    } else {
        return null;
    }

    $score = $stmt->fetchColumn();
    return $score === false || $score === null ? null : (float) $score;
}

function py_is_score_at_least_best(PDO $pdo, string $quizId, array $identity, float $score): bool
{
    $bestScore = py_find_existing_best_score($pdo, $quizId, $identity);
    return $bestScore === null || $score >= $bestScore - 0.001;
}

function py_attempt_summary(PDO $pdo, string $quizId, array $identity): array
{
    if (
        !empty($identity['canvas_course_id'])
        && !empty($identity['canvas_assignment_id'])
        && !empty($identity['canvas_user_id'])
    ) {
        $stmt = $pdo->prepare(
            'SELECT COUNT(*) AS attempt_count, MAX(score) AS best_score
             FROM py_quiz_attempts
             WHERE quiz_id = :quiz_id
               AND canvas_course_id = :canvas_course_id
               AND canvas_assignment_id = :canvas_assignment_id
               AND canvas_user_id = :canvas_user_id'
        );
        $stmt->execute([
            'quiz_id' => $quizId,
            'canvas_course_id' => $identity['canvas_course_id'],
            'canvas_assignment_id' => $identity['canvas_assignment_id'],
            'canvas_user_id' => $identity['canvas_user_id'],
        ]);
    } elseif (!empty($identity['student_identifier'])) {
        $stmt = $pdo->prepare(
            'SELECT COUNT(*) AS attempt_count, MAX(score) AS best_score
             FROM py_quiz_attempts
             WHERE quiz_id = :quiz_id
               AND student_identifier = :student_identifier'
        );
        $stmt->execute([
            'quiz_id' => $quizId,
            'student_identifier' => $identity['student_identifier'],
        ]);
    } else {
        return ['attempt_count' => 0, 'best_score' => null];
    }

    $row = $stmt->fetch() ?: [];
    return [
        'attempt_count' => (int) ($row['attempt_count'] ?? 0),
        'best_score' => ($row['best_score'] ?? null) === null ? null : (float) $row['best_score'],
    ];
}

function py_sync_canvas_grade(array $canvas, array $identity, string $postedGrade): array
{
    $baseUrl = rtrim((string) $canvas['base_url'], '/');
    $path = sprintf(
        '/api/v1/courses/%s/assignments/%s/submissions/%s',
        rawurlencode((string) $identity['canvas_course_id']),
        rawurlencode((string) $identity['canvas_assignment_id']),
        rawurlencode((string) $identity['canvas_user_id'])
    );

    $ch = curl_init($baseUrl . $path);
    curl_setopt_array($ch, [
        CURLOPT_CUSTOMREQUEST => 'PUT',
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 20,
        CURLOPT_HTTPHEADER => [
            'Authorization: Bearer ' . $canvas['access_token'],
        ],
        CURLOPT_POSTFIELDS => http_build_query([
            'submission' => ['posted_grade' => $postedGrade],
            'comment' => ['text_comment' => 'Python quiz score synced automatically.'],
        ]),
    ]);

    $body = curl_exec($ch);
    $error = curl_error($ch);
    $status = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    curl_close($ch);

    if ($body !== false && $status >= 200 && $status < 300) {
        return [
            'status' => 'synced',
            'error' => null,
            'synced_at' => gmdate('Y-m-d H:i:s'),
        ];
    }

    return [
        'status' => 'failed',
        'error' => $error !== '' ? $error : 'Canvas returned HTTP ' . $status,
        'synced_at' => null,
    ];
}

function py_list_attempts(PDO $pdo, int $limit = 200): array
{
    $stmt = $pdo->prepare(
        'SELECT id, quiz_id, chapter, assignment_slug, canvas_course_id, canvas_assignment_id,
                canvas_user_id, lti_deployment_id, lti_context_id, lti_resource_link_id,
                lti_lineitem_url, student_identifier, score, max_score, answers_json,
                canvas_sync_status, canvas_sync_error, synced_to_canvas_at, submitted_at
         FROM py_quiz_attempts
         ORDER BY submitted_at DESC, id DESC
         LIMIT :limit'
    );
    $stmt->bindValue(':limit', $limit, PDO::PARAM_INT);
    $stmt->execute();
    return $stmt->fetchAll();
}

function py_list_student_attempts(PDO $pdo, int $studentUserId, int $limit = 200): array
{
    $stmt = $pdo->prepare(
        'SELECT id, quiz_id, chapter, assignment_slug, score, max_score,
                canvas_sync_status, submitted_at
         FROM py_quiz_attempts
         WHERE student_user_id = :student_user_id
         ORDER BY submitted_at DESC, id DESC
         LIMIT :limit'
    );
    $stmt->bindValue(':student_user_id', $studentUserId, PDO::PARAM_INT);
    $stmt->bindValue(':limit', $limit, PDO::PARAM_INT);
    $stmt->execute();
    return $stmt->fetchAll();
}

function py_list_student_score_summary(PDO $pdo, int $studentUserId): array
{
    $stmt = $pdo->prepare(
        'SELECT quiz_id, assignment_slug, COUNT(*) AS attempt_count,
                MAX(score) AS best_score, MAX(max_score) AS max_score,
                MAX(submitted_at) AS last_submitted_at
         FROM py_quiz_attempts
         WHERE student_user_id = :student_user_id
         GROUP BY quiz_id, assignment_slug
         ORDER BY quiz_id ASC'
    );
    $stmt->execute(['student_user_id' => $studentUserId]);
    return $stmt->fetchAll();
}

function py_list_admin_score_report(PDO $pdo): array
{
    $stmt = $pdo->query(
        'SELECT
             COALESCE(u.student_identifier, qa.student_identifier, qa.canvas_user_id, \'Unknown\') AS student_identifier,
             COALESCE(u.display_name, \'\') AS display_name,
             qa.quiz_id,
             qa.assignment_slug,
             COUNT(*) AS attempt_count,
             MAX(qa.score) AS best_score,
             MAX(qa.max_score) AS max_score,
             MAX(qa.submitted_at) AS last_submitted_at
         FROM py_quiz_attempts qa
         LEFT JOIN py_quiz_users u ON u.id = qa.student_user_id
         GROUP BY student_identifier, display_name, qa.quiz_id, qa.assignment_slug
         ORDER BY student_identifier ASC, qa.quiz_id ASC'
    );
    return $stmt->fetchAll();
}

function py_sync_pending_attempts(PDO $pdo, array $config, int $limit = 100): array
{
    $stmt = $pdo->prepare(
        'SELECT id, quiz_id, canvas_course_id, canvas_assignment_id, canvas_user_id, student_identifier, score
         FROM py_quiz_attempts
         WHERE canvas_sync_status IN (\'pending\', \'failed\')
         ORDER BY submitted_at ASC, id ASC
         LIMIT :limit'
    );
    $stmt->bindValue(':limit', $limit, PDO::PARAM_INT);
    $stmt->execute();
    $attempts = $stmt->fetchAll();

    $summary = ['synced' => 0, 'failed' => 0, 'skipped' => 0, 'checked' => count($attempts)];
    foreach ($attempts as $attempt) {
        if (
            empty($attempt['canvas_course_id'])
            || empty($attempt['canvas_assignment_id'])
            || empty($attempt['canvas_user_id'])
        ) {
            py_update_sync_status($pdo, (int) $attempt['id'], [
                'status' => 'skipped',
                'error' => 'Missing Canvas course, assignment, or user ID.',
                'synced_at' => null,
            ]);
            $summary['skipped']++;
            continue;
        }

        if (!py_is_score_at_least_best($pdo, (string) $attempt['quiz_id'], $attempt, (float) $attempt['score'])) {
            py_update_sync_status($pdo, (int) $attempt['id'], [
                'status' => 'skipped',
                'error' => 'Lower than the student\'s highest attempt for this assignment.',
                'synced_at' => null,
            ]);
            $summary['skipped']++;
            continue;
        }

        if (empty($config['canvas']['enabled'])) {
            py_update_sync_status($pdo, (int) $attempt['id'], [
                'status' => 'failed',
                'error' => 'Canvas sync is not enabled.',
                'synced_at' => null,
            ]);
            $summary['failed']++;
            continue;
        }

        $result = py_sync_canvas_grade($config['canvas'], $attempt, (string) $attempt['score']);
        py_update_sync_status($pdo, (int) $attempt['id'], $result);
        $summary[$result['status'] === 'synced' ? 'synced' : 'failed']++;
    }

    return $summary;
}

function py_update_sync_status(PDO $pdo, int $attemptId, array $result): void
{
    $stmt = $pdo->prepare(
        'UPDATE py_quiz_attempts
         SET canvas_sync_status = :status,
             canvas_sync_error = :error,
             synced_to_canvas_at = :synced_at
         WHERE id = :id'
    );
    $stmt->execute([
        'status' => $result['status'],
        'error' => $result['error'],
        'synced_at' => $result['synced_at'],
        'id' => $attemptId,
    ]);
}

function py_start_admin_session(array $config): void
{
    session_name((string) $config['auth']['session_name']);
    session_start();
}

function py_start_lti_session(array $config): void
{
    if (session_status() === PHP_SESSION_ACTIVE) {
        return;
    }
    session_name((string) $config['lti']['session_name']);
    session_set_cookie_params([
        'lifetime' => 0,
        'path' => '/',
        'secure' => true,
        'httponly' => true,
        'samesite' => 'None',
    ]);
    session_start();
}

function py_start_student_session(array $config): void
{
    if (session_status() === PHP_SESSION_ACTIVE) {
        return;
    }
    $sessionName = (string) ($config['student_auth']['session_name'] ?? 'py_student');
    session_name($sessionName);
    if (isset($_COOKIE[$sessionName]) && preg_match('/^[a-zA-Z0-9,-]{16,128}$/', (string) $_COOKIE[$sessionName])) {
        session_id((string) $_COOKIE[$sessionName]);
    }
    session_set_cookie_params([
        'lifetime' => 0,
        'path' => '/',
        'secure' => true,
        'httponly' => true,
        'samesite' => 'Lax',
    ]);
    session_start();
}

function py_start_fresh_student_session(array $config): void
{
    if (session_status() === PHP_SESSION_ACTIVE) {
        session_write_close();
        $_SESSION = [];
    }
    session_name((string) ($config['student_auth']['session_name'] ?? 'py_student'));
    session_set_cookie_params([
        'lifetime' => 0,
        'path' => '/',
        'secure' => true,
        'httponly' => true,
        'samesite' => 'Lax',
    ]);
    session_id(py_random_token());
    session_start();
}

function py_submission_auth_required(array $config): bool
{
    return !empty($config['student_auth']['require_authenticated_submissions']);
}

function py_student_email_verification_required(array $config): bool
{
    return !empty($config['student_auth']['require_university_email_verification']);
}

function py_find_student_for_login(PDO $pdo, string $identifier): ?array
{
    $normalized = py_normalize_student_identifier($identifier);
    if ($normalized === '') {
        return null;
    }

    $stmt = $pdo->prepare(
        'SELECT id, email, display_name, role, status, password_hash, student_identifier,
                email_verified_at, verification_code_hash, verification_code_expires_at
         FROM py_quiz_users
         WHERE role = \'student\'
           AND status = \'active\'
           AND (
                LOWER(email) = LOWER(:identifier)
                OR LOWER(student_identifier) = LOWER(:normalized_identifier)
           )
         LIMIT 1'
    );
    $stmt->execute([
        'identifier' => trim($identifier),
        'normalized_identifier' => $normalized,
    ]);
    $student = $stmt->fetch();
    return is_array($student) ? $student : null;
}

function py_university_email_allowed(array $config, string $studentIdentifier, string $email): bool
{
    $email = strtolower(trim($email));
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return false;
    }

    [$localPart, $domain] = explode('@', $email, 2);
    $allowedDomains = array_map('strtolower', array_map('strval', $config['student_auth']['allowed_email_domains'] ?? []));
    if ($allowedDomains !== [] && !in_array($domain, $allowedDomains, true)) {
        return false;
    }

    return py_normalize_student_identifier($localPart) === py_normalize_student_identifier($studentIdentifier);
}

function py_send_student_verification_code(PDO $pdo, array $config, string $identifier, string $email): bool
{
    $student = py_find_student_for_login($pdo, $identifier);
    if (!is_array($student)) {
        return false;
    }

    $studentIdentifier = (string) ($student['student_identifier'] ?: py_normalize_student_identifier((string) $student['email']));
    if (!py_university_email_allowed($config, $studentIdentifier, $email)) {
        return false;
    }

    $code = (string) random_int(100000, 999999);
    $minutes = max(5, (int) ($config['student_auth']['verification_code_minutes'] ?? 20));
    $expiresAt = gmdate('Y-m-d H:i:s', time() + ($minutes * 60));

    $stmt = $pdo->prepare(
        'UPDATE py_quiz_users
         SET email = :email,
             verification_code_hash = :verification_code_hash,
             verification_code_expires_at = :verification_code_expires_at
         WHERE id = :id'
    );
    $stmt->execute([
        'email' => strtolower(trim($email)),
        'verification_code_hash' => password_hash($code, PASSWORD_DEFAULT),
        'verification_code_expires_at' => $expiresAt,
        'id' => (int) $student['id'],
    ]);

    $subject = 'Your ThinkPy verification code';
    $body = "Your ThinkPy verification code is {$code}.\n\nThis code expires in {$minutes} minutes.";
    if (!py_send_email($config, strtolower(trim($email)), $subject, $body)) {
        error_log('Python student verification email failed for user id ' . (int) $student['id']);
        return false;
    }

    return true;
}

function py_verify_student_email_code(PDO $pdo, string $identifier, string $code, string $newPassword): bool
{
    $student = py_find_student_for_login($pdo, $identifier);
    if (!is_array($student)) {
        return false;
    }

    if (strlen($newPassword) < 10) {
        return false;
    }

    $hash = (string) ($student['verification_code_hash'] ?? '');
    $expiresAt = strtotime((string) ($student['verification_code_expires_at'] ?? ''));
    if ($hash === '' || $expiresAt === false || $expiresAt < time()) {
        return false;
    }

    if (!password_verify(trim($code), $hash)) {
        return false;
    }

    $stmt = $pdo->prepare(
        'UPDATE py_quiz_users
         SET email_verified_at = CURRENT_TIMESTAMP,
             password_hash = :password_hash,
             verification_code_hash = NULL,
             verification_code_expires_at = NULL
         WHERE id = :id'
    );
    $stmt->execute([
        'password_hash' => password_hash($newPassword, PASSWORD_DEFAULT),
        'id' => (int) $student['id'],
    ]);
    return true;
}

function py_send_student_verification_link(PDO $pdo, array $config, string $email, string $target = '/'): bool
{
    $email = strtolower(trim($email));
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return false;
    }

    [$localPart] = explode('@', $email, 2);
    $identifier = py_normalize_student_identifier($localPart);
    $student = py_find_student_for_login($pdo, $identifier);
    if (!is_array($student)) {
        return false;
    }

    $studentIdentifier = (string) ($student['student_identifier'] ?: py_normalize_student_identifier((string) $student['email']));
    if (!py_university_email_allowed($config, $studentIdentifier, $email)) {
        return false;
    }

    $token = bin2hex(random_bytes(16));
    $minutes = max(5, (int) ($config['student_auth']['verification_code_minutes'] ?? 20));
    $expiresAt = gmdate('Y-m-d H:i:s', time() + ($minutes * 60));

    $stmt = $pdo->prepare(
        'UPDATE py_quiz_users
         SET email = :email,
             verification_code_hash = :verification_code_hash,
             verification_code_expires_at = :verification_code_expires_at
         WHERE id = :id'
    );
    $stmt->execute([
        'email' => $email,
        'verification_code_hash' => py_token_fingerprint($token),
        'verification_code_expires_at' => $expiresAt,
        'id' => (int) $student['id'],
    ]);

    $link = 'https://thinkpy.org/api/student/create-password.php?uid=' . rawurlencode((string) $student['id'])
        . '&token=' . rawurlencode($token)
        . '&next=' . rawurlencode(py_safe_target($target));
    $subject = 'Create your ThinkPy password';
    $body = "Use this link to create or reset your ThinkPy password:\n\n{$link}\n\nThis link expires in {$minutes} minutes.";
    if (!py_send_email($config, $email, $subject, $body)) {
        error_log('Python student verification link email failed for user id ' . (int) $student['id']);
        return false;
    }

    return true;
}

function py_verify_student_email_token(PDO $pdo, string $token, string $newPassword, ?int $userId = null): ?string
{
    $token = trim($token);
    if ($token === '' || strlen($newPassword) < 10) {
        return null;
    }

    if ($userId !== null && $userId > 0) {
        $stmt = $pdo->prepare(
            'SELECT id, student_identifier, email, verification_code_hash, verification_code_expires_at
             FROM py_quiz_users
             WHERE id = :id
               AND role = \'student\'
               AND status = \'active\'
               AND verification_code_hash IS NOT NULL
               AND verification_code_expires_at IS NOT NULL'
        );
        $stmt->execute(['id' => $userId]);
    } else {
        $stmt = $pdo->query(
            'SELECT id, student_identifier, email, verification_code_hash, verification_code_expires_at
             FROM py_quiz_users
             WHERE role = \'student\'
               AND status = \'active\'
               AND verification_code_hash IS NOT NULL
               AND verification_code_expires_at IS NOT NULL'
        );
    }

    foreach ($stmt as $student) {
        $expiresAt = strtotime((string) ($student['verification_code_expires_at'] ?? ''));
        if ($expiresAt === false || $expiresAt < time()) {
            continue;
        }
        if (!py_token_matches($token, (string) ($student['verification_code_hash'] ?? ''))) {
            continue;
        }

        $update = $pdo->prepare(
            'UPDATE py_quiz_users
             SET email_verified_at = CURRENT_TIMESTAMP,
                 password_hash = :password_hash,
                 verification_code_hash = NULL,
                 verification_code_expires_at = NULL
             WHERE id = :id'
        );
        $update->execute([
            'password_hash' => password_hash($newPassword, PASSWORD_DEFAULT),
            'id' => (int) $student['id'],
        ]);

        return (string) ($student['student_identifier'] ?: py_normalize_student_identifier((string) $student['email']));
    }

    return null;
}

function py_safe_target(string $target): string
{
    if ($target === '' || $target[0] !== '/' || str_starts_with($target, '//')) {
        return '/';
    }
    return $target;
}

function py_token_fingerprint(string $token): string
{
    return 'sha256:' . hash('sha256', $token);
}

function py_token_matches(string $token, string $storedHash): bool
{
    if (str_starts_with($storedHash, 'sha256:')) {
        return hash_equals($storedHash, py_token_fingerprint($token));
    }
    return password_verify($token, $storedHash);
}

function py_send_email(array $config, string $to, string $subject, string $body): bool
{
    $from = (string) ($config['student_auth']['email_from'] ?? 'no-reply@thinkpy.org');
    $smtp = $config['student_auth']['smtp'] ?? [];
    if (is_array($smtp) && !empty($smtp['host']) && !empty($smtp['username']) && !empty($smtp['password'])) {
        return py_send_smtp_email($smtp, $from, $to, $subject, $body);
    }

    $headers = "From: {$from}\r\nContent-Type: text/plain; charset=UTF-8";
    return mail($to, $subject, $body, $headers);
}

function py_send_smtp_email(array $smtp, string $from, string $to, string $subject, string $body): bool
{
    if (!filter_var($from, FILTER_VALIDATE_EMAIL) || !filter_var($to, FILTER_VALIDATE_EMAIL)) {
        return false;
    }

    $host = (string) $smtp['host'];
    $port = (int) ($smtp['port'] ?? 587);
    $secure = strtolower((string) ($smtp['secure'] ?? 'tls'));
    $username = (string) $smtp['username'];
    $password = (string) $smtp['password'];
    $remote = ($secure === 'ssl' ? 'ssl://' : '') . $host . ':' . $port;
    $errno = 0;
    $errstr = '';
    $socket = stream_socket_client($remote, $errno, $errstr, 20, STREAM_CLIENT_CONNECT);
    if (!is_resource($socket)) {
        error_log('Python SMTP connect failed: ' . $errstr);
        return false;
    }
    stream_set_timeout($socket, 20);

    try {
        py_smtp_expect($socket, [220]);
        py_smtp_command($socket, 'EHLO thinkpy.org', [250]);
        if ($secure === 'tls') {
            py_smtp_command($socket, 'STARTTLS', [220]);
            if (!stream_socket_enable_crypto($socket, true, STREAM_CRYPTO_METHOD_TLS_CLIENT)) {
                throw new RuntimeException('SMTP STARTTLS failed.');
            }
            py_smtp_command($socket, 'EHLO thinkpy.org', [250]);
        }
        py_smtp_command($socket, 'AUTH LOGIN', [334]);
        py_smtp_command($socket, base64_encode($username), [334]);
        py_smtp_command($socket, base64_encode($password), [235]);
        py_smtp_command($socket, 'MAIL FROM:<' . $from . '>', [250]);
        py_smtp_command($socket, 'RCPT TO:<' . $to . '>', [250, 251]);
        py_smtp_command($socket, 'DATA', [354]);

        $message = py_smtp_message($from, $to, $subject, $body);
        fwrite($socket, $message . "\r\n.\r\n");
        py_smtp_expect($socket, [250]);
        py_smtp_command($socket, 'QUIT', [221]);
        fclose($socket);
        return true;
    } catch (Throwable $exception) {
        error_log('Python SMTP send failed: ' . $exception->getMessage());
        if (is_resource($socket)) {
            fclose($socket);
        }
        return false;
    }
}

function py_smtp_message(string $from, string $to, string $subject, string $body): string
{
    $headers = [
        'Date: ' . date(DATE_RFC2822),
        'From: ' . $from,
        'To: ' . $to,
        'Subject: ' . str_replace(["\r", "\n"], '', $subject),
        'MIME-Version: 1.0',
        'Content-Type: text/plain; charset=UTF-8',
    ];
    $normalizedBody = preg_replace("/\r\n|\r|\n/", "\r\n", $body) ?? $body;
    $normalizedBody = preg_replace('/^\./m', '..', $normalizedBody) ?? $normalizedBody;
    return implode("\r\n", $headers) . "\r\n\r\n" . $normalizedBody;
}

function py_smtp_command(mixed $socket, string $command, array $expectedCodes): string
{
    fwrite($socket, $command . "\r\n");
    return py_smtp_expect($socket, $expectedCodes);
}

function py_smtp_expect(mixed $socket, array $expectedCodes): string
{
    $response = '';
    do {
        $line = fgets($socket, 515);
        if ($line === false) {
            throw new RuntimeException('SMTP server closed the connection.');
        }
        $response .= $line;
    } while (isset($line[3]) && $line[3] === '-');

    $code = (int) substr($response, 0, 3);
    if (!in_array($code, $expectedCodes, true)) {
        throw new RuntimeException('Unexpected SMTP response: ' . trim($response));
    }
    return $response;
}

function py_lti_claim(array $claims, string $name, mixed $default = null): mixed
{
    return $claims[$name] ?? $default;
}

function py_lti_nested_claim(array $claims, string $name, string $key, mixed $default = null): mixed
{
    $value = $claims[$name] ?? null;
    return is_array($value) ? ($value[$key] ?? $default) : $default;
}

function py_lti_login_redirect(array $config, array $request): never
{
    if (empty($config['lti']['enabled'])) {
        http_response_code(503);
        exit('LTI is not enabled.');
    }

    foreach (['iss', 'login_hint', 'client_id'] as $required) {
        if (empty($request[$required])) {
            http_response_code(400);
            exit('Missing LTI login parameter: ' . py_h($required));
        }
    }

    if ((string) $request['iss'] !== (string) $config['lti']['issuer']) {
        http_response_code(400);
        exit('Unexpected LTI issuer.');
    }

    if ((string) $request['client_id'] !== (string) $config['lti']['client_id']) {
        http_response_code(400);
        exit('Unexpected LTI client ID.');
    }

    py_start_lti_session($config);

    $state = py_random_token();
    $nonce = py_random_token();
    $target = (string) ($request['target_link_uri'] ?? $config['lti']['default_target_link_uri']);

    $_SESSION['lti_state'][$state] = [
        'nonce' => $nonce,
        'target_link_uri' => $target,
        'created_at' => time(),
    ];

    $query = http_build_query([
        'scope' => 'openid',
        'response_type' => 'id_token',
        'response_mode' => 'form_post',
        'prompt' => 'none',
        'client_id' => $config['lti']['client_id'],
        'redirect_uri' => $config['lti']['redirect_uri'],
        'login_hint' => $request['login_hint'],
        'state' => $state,
        'nonce' => $nonce,
        'lti_message_hint' => $request['lti_message_hint'] ?? '',
    ]);

    header('Location: ' . rtrim((string) $config['lti']['auth_login_url'], '?') . '?' . $query);
    exit;
}

function py_lti_handle_launch(PDO $pdo, array $config, array $post): string
{
    if (empty($config['lti']['enabled'])) {
        throw new RuntimeException('LTI is not enabled.');
    }

    py_start_lti_session($config);

    $state = (string) ($post['state'] ?? '');
    $launchState = $_SESSION['lti_state'][$state] ?? null;
    unset($_SESSION['lti_state'][$state]);

    if (!is_array($launchState) || time() - (int) ($launchState['created_at'] ?? 0) > 600) {
        throw new RuntimeException('Invalid or expired LTI launch state.');
    }

    $claims = py_verify_lti_id_token((string) ($post['id_token'] ?? ''), $config, (string) $launchState['nonce']);
    $userId = py_upsert_lti_user($pdo, $claims);

    $contextClaim = 'https://purl.imsglobal.org/spec/lti/claim/context';
    $resourceClaim = 'https://purl.imsglobal.org/spec/lti/claim/resource_link';
    $deploymentClaim = 'https://purl.imsglobal.org/spec/lti/claim/deployment_id';
    $agsClaim = 'https://purl.imsglobal.org/spec/lti-ags/claim/endpoint';

    $lineitem = py_lti_nested_claim($claims, $agsClaim, 'lineitem');
    $_SESSION['lti_user'] = [
        'authenticated' => true,
        'student_user_id' => $userId,
        'canvas_user_id' => (string) ($claims['sub'] ?? ''),
        'student_identifier' => (string) ($claims['email'] ?? $claims['sub'] ?? ''),
        'display_name' => (string) ($claims['name'] ?? $claims['email'] ?? ''),
        'email' => (string) ($claims['email'] ?? ''),
        'lti_deployment_id' => (string) py_lti_claim($claims, $deploymentClaim, ''),
        'lti_context_id' => (string) py_lti_nested_claim($claims, $contextClaim, 'id', ''),
        'lti_resource_link_id' => (string) py_lti_nested_claim($claims, $resourceClaim, 'id', ''),
        'lti_lineitem_url' => is_string($lineitem) ? $lineitem : '',
    ];

    return (string) ($claims['https://purl.imsglobal.org/spec/lti/claim/target_link_uri']
        ?? $launchState['target_link_uri']
        ?? $config['lti']['default_target_link_uri']);
}

function py_current_lti_user(array $config): ?array
{
    py_start_lti_session($config);
    $user = $_SESSION['lti_user'] ?? null;
    return is_array($user) && !empty($user['authenticated']) ? $user : null;
}

function py_current_student_user(PDO $pdo, array $config): ?array
{
    $ltiUser = py_current_lti_user($config);
    if (is_array($ltiUser)) {
        return $ltiUser + ['auth_source' => 'lti'];
    }
    if (session_status() === PHP_SESSION_ACTIVE) {
        session_write_close();
        $_SESSION = [];
        session_id('');
    }

    py_start_student_session($config);
    $id = $_SESSION['student_user_id'] ?? null;
    if (!is_int($id) && !ctype_digit((string) $id)) {
        return null;
    }

    $stmt = $pdo->prepare(
        'SELECT id, email, display_name, role, status, canvas_user_id, student_identifier
         FROM py_quiz_users
         WHERE id = :id AND role = \'student\' AND status = \'active\'
         LIMIT 1'
    );
    $stmt->execute(['id' => (int) $id]);
    $student = $stmt->fetch();
    if (!is_array($student)) {
        return null;
    }

    return [
        'authenticated' => true,
        'student_user_id' => (int) $student['id'],
        'canvas_user_id' => (string) ($student['canvas_user_id'] ?? ''),
        'student_identifier' => (string) ($student['student_identifier'] ?: py_normalize_student_identifier((string) $student['email'])),
        'display_name' => (string) ($student['display_name'] ?? ''),
        'email' => (string) ($student['email'] ?? ''),
        'lti_deployment_id' => '',
        'lti_context_id' => '',
        'lti_resource_link_id' => '',
        'lti_lineitem_url' => '',
        'auth_source' => 'password',
    ];
}

function py_login_student(PDO $pdo, array $config, string $identifier, string $password): bool
{
    $identifier = trim($identifier);
    if ($identifier === '' || $password === '') {
        return false;
    }

    $student = py_find_student_for_login($pdo, $identifier);
    if (!is_array($student) || !password_verify($password, (string) $student['password_hash'])) {
        return false;
    }
    if (py_student_email_verification_required($config) && empty($student['email_verified_at'])) {
        return false;
    }

    py_start_fresh_student_session($config);
    $_SESSION['student_user_id'] = (int) $student['id'];
    $pdo->prepare('UPDATE py_quiz_users SET last_login_at = CURRENT_TIMESTAMP WHERE id = :id')
        ->execute(['id' => (int) $student['id']]);
    return true;
}

function py_upsert_lti_user(PDO $pdo, array $claims): ?int
{
    $canvasUserId = (string) ($claims['sub'] ?? '');
    $email = trim((string) ($claims['email'] ?? ''));
    $studentIdentifier = py_normalize_student_identifier($email !== '' ? $email : $canvasUserId);
    $displayName = trim((string) ($claims['name'] ?? $email ?: $canvasUserId));

    if ($email === '' && $canvasUserId === '') {
        return null;
    }

    $where = $email !== ''
        ? '(LOWER(email) = LOWER(:email) OR LOWER(student_identifier) = LOWER(:student_identifier))'
        : '(canvas_user_id = :canvas_user_id OR LOWER(student_identifier) = LOWER(:student_identifier))';
    $stmt = $pdo->prepare('SELECT id FROM py_quiz_users WHERE ' . $where . ' LIMIT 1');
    $stmt->execute($email !== ''
        ? ['email' => $email, 'student_identifier' => $studentIdentifier]
        : ['canvas_user_id' => $canvasUserId, 'student_identifier' => $studentIdentifier]);
    $existing = $stmt->fetch();

    if (is_array($existing)) {
        $update = $pdo->prepare(
            'UPDATE py_quiz_users
             SET display_name = :display_name,
                 canvas_user_id = :canvas_user_id,
                 student_identifier = :student_identifier,
                 status = \'active\'
             WHERE id = :id'
        );
        $update->execute([
            'display_name' => $displayName,
            'canvas_user_id' => $canvasUserId !== '' ? $canvasUserId : null,
            'student_identifier' => $studentIdentifier !== '' ? $studentIdentifier : null,
            'id' => (int) $existing['id'],
        ]);
        return (int) $existing['id'];
    }

    $insert = $pdo->prepare(
        'INSERT INTO py_quiz_users (email, display_name, role, password_hash, status, canvas_user_id, student_identifier)
         VALUES (:email, :display_name, \'student\', NULL, \'active\', :canvas_user_id, :student_identifier)'
    );
    $insert->execute([
        'email' => $email !== '' ? $email : $canvasUserId . '@lti.local',
        'display_name' => $displayName,
        'canvas_user_id' => $canvasUserId !== '' ? $canvasUserId : null,
        'student_identifier' => $studentIdentifier !== '' ? $studentIdentifier : null,
    ]);

    return (int) $pdo->lastInsertId();
}

function py_verify_lti_id_token(string $jwt, array $config, string $expectedNonce): array
{
    $parts = explode('.', $jwt);
    if (count($parts) !== 3) {
        throw new RuntimeException('Invalid LTI token shape.');
    }

    $header = py_json_decode_assoc(py_base64url_decode($parts[0]));
    $claims = py_json_decode_assoc(py_base64url_decode($parts[1]));
    if (($header['alg'] ?? '') !== 'RS256') {
        throw new RuntimeException('Unsupported LTI token algorithm.');
    }

    $publicKey = py_lti_public_key((string) ($header['kid'] ?? ''), (string) $config['lti']['jwks_url']);
    $signed = $parts[0] . '.' . $parts[1];
    $signature = py_base64url_decode($parts[2]);
    if (openssl_verify($signed, $signature, $publicKey, OPENSSL_ALGO_SHA256) !== 1) {
        throw new RuntimeException('Invalid LTI token signature.');
    }

    $now = time();
    if ((string) ($claims['iss'] ?? '') !== (string) $config['lti']['issuer']) {
        throw new RuntimeException('Invalid LTI token issuer.');
    }
    $aud = $claims['aud'] ?? null;
    $audiences = is_array($aud) ? $aud : [$aud];
    if (!in_array((string) $config['lti']['client_id'], array_map('strval', $audiences), true)) {
        throw new RuntimeException('Invalid LTI token audience.');
    }
    if ((int) ($claims['exp'] ?? 0) < $now) {
        throw new RuntimeException('Expired LTI token.');
    }
    if ((int) ($claims['iat'] ?? 0) > $now + 300) {
        throw new RuntimeException('Invalid LTI token issued-at time.');
    }
    if ((string) ($claims['nonce'] ?? '') !== $expectedNonce) {
        throw new RuntimeException('Invalid LTI token nonce.');
    }

    $deploymentId = (string) ($claims['https://purl.imsglobal.org/spec/lti/claim/deployment_id'] ?? '');
    $allowedDeployments = array_filter(array_map('strval', $config['lti']['deployment_ids'] ?? []));
    if ($allowedDeployments !== [] && !in_array($deploymentId, $allowedDeployments, true)) {
        throw new RuntimeException('Unexpected LTI deployment.');
    }

    return $claims;
}

function py_lti_public_key(string $kid, string $jwksUrl): string
{
    $jwks = py_fetch_jwks($jwksUrl);
    foreach (($jwks['keys'] ?? []) as $key) {
        if (($key['kid'] ?? '') === $kid && ($key['kty'] ?? '') === 'RSA') {
            return py_rsa_jwk_to_pem($key);
        }
    }
    throw new RuntimeException('LTI public key not found.');
}

function py_fetch_jwks(string $jwksUrl): array
{
    $cachePath = sys_get_temp_dir() . '/py_canvas_jwks_' . sha1($jwksUrl) . '.json';
    if (is_readable($cachePath) && filemtime($cachePath) !== false && filemtime($cachePath) > time() - 3600) {
        return py_json_decode_assoc((string) file_get_contents($cachePath));
    }

    $ch = curl_init($jwksUrl);
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 15,
    ]);
    $body = curl_exec($ch);
    $status = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
    $error = curl_error($ch);
    curl_close($ch);

    if ($body === false || $status < 200 || $status >= 300) {
        throw new RuntimeException($error !== '' ? $error : 'Could not fetch Canvas JWKS.');
    }
    file_put_contents($cachePath, $body, LOCK_EX);
    return py_json_decode_assoc((string) $body);
}

function py_rsa_jwk_to_pem(array $jwk): string
{
    $modulus = py_base64url_decode((string) $jwk['n']);
    $exponent = py_base64url_decode((string) $jwk['e']);
    $rsaPublicKey = py_asn1_sequence(
        py_asn1_integer($modulus)
        . py_asn1_integer($exponent)
    );
    $publicKeyInfo = py_asn1_sequence(
        py_asn1_sequence(py_asn1_oid('1.2.840.113549.1.1.1') . py_asn1_null())
        . py_asn1_bit_string($rsaPublicKey)
    );
    return "-----BEGIN PUBLIC KEY-----\n"
        . chunk_split(base64_encode($publicKeyInfo), 64, "\n")
        . "-----END PUBLIC KEY-----\n";
}

function py_base64url_decode(string $value): string
{
    $decoded = base64_decode(strtr($value, '-_', '+/') . str_repeat('=', (4 - strlen($value) % 4) % 4), true);
    if ($decoded === false) {
        throw new RuntimeException('Invalid base64url value.');
    }
    return $decoded;
}

function py_json_decode_assoc(string $json): array
{
    $decoded = json_decode($json, true);
    if (!is_array($decoded)) {
        throw new RuntimeException('Invalid JSON.');
    }
    return $decoded;
}

function py_random_token(): string
{
    return bin2hex(random_bytes(24));
}

function py_asn1_length(int $length): string
{
    if ($length < 128) {
        return chr($length);
    }
    $out = '';
    while ($length > 0) {
        $out = chr($length & 0xff) . $out;
        $length >>= 8;
    }
    return chr(0x80 | strlen($out)) . $out;
}

function py_asn1_sequence(string $value): string
{
    return "\x30" . py_asn1_length(strlen($value)) . $value;
}

function py_asn1_integer(string $value): string
{
    if ($value !== '' && (ord($value[0]) & 0x80)) {
        $value = "\x00" . $value;
    }
    return "\x02" . py_asn1_length(strlen($value)) . $value;
}

function py_asn1_oid(string $oid): string
{
    $parts = array_map('intval', explode('.', $oid));
    $body = chr(40 * $parts[0] + $parts[1]);
    for ($i = 2; $i < count($parts); $i++) {
        $value = $parts[$i];
        $bytes = chr($value & 0x7f);
        while ($value >>= 7) {
            $bytes = chr(($value & 0x7f) | 0x80) . $bytes;
        }
        $body .= $bytes;
    }
    return "\x06" . py_asn1_length(strlen($body)) . $body;
}

function py_asn1_null(): string
{
    return "\x05\x00";
}

function py_asn1_bit_string(string $value): string
{
    return "\x03" . py_asn1_length(strlen($value) + 1) . "\x00" . $value;
}

function py_current_admin(PDO $pdo): ?array
{
    $id = $_SESSION['admin_user_id'] ?? null;
    if (!is_int($id) && !ctype_digit((string) $id)) {
        return null;
    }

    $stmt = $pdo->prepare(
        'SELECT id, email, display_name, role, status
         FROM py_quiz_users
         WHERE id = :id AND role = \'admin\' AND status = \'active\'
         LIMIT 1'
    );
    $stmt->execute(['id' => (int) $id]);
    $admin = $stmt->fetch();
    return is_array($admin) ? $admin : null;
}

function py_login_admin(PDO $pdo, string $email, string $password): bool
{
    $stmt = $pdo->prepare(
        'SELECT id, password_hash
         FROM py_quiz_users
         WHERE LOWER(email) = LOWER(:email) AND role = \'admin\' AND status = \'active\'
         LIMIT 1'
    );
    $stmt->execute(['email' => trim($email)]);
    $admin = $stmt->fetch();
    if (!is_array($admin) || !password_verify($password, (string) $admin['password_hash'])) {
        return false;
    }

    $_SESSION['admin_user_id'] = (int) $admin['id'];
    return true;
}

function py_h(mixed $value): string
{
    return htmlspecialchars((string) $value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}
