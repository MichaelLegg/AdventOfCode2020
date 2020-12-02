import data from "../data";

const start = process.hrtime();

function compare() {
    for(let i = 0; i < data.length; i++) {
        for(let j = 0; j < data.length; j++) {
            if(data[i] + data[j] === 2020) {
                return data[i] * data[j];
            }
        }
    }
}
console.log(compare());

const end = process.hrtime(start);

console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);