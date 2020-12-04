import Fs from "fs"

let allFields: string[] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

export default function Solution(): number{
    let input: string[] = Fs.readFileSync(`src/4/data.txt`).toString().split('\r\n\r\n').filter(x => x.length > 0).map(x => x.replace(/\r?\n|\r/g, ' '));
    
    let validCount = 0;
    input.forEach(x => {
        let current = x.split(' ');
        let keysValid = 0;
        current.forEach(y => {
            const key = y.substring(0, 3);
            if(allFields.includes(key))
                keysValid++;
        })
        if(keysValid === allFields.length)
            validCount++;
    })
    return validCount;
}