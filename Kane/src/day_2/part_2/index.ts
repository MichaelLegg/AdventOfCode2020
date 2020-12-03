import data from "../data";

const start = process.hrtime();

function pwdPolicyCheck(input: string[]) {
    let map = input.map(x => x.replace(":", "").split(" "));
    let count = 0;
    map.filter(y => {
        let min = parseInt(y[0].split('-')[0]);
        let max = parseInt(y[0].split('-')[1]);
        let char = y[1];
        let pwd = y[2];

        if((pwd.charAt(min-1) === char && pwd.charAt(max-1) !== char) || (pwd.charAt(min-1) !== char && pwd.charAt(max-1) === char)) count++;;
    });
    return count;
}
console.log("Puzzle answer: " + pwdPolicyCheck(data));

const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);