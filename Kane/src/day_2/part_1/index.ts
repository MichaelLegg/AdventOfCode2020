import data from "../data";
import data2 from "../data2";

const start = process.hrtime();

function pwdPolicyCheck(input: string[]) {
    let map = input.map(x => x.replace(":", "").split(" "));
    let count = 0;
    map.filter(y => {
        let charCount = 0;
        for(let i=0; i < y[2].length; i++) {
            if(y[2].charAt(i) === y[1]) charCount++;
        }
        if(charCount >= parseInt(y[0].split('-')[0]) && charCount <= parseInt(y[0].split('-')[1])) count++;
    });
    return count;
}
console.log(pwdPolicyCheck(data));

const end = process.hrtime(start);

console.info('Execution time: %ds %dms', end[0], end[1] / 1000000);