import data from "../data";

const start = process.hrtime();

function pwdPolicyCheck() {
    let map = data.map(x => x.replace(":", "").split(" "));
    let count = 0;
    map.filter(y => {
        if(y[2].length >= parseInt(y[0].split('-')[0]) && y[2].length <= parseInt(y[0].split('-')[1]) && y[2].includes(y[1])) count++;
    });
    return count;
}
console.log(pwdPolicyCheck());

const end = process.hrtime(start);

console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);