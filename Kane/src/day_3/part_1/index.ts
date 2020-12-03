import data from "../data";

const start = process.hrtime();

function pwdPolicyCheck(input: string[]) {
    
}
console.log(pwdPolicyCheck(data));

const end = process.hrtime(start);
console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);