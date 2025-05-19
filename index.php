<?php
// Get parameters from the URL
$a = isset($_GET['a']) ? $_GET['a'] : null;
$b = isset($_GET['b']) ? $_GET['b'] : null;
$c = isset($_GET['c']) ? $_GET['c'] : null;

// Check if all parameters are provided
if ($a !== null && $b !== null && $c !== null) {
    // Construct the command with parameters
    $command = escapeshellcmd("python3 /var/www/html/calculate.py $a $b $c");
    $output = shell_exec($command);
    echo $output;
} else {
    echo "Error: Missing parameters. Please provide 'a', 'b', and 'c' in the URL. Example: /index.php?a=2&b=3&c=4";
}
?>
