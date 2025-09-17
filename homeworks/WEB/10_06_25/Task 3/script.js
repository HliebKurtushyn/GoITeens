const button = document.getElementById('button');

const body = document.body;
let colorIndex = 0;

colors = ["red", "blue", "green", "yellow", "purple"];

button.addEventListener('click', () => {
    body.style.backgroundColor = colors[colorIndex];

    colorIndex = (colorIndex + 1) % colors.length;
})