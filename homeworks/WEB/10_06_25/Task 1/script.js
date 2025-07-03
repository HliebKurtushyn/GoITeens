const input = document.getElementById('number');

const textSquare = document.getElementById('Square');
const textCube = document.getElementById('Cube');
const textRemainder = document.getElementById('Remainder by 5');

const button = document.getElementById('calculate');

button.addEventListener('click', () => {
    const value = Number(input.value);

    textSquare.textContent = value ** 2;
    textCube.textContent = value ** 3;
    textRemainder.textContent = value % 5;
});
