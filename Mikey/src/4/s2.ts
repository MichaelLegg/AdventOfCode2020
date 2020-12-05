import Fs from "fs"

let requiredFields: string[] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

export default function Solution(): number{
    let input: string[] = Fs.readFileSync(`src/4/data.txt`).toString().split('\r\n\r\n').filter(x => x.length > 0).map(x => x.replace(/\r?\n|\r/g, ' '));
    
    let validCount = 0;
    input.forEach(x => {
        let current = x.split(' ');
        let keysValid = 0;

        const allReq  = requiredFields.every(req => {
            return !!current.find(x => x.substring(0, 3) === req)
        })

        if(allReq){
            current.forEach(y => {
                const key = y.substring(0, 3);
                const value = y.substring(4, y.length);

                switch (key){
                    case "byr":
                        if(+value >= 1920 && +value <= 2002) keysValid++;
                        break;
                    case "iyr":
                        if(+value >= 2010 && +value <= 2020) keysValid++;
                        break;
                    case "eyr":
                        if(+value >= 2020 && +value <= 2030) keysValid++;
                        break;
                    case "hgt": 
                        const val = +(value.substring(0, value.length-2));
                        if(value.includes("cm")) 
                            if(val >=150 && val <=193) keysValid++;
                        else if(value.includes("in"))
                            if(val >=59 && val <=76) keysValid++;      
                        break;
                    case "hcl":
                        if(value.length === 7)
                            if(value[0] === "#")
                                if([...value.substring(1, value.length)].every(char => !!char.match(/^[a-f0-9]+$/)))
                                    keysValid++;
                        break;
                    case "ecl":
                        const validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                        if (validEcl.some(x=> x === value))
                            keysValid++;
                        break;
                    case "pid":
                        if(value.length === 9)
                            keysValid++;
                        break;
                }           
            })

            if(keysValid === requiredFields.length)
                validCount++;
            } 
    })
    return validCount;
}