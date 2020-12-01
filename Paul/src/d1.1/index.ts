import data from "./data";

const start = process.hrtime();
console.table(data.map(a => data.map(b => ({sum: a + b, mul: a * b })).filter(b => b.sum === 2020).map(b => b.mul)).filter(a => a.length > 0));
const end = process.hrtime(start);

 console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);
