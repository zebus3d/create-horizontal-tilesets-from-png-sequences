// Get canvas
canvas = document.getElementById("bunny");
// size of single frame
canvas.width = 286;
canvas.height = 222;

// Create sprite sheet
coinImage = new Image();

// Create sprite
coin = sprite({
    context: canvas.getContext("2d"),
    // size of tileset
    width: 2002,
    height: 222,
    image: coinImage,
    numberOfFrames: 7,
    ticksPerFrame: 4
});

// Load sprite sheet
coinImage.addEventListener("load", gameLoop);
coinImage.src = "images/tileset-bunny.png";

// set if you need autoplay on (1) or off (0):
autoplay = true;

// start and pause
canvas.addEventListener('click', function() {
    if (autoplay == 1) {
        pause();
        autoplay = false;
    } else {
        start();
        autoplay = true;
    }
}, false);
