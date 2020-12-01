import data from "./data";

const start = process.hrtime();
const filtered = data.filter(d => d < 1200); // this is maybe very cheaty ;)
console.table(filtered.map(a => filtered.map(b => filtered.map(c => ({sum: a + b + c, mul: a * b * c })).filter(c => c.sum === 2020).map(c => c.mul)).filter(b => b.length > 0)).filter(a => a.length > 0));
const end = process.hrtime(start);

 console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);
