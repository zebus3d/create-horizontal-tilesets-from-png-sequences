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
    numberOfFrames: 10,
    ticksPerFrame: 4
});

// Load sprite sheet
coinImage.addEventListener("load", gameLoop);
coinImage.src = "images/tileset-bunny.png";