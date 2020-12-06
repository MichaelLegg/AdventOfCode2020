import Fs from "fs"

export default function Solution(): number{
    let groups: string[] = Fs.readFileSync(`src/6/data.txt`).toString().split('\r\n\r\n').filter(x => x.length > 0);  
    let total = 0;
    groups.forEach(group => {
        let groupTotal = 0;
        const people = group.split(/\r?\n|\r/g)
        let seen: string[] = [];
        people.forEach((person) => {
            [...person].filter(x => !seen.includes(x)).forEach(character => {   
                groupTotal += +people.every((person2) => person2 === person || person2.includes(character) ? true : false)
            })          
        })
        total += groupTotal;
    })
    return total;
} 