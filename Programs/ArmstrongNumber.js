/* Program Name: Armstrong Number */
/* By Hrishikesh Sharma */

let sum = 0;
let number = prompt('Please enter a three-digit positive integer: ');
// first we create a temp number
let temp = number;
while (temp > 0) {
    // next up is we find the one's
    let remainder = temp % 10;
    sum += remainder * remainder * remainder;
    temp = parseInt(temp / 10);
}
sum == number ? console.log(`${number} is an Armstrong number`) : console.log(`${number} is not an Armstrong number.`)
