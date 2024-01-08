#!/usr/bin/node

function findSecondBiggest(numbers) {
  if (numbers.length < 2) {
    return 0;
  }

  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < numbers.length; i++) {
    const currentNumber = parseInt(numbers[i]);

    if (currentNumber > largest) {
      secondLargest = largest;
      largest = currentNumber;
    } else if (currentNumber > secondLargest && currentNumber !== largest) {
      secondLargest = currentNumber;
    }
  }

  return secondLargest;
}

const argumentsList = process.argv.slice(2);
const secondBiggest = findSecondBiggest(argumentsList);

console.log(`The second biggest integer is: ${secondBiggest}`);
