<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Racing Game</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        #gameCanvas {
            border: 2px solid #333;
            background-color: green;
        }
        #scoreDisplay {
            position: absolute;
            top: 10px;
            left: 10px;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="800" height="600"></canvas>
    <div id="scoreDisplay">Score: 0</div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const scoreDisplay = document.getElementById('scoreDisplay');

        // Game constants
        const SCREEN_WIDTH = 800;
        const SCREEN_HEIGHT = 600;
        const ROAD_LEFT = 200;
        const ROAD_RIGHT = SCREEN_WIDTH - 200;

        // Colors
        const ROAD_COLOR = '#808080';
        const LINE_COLOR = '#FFFFFF';
        const CAR_COLOR = '#FF0000';
        const OBSTACLE_COLOR = '#000000';

        // Game state
        let player = {
            x: SCREEN_WIDTH / 2,
            y: SCREEN_HEIGHT - 100,
            width: 50,
            height: 80,
            speed: 5
        };

        let obstacles = [];
        let score = 0;
        let gameOver = false;
        let animationFrameId;

        function drawRoad() {
            // Road background
            ctx.fillStyle = ROAD_COLOR;
            ctx.fillRect(ROAD_LEFT, 0, ROAD_RIGHT - ROAD_LEFT, SCREEN_HEIGHT);

            // Road borders
            ctx.strokeStyle = LINE_COLOR;
            ctx.lineWidth = 5;
            ctx.beginPath();
            ctx.moveTo(ROAD_LEFT, 0);
            ctx.lineTo(ROAD_LEFT, SCREEN_HEIGHT);
            ctx.moveTo(ROAD_RIGHT, 0);
            ctx.lineTo(ROAD_RIGHT, SCREEN_HEIGHT);
            ctx.stroke();

            // Center lines
            for (let y = 0; y < SCREEN_HEIGHT; y += 100) {
                ctx.beginPath();
                ctx.moveTo(SCREEN_WIDTH / 2, y);
                ctx.lineTo(SCREEN_WIDTH / 2, y + 50);
                ctx.stroke();
            }
        }

        function drawPlayer() {
            ctx.fillStyle = CAR_COLOR;
            ctx.fillRect(player.x, player.y, player.width, player.height);
        }

        function createObstacle() {
            return {
                x: Math.random() * (ROAD_RIGHT - ROAD_LEFT - 50) + ROAD_LEFT,
                y: -50,
                width: 50,
                height: 50,
                speed: Math.random() * 4 + 3
            };
        }

        function drawObstacles() {
            ctx.fillStyle = OBSTACLE_COLOR;
            obstacles.forEach(obstacle => {
                ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
            });
        }

        function moveObstacles() {
            obstacles.forEach(obstacle => {
                obstacle.y += obstacle.speed;
            });

            // Remove obstacles that are off screen
            obstacles = obstacles.filter(obstacle => obstacle.y < SCREEN_HEIGHT);
        }

        function checkCollision() {
            return obstacles.some(obstacle => 
                player.x < obstacle.x + obstacle.width &&
                player.x + player.width > obstacle.x &&
                player.y < obstacle.y + obstacle.height &&
                player.y + player.height > obstacle.y
            );
        }

        function gameLoop() {
            // Clear canvas
            ctx.clearRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);

            // Draw game elements
            drawRoad();
            drawPlayer();
            drawObstacles();

            // Move obstacles
            moveObstacles();

            // Spawn new obstacles
            if (Math.random() < 0.02) {
                obstacles.push(createObstacle());
            }

            // Update score
            score++;
            scoreDisplay.textContent = `Score: ${score}`;

            // Check for collision
            if (checkCollision()) {
                gameOver = true;
                cancelAnimationFrame(animationFrameId);
                drawGameOver();
            } else {
                animationFrameId = requestAnimationFrame(gameLoop);
            }
        }

        function drawGameOver() {
            ctx.fillStyle = 'black';
            ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);
            
            ctx.fillStyle = 'white';
            ctx.font = '48px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`Game Over! Score: ${score}`, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2);
        }

        // Keyboard controls
        document.addEventListener('keydown', (e) => {
            if (gameOver) return;

            switch (e.key) {
                case 'ArrowLeft':
                    if (player.x > ROAD_LEFT) {
                        player.x -= player.speed;
                    }
                    break;
                case 'ArrowRight':
                    if (player.x + player.width < ROAD_RIGHT) {
                        player.x += player.speed;
                    }
                    break;
            }
        });

        // Start the game
        function startGame() {
            // Reset game state
            player.x = SCREEN_WIDTH / 2;
            obstacles = [];
            score = 0;
            gameOver = false;
            scoreDisplay.textContent = 'Score: 0';

            // Start game loop
            gameLoop();
        }

        // Initial game start
        startGame();
    </script>
</body>
</html>
