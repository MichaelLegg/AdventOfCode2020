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
            const value = y.substring(4, y.length);
            switch (key){
                case "byr":
                    if(+value >= 1920 && +value <= 2002) keysValid++;
                case "iyr":
                    if(+value >= 2010 && +value <= 2020) keysValid++;
                case "eyr":
                    if(+value >= 2020 && +value <= 2030) keysValid++;
                case "hgt": {
                    const val = +value.substring(0, value.length-2);
                    if(value.includes("cm")) 
                        if(val >=150 && val <=193) keysValid++;
                    else if(value.includes("in"))
                        if(val >=59 && val <=76) keysValid++;          
                }
                case "hcl":{
                    if(value.length === 7)
                        if(value[0] === "#")
                            if([...value.substring(1, value.length)].every(char => char.match(/^[a-f0-9]+$/)))
                                keysValid++;   
                }
                case "ecl":{
                    const validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    if (validEcl.some(x=> x === value))
                        keysValid++;
                }
                case "pid":
                    if(value.length === 9)
                        keysValid++;
            }

            if(keysValid === current.length && keysValid === allFields.length)
                validCount++;            
        })
    })
    return validCount;
}