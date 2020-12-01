import data from "./data";

const start = process.hrtime();
console.table(data.map(a => data.map(b => data.map(c => ({sum: a + b + c, mul: a * b * c })).filter(c => c.sum === 2020).map(c => c.mul)).filter(b => b.length > 0)).filter(a => a.length > 0));
const end = process.hrtime(start);

 console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);
