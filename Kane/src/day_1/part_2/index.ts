import data from "../data";

const start = process.hrtime();

function compare() {
    for(let i = 0; i < data.length; i++) {
        for(let j = 0; j < data.length; j++) {
            for(let k = 0; k < data.length; k++) {
                if(data[i] + data[j] + data[k] === 2020) {
                    console.log(data[i] * data[j] * data[k]);
                }
            }
        }
    }
}

console.log(compare());

const end = process.hrtime(start);

console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);