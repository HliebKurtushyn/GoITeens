let number = 10;

function isEven() {
    console.log(number % 2 === 0)
}

isEven();

console.log("Task 2")

let numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]

for (num in numbers) {
    console.log(num % 2 === 0)
}