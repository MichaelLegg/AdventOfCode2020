import data from "./data";

const WIDTH = 31;
const HEIGHT = 323;

function solution() {
  console.log(
    [
      checkSlope(1, 1),
      checkSlope(3, 1),
      checkSlope(5, 1),
      checkSlope(7, 1),
      checkSlope(1, 2),
    ].reduce((a, b) => a * b, 1)
  );
}

function checkSlope(xInc: number, yInc: number) {
  let x = 0;
  let y = 0;
  let trees = 0;

  while (y < HEIGHT) {
    x += xInc;
    y += yInc;

    if (x >= WIDTH) x = x - WIDTH;

    const pos = y * 31 + x;

    trees += Number(data[pos] === "#");
  }

  return trees;
}

const start = process.hrtime();
solution();
const end = process.hrtime(start);
console.info("Execution time: %ds %dms", end[0], end[1] / 1000000);
