import data from "./data";

const start = process.hrtime();
const max = 2020 - (data.reduce((a, b) => a < b ? a : b) * 2);
const filtered = data.filter(d => d <= max);
const sorted = filtered.sort((a, b) => Number(a) - Number(b));

let i = 0;
let k = 1;
let j = sorted.length - 1;

while (i < sorted.length && k < sorted.length && j > 0) {
    if (sorted[i] + sorted[k] + sorted[j] === 2020) {
        console.log(sorted[i] * sorted[k] * sorted[j]);
        break;
    }

    if (sorted[i] + sorted[k] + sorted[j] > 2020) {
        j--;
    } else {
        if (i + 1 === k) {
            k++;
        } else {
            i++;
        }
    }
}
const end = process.hrtime(start);

console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);
